---
name: govern-sensitive-data
description: Assess and govern the authorized use, storage, model processing, persistence, and disclosure of confidential, personal, privileged, regulated, or otherwise sensitive project data. Produce a handling and disclosure plan while preserving authorized analytical precision; never automatically redact, anonymize, delete, weaken conclusions, or modify canonical artifacts. Use only when explicitly invoked as `$govern-sensitive-data`; never invoke implicitly.
---

# Gobernar datos sensibles

Separar protección de datos, análisis autorizado y divulgación. La privacidad no autoriza a degradar conclusiones.

## Procedimiento

1. Identificar conjuntos de datos, responsables, autorización, finalidad, audiencia y ambientes de procesamiento.
2. Clasificar sensibilidad y restricciones con [references/handling-model.md](references/handling-model.md).
3. Mapear el flujo: origen, transformaciones, herramientas, persistencia, accesos y salidas.
4. Determinar el mínimo dato necesario para cada etapa, no para el proyecto entero.
5. Separar:
   - corpus analítico autorizado;
   - contexto que puede recibir un modelo;
   - artefactos internos persistentes;
   - entregables para cada audiencia.
6. Proponer controles proporcionales: acceso, ubicación, seudonimización, agregación, revisión o prohibición.
7. Preservar en el ledger conclusiones y decisiones con la precisión necesaria; enlazar la fuente segura y registrar clasificación de acceso en vez de copiar datos crudos.
8. Antes de divulgar, comparar contenido con la autorización de la audiencia.
9. Señalar decisiones que requieren al responsable de datos, cliente, asesor jurídico o usuario.

## Autoridad y no automatización

No:

- anonimizar ni redactar automáticamente;
- borrar identificadores o variables;
- sustituir resultados específicos por generalidades;
- modificar conclusiones para reducir sensibilidad;
- escribir datos personales en el ledger para “documentarlos”;
- inferir consentimiento, base jurídica o privilegio;
- bloquear análisis expresamente autorizado.

Se pueden detectar y advertir secretos técnicos de formato inequívoco, pero no transformar el archivo sin permiso. Las categorías contextuales —identidad, ubicación, expediente, organización o combinaciones reidentificables— requieren juicio humano.

## Entrega

Entregar:

- inventario y clasificación;
- matriz etapa–dato–herramienta–audiencia;
- controles necesarios;
- precisión que debe preservarse;
- decisiones humanas pendientes;
- plan de divulgación;
- riesgo residual.
