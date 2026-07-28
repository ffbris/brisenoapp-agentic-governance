# Loop engineering

## Contrato del ciclo

Definir:

- objetivo y unidad de trabajo;
- estado de entrada y salida;
- acciones permitidas;
- evidencia de éxito;
- validación;
- estado persistente;
- presupuesto;
- condiciones de reintento, escalamiento y terminación.

## Máquina mínima

`observar → seleccionar → actuar → validar → registrar → decidir`

Estados terminales:

- completado;
- completado con reservas;
- escalado;
- fallido.

## Invariantes

- Cada unidad tiene un identificador estable.
- Una unidad validada no se repite sin causa registrada.
- El estado se guarda después de una operación costosa.
- Un reintento modifica una condición relevante.
- Dos iteraciones sin nueva evidencia obligan a cambiar estrategia o escalar.
- El validador no confía únicamente en la declaración del generador.

## Fallas

Clasificar antes de actuar:

| Tipo | Respuesta |
|---|---|
| Transitoria | Reintento acotado con backoff |
| Datos | Aislar unidad y registrar defecto |
| Lógica | Detener rama y corregir |
| Permisos | Escalar con objetivo exacto |
| Diseño | Detener y revisar arquitectura |
| Calidad | Reprocesar selectivamente o escalar |

## Observabilidad

Registrar lo necesario para reconstruir:

- versión del flujo;
- unidad y estado;
- entradas y procedencia;
- acción y herramienta;
- salida o referencia;
- validación;
- costo y duración cuando sean materiales;
- motivo de escalamiento o terminación.
