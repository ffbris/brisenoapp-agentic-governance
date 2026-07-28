---
name: build-reproducible-analysis
description: Design, implement, or audit a reproducible quantitative, qualitative, mixed-methods, scientific, policy, or consulting analysis. Establish data contracts, provenance, raw-to-derived transformations, deterministic processing before LLM judgment, validation, uncertainty, environment capture, and traceable outputs. Use only when explicitly invoked as `$build-reproducible-analysis`; never invoke implicitly.
---

# Construir análisis reproducible

Permitir que otra persona autorizada reconstruya cómo se pasó de fuentes a resultados sin depender de la conversación.

## Procedimiento

1. Definir pregunta, decisión, unidad de análisis, población, periodo y estándar de evidencia.
2. Inventariar fuentes y permisos sin copiar datos sensibles al contexto.
3. Definir contratos de entrada, llaves, tipos, unidades, codificaciones, valores faltantes y reglas de exclusión.
4. Separar:
   - datos crudos inmutables;
   - datos intermedios reproducibles;
   - datos analíticos;
   - resultados y entregables.
5. Diseñar transformaciones deterministas para búsqueda, limpieza, unión, deduplicación, cálculo y validación.
6. Reservar el LLM para clasificación o interpretación que requiera juicio. Conservar prompt, modelo, versión, muestra, excepciones y revisión.
7. Definir pruebas de integridad y casos límite antes de procesar el volumen completo.
8. Registrar código, configuración, dependencias, semillas, fechas de corte y versiones de fuentes que puedan cambiar resultados.
9. Tratar incertidumbre, sensibilidad, explicaciones alternativas y límites según el tipo de afirmación.
10. Adaptar [assets/ANALYSIS_PLAN.md](assets/ANALYSIS_PLAN.md) sólo cuando el análisis sea material o repetible.

Consultar [references/reproducibility-contract.md](references/reproducibility-contract.md) para el contrato mínimo.

## Economía

- No programar una infraestructura extensa para un análisis único y reversible.
- Automatizar primero operaciones repetibles, voluminosas o propensas a error.
- Probar una muestra representativa antes del lote completo.
- Persistir resultados intermedios costosos e identificarlos por versión.
- Escalar al modelo o a revisión humana sólo los casos ambiguos.

## Datos sensibles

Respetar la clasificación y permisos existentes. Si se invoca `$govern-sensitive-data`, usar su plan como restricción. No anonimizar, resumir ni eliminar precisión analítica automáticamente; separar análisis autorizado de divulgación.

## Entrega

Entregar plan o auditoría con:

- pregunta y afirmaciones permitidas;
- fuentes y contratos;
- transformaciones;
- validaciones;
- puntos de juicio humano o del modelo;
- trazabilidad de resultados;
- límites y riesgos residuales;
- instrucciones mínimas para reproducir.
