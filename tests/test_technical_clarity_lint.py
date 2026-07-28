import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "technical-clarity-editor" / "scripts" / "technical_clarity_lint.py"
SPEC = importlib.util.spec_from_file_location("technical_clarity_lint", SCRIPT)
LINTER = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = LINTER
SPEC.loader.exec_module(LINTER)


class TechnicalClarityLintTests(unittest.TestCase):
    def test_does_not_claim_to_detect_passive_voice(self):
        issues = LINTER.lint(
            "El resultado es válido. El archivo fue generado por el sistema.",
            "es",
            "strict-instructional",
            {},
        )
        self.assertNotIn("possible_passive_voice", {item.code for item in issues})

    def test_spanish_and_english_use_different_default_limits(self):
        self.assertEqual(LINTER.PROFILES["strict-instructional"]["en"]["instruction"], 20)
        self.assertEqual(LINTER.PROFILES["strict-instructional"]["es"]["instruction"], 22)

    def test_limit_override_is_hard_in_strict_mode(self):
        issues = LINTER.lint(
            "- Abra ahora el panel de configuración principal.",
            "es",
            "strict-instructional",
            {},
            instruction_limit=4,
        )
        matches = [item for item in issues if item.code == "sentence_too_long"]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0].severity, "error")

    def test_deprecated_concept_label_is_reported(self):
        registry = {
            "concepts": [
                {
                    "id": "enrollment",
                    "canonical_labels": {"es": "inscripción"},
                    "deprecated_labels": {"es": ["registro"]},
                }
            ]
        }
        issues = LINTER.concept_issues("El registro final aumentó.", "es", registry, strict=True)
        self.assertEqual(issues[0].code, "deprecated_term")
        self.assertIn("inscripción", issues[0].message)

    def test_registry_rejects_duplicate_canonical_labels(self):
        registry_path = ROOT / "tests" / "_temporary_concepts.json"
        registry_path.write_text(
            json.dumps(
                {
                    "concepts": [
                        {"id": "a", "canonical_labels": {"es": "resultado"}},
                        {"id": "b", "canonical_labels": {"es": "resultado"}},
                    ]
                }
            ),
            encoding="utf-8",
        )
        try:
            _, issues = LINTER.load_concepts(registry_path)
        finally:
            registry_path.unlink()
        self.assertIn("canonical_label_conflict", {item.code for item in issues})

    def test_reports_excluded_table_and_heading_lines(self):
        counts = LINTER.excluded_line_counts("# Título\n| Campo | Valor |\nTexto.")
        self.assertEqual(counts["headings"], 1)
        self.assertEqual(counts["tables"], 1)


if __name__ == "__main__":
    unittest.main()
