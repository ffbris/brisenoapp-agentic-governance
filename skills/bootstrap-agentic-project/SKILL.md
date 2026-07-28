---
name: bootstrap-agentic-project
description: Inicializar o reorganizar un proyecto para trabajo humano-agente mediante reglas operativas, contexto material, memoria trazable y evaluación proporcional. Usar únicamente cuando la persona invoque explícitamente `$bootstrap-agentic-project`; no activar por una solicitud genérica de iniciar, documentar o configurar un proyecto.
---

# Inicializar un proyecto agéntico

Crear el sistema mínimo de contexto persistente que reduzca trabajo futuro sin convertir el repositorio en un archivo de documentación.

## Procedimiento

1. Inspeccionar la estructura, instrucciones y cambios existentes. No modificar insumos originales ni sobrescribir artefactos sin leerlos.
2. Determinar, a partir de la solicitud y el repositorio:
   - propósito, audiencia y decisión que debe apoyar;
   - fuentes de verdad y carpetas de solo lectura;
   - entregables y consumidores;
   - tareas repetibles o de alto costo;
   - riesgos de error, privacidad y mantenimiento.
   - conceptos científicos, técnicos, jurídicos o analíticos cuyo significado deba permanecer estable.
3. Aplicar la prueba de materialidad de [references/artifact-selection.md](references/artifact-selection.md).
4. Proponer el conjunto mínimo de artefactos. Crear directamente los de bajo riesgo; pedir una decisión solo si dos estructuras plausibles cambiarían materialmente el proyecto.
5. Adaptar las plantillas pertinentes de `assets/`. Eliminar instrucciones y campos que no apliquen; no dejar marcadores genéricos.
6. Enlazar los artefactos entre sí y designar una única fuente canónica para cada tipo de conocimiento.
7. Verificar que:
   - `AGENTS.md` sea breve, operativo y no duplique documentación;
   - los datos o fuentes originales estén protegidos;
   - las decisiones materiales tengan procedencia;
   - cada artefacto tenga una condición de actualización;
   - el contexto activo pueda cargarse selectivamente.
8. Informar qué se creó, por qué es material y qué se omitió deliberadamente.

## Arquitectura predeterminada

Crear solo los elementos justificados:

- `AGENTS.md`: reglas obligatorias y duraderas.
- `PROJECT.md`: propósito, alcance, actores, entregables y criterios de éxito.
- `CONTEXT_POLICY.md`: fuentes canónicas, materialidad y ciclo de vida del contexto.
- `KNOWLEDGE_LEDGER.md`: índice de decisiones, supuestos, evidencia e incertidumbres.
- `CONCEPT_REGISTRY.json`: conceptos controlados, definiciones, alcance, autoridad y relaciones.
- `workflows/<nombre>.md`: especificación de un proceso recurrente.
- `EVALUATION.md`: línea base, casos de prueba y métricas si se automatizará una decisión material.

No usar el ledger como almacén universal. Enlazar documentos extensos, datos y resultados en vez de copiarlos.
Crear el registro conceptual cuando el proyecto dependa de términos definidos, varias disciplinas, traducción, regulación o distinciones capaces de cambiar conclusiones. No crearlo para vocabulario ordinario.

## Economía de contexto

- Mantener en `AGENTS.md` solo normas que deban estar presentes en casi todas las tareas.
- Cargar contexto de proyecto solo cuando la tarea lo requiera.
- Mantener el estado de ejecución separado del conocimiento durable.
- Preferir índices y enlaces a duplicación.
- Crear un archivo nuevo solo si pasa la prueba de materialidad.
- Cargar del registro conceptual solo las entradas pertinentes cuando crezca.

## Límites

- No inicializar herramientas, dependencias, repositorios remotos ni servicios externos salvo que la persona lo solicite.
- No convertir preferencias provisionales en reglas permanentes.
- No documentar hechos que puedan derivarse de forma fiable y económica del código o los datos.
- No declarar completo un artefacto que conserve campos sin resolver.
