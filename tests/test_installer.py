import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "install_skills.py"
SPEC = importlib.util.spec_from_file_location("install_skills", SCRIPT)
INSTALLER = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = INSTALLER
SPEC.loader.exec_module(INSTALLER)


class InstallerTests(unittest.TestCase):
    def test_codex_uses_symlinks(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            INSTALLER.install(ROOT / "skills", target, "codex", replace=False)
            self.assertTrue((target / "whole-problem-reviewer").is_symlink())

    def test_claude_adapts_explicit_invocation(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            INSTALLER.install(ROOT / "skills", target, "claude-code", replace=False)
            explicit = (target / "whole-problem-reviewer" / "SKILL.md").read_text(encoding="utf-8")
            implicit = (target / "writing-quality-gate" / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("disable-model-invocation: true", explicit)
            self.assertNotIn("disable-model-invocation:", implicit)
            self.assertFalse((target / "whole-problem-reviewer" / "agents").exists())


if __name__ == "__main__":
    unittest.main()
