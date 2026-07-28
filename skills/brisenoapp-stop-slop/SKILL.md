---
name: brisenoapp-stop-slop
description: Review or edit an existing Spanish or English draft or final prose artifact to remove recognizable AI mannerisms, filler, mechanical structure, jargon, false certainty, and metacommentary without erasing voice, nuance, evidence, controlled terminology, or technical precision. Use only when the user explicitly invokes `$brisenoapp-stop-slop`; never invoke implicitly or for ordinary conversation.
---

# Brisenoapp Stop Slop

Editar para que cada frase haga trabajo real. Conservar intención, evidencia, voz, conceptos y nivel técnico. No uniformar el texto ni aplicar prohibiciones mecánicas.

## Alcance

Usar para borradores y productos finales: informes, análisis, propuestas, documentación, correos, presentaciones, resúmenes y entregables.

No asumir responsabilidad por:

- definir el problema;
- comprobar evidencia;
- resolver contradicciones;
- reorganizar la tesis;
- imponer lenguaje técnico controlado;
- certificar suficiencia científica o jurídica.

Cuando la tarea requiera límites duros, procedimientos o terminología controlada, indicar que `$technical-clarity-editor` es la herramienta pertinente. No invocarla automáticamente.

## Flujo

1. Identificar audiencia, propósito, idioma, registro y restricciones.
2. Leer `STYLE.md` cuando exista y sea pertinente; tratarlo como autoridad sobre preferencias predeterminadas.
3. Si existe `CONCEPT_REGISTRY.json`, conservar las etiquetas canónicas pertinentes. No cargar el registro completo cuando baste buscar términos concretos.
4. Detectar patrones, no palabras aisladas. Consultar [references/patterns.md](references/patterns.md).
5. Separar estilo de contenido. No ocultar una afirmación débil con mejor prosa.
6. Revisar en este orden: significado, evidencia, estructura, frases, ritmo y formato.
7. Conservar términos técnicos, cifras, citas, incertidumbre y decisiones del autor.
8. No añadir afirmaciones, resolver lagunas analíticas ni cambiar conceptos durante una edición de estilo. Señalar esos problemas por separado.
9. Entregar el texto limpio. Explicar cambios solo si la persona pide una revisión comentada o si una corrección puede alterar el sentido.

## Reglas centrales

- Abrir con el resultado, la decisión o el dato que importa. Quitar preámbulos que solo anuncian contenido.
- Nombrar actores, acciones, objetos y consecuencias.
- Reducir jerga, intensificadores, muletillas y frases que fabrican importancia.
- Romper paralelismos, contrastes, tríadas y cierres sentenciosos cuando sustituyan razonamiento.
- Variar longitud y estructura según el contenido; no simular énfasis con fragmentos.
- Usar voz activa cuando aclara responsabilidad; conservar la pasiva cuando sea adecuada al género o el actor no importe.
- Conservar adverbios que añadan precisión.
- Usar listas, encabezados y tablas solo cuando reduzcan esfuerzo de lectura.
- No inventar consenso, causalidad, certeza, urgencia ni experiencia personal.
- Distinguir hechos, inferencias, recomendaciones y dudas.
- Evitar calcos entre idiomas y respetar el registro regional.
- No sustituir términos canónicos por sinónimos para conseguir variedad.
- Respetar la voz del autor sin volver todos los textos secos o idénticos.

## Ajustar al trabajo

### Análisis e investigación

Priorizar tesis, evidencia, límites y consecuencias. No suavizar contradicciones ni convertir correlaciones en causas.

### Propuestas y clientes

Precisar alcance, responsables, entregables, dependencias y decisiones. Evitar promesas sin mecanismo.

### Documentación técnica

Describir conducta observable y conservar nombres exactos. No aplicar reglas rígidas de lenguaje controlado salvo que la persona las solicite mediante la skill pertinente.

### Comunicación breve

Responder primero. No repetir la solicitud ni cerrar con ofrecimientos automáticos.

## Revisión final

Preguntar:

- ¿La primera oración aporta contenido?
- ¿Cada afirmación importante dice quién, qué, cuánto, cómo o con qué evidencia?
- ¿Algún giro intenta parecer profundo?
- ¿La estructura refleja el tema o una plantilla recurrente?
- ¿Se conservaron excepciones, incertidumbre y términos autorizados?
- ¿El idioma suena escrito en ese idioma?
- ¿Puede cortarse algo sin perder significado, tono o utilidad?

Si la última respuesta es sí, cortar y volver a leer. No optimizar solo por brevedad.

## Referencias

- Leer [references/patterns.md](references/patterns.md) para el diagnóstico completo.
- Leer [references/examples.md](references/examples.md) cuando haga falta calibrar una transformación.
