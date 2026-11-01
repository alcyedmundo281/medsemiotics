# medsemiotics v1.1.0 — borrador de notas de la versión

> **Borrador.** Estas notas acompañan al release en borrador de GitHub; no se publican hasta que
> lo autorice Alcy Edmundo Torres Guerrero. El libro de neurología **no está publicado**: esta
> versión trae su infraestructura y una lección piloto en borrador.

DOI de concepto (cita siempre la última versión): [10.5281/zenodo.22069641](https://doi.org/10.5281/zenodo.22069641).
El DOI de esta versión lo asigna Zenodo al publicarla. La v1.0.0 sigue fija en
[10.5281/zenodo.22069642](https://doi.org/10.5281/zenodo.22069642).

## Licencias

El registro (plataforma) sigue bajo **CC BY-SA 4.0**. El directorio `lecciones/` y el libro de
neurología se publican bajo **CC BY-NC-SA 4.0**: uso, copia y adaptación libres con fines no
comerciales; la explotación comercial queda reservada a los autores (ADR-001, D4).

## Qué trae

### Arquitectura de lecciones (ADR-001)
- **`lecciones/<id>.qmd` es la fuente única del texto**: de cada lección salen el artículo del
  blog y el capítulo del libro. Contrato en `assets/plantilla-leccion.qmd`; seis secciones fijas
  (*Cómo se explora · Qué significa · Por qué ocurre · Qué hacer · Cómo prevenir · Nuestra
  realidad*), bloques `legado` con cita literal y página, y límites obligatorios.
- **`lecciones check`** (dentro de `npm run gates`) valida el contrato: las cifras de rendimiento
  diagnóstico solo entran por token desde medsemiotics-db y cualquier otra cifra lleva cita con
  PMID y DOI. **`lecciones citas`** verifica `lecciones/refs.bib` contra PubMed y Crossref.
- Un token `{{lr+ HM:concepto>HM:condición}}` resuelve contra la arista concepto→condición; si es
  ambiguo, no existe en esa revisión o no tiene la métrica pedida, falla.

### Mapa del libro
- **`lecciones/mapa.yaml`** es el plan editorial legible por máquina: partes, personas, 54
  lecciones planificadas por fases y la cobertura del sílabo; `mapa-maestro-libro.md` se genera
  de él.
- **La autoría y la licencia del libro salen del mapa**, sin valores de respaldo: autor
  fundador Alcy Torres Catefort †, Alcy Ramiro Torres Guerrero, Gladys Torres Guerrero y Alcy
  Edmundo Torres Guerrero (coordinación editorial), con ORCID donde existe.
- **El editor revisa todas las partes**; los créditos declaran que donde también es autor su
  revisión no es independiente.
- `libro qmd|build` compila solo lecciones y sus paratextos (revisadas o publicadas;
  `--incluir-borradores` para vistas previas con aviso). Las fichas de condiciones y los
  resúmenes de módulos anteriores quedan fuera de la obra, tras `--material-previo`.

### Declaración de uso de inteligencia artificial
- **`lecciones/AI-USE.md`**: herramientas, etapas, prohibiciones y decisiones que no se delegan,
  con la sección **«Qué ya falló»** (fallos documentados de esta edición y los controles que los
  impiden). Cada lección declara en `uso_ia` dónde intervino la IA; el colofón del libro está en
  `lecciones/paratextos/declaracion-ia.md`.
- La IA no genera imágenes, no produce referencias ni cifras clínicas y no revisa.

### Evidencia a una sola revisión fijada
- Blog y libro citan los mismos números: `topics:sync` fija los artículos a una revisión de
  medsemiotics-db (hoy `ea2f6e6`); las lecciones leen de `posts/` y de `lecciones/evidencia/`
  de **esa** revisión, nunca de la rama viva. Mezclar revisiones es un error de `lecciones check`.

### Exclusión de condiciones no revisadas
- **`tools/topics-excluidos.yaml`** permite sincronizar una condición con la base sin publicarla
  en el blog (con motivo obligatorio). La exclusión no afecta a las lecciones, nunca borra un
  artículo en silencio. Hoy excluye solo HM:6049 (parálisis cerebral), pendiente de su caso
  socrático y de su revisión; su evidencia queda reservada en `lecciones/evidencia/`.

### Autoría de casos y fichas
- La autoría de los casos socráticos es una lista de personas del mapa (ORCID y roles CRediT) con
  un revisor humano; las fichas del blog muestran su autor real, sin respaldos.

### Lección piloto, en borrador
- **«Examen neurológico del recién nacido»** (1 de las 54 lecciones planificadas) está **en
  borrador y sin revisor**: no forma parte de ninguna publicación del libro. Sirve para probar la
  arquitectura de punta a punta.

## Qué no es esta versión
- **No es la publicación del libro de neurología.** Ninguna lección está revisada o publicada;
  el libro por defecto sale sin lecciones hasta que una persona las revise.
- Los DOI e ISBN del libro están pendientes.
