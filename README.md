# Briseño, ayúdame a iniciar

Una guía abierta para comenzar y conducir proyectos con inteligencia artificial de manera ordenada, clara y responsable.

Está pensada para estudiantes, docentes, consultores, investigadores y equipos que usan IA para desarrollar proyectos, analizar información, crear aplicaciones o preparar documentos. Ayuda a que la IA:

- entienda qué se espera del proyecto;
- conserve las decisiones importantes;
- use el contexto y el cómputo con cuidado;
- distinga datos, supuestos e interpretaciones;
- mantenga conceptos consistentes;
- produzca resultados que puedan revisarse;
- deje las decisiones importantes en manos de las personas.

No es necesario saber programar. Algunas funciones avanzadas incluyen scripts, pero la mayor parte del trabajo se realiza conversando con la IA.

## Qué necesitas antes de empezar

### 1. Una aplicación de IA que pueda trabajar con archivos locales

La experiencia más sencilla se obtiene con la aplicación de escritorio de Codex. Claude Code también puede utilizar la colección, aunque su interfaz está más orientada a personas familiarizadas con la terminal.

Trabajar con archivos locales permite que la IA cree y mantenga documentos, código y contexto dentro de una carpeta controlada.

### 2. Una carpeta local exclusiva para el proyecto

Crea una carpeta por proyecto y ábrela como espacio de trabajo en la aplicación. Puede estar vacía al comenzar.

Evita usar como proyecto toda la carpeta de Descargas, el Escritorio completo o una ubicación donde se mezclen archivos personales sin relación.

### 3. La colección de skills instalada

La colección completa está disponible en:

https://github.com/ffbris/briseno-ayudame-a-iniciar

No es necesario instalar cada skill por separado. Puedes descargar o clonar el repositorio y utilizar el instalador incluido. También puedes pedir a tu asistente:

```text
Instala la colección de skills de
https://github.com/ffbris/briseno-ayudame-a-iniciar
para esta aplicación. Antes de modificar archivos existentes,
explícame qué vas a cambiar.
```

### 4. Abrir la carpeta en la aplicación

Inicia la tarea desde la carpeta específica del proyecto. Una conversación general sin acceso a esa carpeta no podrá mantener de la misma manera los archivos, decisiones y resultados.

### 5. Una idea inicial

No necesitas tener requisitos técnicos ni un plan completo. Describe qué quieres lograr, para quién y cualquier restricción que ya conozcas.

En Codex:

```text
Usa $briseno-ayudame-a-iniciar.
Quiero crear una aplicación para que mis estudiantes registren
y comparen sus proyectos. Ayúdame a definir por dónde empezar.
```

En Claude Code:

```text
/briseno-ayudame-a-iniciar
Quiero crear una aplicación para que mis estudiantes registren
y comparen sus proyectos. Ayúdame a definir por dónde empezar.
```

La skill formulará las preguntas necesarias, propondrá el primer alcance y señalará las capacidades adicionales que hagan falta.

## Recomendado para código o ciencia de datos

- **Git:** permite recuperar cambios y entender cómo evolucionó el proyecto.
- **Una cuenta de GitHub:** resulta útil para respaldo remoto, colaboración y publicación, pero no es obligatoria para comenzar.
- **Una decisión inicial sobre confidencialidad:** identifica si trabajarás con datos personales, institucionales, de clientes o regulados.
- **Una ubicación para datos pesados:** Git no debe convertirse en almacén de bases grandes o archivos confidenciales.

La skill puede ayudarte a configurar estos elementos y debe explicar cualquier cambio antes de realizarlo.

## ¿Qué problema busca resolver?

Cuando un proyecto con IA dura más de una sesión, es común que:

- la conversación se vuelva demasiado larga y costosa;
- la IA olvide decisiones o las interprete de otra manera;
- se creen archivos que después nadie mantiene;
- el proyecto cambie de dirección sin que quede claro cuándo ocurrió;
- se usen palabras distintas para un mismo concepto;
- una conclusión no pueda rastrearse hasta sus fuentes;
- se mejore un documento sin comprobar primero si su argumento es correcto;
- los controles de confidencialidad terminen quitando precisión al análisis.

Briseño, ayúdame a iniciar organiza estos problemas en módulos pequeños. Cada módulo tiene una responsabilidad y límites explícitos.

## ¿Qué es una skill?

Una *skill* es una guía de trabajo reutilizable para una herramienta de IA.

En vez de explicar el mismo procedimiento en cada conversación, se invoca una skill por su nombre. En Codex se utiliza `$`; en Claude Code se utiliza `/`.

Las skills no sustituyen el juicio profesional. Ayudan a organizar preguntas, documentar decisiones, detectar riesgos y producir resultados más fáciles de revisar.

## No es necesario invocar todas las skills

La colección funciona como un sistema conectado, no como una lista que deba ejecutarse completa.

En la mayoría de los casos basta con invocar la skill correspondiente a la necesidad actual:

- `$briseno-ayudame-a-iniciar` para comenzar o reencuadrar;
- `$write-decision-document` para preparar un informe;
- `$whole-problem-reviewer` para revisar un argumento;
- `$design-efficient-workflow` para mejorar un proceso repetible.

Cada skill comparte una arquitectura, conoce sus límites y señala cuándo otra especialidad podría ser necesaria. Los archivos canónicos del proyecto permiten conservar decisiones y conceptos sin repetir toda la conversación.

La integración funciona así:

1. la skill activa realiza su tarea;
2. consulta el contexto pertinente;
3. respeta decisiones y conceptos ya registrados;
4. detecta necesidades fuera de su responsabilidad;
5. propone otra skill sólo cuando podría cambiar materialmente el resultado.

La persona decide si autoriza el siguiente paso. Así se conserva la integración sin gastar contexto en revisiones innecesarias.

`$writing-quality-gate` es la única skill que puede activarse implícitamente. Las demás se ejecutan expresamente, directamente o como parte de un flujo autorizado.

## Qué puede hacer la colección

### 1. Iniciar y encuadrar un proyecto

`$briseno-ayudame-a-iniciar` distingue la solicitud inicial, la decisión, el problema completo, los límites y los criterios de éxito.

Si el proyecto se dirige a software, una aplicación web o ciencia de datos, también:

- propone un prototipo para probar primero la incertidumbre principal;
- diseña una ruta de crecimiento sin construir infraestructura prematuramente;
- recomienda Git y GitHub;
- propone qué datos y archivos deben excluirse de Git;
- revisa las capacidades disponibles;
- busca en internet skills actuales para las brechas materiales;
- presenta las sugerencias antes de instalar o ampliar el alcance.

La IA recomienda, pero no puede cambiar el alcance, publicar código ni instalar capacidades sin autorización.

### 2. Crear el contexto mínimo necesario

`$bootstrap-agentic-project` propone los archivos que vale la pena conservar: definición del proyecto, política de contexto, registro de decisiones, conceptos, workflows y criterios de evaluación.

No busca llenar el proyecto de documentación. Cada archivo debe justificar el costo de crearlo y mantenerlo.

### 3. Diseñar procesos eficientes

`$design-efficient-workflow` ayuda a decidir qué trabajo debe hacerse con código, búsqueda, modelos económicos, modelos avanzados o revisión humana.

La evaluación debe ser proporcional: no conviene gastar más en comprobar un proceso que el error o retrabajo que se intenta evitar.

### 4. Conservar decisiones y conocimiento

`$maintain-knowledge-ledger` mantiene un índice de decisiones, supuestos, evidencia, incertidumbres, preguntas abiertas y resultados reutilizables.

Este *knowledge ledger* permite responder qué sabemos, con qué respaldo, qué decidimos, qué sigue incierto y qué cambió. No es una copia de los documentos ni una transcripción de conversaciones.

### 5. Mantener conceptos consistentes

`$maintain-concept-registry` administra conceptos cuyo significado debe permanecer estable, como “causalidad”, “perspectiva de género”, “riesgo”, “beneficiario” o “impacto”.

También maneja términos jurídicos, variables, indicadores y procesos sin obligarlos a compartir el mismo tipo de ficha. No resuelve conflictos mediante sinónimos ni impone definiciones fuera de su alcance.

### 6. Construir análisis reproducibles

`$build-reproducible-analysis` documenta cómo se pasa de fuentes y datos a resultados: permisos, estructura, limpieza, transformaciones, código, modelos, validaciones e incertidumbre.

El objetivo es que una persona autorizada pueda reconstruir el análisis sin depender de la conversación original.

### 7. Trabajar con datos sensibles

`$govern-sensitive-data` ayuda a decidir qué datos pueden utilizarse, dónde pueden procesarse y con quién pueden compartirse.

No anonimiza, elimina ni generaliza datos automáticamente. Tampoco debilita conclusiones para que parezcan menos sensibles.

### 8. Revisar si el trabajo resuelve el problema

`$whole-problem-reviewer` puede revisar:

- `project`: el encuadre o una desviación;
- `substantive`: el respaldo de afirmaciones y conclusiones;
- `communication`: la capacidad de un documento para comunicar a su audiencia.

Detecta problemas y recomienda qué revisar. No edita, abre nuevas investigaciones ni toma decisiones por el equipo.

### 9. Preparar documentos para decidir o actuar

`$write-decision-document` ayuda a planear, redactar e integrar informes, propuestas, notas técnicas y documentos científicos.

Para entregables importantes, primero revisa la solidez del contenido y después la comunicación. La claridad y el estilo se trabajan al final para no pulir un argumento equivocado.

### 10. Mejorar la escritura

- `$technical-clarity-editor`: claridad científica, técnica, jurídica o instructiva;
- `$brisenoapp-stop-slop`: elimina relleno y patrones de IA sin borrar voz ni precisión;
- `$writing-quality-gate`: aplica una línea base ligera y pregunta si hace falta otra revisión.

Sólo `$writing-quality-gate` puede activarse implícitamente.

## Ejemplo de un proyecto completo

Una investigación o desarrollo podría recorrer estas etapas:

```text
1. Encuadrar la decisión y el problema.
2. Crear únicamente el contexto que será útil después.
3. Fijar los conceptos cuyo significado debe permanecer estable.
4. Diseñar y documentar el análisis o prototipo.
5. Conservar decisiones y hallazgos materiales.
6. Construir el entregable.
7. Revisar primero el contenido y después la comunicación.
8. Aplicar claridad técnica o edición natural si hace falta.
```

No hace falta invocar manualmente una skill por cada renglón. Una skill de entrada puede cubrir su etapa, utilizar el contexto compartido y recomendar el siguiente módulo. Un proyecto corto puede requerir sólo una o dos skills.

## Principios de diseño

- usar modelos principalmente cuando se necesita juicio;
- usar código, búsqueda o reglas simples cuando sean más confiables y económicos;
- trabajar con prototipos antes de construir infraestructura extensa;
- cargar únicamente el contexto pertinente;
- crear artefactos sólo cuando eviten retrabajo o conserven conocimiento material;
- distinguir hechos, inferencias, supuestos e incertidumbres;
- conservar la procedencia de datos, decisiones y resultados;
- separar análisis, edición y revisión independiente;
- automatizar señales y validaciones objetivas, no decisiones sustantivas;
- devolver a las personas las decisiones sobre alcance, significado y confidencialidad.

## Instalación

La colección utiliza el formato abierto de Agent Skills e incluye adaptaciones para Codex y Claude Code.

Desde la carpeta del repositorio:

```bash
python3 scripts/install_skills.py --runtime codex
```

Para Claude Code:

```bash
python3 scripts/install_skills.py --runtime claude-code
```

Para actualizar una instalación:

```bash
python3 scripts/install_skills.py --runtime codex --replace
```

Codex recibe enlaces al repositorio local. Claude Code recibe copias con su política de invocación adaptada. Consulta [RUNTIME_COMPATIBILITY.md](RUNTIME_COMPATIBILITY.md) para conocer las diferencias.

## Para docentes y responsables de cursos

Las skills pueden presentarse de forma gradual:

1. encuadre del problema;
2. decisiones y evidencia;
3. conceptos consistentes;
4. análisis o prototipos reproducibles;
5. revisión sustantiva;
6. comunicación y escritura.

No es necesario enseñar toda la arquitectura antes del primer uso. Cada skill puede practicarse de forma independiente y después conectarse con las demás.

## Estructura y verificación

- [ARCHITECTURE.md](ARCHITECTURE.md) explica los límites entre módulos.
- [RUNTIME_COMPATIBILITY.md](RUNTIME_COMPATIBILITY.md) explica distintos entornos.
- [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) documenta procedencia.
- El registro conceptual cuenta con un JSON Schema y un validador.
- Las pruebas automatizadas se ejecutan con GitHub Actions.

Los validadores detectan problemas estructurales y algunas reglas mecánicas. No sustituyen una revisión científica, jurídica, ética, metodológica o profesional.

## Licencia

El código original se distribuye bajo MIT. Esto permite usarlo, estudiarlo, adaptarlo y compartirlo de acuerdo con la licencia.
