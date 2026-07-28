---
name: writing-quality-gate
description: Detect when the user requests a reusable or outward-facing prose artifact—such as a report draft, proposal, email, message to copy and paste, publication, instructions, or final client text—and ask once which editorial treatment to use when none was specified. Do not trigger for ordinary conversation, brainstorming, temporary notes, code, plans, structured ledger entries, or intermediate analysis.
---

# Puerta de calidad editorial

Aplicar una línea base ligera y enrutar revisiones profundas. No cargar las reglas completas de otras skills.

## Línea base implícita

Aplicar silenciosamente a la prosa sustantiva:

- responder con contenido antes que metacomentario;
- evitar relleno, importancia fabricada y certeza sin respaldo;
- no imponer una estructura mecánica;
- conservar términos canónicos y grados de incertidumbre;
- evitar cierres y ofrecimientos automáticos cuando la tarea ya terminó.

No convertir esta línea base en una revisión extensa ni interrumpir conversación, exploración o respuestas breves.

## Decidir una pasada adicional

Si la persona ya pidió una skill, un perfil o un estilo, continuar sin preguntar.

Si solicita un artefacto reutilizable o externo y no indicó tratamiento, aplicar la línea base y preguntar una sola vez antes de producir la versión reutilizable:

> ¿Quieres una pasada natural, claridad técnica, ambas o ninguna?

Explicar brevemente solo cuando haga falta:

- **Natural:** invocar `$brisenoapp-stop-slop`.
- **Técnica:** invocar `$technical-clarity-editor` y seleccionar el perfil pertinente.
- **Ambas:** aplicar claridad técnica primero y naturalidad después.
- **Ninguna:** redactar sin una pasada editorial adicional.

Recordar la elección para ese artefacto y sus revisiones durante la tarea. Volver a preguntar solo si cambia materialmente la audiencia, el género documental o el uso final.

No interrumpir respuestas breves, conversación, exploración, notas internas ni contenido estructurado. No convertir una solicitud urgente o trivial en un cuestionario.
