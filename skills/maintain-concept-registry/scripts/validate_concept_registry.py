#!/usr/bin/env python3
"""Validate material invariants in CONCEPT_REGISTRY.json using stdlib only."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
STATUSES = {"draft", "current", "deprecated", "superseded", "contested"}
TYPES = {"concept", "analytical-framework", "legal-term", "variable", "indicator", "process"}
RELATIONS = {"broader_than", "narrower_than", "related_not_equivalent", "conflicts_with", "supersedes"}


def validate(data: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["Registry must be a JSON object."]
    if data.get("schema_version") != "1.0":
        errors.append("schema_version must equal `1.0`.")
    authority_order = data.get("authority_order")
    if not isinstance(authority_order, list) or not authority_order or len(authority_order) != len(set(authority_order)):
        errors.append("authority_order must be a non-empty list without duplicates.")
        authority_order = []
    concepts = data.get("concepts")
    if not isinstance(concepts, list):
        return errors + ["concepts must be an array."]
    ids: set[str] = set()
    labels: dict[tuple[str, str], str] = {}
    relation_targets: list[tuple[str, str]] = []
    for index, concept in enumerate(concepts):
        prefix = f"concepts[{index}]"
        if not isinstance(concept, dict):
            errors.append(f"{prefix} must be an object.")
            continue
        concept_id = concept.get("id")
        if not isinstance(concept_id, str) or not ID_RE.fullmatch(concept_id):
            errors.append(f"{prefix}.id must be stable lower-case hyphen-case.")
            concept_id = f"<index-{index}>"
        elif concept_id in ids:
            errors.append(f"Duplicate concept id `{concept_id}`.")
        ids.add(concept_id)
        if concept.get("type") not in TYPES:
            errors.append(f"{prefix}.type is invalid.")
        if concept.get("status") not in STATUSES:
            errors.append(f"{prefix}.status is invalid.")
        definition = concept.get("definition")
        if not isinstance(definition, str) or not definition.strip():
            errors.append(f"{prefix}.definition is required.")
        scope = concept.get("scope")
        if not isinstance(scope, list) or not scope or any(not isinstance(item, str) or not item for item in scope):
            errors.append(f"{prefix}.scope must contain at least one string.")
        authority = concept.get("authority")
        if not isinstance(authority, dict) or not authority.get("level") or not authority.get("source"):
            errors.append(f"{prefix}.authority requires level and source.")
        elif authority_order and authority["level"] not in authority_order:
            errors.append(f"{prefix}.authority.level is absent from authority_order.")
        canonical = concept.get("canonical_labels")
        if not isinstance(canonical, dict) or not canonical:
            errors.append(f"{prefix}.canonical_labels requires at least one language.")
        else:
            for lang, label in canonical.items():
                if not isinstance(label, str) or not label.strip():
                    errors.append(f"{prefix}.canonical_labels.{lang} is empty.")
                    continue
                key = (str(lang), label.casefold())
                if key in labels and labels[key] != concept_id:
                    errors.append(f"Canonical label `{label}` is shared by `{labels[key]}` and `{concept_id}`.")
                labels[key] = concept_id
        for relation in concept.get("relations", []):
            if not isinstance(relation, dict) or relation.get("type") not in RELATIONS or not relation.get("target"):
                errors.append(f"{prefix}.relations contains an invalid relation.")
            else:
                relation_targets.append((concept_id, relation["target"]))
    for source, target in relation_targets:
        if target not in ids:
            errors.append(f"Relation from `{source}` targets missing concept `{target}`.")
        if source == target:
            errors.append(f"Concept `{source}` cannot relate to itself.")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry", type=Path)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    try:
        data = json.loads(args.registry.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors = [str(exc)]
    else:
        errors = validate(data)
    if args.format == "json":
        print(json.dumps({"valid": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    elif errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
    else:
        print(f"{args.registry}: valid")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
