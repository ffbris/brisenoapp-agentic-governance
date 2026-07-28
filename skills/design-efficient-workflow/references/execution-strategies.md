# Estrategias de ejecución

## Comparación

Evaluar únicamente factores capaces de cambiar la arquitectura:

| Factor | Pregunta |
|---|---|
| Frecuencia | ¿Se repetirá lo suficiente para amortizar código y pruebas? |
| Volumen | ¿El contexto completo es costoso o imposible de cargar? |
| Variabilidad | ¿Las reglas cubren la mayoría de los casos? |
| Ambigüedad | ¿Qué proporción requiere juicio semántico? |
| Riesgo | ¿Cuál es el costo de un error silencioso? |
| Latencia | ¿Debe responderse en tiempo real o puede procesarse por lotes? |
| Mantenimiento | ¿Quién actualizará reglas, prompts y esquemas? |
| Reproducibilidad | ¿Debe reconstruirse el resultado exacto? |

## Patrones

### Directo

Usar el modelo directamente cuando el trabajo sea pequeño, único, contextual y difícil de formalizar.

### Compute-first

Preprocesar mediante código cuando haya volumen, transformaciones estables, deduplicación, agregación o validaciones objetivas.

### Recuperación selectiva

Buscar y cargar fragmentos relevantes cuando las fuentes sean extensas y las respuestas dependan de una fracción pequeña.

### Enrutamiento por confianza

Resolver casos rutinarios con reglas o un modelo económico; escalar únicamente casos ambiguos o de alto impacto.

### Humano en el circuito

Solicitar revisión cuando la decisión sea irreversible, regulada, sensible o tenga alto costo de error.

## Experimento mínimo

Antes de escalar:

1. seleccionar una muestra representativa;
2. incluir casos fáciles, ambiguos y extremos;
3. medir calidad, costo y duración;
4. revisar errores, no solo promedios;
5. decidir continuar, adaptar, escalar o abandonar.
