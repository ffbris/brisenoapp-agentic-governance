---
name: design-efficient-workflow
description: Diseñar, revisar o mejorar un workflow agéntico reutilizable optimizando costo total, uso de contexto, calidad, trazabilidad y mantenimiento; incluye estrategia compute-first, estados, validaciones, presupuestos, reintentos y condiciones de salida. Usar únicamente cuando la persona invoque explícitamente `$design-efficient-workflow`; no activar ante solicitudes genéricas de automatización o planificación.
---

# Diseñar un workflow eficiente

Diseñar el flujo de menor costo total que preserve la calidad y el control requeridos.

## Principio rector

Reservar el modelo para trabajo que requiera juicio. Usar recuperación selectiva y código determinista para buscar, filtrar, limpiar, deduplicar, transformar, agregar y validar cuando resulte más económico en el ciclo de vida completo.

No asumir que programar primero siempre es mejor. Comparar:

`costo total = cómputo + contexto + desarrollo + supervisión + corrección + mantenimiento`

## Procedimiento

1. Definir el resultado, consumidor, frecuencia, volumen, tolerancia al error y costo de fallo.
2. Separar las operaciones en:
   - deterministas;
   - recuperables mediante búsqueda;
   - semánticas rutinarias;
   - ambiguas o de alto impacto;
   - reservadas para revisión humana.
3. Comparar estrategias con [references/execution-strategies.md](references/execution-strategies.md). Mostrar opciones solo cuando difieran materialmente en costo, calidad o mantenimiento.
4. Diseñar el ciclo con [references/loop-engineering.md](references/loop-engineering.md).
5. Adaptar `assets/WORKFLOW_SPEC.md` y eliminar campos que no apliquen.
6. Diseñar una prueba pequeña antes del procesamiento completo:
   - muestra representativa;
   - casos límite;
   - criterio de aceptación;
   - presupuesto inicial.
   Aplicar [references/proportional-evaluation.md](references/proportional-evaluation.md): la evaluación no debe costar más que el error o retrabajo que pretende evitar.
7. Definir persistencia, caché, checkpoints e idempotencia para evitar repetir trabajo costoso.
8. Separar generación y validación cuando el riesgo lo justifique.
9. Registrar versiones de código, reglas, modelos, prompts, fuentes y esquemas que afecten la reproducibilidad.
10. Verificar que el flujo pueda detenerse, reanudarse y auditarse sin depender de la conversación.

## Orden de preferencia

Usar el nivel más bajo que alcance la calidad requerida:

1. Función o herramienta determinista existente.
2. Recuperación selectiva.
3. Código de preprocesamiento o validación.
4. Modelo económico para casos rutinarios.
5. Modelo avanzado para ambigüedad o alto impacto.
6. Revisión humana según riesgo.

Aplicar escalamiento selectivo: no elevar todo el lote por unos pocos casos difíciles.

## Reglas de ciclo

- Acotar por iteraciones, tiempo, costo, ausencia de progreso o combinación.
- Medir progreso mediante nueva evidencia, reducción de incertidumbre o unidades validadas.
- Tras dos iteraciones consecutivas sin progreso, cambiar de estrategia o escalar.
- Reintentar solo errores plausiblemente transitorios; no repetir ciegamente.
- Guardar estado después de cada unidad costosa.
- Hacer operaciones idempotentes o detectar trabajo ya realizado.
- Definir estados terminales: completado, completado con reservas, escalado o fallido.
- Detener la evaluación cuando el criterio de aceptación se cumpla, la información adicional no pueda cambiar la decisión o se agote su presupuesto.

## Entrega

Entregar:

- recomendación de arquitectura;
- alternativas descartadas y razón material;
- especificación ejecutable del flujo;
- presupuesto y estrategia de escalamiento;
- validaciones y condiciones de salida;
- riesgos residuales y señales de revisión.

No presentar actividad, número de iteraciones ni volumen procesado como evidencia suficiente de calidad.
