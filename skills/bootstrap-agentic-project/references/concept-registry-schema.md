# Esquema del registro conceptual

## Núcleo común

Cada concepto debe incluir:

```json
{
  "id": "stable-concept-id",
  "type": "analytical-framework",
  "status": "current",
  "canonical_labels": {
    "es": "término",
    "en": "term"
  },
  "definition": "Definición adoptada.",
  "scope": ["analysis"],
  "authority": {
    "level": "project-approved",
    "source": "PROJECT.md"
  }
}
```

## Campos opcionales

- `deprecated_labels`: variantes que ya no deben usarse, por idioma.
- `allowed_abbreviations`: abreviaturas autorizadas.
- `entails`: consecuencias necesarias de adoptar el concepto.
- `does_not_mean`: interpretaciones expresamente excluidas.
- `preferred_alternatives_when_unsupported`: lenguaje más débil permitido.
- `relations`: `broader_than`, `narrower_than`, `related_not_equivalent`, `conflicts_with` o `supersedes`.
- `jurisdiction`, `effective_date`: términos jurídicos o normativos.
- `unit`, `population`, `measurement_method`: variables.
- `formula`, `source`, `periodicity`: indicadores.
- `states`, `inputs`, `outputs`: procesos.

No completar campos que no apliquen. Cuando dos autoridades compitan y la precedencia no sea clara, registrar el conflicto y solicitar decisión.
