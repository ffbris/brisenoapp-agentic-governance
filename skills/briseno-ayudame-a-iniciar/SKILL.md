---
name: briseno-ayudame-a-iniciar
description: Start or reframe a consulting, research, course, software, web app, data science, policy, legal, scientific, or solution-design project around the decision and result it must support. For development or data work, require prototype-first scalable architecture, Git/GitHub guidance, visible progress reporting, and a bounded internet search for missing skills. Distinguish continuation, extension, branch, and reframing while returning material decisions to the user. Use only when explicitly invoked as `$briseno-ayudame-a-iniciar`; never invoke implicitly.
---

# Briseño, ayúdame a iniciar

Guiar a una persona desde una idea hasta un proyecto viable sin exigir que conozca de antemano la arquitectura, las skills ni las herramientas disponibles.

## Seleccionar un modo

- `start`: construir el encuadre inicial.
- `drift`: comparar un hallazgo o cambio con el encuadre vigente.

No ejecutar ambos por defecto.

## Modo `start`

1. Reconstruir la solicitud literal, la decisión subyacente y el problema completo.
2. Clasificar la dirección principal: investigación, desarrollo, datos, documento, intervención o combinación.
3. Identificar dueño de la decisión, usuarios o audiencias, unidad de análisis, población, periodo, jurisdicción y uso esperado.
4. Separar resultados necesarios de características o preguntas interesantes.
5. Declarar entregables, exclusiones, restricciones y costo de equivocarse.
6. Definir evidencia suficiente, criterios de aceptación e incertidumbre tolerable.
7. Si predomina desarrollo o ciencia de datos, aplicar [references/development-routing.md](references/development-routing.md).
8. Definir señales materiales que obligarían a revisar el encuadre.
9. Adaptar [assets/PROJECT_FRAME.md](assets/PROJECT_FRAME.md) o actualizar `PROJECT.md`.
10. Solicitar confirmación antes de adoptar el encuadre como contexto canónico.

## Desarrollo y ciencia de datos

Cuando la dirección sea claramente software, web app, automatización, código o ciencia de datos:

1. Explicar que esta familia gobernará el proyecto, pero no pretende contener todas las capacidades técnicas.
2. Inventariar primero las skills y herramientas ya disponibles.
3. Identificar capacidades materiales faltantes: prototipado, interfaz, arquitectura, pruebas, accesibilidad, seguridad, datos, despliegue u otras pertinentes.
4. Buscar en internet skills actuales sólo para esas brechas. Preferir fuentes oficiales, estándares abiertos y repositorios con licencia y mantenimiento visibles.
5. Recomendar como máximo cinco, ordenadas por necesidad. Informar procedencia, función, compatibilidad, costo de contexto y por qué son necesarias ahora.
6. No instalar, conectar ni ejecutar una skill sugerida sin autorización.

No ampliar el proyecto para justificar una skill. Si una capacidad puede esperar hasta después del prototipo, decirlo.
Si no hay acceso a internet, informar la limitación y no inventar disponibilidad, mantenimiento ni compatibilidad.

## Prototipo y arquitectura

Trabajar siempre con una arquitectura capaz de crecer, sin construir por adelantado la escala que todavía no existe:

- identificar la incertidumbre técnica o de usuario más costosa;
- construir primero el prototipo mínimo que pueda probarla;
- separar componentes mediante interfaces simples;
- conservar una ruta explícita desde prototipo hasta versión mantenible;
- definir señales que justifiquen base de datos, servicios, automatización, infraestructura o modelos más complejos;
- reutilizar código, resultados y contexto antes de generar de nuevo;
- medir costo de tokens, revisión y mantenimiento junto con cómputo.

Escalable significa que el prototipo puede evolucionar o desecharse de forma informada; no significa comenzar con arquitectura empresarial.

## Git y GitHub

Para cualquier proyecto de código o ciencia de datos:

- inspeccionar si ya existe un repositorio Git;
- proponer control de versiones local desde el inicio;
- sugerir GitHub como remoto para respaldo, colaboración y trazabilidad;
- explicar antes de inicializar, crear un remoto, hacer commit, publicar o abrir una solicitud de cambios;
- no publicar ni crear recursos externos sin autorización;
- mantener commits pequeños con propósito comprensible;
- incluir en `.gitignore` credenciales, ambientes locales, resultados regenerables y datos crudos, confidenciales o pesados;
- conservar esquemas, diccionarios, muestras pequeñas seguras e instrucciones de obtención cuando ayuden a reproducir;
- no usar Git LFS ni otro almacén de datos sin justificarlo y obtener autorización.

## Comunicación durante el trabajo

No trabajar como una caja negra. Antes de una acción material, explicar brevemente:

- qué se hará;
- por qué corresponde ahora;
- qué archivo, servicio o estado cambiará.

Después, informar resultado, validación, costo o riesgo material y siguiente decisión. Agrupar operaciones rutinarias para no saturar a la persona con mensajes.

## Modo `drift`

Activar sólo en un hito o ante una señal material:

- cambia la decisión, su dueño o la audiencia que actuará;
- cambia población, periodo, jurisdicción o unidad de análisis;
- la evidencia contradice un supuesto rector;
- aparece una pregunta separable con evidencia o entregable propio;
- cambia el estándar de evidencia, el criterio de éxito o la lógica del entregable;
- el nuevo trabajo obligaría a sustituir contexto canónico.

No considerar desviación material una aclaración local, una nueva fuente compatible, una corrección editorial ni un hallazgo previsto por el diseño.

Comparar con [references/drift-decisions.md](references/drift-decisions.md) y recomendar exactamente una:

- `continue`: registrar el aprendizaje y continuar;
- `extend`: modificar elementos acotados dentro del mismo proyecto;
- `branch`: abrir una pregunta separable que conserve vínculo con la decisión matriz;
- `reframe`: sustituir el encuadre porque cambió su lógica gobernante.

## Autoridad

La skill detecta, compara y recomienda. No debe:

- reescribir autónomamente `PROJECT.md`;
- crear una rama;
- invalidar resultados existentes;
- cambiar alcance, presupuesto o entregables;
- decidir que un concepto o conclusión dejó de ser válido.

Presentar el impacto previsto sobre contexto, resultados, costo y trazabilidad. Esperar autorización explícita del usuario o del dueño designado antes de materializar la decisión.

## Entrega

Incluir:

- modo y disparador;
- encuadre vigente y cambio observado;
- clasificación recomendada;
- evidencia y grado de confianza;
- artefactos afectados;
- resultados que permanecen válidos;
- arquitectura de prototipo y ruta de crecimiento cuando aplique;
- plan Git/GitHub y exclusiones de datos cuando aplique;
- skills técnicas sugeridas y no instaladas cuando aplique;
- decisión humana requerida.

Si no hay cambio material, decir `continue` y evitar producir documentación adicional.
