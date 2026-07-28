# Brisenoapp Agentic Governance

Familia personal y abierta de Agent Skills para proyectos de consultoría, investigación y diseño de soluciones. Gobierna encuadre, contexto, conceptos, ejecución, análisis y documentos sin trasladar automáticamente al modelo decisiones de alcance, significado o confidencialidad.

## Principios

- Usar código y recuperación selectiva antes que modelos cuando reduzcan el costo total.
- Crear contexto persistente sólo cuando sea material, trazable y mantenible.
- Conservar decisiones y conocimiento en un ledger; conservar definiciones en un registro conceptual.
- Automatizar estructura, validaciones objetivas y señales; no automatizar decisiones sustantivas.
- Separar análisis autorizado de divulgación de datos sensibles.
- Evaluar proporcionalmente al costo esperado del error.
- Mantener una sola skill implícita.

## Núcleo

- `$bootstrap-agentic-project`: materializa el contexto mínimo.
- `$frame-decision-project`: encuadra el proyecto y distingue continuación, extensión, rama y reencuadre.
- `$design-efficient-workflow`: diseña workflows compute-first, ciclos y evaluación proporcional.
- `$maintain-knowledge-ledger`: mantiene decisiones, supuestos, evidencia e incertidumbres.
- `$maintain-concept-registry`: gobierna conceptos, autoridad, alcance y cambios.
- `$whole-problem-reviewer`: revisa proyecto, sustancia o comunicación sin ejecutar cambios.
- `$write-decision-document`: construye documentos y coordina revisiones sustantivas y comunicativas.

## Extensiones

- `$build-reproducible-analysis`: diseña y audita análisis reproducibles.
- `$govern-sensitive-data`: define manejo y divulgación sin diluir conclusiones.
- `$technical-clarity-editor`: edita prosa científica, técnica, jurídica e instructiva.
- `$brisenoapp-stop-slop`: elimina patrones de IA sin borrar voz ni precisión.
- `$writing-quality-gate`: aplica una línea base ligera y pregunta por tratamiento editorial.

Sólo `$writing-quality-gate` permite invocación implícita. Las demás requieren invocación expresa.

## Instalación

El núcleo de las skills sigue el formato portable `SKILL.md` con recursos adyacentes.

```bash
python3 scripts/install_skills.py --runtime codex
python3 scripts/install_skills.py --runtime claude-code
```

Usar `--replace` para actualizar una instalación existente. Codex recibe enlaces al repositorio; Claude Code recibe copias adaptadas con su política de invocación. Consultar [RUNTIME_COMPATIBILITY.md](RUNTIME_COMPATIBILITY.md).

## Arquitectura y verificación

- [ARCHITECTURE.md](ARCHITECTURE.md): límites y contratos entre módulos.
- `python3 -m unittest discover -s tests -v`: pruebas deterministas.
- `skills/maintain-concept-registry/references/concept-registry.schema.json`: esquema formal.
- GitHub Actions ejecuta las pruebas en cada push y pull request.

Los validadores comprueban estructura y reglas mecánicas. No certifican claridad, ciencia, derecho, privacidad ni corrección analítica.

## Procedencia y licencia

El código del repositorio se distribuye bajo MIT. Las adaptaciones y fuentes intelectuales se documentan en [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
