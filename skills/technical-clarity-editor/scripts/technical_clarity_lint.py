#!/usr/bin/env python3
"""Run mechanical bilingual checks on technical prose.

The checker enforces explicit word limits and detects exact deprecated labels.
It does not infer grammar, passive voice, clarity, or substantive validity.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


PROFILES = {
    "strict-instructional": {
        "en": {"instruction": 20, "descriptive": 25},
        "es": {"instruction": 22, "descriptive": 28},
        "hard_limits": True,
    },
    "technical": {
        "en": {"instruction": 30, "descriptive": 35},
        "es": {"instruction": 32, "descriptive": 35},
        "hard_limits": False,
    },
    "scientific": {
        "en": {"instruction": 35, "descriptive": 45},
        "es": {"instruction": 38, "descriptive": 45},
        "hard_limits": False,
    },
    "legal": {
        "en": {"instruction": 40, "descriptive": 50},
        "es": {"instruction": 42, "descriptive": 50},
        "hard_limits": False,
    },
}

SPANISH_HINTS = {
    "el", "la", "los", "las", "de", "del", "que", "para", "por", "con",
    "una", "un", "se", "como", "cuando", "debe", "puede",
}
ENGLISH_HINTS = {
    "the", "a", "an", "of", "that", "for", "by", "with", "and", "or",
    "when", "must", "should", "can", "is", "are",
}
IMPERATIVE_HINTS = {
    "en": {
        "add", "apply", "check", "click", "close", "confirm", "connect",
        "copy", "delete", "enter", "open", "press", "remove", "run",
        "save", "select", "set", "type", "use", "verify", "wait",
    },
    "es": {
        "abra", "aplique", "añada", "compruebe", "conecte", "confirme",
        "copie", "elimine", "escriba", "espere", "guarde", "haga",
        "ingrese", "presione", "retire", "seleccione", "use", "verifique",
    },
}
WORD_RE = re.compile(
    r"[^\W\d_]+(?:[-’'][^\W\d_]+)*|\d+(?:[.,]\d+)*", re.UNICODE
)
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
LIST_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")


@dataclass
class Issue:
    severity: str
    code: str
    line: int
    message: str
    excerpt: str


def words(text: str) -> list[str]:
    return WORD_RE.findall(text)


def detect_language(text: str) -> str:
    """Best-effort convenience for non-strict profiles."""
    tokens = {token.casefold() for token in words(text)}
    es_score = len(tokens & SPANISH_HINTS)
    en_score = len(tokens & ENGLISH_HINTS)
    if re.search(r"[áéíóúüñ¿¡]", text, re.IGNORECASE):
        es_score += 2
    return "es" if es_score > en_score else "en"


def excluded_line_counts(text: str) -> dict[str, int]:
    counts = {"code": 0, "headings": 0, "tables": 0}
    in_fence = False
    for raw in text.splitlines():
        stripped = raw.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            counts["code"] += 1
        elif in_fence:
            counts["code"] += 1
        elif stripped.startswith("#"):
            counts["headings"] += 1
        elif "|" in stripped:
            counts["tables"] += 1
    return counts


def prose_lines(text: str) -> Iterable[tuple[int, str]]:
    in_fence = False
    for number, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not stripped or stripped.startswith("#") or "|" in stripped:
            continue
        yield number, raw


def sentences(text: str) -> Iterable[tuple[int, str, bool]]:
    for line_number, raw in prose_lines(text):
        is_list = bool(LIST_RE.match(raw))
        content = LIST_RE.sub("", raw.strip())
        for sentence in SENTENCE_SPLIT_RE.split(content):
            if sentence.strip():
                yield line_number, sentence.strip(), is_list


def is_instruction(sentence: str, is_list: bool, lang: str) -> bool:
    first = words(sentence)
    return bool(
        first and is_list and first[0].casefold() in IMPERATIVE_HINTS[lang]
    )


def phrase_pattern(phrase: str) -> re.Pattern[str]:
    return re.compile(r"(?<!\w)" + re.escape(phrase) + r"(?!\w)", re.IGNORECASE)


def load_concepts(path: Path | None) -> tuple[dict, list[Issue]]:
    if path is None:
        return {}, []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {}, [Issue("error", "concept_registry_invalid", 0, str(exc), str(path))]
    concepts = data.get("concepts")
    if not isinstance(concepts, list):
        return {}, [
            Issue("error", "concept_registry_invalid", 0, "`concepts` must be an array.", str(path))
        ]
    seen: dict[tuple[str, str], str] = {}
    issues: list[Issue] = []
    for concept in concepts:
        concept_id = str(concept.get("id", ""))
        labels = concept.get("canonical_labels", {})
        if not concept_id or not isinstance(labels, dict):
            issues.append(
                Issue("error", "concept_missing_core", 0, "Each concept needs `id` and `canonical_labels`.", concept_id or "<missing id>")
            )
            continue
        for lang, label in labels.items():
            key = (str(lang), str(label).casefold())
            if key in seen and seen[key] != concept_id:
                issues.append(
                    Issue("error", "canonical_label_conflict", 0, f"`{label}` is canonical for both {seen[key]} and {concept_id}.", str(label))
                )
            else:
                seen[key] = concept_id
    return data, issues


def concept_issues(text: str, lang: str, registry: dict, strict: bool) -> list[Issue]:
    issues: list[Issue] = []
    for concept in registry.get("concepts", []):
        canonical = concept.get("canonical_labels", {}).get(lang)
        deprecated = concept.get("deprecated_labels", {}).get(lang, [])
        if not canonical or not isinstance(deprecated, list):
            continue
        for old_label in deprecated:
            if phrase_pattern(str(old_label)).search(text):
                issues.append(
                    Issue(
                        "error" if strict else "warning",
                        "deprecated_term",
                        0,
                        f"Use canonical `{canonical}` instead of `{old_label}` for concept `{concept.get('id')}`.",
                        str(old_label),
                    )
                )
    return issues


def lint(
    text: str,
    lang: str,
    profile_name: str,
    registry: dict,
    instruction_limit: int | None = None,
    descriptive_limit: int | None = None,
) -> list[Issue]:
    profile = PROFILES[profile_name]
    strict = bool(profile["hard_limits"])
    issues: list[Issue] = []
    for line, sentence, is_list in sentences(text):
        category = "instruction" if is_instruction(sentence, is_list, lang) else "descriptive"
        count = len(words(sentence))
        override = instruction_limit if category == "instruction" else descriptive_limit
        limit = override if override is not None else profile[lang][category]
        if count > limit:
            issues.append(
                Issue(
                    "error" if strict else "warning",
                    "sentence_too_long",
                    line,
                    f"{count} words; {profile_name}/{lang} limit is {limit}.",
                    sentence[:180],
                )
            )
    issues.extend(concept_issues(text, lang, registry, strict))
    return issues


def render_text(path: Path, lang: str, profile: str, issues: list[Issue], excluded: dict[str, int]) -> str:
    errors = sum(issue.severity == "error" for issue in issues)
    warnings = sum(issue.severity == "warning" for issue in issues)
    lines = [
        f"{path}: language={lang} profile={profile} errors={errors} warnings={warnings}",
        "Excluded from sentence checks: "
        + ", ".join(f"{name}={count}" for name, count in excluded.items()),
    ]
    for issue in issues:
        location = f"line {issue.line}" if issue.line else "registry/text"
        lines.append(f"{issue.severity.upper()} {issue.code} ({location}): {issue.message}")
        if issue.excerpt:
            lines.append(f"  {issue.excerpt}")
    if not issues:
        lines.append("No mechanical violations detected in checked prose.")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--lang", choices=("auto", "es", "en"), default="auto")
    parser.add_argument("--profile", choices=tuple(PROFILES), default="technical")
    parser.add_argument("--concepts", type=Path)
    parser.add_argument("--instruction-max-words", type=int)
    parser.add_argument("--descriptive-max-words", type=int)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--fail-on-warnings", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        text = args.file.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    lang = detect_language(text) if args.lang == "auto" else args.lang
    registry, registry_issues = load_concepts(args.concepts)
    if args.profile == "strict-instructional" and args.lang == "auto":
        registry_issues.append(
            Issue("error", "explicit_language_required", 0, "Use --lang es or --lang en in strict-instructional mode.", "")
        )
    issues = registry_issues + lint(
        text,
        lang,
        args.profile,
        registry,
        instruction_limit=args.instruction_max_words,
        descriptive_limit=args.descriptive_max_words,
    )
    excluded = excluded_line_counts(text)
    if args.format == "json":
        print(
            json.dumps(
                {
                    "file": str(args.file),
                    "language": lang,
                    "profile": args.profile,
                    "errors": sum(item.severity == "error" for item in issues),
                    "warnings": sum(item.severity == "warning" for item in issues),
                    "excluded_lines": excluded,
                    "issues": [asdict(item) for item in issues],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(render_text(args.file, lang, args.profile, issues, excluded))
    if any(item.severity == "error" for item in issues):
        return 1
    if args.fail_on_warnings and issues:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
