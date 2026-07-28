# Política de entradas

## Materialidad

Registrar una entrada cuando pueda cambiar una decisión, resultado, interpretación, workflow o costo futuro.

## Tipos

- `DEC`: decisión.
- `ASM`: supuesto.
- `DEF`: definición.
- `EVD`: evidencia.
- `UNC`: incertidumbre o límite.
- `QUE`: pregunta abierta.
- `RES`: resultado reutilizable.
- `CHG`: cambio que sustituye conocimiento anterior.

Una decisión conceptual se registra como `DEC` o `CHG` y enlaza la entrada correspondiente de `CONCEPT_REGISTRY.json`; no copia toda su definición.

## Estado epistémico

- verificado;
- respaldado por material disponible;
- inferencia razonable;
- supuesto no probado;
- incierto.

## Estados de ciclo de vida

- propuesto;
- vigente;
- resuelto;
- sustituido;
- archivado.

## Identificadores

Usar `<TIPO>-NNN`, conservarlos al editar y no reutilizar identificadores eliminados.

## Prueba antes de añadir

1. ¿Tiene una consecuencia material?
2. ¿Ya existe una entrada equivalente?
3. ¿Existe una fuente canónica mejor?
4. ¿Puede expresarse como una afirmación breve y verificable?
5. ¿Se puede indicar procedencia y estado?

Si la respuesta a 1, 4 o 5 es no, no registrar todavía.
