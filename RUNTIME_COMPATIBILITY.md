# Compatibilidad de runtimes

El núcleo portable de cada skill es:

- `SKILL.md`;
- `references/`;
- `assets/`;
- scripts de biblioteca estándar.

No presupone un proveedor, modelo ni nombre de herramienta. Cada runtime controla descubrimiento, invocación y permisos.

## Codex

Instalar las carpetas en el directorio personal de skills de Codex. `agents/openai.yaml` es un adaptador de interfaz e invocación exclusivo de Codex.

## Claude Code

Claude Code usa el estándar Agent Skills y descubre skills personales en `~/.claude/skills/` o de proyecto en `.claude/skills/`.

Para preservar la política de invocación:

- las skills explícitas deben incluir `disable-model-invocation: true` en el frontmatter de la copia instalada para Claude Code;
- `writing-quality-gate` debe omitir ese campo.

El instalador genera esa adaptación sin modificar los archivos portables del repositorio.

## Otros runtimes

Instalar el núcleo portable y mapear:

- política de invocación explícita;
- rutas de recursos;
- permisos de scripts;
- sintaxis de referencia entre skills.

Si el runtime no puede impedir invocación automática, tratar todas las skills salvo `writing-quality-gate` como instrucciones manuales y documentar la limitación. No asumir equivalencia de políticas entre runtimes.
