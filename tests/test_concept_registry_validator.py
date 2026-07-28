import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "maintain-concept-registry" / "scripts" / "validate_concept_registry.py"
SPEC = importlib.util.spec_from_file_location("validate_concept_registry", SCRIPT)
VALIDATOR = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


def registry(concepts):
    return {
        "schema_version": "1.0",
        "status": "draft",
        "authority_order": ["project-approved", "general-language"],
        "concepts": concepts,
    }


class ConceptRegistryValidatorTests(unittest.TestCase):
    def test_accepts_general_concept_without_indicator_fields(self):
        errors = VALIDATOR.validate(
            registry(
                [
                    {
                        "id": "causality",
                        "type": "concept",
                        "status": "current",
                        "canonical_labels": {"es": "causalidad"},
                        "definition": "Relación en la que un cambio produce otro.",
                        "scope": ["analysis"],
                        "authority": {"level": "project-approved", "source": "PROJECT.md"},
                    }
                ]
            )
        )
        self.assertEqual(errors, [])

    def test_rejects_missing_relation_target(self):
        errors = VALIDATOR.validate(
            registry(
                [
                    {
                        "id": "a",
                        "type": "concept",
                        "status": "current",
                        "canonical_labels": {"es": "A"},
                        "definition": "A.",
                        "scope": ["analysis"],
                        "authority": {"level": "project-approved", "source": "PROJECT.md"},
                        "relations": [{"type": "conflicts_with", "target": "missing"}],
                    }
                ]
            )
        )
        self.assertTrue(any("missing concept" in error for error in errors))

    def test_rejects_duplicate_canonical_label(self):
        common = {
            "type": "concept",
            "status": "current",
            "definition": "Definition.",
            "scope": ["analysis"],
            "authority": {"level": "project-approved", "source": "PROJECT.md"},
        }
        errors = VALIDATOR.validate(
            registry(
                [
                    {**common, "id": "a", "canonical_labels": {"es": "resultado"}},
                    {**common, "id": "b", "canonical_labels": {"es": "resultado"}},
                ]
            )
        )
        self.assertTrue(any("shared" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
