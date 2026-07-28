# Brisenoapp Agentic Governance

Una colección abierta de herramientas para trabajar con inteligencia artificial de manera más ordenada, clara y responsable.

Está pensada para estudiantes, docentes, consultores, investigadores y equipos que usan IA para desarrollar proyectos, analizar información o preparar documentos. Su propósito es ayudar a que la IA:

- entienda mejor qué se espera de un proyecto;
- conserve las decisiones importantes sin depender de una conversación interminable;
- use el contexto y el cómputo con cuidado;
- distinga entre datos, supuestos e interpretaciones;
- mantenga conceptos y términos consistentes;
- produzca análisis y documentos que puedan revisarse;
- deje las decisiones importantes en manos de las personas.

No es necesario saber programar para entender o utilizar las instrucciones. Algunas funciones avanzadas incluyen scripts de apoyo, pero la mayor parte del trabajo se realiza conversando con la IA.

## ¿Qué problema busca resolver?

Cuando un proyecto con IA dura más de una sesión, es común que aparezcan problemas como estos:

- la conversación se vuelve demasiado larga y costosa;
- la IA olvida decisiones anteriores o las interpreta de otra manera;
- se crean muchos archivos que después nadie mantiene;
- el proyecto cambia de dirección sin que quede claro cuándo ocurrió;
- se usan palabras distintas para un mismo concepto;
- una conclusión no puede rastrearse hasta sus datos o fuentes;
- se mejora la redacción de un documento sin comprobar primero si su argumento es correcto;
- se aplican controles de confidencialidad que terminan quitando precisión al análisis.

Brisenoapp Agentic Governance organiza estos problemas en módulos pequeños. Cada módulo tiene una responsabilidad concreta y límites explícitos.

## ¿Qué es una skill?

Una *skill* es un conjunto de instrucciones reutilizables para una herramienta de IA. Funciona como una guía de trabajo especializada.

En vez de explicar el mismo procedimiento cada vez, se puede invocar una skill por su nombre. Por ejemplo:

```text
Usa $frame-decision-project para ayudarme a definir este proyecto.
```

El signo `$` indica el nombre de la skill en Codex. En otras herramientas la forma de invocarla puede cambiar; por ejemplo, Claude Code utiliza `/frame-decision-project`.

Las skills de esta colección no sustituyen el juicio profesional. Ayudan a organizar preguntas, documentar decisiones, detectar riesgos y producir resultados más fáciles de revisar.

## No es necesario invocar todas las skills

La colección funciona como un sistema conectado, no como una lista que deba ejecutarse completa.

En la mayoría de los casos basta con invocar la skill que corresponde a la necesidad del momento. Por ejemplo:

- para iniciar un proyecto, usar `$frame-decision-project`;
- para preparar un informe, usar `$write-decision-document`;
- para revisar un argumento, usar `$whole-problem-reviewer`;
- para mejorar un proceso repetible, usar `$design-efficient-workflow`.

Cada skill conoce sus límites, comparte una arquitectura común y señala cuándo otra especialidad podría ser necesaria. Los archivos canónicos del proyecto —como la definición del proyecto, el registro de decisiones o el registro conceptual— permiten que las reglas acordadas sigan presentes entre etapas sin repetir toda la conversación.

Esto no significa que todas las skills se ejecuten automáticamente. La integración funciona así:

1. la skill activa realiza su propia tarea;
2. consulta el contexto pertinente;
3. respeta decisiones y conceptos ya registrados;
4. detecta si existe una necesidad fuera de su responsabilidad;
5. propone un traspaso a otra skill sólo cuando podría cambiar materialmente el resultado.

La persona decide si autoriza ese siguiente paso. Así se conserva la integración sin gastar contexto y cómputo en revisiones que el proyecto no necesita.

`$writing-quality-gate` es la única skill que puede activarse implícitamente. Su función es ligera: aplicar una línea editorial básica y preguntar si un entregable necesita una revisión adicional. Las demás se ejecutan de forma expresa, directamente o como parte de un flujo que la persona haya autorizado.

## ¿Qué puede hacer la colección?

### 1. Iniciar y encuadrar un proyecto

`$frame-decision-project` ayuda a distinguir:

- lo que se pidió literalmente;
- la decisión que realmente debe apoyarse;
- el problema completo que debe resolverse;
- los límites, entregables y criterios de éxito.

También puede revisar si un hallazgo nuevo forma parte del mismo proyecto, requiere una extensión, merece una rama separada o cambia el encuadre completo.

La IA sólo recomienda. No puede cambiar el alcance, abrir una rama ni reescribir el contexto principal sin autorización.

Ejemplo:

```text
Usa $frame-decision-project para convertir esta idea en un proyecto de investigación.
Quiero estudiar por qué disminuyó la participación en el programa y qué decisión
debería tomar la organización.
```

### 2. Crear el contexto mínimo necesario

`$bootstrap-agentic-project` propone los archivos que vale la pena conservar durante el proyecto.

Puede crear, cuando sean necesarios:

- una definición general del proyecto;
- una política para decidir qué contexto conservar;
- un registro de decisiones y conocimiento;
- un registro de conceptos;
- especificaciones de procesos repetibles;
- criterios de evaluación.

No busca llenar el proyecto de documentación. Cada archivo debe justificar el costo de crearlo y mantenerlo.

### 3. Diseñar procesos eficientes

`$design-efficient-workflow` ayuda a decidir qué trabajo debe hacerse con:

- código o reglas deterministas;
- búsqueda y recuperación de información;
- un modelo de IA económico;
- un modelo más avanzado;
- revisión humana.

La idea no es usar menos IA a cualquier costo, sino escoger la combinación que reduzca el costo total sin perder calidad, trazabilidad o control.

La evaluación también debe ser proporcional: no conviene gastar más en comprobar un proceso que el error o retrabajo que se intenta evitar.

### 4. Conservar decisiones y conocimiento

`$maintain-knowledge-ledger` mantiene un índice de:

- decisiones;
- supuestos;
- evidencia;
- incertidumbres;
- preguntas abiertas;
- resultados que vale la pena reutilizar.

Este índice se llama *knowledge ledger*. No es una copia de todos los documentos ni una transcripción de conversaciones. Su función es responder:

- ¿qué sabemos?;
- ¿con qué respaldo?;
- ¿qué decidimos?;
- ¿qué sigue siendo incierto?;
- ¿qué cambió?;
- ¿qué partes del proyecto dependen de ello?

### 5. Mantener conceptos consistentes

`$maintain-concept-registry` administra el registro conceptual del proyecto.

Sirve cuando palabras como “causalidad”, “perspectiva de género”, “riesgo”, “beneficiario” o “impacto” necesitan una definición estable. También puede manejar términos jurídicos, variables, indicadores y procesos, sin obligarlos a compartir el mismo tipo de ficha.

Cuando existen definiciones en conflicto, la skill identifica:

- qué significa cada una;
- quién o qué fuente tiene autoridad;
- en qué ámbito se aplica;
- qué documentos podrían verse afectados.

No resuelve conflictos sustantivos mediante sinónimos ni impone una definición fuera de su alcance.

### 6. Construir análisis reproducibles

`$build-reproducible-analysis` ayuda a documentar cómo se pasa de las fuentes a los resultados.

Puede utilizarse en análisis cuantitativos, cualitativos o mixtos para organizar:

- fuentes y permisos;
- estructura y calidad de los datos;
- reglas de limpieza y transformación;
- código, configuraciones y versiones;
- intervenciones de modelos de IA;
- validaciones;
- incertidumbre y límites de interpretación.

El objetivo es que una persona autorizada pueda reconstruir el análisis sin depender de recordar la conversación original.

### 7. Trabajar con datos sensibles

`$govern-sensitive-data` ayuda a decidir qué datos pueden utilizarse, dónde pueden procesarse y con quién pueden compartirse.

Separa tres cuestiones que suelen confundirse:

1. qué información necesita el análisis;
2. qué información puede recibir una herramienta de IA;
3. qué información puede divulgarse a cada audiencia.

La skill no anonimiza, elimina ni generaliza datos automáticamente. Tampoco puede debilitar conclusiones para que parezcan menos sensibles. Propone controles y señala las decisiones que corresponden a la persona responsable, al cliente o a un especialista.

### 8. Revisar si el trabajo resuelve el problema

`$whole-problem-reviewer` es un revisor independiente y acotado. Puede trabajar en tres modos:

- `project`: revisa el encuadre o una posible desviación;
- `substantive`: revisa si las afirmaciones y conclusiones están suficientemente respaldadas;
- `communication`: revisa si un documento comunica fielmente su contenido a una audiencia.

La separación es importante. Un documento puede estar bien escrito y tener un argumento incorrecto; también puede contener un análisis sólido y comunicarlo mal.

Whole Problem Reviewer detecta problemas y recomienda qué revisar. No edita el documento, no abre nuevas investigaciones y no toma decisiones por el equipo.

### 9. Preparar documentos para decidir o actuar

`$write-decision-document` ayuda a planear, redactar e integrar informes, propuestas, notas técnicas, documentos científicos y otros entregables.

Para documentos importantes, el flujo recomendado es:

```text
Definir audiencia y propósito
        ↓
Diseñar el argumento
        ↓
Redactar e integrar secciones
        ↓
Revisar la solidez del contenido
        ↓
Corregir el análisis
        ↓
Revisar la comunicación
        ↓
Mejorar claridad y estilo
        ↓
Verificar el entregable final
```

No todos los documentos necesitan todas las etapas. El flujo se ajusta al riesgo, al uso previsto y al estado del contenido.

### 10. Mejorar la escritura

La colección separa tres necesidades:

- `$technical-clarity-editor`: claridad científica, técnica, jurídica o instructiva en español e inglés;
- `$brisenoapp-stop-slop`: elimina relleno y patrones reconocibles de escritura de IA sin borrar voz ni precisión;
- `$writing-quality-gate`: aplica una línea base ligera y pregunta si un entregable necesita una revisión adicional.

Sólo `$writing-quality-gate` puede activarse de manera implícita. Las demás skills se ejecutan de forma expresa, pero sus límites, artefactos compartidos y reglas de traspaso permiten que trabajen como partes de un mismo sistema.

El editor técnico incluye comprobaciones mecánicas de extensión y términos controlados. Estas comprobaciones no certifican que un texto sea correcto, claro, científico o jurídicamente suficiente.

## Ejemplo de un proyecto completo

Una investigación para preparar una recomendación podría recorrer estas etapas:

```text
1. Encuadrar la decisión y el problema.
2. Crear únicamente el contexto que será útil después.
3. Fijar los conceptos cuyo significado debe permanecer estable.
4. Diseñar y documentar el análisis.
5. Conservar decisiones y hallazgos materiales.
6. Construir el informe.
7. Revisar primero el contenido y después la comunicación.
8. Aplicar claridad técnica o edición natural si hace falta.
```

No es necesario invocar manualmente una skill para cada renglón. Una skill de entrada puede cubrir su etapa, utilizar el contexto compartido y recomendar el siguiente módulo cuando sea material. El flujo tampoco es obligatorio: un proyecto corto puede requerir sólo una o dos skills.

## Principios de diseño

La colección sigue estas reglas:

- usar modelos de IA principalmente cuando se necesita juicio;
- usar código, búsqueda o reglas simples cuando sean más confiables y económicos;
- cargar únicamente el contexto pertinente para la tarea;
- crear artefactos sólo cuando eviten retrabajo o conserven conocimiento material;
- distinguir hechos, inferencias, supuestos e incertidumbres;
- conservar la procedencia de datos, decisiones y resultados;
- mantener separados análisis, edición y revisión independiente;
- automatizar señales y validaciones objetivas, no decisiones sustantivas;
- devolver a las personas las decisiones sobre alcance, significado y confidencialidad.

## Instalación

La colección utiliza el formato abierto de Agent Skills. Actualmente incluye adaptaciones para Codex y Claude Code.

### Instalación con el script incluido

Desde la carpeta del repositorio:

```bash
python3 scripts/install_skills.py --runtime codex
```

Para Claude Code:

```bash
python3 scripts/install_skills.py --runtime claude-code
```

Si ya existe una instalación anterior y se desea actualizar:

```bash
python3 scripts/install_skills.py --runtime codex --replace
```

Codex recibe enlaces al repositorio local. Claude Code recibe copias con su política de invocación adaptada.

Quienes no estén familiarizados con la terminal pueden pedir a su asistente de IA:

```text
Instala las skills de este repositorio para mi herramienta de IA.
Antes de modificar archivos existentes, explícame qué vas a cambiar.
```

Consultar [RUNTIME_COMPATIBILITY.md](RUNTIME_COMPATIBILITY.md) para conocer las diferencias entre herramientas.

## Para docentes y responsables de cursos

Las skills pueden presentarse de forma gradual:

1. encuadre del problema;
2. decisiones y evidencia;
3. conceptos consistentes;
4. análisis reproducible;
5. revisión sustantiva;
6. comunicación y escritura.

No es necesario enseñar toda la arquitectura antes del primer uso. Cada skill puede utilizarse como una práctica independiente y después conectarse con las demás.

El repositorio puede adaptarse a un curso, institución o proyecto. Se recomienda conservar los límites de autoridad: una adaptación no debería permitir que la IA cambie silenciosamente el alcance, los conceptos aprobados o el tratamiento de datos sensibles.

## Estructura y verificación

- [ARCHITECTURE.md](ARCHITECTURE.md) explica los límites y contratos entre módulos.
- [RUNTIME_COMPATIBILITY.md](RUNTIME_COMPATIBILITY.md) explica la instalación en distintos entornos.
- [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) documenta procedencia y fuentes.
- El registro conceptual cuenta con un JSON Schema y un validador estructural.
- Las pruebas automatizadas se ejecutan con GitHub Actions.

Los validadores detectan problemas de estructura y algunas reglas mecánicas. No sustituyen una revisión científica, jurídica, ética, metodológica o profesional.

## Licencia

El código original del repositorio se distribuye bajo la licencia MIT. Esto permite usarlo, estudiarlo, adaptarlo y compartirlo de acuerdo con los términos de la licencia.

Las fuentes intelectuales y adaptaciones de terceros se reconocen en [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
