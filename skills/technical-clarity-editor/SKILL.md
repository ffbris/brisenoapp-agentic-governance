---
name: technical-clarity-editor
description: Edit or draft scientific, technical, legal, regulatory, and instructional prose in Spanish or English using explicit clarity profiles, controlled terminology, and deterministic linting. Supports ultra-strict user instructions and safety procedures as well as flexible technical, scientific, and legal writing. Use only when the user explicitly invokes `$technical-clarity-editor`; never invoke implicitly.
---

# Editor de claridad técnica

Producir texto preciso, comprobable y adecuado a su género. Simplificar la forma sin reducir el contenido, alterar el alcance ni sustituir términos autorizados.

## Procedimiento

1. Identificar idioma, audiencia, género, uso final y consecuencias de una interpretación incorrecta.
2. Seleccionar un perfil:
   - `strict-instructional`: instructivos, procedimientos, seguridad y mensajes de error;
   - `technical`: manuales, especificaciones y documentación;
   - `scientific`: métodos, resultados, discusión y comunicación científica;
   - `legal`: análisis, lineamientos, contratos y texto regulado.
3. Leer solo el módulo de idioma pertinente:
   - español: [references/spanish.md](references/spanish.md);
   - inglés: [references/english.md](references/english.md).
4. Leer [references/profiles.md](references/profiles.md) para aplicar el perfil elegido.
5. Si existe `CONCEPT_REGISTRY.json`, leer las entradas pertinentes y aplicar [references/concept-governance.md](references/concept-governance.md).
6. Revisar en este orden:
   - significado, evidencia y alcance;
   - conceptos y términos;
   - actores, condiciones y acciones;
   - estructura y secuencia;
   - oraciones y palabras;
   - formato.
7. No resolver mediante estilo una contradicción, ambigüedad conceptual o afirmación sin respaldo. Señalarla por separado.
8. Cuando haya un archivo, ejecutar `scripts/technical_clarity_lint.py` con idioma, perfil y registro conceptual. Tratar el resultado como detección heurística, no certificación.
9. En `strict-instructional`, corregir todos los errores o registrar una excepción explícita. En otros perfiles, usar las advertencias como candidatos sujetos a juicio.
10. Entregar únicamente el texto solicitado, salvo que la persona pida diagnóstico o que persista un conflicto material.

## Invariantes

- Conservar cifras, unidades, citas, referencias, nombres oficiales, obligaciones, excepciones y nivel de certeza.
- Usar un término canónico por concepto dentro del alcance declarado.
- No sustituir lenguaje jurídico o científico por una palabra “simple” si cambia su efecto.
- No imponer una definición del proyecto fuera de su alcance.
- No resolver silenciosamente conflictos entre autoridades terminológicas.
- Definir en el primer uso los conceptos controlados que una audiencia general pueda interpretar de otra manera.
- Mantener separados contenido, claridad técnica y voz editorial.

## Perfil ultraestricto

En `strict-instructional`:

- usar una acción por oración y una instrucción por paso;
- usar imperativo para acciones del usuario;
- colocar la condición antes de la acción;
- nombrar al actor;
- usar voz activa;
- respetar límites duros configurados por idioma;
- presentar advertencias antes de la acción riesgosa;
- conservar literalmente controles, rutas, códigos y nombres de interfaz;
- bloquear la entrega por errores no resueltos.

Permitir excepciones solo para citas, denominaciones vinculantes, fórmulas o texto que perdería exactitud al dividirse. Explicar la excepción en una revisión comentada; no insertarla en el entregable.

## Linter

Ejecutar:

```bash
python3 scripts/technical_clarity_lint.py FILE \
  --lang es \
  --profile strict-instructional \
  --concepts CONCEPT_REGISTRY.json
```

Usar `--instruction-max-words` y `--descriptive-max-words` para límites calibrados del proyecto. Usar `--format json` para workflows. El linter aplica límites distintos por idioma, omite bloques de código y marca términos obsoletos. No confirma verdad, suficiencia jurídica, validez científica ni cumplimiento de ASD-STE100.

## Procedencia

El enfoque toma ideas generales de ASD-STE100 y de la demostración pública “The cure for AI slop is a 1986 aircraft manual”. La implementación, los módulos bilingües y el linter de esta skill son originales y no certifican conformidad con ASD-STE100. Ver [references/sources.md](references/sources.md).
