# Enrutamiento para desarrollo y datos

## Prototipo primero

Definir:

- usuario y tarea principal;
- hipótesis o incertidumbre más costosa;
- recorrido mínimo que la prueba;
- criterio observable de aprendizaje;
- límite de tiempo, tokens y complejidad;
- decisión posterior: desechar, iterar o profundizar.

No construir autenticación, multitenencia, microservicios, infraestructura distribuida ni automatización extensa si el prototipo no los necesita para probar su hipótesis.

## Ruta de crecimiento

Identificar sin implementar por adelantado:

- límites entre interfaz, lógica, datos y servicios;
- contratos que deben permanecer estables;
- componentes desechables;
- riesgos de seguridad y privacidad;
- señales de volumen, colaboración o confiabilidad que justificarían profundizar la arquitectura.

## Búsqueda de skills

Buscar sólo capacidades ausentes y necesarias para la siguiente etapa. Evaluar:

- compatibilidad con el runtime;
- alcance y autoridad solicitada;
- mantenimiento reciente;
- licencia y procedencia;
- dependencias y permisos;
- costo de contexto;
- solapamiento con capacidades existentes;
- evidencia de uso o pruebas.

Preferir pocas skills profundas a una colección grande y redundante. Presentar la recomendación antes de instalar.

## Git y datos

Recomendar `.gitignore` para:

- credenciales y archivos de entorno;
- bases de datos locales;
- datos crudos, sensibles o pesados;
- modelos y resultados regenerables de gran tamaño;
- cachés, ambientes y artefactos de compilación.

Conservar cuando sea seguro:

- esquema y diccionario de datos;
- muestra pequeña anonimizada o sintética;
- script de descarga o preparación;
- checksums, versiones y fechas de corte;
- instrucciones para reconstruir resultados.

Git no sustituye un almacén de datos ni un sistema de respaldo especializado.
