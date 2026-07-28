# Evaluación proporcional

Evaluar sólo cuando el valor esperado de detectar errores justifique el costo.

## Escalera

1. Comprobación determinista ya disponible.
2. Uno o dos casos manuales representativos.
3. Muestra acotada con casos límite.
4. Revisión con modelo sólo para dimensiones semánticas materiales.
5. Evaluación extensa sólo para flujos recurrentes, voluminosos o de alto riesgo.

No ejecutar todos los niveles por defecto.

## Presupuesto

Comparar:

`valor de evaluación = probabilidad de detectar un error × costo evitado`

con:

`costo de evaluación = cómputo + contexto + revisión + mantenimiento`

Si no puede estimarse con precisión, usar rangos y escoger la prueba más barata capaz de cambiar la decisión.

## Condiciones de salida

Detener cuando:

- se cumple el criterio de aceptación;
- otra prueba difícilmente cambiaría la decisión;
- el costo marginal supera el riesgo residual;
- el presupuesto se agota;
- el defecto requiere una decisión humana, no más evaluación.

La ausencia de una evaluación extensa no equivale a ausencia de control.
