# Instrucciones para agentes

Este repositorio es público y publica material educativo de medicina. No se versionan
credenciales, tokens, datos de estudiantes ni información clínica de pacientes reales.

## Contrato de ingeniería

- **Fuente clínica única:** [medsemiotics-db](https://github.com/alcyedmundo281/medsemiotics-db).
  `posts/*.md` y `assets/data/posts/*.json` son derivados: se regeneran con
  `tools/generate_topic.py` y no se editan a mano. Un error clínico se corrige en la base.
- **Casos socráticos (ABP dirigido):** viven en `casos/HM####.yaml` y siguen la skill
  [`caso-socratico`](.claude/skills/caso-socratico/SKILL.md). Aportan contexto clínico; el foco
  sigue siendo la evidencia de la base, que entra al texto solo por tokens.
- **Imágenes destacadas:** obligatorias, de Wikimedia Commons y en dominio público o CC0,
  registradas con `python -m imagenes asignar`, que verifica la licencia en Commons.
- **La salida de un LLM es un borrador.** Un caso solo se publica con la aprobación explícita
  de una persona nominada como `autoria.revisor`. El agente no se nombra revisor.
- **Fechas:** no se inventan ni retrotraen fechas de publicación o revisión.
- **Fin de línea:** cada archivo conserva el suyo (hay archivos CRLF y LF). Comprobar con
  `git diff --stat` que una edición no reescribe el archivo entero.

## Gates

Python 3.12 con `uv`. Antes de proponer un merge, todo en verde:

```bash
npm run gates
```

Equivale a Ruff (lint y formato), mypy estricto, pytest, `casos check`, `imagenes check`,
ESLint, `build-blog --check` y los tests del blog. `npm run topics:check` además compara los
artículos con medsemiotics-db (requiere red o `--db-dir`).

Se trabaja en una rama, con cambios revisables y un commit por artículo editado.
