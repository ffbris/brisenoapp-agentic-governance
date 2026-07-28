#!/usr/bin/env python3
"""Install portable skills for Codex or Claude Code."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def explicit_for_codex(skill: Path) -> bool:
    policy = skill / "agents" / "openai.yaml"
    return policy.exists() and "allow_implicit_invocation: false" in policy.read_text(encoding="utf-8")


def adapt_for_claude(skill_md: Path) -> None:
    text = skill_md.read_text(encoding="utf-8")
    if "disable-model-invocation:" in text:
        return
    closing = text.find("\n---", 4)
    if closing < 0:
        raise ValueError(f"Invalid frontmatter: {skill_md}")
    text = text[:closing] + "\ndisable-model-invocation: true" + text[closing:]
    skill_md.write_text(text, encoding="utf-8")


def install(source: Path, target_root: Path, runtime: str, replace: bool) -> None:
    for skill in sorted(path for path in source.iterdir() if (path / "SKILL.md").exists()):
        target = target_root / skill.name
        if target.exists() or target.is_symlink():
            if not replace:
                raise FileExistsError(f"{target} exists; rerun with --replace")
            if target.is_symlink() or target.is_file():
                target.unlink()
            else:
                shutil.rmtree(target)
        if runtime == "codex":
            target.symlink_to(skill.resolve(), target_is_directory=True)
        else:
            shutil.copytree(skill, target)
            shutil.rmtree(target / "agents", ignore_errors=True)
            if explicit_for_codex(skill):
                adapt_for_claude(target / "SKILL.md")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime", choices=("codex", "claude-code"), required=True)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--replace", action="store_true")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    if args.target:
        target = args.target.expanduser()
    elif args.runtime == "codex":
        target = Path.home() / ".codex" / "skills"
    else:
        target = Path.home() / ".claude" / "skills"
    target.mkdir(parents=True, exist_ok=True)
    install(repo / "skills", target, args.runtime, args.replace)
    print(f"Installed skills for {args.runtime} in {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
