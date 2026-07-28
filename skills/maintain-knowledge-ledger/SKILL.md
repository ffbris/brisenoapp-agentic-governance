---
name: maintain-knowledge-ledger
description: Crear, depurar o actualizar un knowledge ledger como índice canónico de decisiones, supuestos, evidencia, incertidumbres, preguntas abiertas y resultados reutilizables, con procedencia y ciclo de vida. Usar únicamente cuando la persona invoque explícitamente `$maintain-knowledge-ledger`; no activar por solicitudes genéricas de resumir, documentar o tomar notas.
---

# Mantener el knowledge ledger

Conservar conocimiento material del proyecto sin duplicar documentos, datos ni historial de conversación.

## Procedimiento

1. Inspeccionar el ledger existente, el contexto canónico y los artefactos afectados.
   Si existe `CONCEPT_REGISTRY.json`, consultar las entradas pertinentes.
2. Identificar candidatos y aplicar [references/entry-policy.md](references/entry-policy.md).
3. Crear el ledger desde `assets/KNOWLEDGE_LEDGER.md` si no existe y su valor futuro justifica mantenerlo.
4. Actualizar entradas por identificador estable:
   - añadir conocimiento nuevo;
   - enlazar evidencia o artefactos;
   - marcar como sustituido lo que dejó de regir;
   - conservar la relación con la decisión anterior;
   - resolver o cerrar preguntas sin borrar su historia material.
5. Deduplicar entradas semánticamente equivalentes y escoger una formulación canónica.
6. Detectar contradicciones. No resolverlas sin evidencia; registrarlas como incertidumbre o pregunta abierta.
   No resolver conflictos terminológicos mediante sinónimos. Aplicar la autoridad y el alcance declarados o escalar.
7. Comprobar enlaces, estados, fechas y procedencia.
8. Si existe un plan de datos sensibles, respetar sus límites. Conservar conclusiones autorizadas con precisión; enlazar fuentes seguras y su clasificación de acceso sin copiar datos crudos.
9. Resumir cambios materiales, elementos obsoletos y cuestiones que requieren decisión.

## Qué registrar

- Decisiones que restringen trabajo futuro.
- Supuestos capaces de cambiar resultados.
- Definiciones operativas no obvias.
- Decisiones que adoptan, sustituyen o restringen un concepto controlado.
- Evidencia que respalda una conclusión material.
- Incertidumbres y límites con consecuencias.
- Preguntas abiertas con responsable o condición de resolución.
- Resultados costosos y reutilizables.
- Cambios que sustituyen una regla o decisión anterior.

## Qué no registrar

- Transcripciones de conversación.
- Tareas rutinarias o estado efímero de ejecución.
- Contenido ya canónico en otro archivo, salvo un enlace y su implicación.
- Definiciones completas ya vigentes en `CONCEPT_REGISTRY.json`.
- Información fácilmente derivable del repositorio.
- Opiniones sin efecto sobre decisiones o resultados.
- Secretos, credenciales o datos personales innecesarios.

## Reglas de integridad

- Usar una entrada por afirmación o decisión material.
- Distinguir hecho verificado, inferencia, supuesto e incertidumbre.
- No convertir ausencia de evidencia en evidencia de ausencia.
- Enlazar la fuente primaria o el artefacto canónico.
- Usar etiquetas canónicas dentro de su alcance y registrar la razón de cambios terminológicos materiales.
- No borrar decisiones sustituidas si explican resultados históricos.
- Mantener el ledger como índice; mover el desarrollo extenso a documentos especializados.
- No anonimizar, generalizar ni debilitar automáticamente una conclusión. Separar persistencia del dato, precisión analítica y divulgación.

## Resultado

El ledger debe permitir responder:

- ¿Qué sabemos y con qué respaldo?
- ¿Qué decidimos y por qué?
- ¿Qué sigue siendo incierto?
- ¿Qué cambió?
- ¿Qué artefactos y workflows dependen de ello?
