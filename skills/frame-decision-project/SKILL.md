---
name: frame-decision-project
description: Frame a consulting, research, policy, legal, scientific, or solution-design project around the decision it must support, or assess material drift during a milestone. Distinguish continuation, extension, branch, and reframing; recommend changes and their context impact but require the user or designated decision owner to authorize restructuring. Use only when explicitly invoked as `$frame-decision-project`; never invoke implicitly.
---

# Encuadrar un proyecto de decisión

Definir el problema mínimo suficiente para orientar trabajo útil. Detectar desviaciones materiales sin convertir cada hallazgo en un nuevo proyecto.

## Seleccionar un modo

- `start`: construir el encuadre inicial.
- `drift`: comparar un hallazgo o cambio con el encuadre vigente.

No ejecutar ambos por defecto.

## Modo `start`

1. Reconstruir la solicitud literal, la decisión subyacente y el problema completo.
2. Identificar dueño de la decisión, audiencias, unidad de análisis, población, periodo, jurisdicción y uso esperado.
3. Separar preguntas necesarias de preguntas interesantes.
4. Declarar resultados, entregables, exclusiones, restricciones y costo de equivocarse.
5. Definir qué evidencia sería suficiente y qué incertidumbre puede aceptarse.
6. Definir señales materiales que obligarían a revisar el encuadre.
7. Adaptar [assets/PROJECT_FRAME.md](assets/PROJECT_FRAME.md) o actualizar `PROJECT.md`.
8. Solicitar confirmación antes de adoptar el encuadre como contexto canónico.

## Modo `drift`

Activar sólo en un hito o ante una señal material:

- cambia la decisión, su dueño o la audiencia que actuará;
- cambia población, periodo, jurisdicción o unidad de análisis;
- la evidencia contradice un supuesto rector;
- aparece una pregunta separable con evidencia o entregable propio;
- cambia el estándar de evidencia, el criterio de éxito o la lógica del entregable;
- el nuevo trabajo obligaría a sustituir contexto canónico.

No considerar desviación material una aclaración local, una nueva fuente compatible, una corrección editorial ni un hallazgo previsto por el diseño.

Comparar con [references/drift-decisions.md](references/drift-decisions.md) y recomendar exactamente una:

- `continue`: registrar el aprendizaje y continuar;
- `extend`: modificar elementos acotados dentro del mismo proyecto;
- `branch`: abrir una pregunta separable que conserve vínculo con la decisión matriz;
- `reframe`: sustituir el encuadre porque cambió su lógica gobernante.

## Autoridad

La skill detecta, compara y recomienda. No debe:

- reescribir autónomamente `PROJECT.md`;
- crear una rama;
- invalidar resultados existentes;
- cambiar alcance, presupuesto o entregables;
- decidir que un concepto o conclusión dejó de ser válido.

Presentar el impacto previsto sobre contexto, resultados, costo y trazabilidad. Esperar autorización explícita del usuario o del dueño designado antes de materializar la decisión.

## Entrega

Incluir:

- modo y disparador;
- encuadre vigente y cambio observado;
- clasificación recomendada;
- evidencia y grado de confianza;
- artefactos afectados;
- resultados que permanecen válidos;
- decisión humana requerida.

Si no hay cambio material, decir `continue` y evitar producir documentación adicional.
