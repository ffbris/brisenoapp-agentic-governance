---
name: write-decision-document
description: Plan, draft, integrate, and revise an analytical, scientific, technical, legal, policy, consulting, or client document intended to help a defined audience understand, decide, or act. Orchestrate evidence-led section work and two distinct Whole Problem reviews—substantive correctness and communication fitness—then optional technical clarity and Stop Slop passes. Use only when explicitly invoked as `$write-decision-document`; never invoke implicitly.
---

# Escribir un documento para una decisión

Construir el argumento antes de pulir la prosa. Tratar el documento como una herramienta para una audiencia, no como un contenedor de información.

## Preparar el contrato

Definir:

- audiencia y decisión o acción;
- propósito comunicativo;
- tesis o mensaje principal;
- corpus autorizado;
- estado de aprobación de hallazgos;
- conceptos canónicos;
- decisiones cerradas;
- restricciones de confidencialidad;
- formato, extensión y criterios de aceptación.

Adaptar [assets/DOCUMENT_BRIEF.md](assets/DOCUMENT_BRIEF.md) cuando reduzca retrabajo.

## Flujo

1. Diseñar la arquitectura: pregunta, tesis, evidencia, implicaciones y acción.
2. Asignar a cada sección una función y evidencia; evitar secciones sin trabajo decisional.
3. Redactar o mejorar secciones conservando trazabilidad y estado epistémico.
4. Integrar transiciones, referencias cruzadas, cifras, conceptos y conclusiones.
5. Ejecutar las revisiones de [references/review-contracts.md](references/review-contracts.md) según materialidad.
6. Corregir primero hallazgos sustantivos y después fallas comunicativas.
7. Invocar `$technical-clarity-editor` sólo si la persona pidió claridad técnica o el flujo autorizado la incluye.
8. Invocar `$brisenoapp-stop-slop` sólo si la persona pidió naturalidad o el flujo autorizado la incluye.
9. Verificar citas, cifras, anexos, formato, confidencialidad y criterio de aceptación.

No invocar skills automáticamente: proponer o ejecutar únicamente las que el usuario haya autorizado para el flujo.

## Dos revisiones de Whole Problem

### `substantive`

Preguntar:

> ¿Lo que el documento afirma está suficientemente respaldado y resuelve el problema o decisión sustantiva?

Aplicar a borradores analíticos, documentos integrados con conclusiones nuevas y versiones prefinales de alto impacto. Puede detectar la necesidad de revisar el encuadre, pero no reencuadrar.

### `communication`

Preguntar:

> Suponiendo provisionalmente que el contenido aprobado es correcto, ¿este documento lo comunica fiel y suficientemente a esta audiencia para el uso previsto?

Aplicar a documentos integrados, adaptaciones de audiencia y versiones prefinales. No reabrir metodología o alcance cerrados salvo que una contradicción haga imposible comunicar honestamente.

Usar ambas para entregables materiales con análisis o recomendaciones nuevas. Usar sólo `communication` cuando el contenido ya fue aprobado. Usar sólo `substantive` para borradores analíticos que todavía no constituyen un documento estable.

## Límites

- No permitir que edición técnica o de estilo cambie tesis, evidencia o nivel de certeza.
- No ocultar una debilidad analítica mediante mejor prosa.
- No convertir cada documento en una revisión completa del proyecto.
- No producir una nueva investigación fuera del corpus autorizado sin decisión explícita.
- No presentar actividad, extensión o número de revisiones como calidad.

## Entrega

Entregar el artefacto solicitado y, cuando sea pertinente, un estado breve:

- revisión sustantiva: no requerida / pendiente / aprobada / con bloqueos;
- revisión comunicativa: no requerida / pendiente / aprobada / con bloqueos;
- tratamientos editoriales aplicados;
- riesgos o decisiones externas al documento.
