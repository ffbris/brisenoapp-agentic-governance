# Arquitectura

Briseño, ayúdame a iniciar separa responsabilidades para evitar que una skill acumule autoridad.

## Núcleo

- `bootstrap-agentic-project`: materializa contexto mínimo.
- `briseno-ayudame-a-iniciar`: encuadra, orienta prototipos y propone decisiones de desviación.
- `design-efficient-workflow`: diseña ejecución y evaluación proporcional.
- `maintain-knowledge-ledger`: conserva conocimiento material.
- `maintain-concept-registry`: gobierna conceptos.
- `whole-problem-reviewer`: revisa independientemente.
- `write-decision-document`: construye entregables orientados a decisiones.

## Extensiones

- `build-reproducible-analysis`: análisis y trazabilidad.
- `govern-sensitive-data`: manejo y divulgación autorizados.
- `technical-clarity-editor`: claridad técnica bilingüe.
- `brisenoapp-stop-slop`: edición natural.
- `writing-quality-gate`: única puerta implícita.

## Contratos

- Framing detecta y recomienda; el usuario autoriza cambios canónicos.
- Whole Problem revisa; no edita, investiga ni decide.
- Document Writing orquesta sólo revisiones autorizadas.
- Ledger enlaza conceptos y fuentes; no los duplica.
- Concept Registry gobierna significado; no propaga cambios sin autorización.
- Reproducible Analysis conserva precisión y respeta el plan de datos.
- Sensitive Data gobierna uso y divulgación; no altera análisis ni conclusiones.
- Technical Clarity conserva significado; Stop Slop conserva precisión y voz.

## Flujo documental material

`contrato → arquitectura → secciones → integración → revisión sustantiva → corrección → revisión comunicativa → corrección → edición autorizada → verificación`

Whole Problem usa un solo target por revisión:

- `project`;
- `substantive`;
- `communication`.

Un hallazgo sustantivo puede recomendar revisar el encuadre, pero vuelve a `briseno-ayudame-a-iniciar`. Un bloqueo sustantivo detectado durante comunicación se reporta sin abrir investigación.
