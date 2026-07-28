# Selección de artefactos

## Prueba de materialidad

Crear o conservar un artefacto solo si cumple al menos una condición:

- evita reabrir una decisión importante;
- conserva conocimiento que no puede inferirse de manera fiable y económica;
- registra una definición, restricción o supuesto que cambia resultados;
- permite reproducir un proceso o resultado;
- coordina varias personas, agentes o etapas;
- conserva procedencia necesaria para auditar un entregable;
- reduce de forma plausible el contexto requerido en ejecuciones futuras.

Si no cumple ninguna, mantenerlo en el contexto temporal de la tarea.

## Selección

| Necesidad | Artefacto canónico |
|---|---|
| Reglas aplicables a casi toda tarea | `AGENTS.md` |
| Propósito, alcance y audiencia | `PROJECT.md` |
| Gobernanza del contexto | `CONTEXT_POLICY.md` |
| Decisiones y conocimiento material | `KNOWLEDGE_LEDGER.md` |
| Conceptos, términos y definiciones controladas | `CONCEPT_REGISTRY.json` |
| Proceso recurrente | `workflows/<nombre>.md` |
| Calidad comparable entre versiones | `EVALUATION.md` |
| Decisión técnica extensa | `docs/decisions/<id>.md` |
| Metodología extensa | `docs/methods/<nombre>.md` |

## Ciclo de vida

Cuando sea útil, incluir:

- propósito;
- autoridad o responsable;
- estado: borrador, vigente, sustituido o archivado;
- última actualización;
- condición de actualización;
- enlaces canónicos;
- exclusiones.

Antes de crear un archivo, buscar si otro artefacto ya cumple la función. No duplicar la misma verdad.

## Registro conceptual

Crearlo si una variación terminológica puede cambiar interpretación, análisis, obligación o interoperabilidad. Usar identificadores conceptuales independientes del idioma y campos opcionales según tipo:

- concepto o marco: implicaciones y exclusiones;
- término jurídico: jurisdicción, fuente y vigencia;
- variable: unidad, población y método;
- indicador: fórmula, fuente y periodicidad;
- proceso: estados, entradas y salidas.

No forzar conceptos generales dentro de un esquema para indicadores.
