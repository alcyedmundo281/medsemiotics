# Claude Code

Seguir [`AGENTS.md`](AGENTS.md) como contrato de ingeniería y de seguridad del repositorio.

Para editar un artículo del blog (caso socrático e imagen destacada), usar la skill
`caso-socratico` en `.claude/skills/caso-socratico/SKILL.md`: un artículo por vez, con
revisión humana antes de publicar y `npm run gates` en verde antes de cada commit.

## Cicatriz de Zenodo v1.1.0 — conservar el archivo histórico

El DOI de concepto `10.5281/zenodo.22069641` resolvía, en la comprobación del
04/11/2026, a v1.1.0 (`10.5281/zenodo.23862211`). Su ZIP de 622 archivos incluye
`lecciones/` y su `LICENSE.md` bajo CC BY-NC-SA 4.0; los metadatos globales
indican CC BY-SA 4.0 y un solo creador. Ese LICENSE archivado nombra cuatro
titulares: Alcy Torres Catefort (†) y sus herederos, Alcy Ramiro Torres Guerrero,
Gladys Torres Guerrero y Alcy Edmundo Torres Guerrero. Daniela Torres Tobar
figura en la fuente actual, no en ese texto histórico.

v1.0.0 (`10.5281/zenodo.22069642`) tiene 459 archivos y no incluye `lecciones/`
ni el libro compilado. No atribuirle automáticamente la misma incoherencia.
Se inspeccionaron ambos ZIP y se verificaron sus MD5 publicados; evidencia
en `docs/propuestas/v1.2.0/alcance-zenodo.json`.

**Lo archivado, archivado queda.** Por decisión de Alcy no se sustituyen los
archivos ni se editan los registros publicados para hacerlos parecer
corregidos. Editar técnicamente metadatos no borra el historial ni revoca
permisos previos. v1.1.0 se supera con una versión nueva, no se reescribe.
Cualquier nota sobre el registro antiguo es solo una propuesta local y
requiere una decisión nueva para publicarse.

Las tres vías para v1.2.0 están en `docs/propuestas/v1.2.0/README.md`.
**Ninguna está elegida ni ejecutada.** No crear etiqueta, release, depósito o
DOI desde estos borradores antes de que Alcy decida objeto, alcance y licencia.
Los `CITATION.cff` y `.zenodo.json` de esa carpeta son propuestas no activas:
no sustituyen a los de la raíz. No trasladar ni editar lecciones o el libro
en este PR. No usar una lista CFF de licencias para repartir ámbitos: el
esquema la interpreta como alternativas OR.

Gladys Torres Guerrero y Daniela Torres Tobar no tienen ORCID todavía: se
omiten y solo se añadirán cuando lo comuniquen. Alcy Torres Catefort (†) es
autor fallecido; no se crea ni asigna ORCID en su nombre.
