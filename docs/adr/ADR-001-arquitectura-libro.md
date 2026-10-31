# ADR-001 — Lecciones como fuente única del texto (blog y libro)

- **Estado:** aceptado (decisiones D1–D5 de Alcy Edmundo Torres Guerrero, 30-oct-2026)
- **Alcance:** `medsemiotics`. Licencia de `lecciones/` y del libro: CC BY-NC-SA 4.0 (D4). No modifica `biosemiotics` (obra en prelanzamiento) ni el
  contrato de `medsemiotics-db`.

## Contexto

El libro de neurología (`tools/libro`, PR #33) se arma con dos regímenes de rigor:

- **Parte I:** 4 capítulos derivados de medsemiotics-db (referencias con PMID y DOI
  verificados, LR por arista).
- **Parte II:** 9 capítulos cuyo texto se copió de los módulos HTML de clase a
  `assets/libro/modulos.yaml`, **sin una sola referencia PMID**. El texto queda duplicado
  (HTML y YAML) y las copias se desincronizan.

Los módulos de neurología publicados son **13**: examen neurológico (partes 1 y 2), cefaleas,
epilepsia II, ACV y ACV isquémico, trastornos del movimiento (1 y 2), desmielinizantes,
neuromusculares, neuropatías, demencias e infecciones del SNC. Esta última no está en el libro.

A esto se suma la tercera edición de *Neurología Pediátrica* (Torres Catefort, UCE, 1991 y
1993), que hay que reconstruir con evidencia actual, y una parte nueva de neuroftalmología.

`biosemiotics` ya demostró un modelo que funciona: un `.qmd` por entidad con frontmatter
contractual, estados borrador → revisado → publicado, autores con ORCID y CRediT, límites
obligatorios y verificación de citas contra PubMed y Crossref.

## Decisión

Tres capas, como PubMed y PMC:

1. **medsemiotics-db** es el proveedor de la evidencia: conceptos, condiciones, LR y
   referencias. Las cifras de rendimiento diagnóstico entran en el texto solo por token
   (`{{lr+ HM:####}}`), la misma regla de los casos socráticos (`tools/casos/evidencia.py`).
2. **`lecciones/<id>.qmd`** es la fuente única del texto. Contrato en
   `assets/plantilla-leccion.qmd`, validado por `tools/lecciones` dentro de `npm run gates`.
3. **Las salidas son proyecciones:** el artículo del blog y el capítulo del libro salen del
   mismo archivo. `tools/libro` pasará a leer un manifiesto de lecciones y `modulos.yaml`
   se retirará cuando no quede nada que migrar.

| | Decisión |
|:-|:-|
| **D1** | Las lecciones viven en este repositorio (`lecciones/`). |
| **D2** | Se adaptan aquí el validador y el verificador de citas de biosemiotics, sin tocar ese repositorio. |
| **D3** | **Los módulos HTML se conservan íntegros**: son material de clase. El texto de cada lección se **reconstruye desde cero** en la nueva arquitectura, no se copia del HTML. Cada lección enlaza sus módulos en `modulos_html`. **Lo mismo vale para la neuropediatría**: la obra de 1993 es fuente (su transcripción queda privada, fuera del repositorio) y en el libro solo aparece citada en los bloques `legado`. |
| **D4** | **CC BY-NC-SA 4.0** para las lecciones y el libro (decisión de los autores, 30-oct-2026): uso, copia y adaptación libres con fines no comerciales; la explotación comercial (Kindle por KDP estándar, impreso con ISBN) queda reservada a los autores. No se usa KDP Select porque exige exclusividad digital y el texto sigue gratis en la web. El resto del repositorio conserva su licencia. |
| **D5** | DOI de Zenodo para la obra viva; el ISBN, ya adquirido, queda reservado para la edición impresa. |

## Mapa del libro

`lecciones/mapa.yaml` es el plan editorial, legible por máquina, como el mapa maestro de
biosemiotics: partes, autores y revisor por parte, y una fila por lección (id, título, orden,
fase, módulos de clase, páginas de la obra de 1993, condiciones de la db). El estado **no** se
escribe en el mapa: se lee de cada lección.

- `uv run python -m lecciones mapa` genera `mapa-maestro-libro.md` (versionado, no se edita).
- `uv run python -m lecciones nuevo <id>` crea la lección en borrador con todo lo que el mapa
  ya sabe: autores de la parte, procedencia de 1993, módulos y condiciones.
- `lecciones check` (dentro de los gates) exige que cada lección figure en el mapa con la misma
  parte, orden, título, módulos, condiciones y páginas de legado; que los 13 módulos enlazados
  desde `neurologia.html` estén asignados, cada uno a una sola lección; y que el mapa
  maestro generado esté al día.
- En la fase 5, `tools/libro` tomará del mapa el orden de los capítulos.

## Declaración de uso de inteligencia artificial

La ética de biosemiotics se conserva y se hace cumplir:

- `lecciones/AI-USE.md` es la declaración completa y auditable: herramientas, etapas,
  prohibiciones, decisiones que no se delegan, cómo comprobarlo y **qué ya falló**.
- `lecciones/paratextos/declaracion-ia.md` es el colofón de cada edición. Lleva el marcador
  `{N}`, que el compilador del libro sustituirá por el número de citas verificadas (fase 5).
- Cada lección declara en `uso_ia` las etapas en que intervino la IA (lista vacía si no
  intervino). Es un campo obligatorio.
- `lecciones check` rechaza la obra si falta la declaración, si falta la sección «Qué ya
  falló» o si el colofón no tiene su marcador.

## Contrato de la lección

- **Frontmatter:** `tools/lecciones/modelo.py`. Incluye identidad y lugar en el libro (`parte`,
  `orden`), `estado` con revisor humano y fecha, autores con ORCID validado (dígito de
  control) y roles CRediT, `legado` (páginas de la obra de 1993), `pregunta_clinica`,
  `abstract` de 40–80 palabras, `dialogo_clinico`, `indispensable` (≤ 5), `limites`
  (obligatorio), aristas de la db, `refs`, `medios` y `modulos_html`.
- **Cuerpo:** las secciones *Cómo se explora · Qué significa · Por qué ocurre · Qué hacer ·
  Cómo prevenir · Nuestra realidad* aparecen exactamente una vez y no vacías. Hay un bloque
  `::: {.legado}` si la lección declara procedencia de 1993.
- **Cifras:** el rendimiento diagnóstico va solo por token. Cualquier otra cifra va en un
  párrafo con cita `[@clave]` de `lecciones/refs.bib` (PMID y DOI). La cita literal del bloque
  legado queda exenta.
- **Autoría:** un autor fallecido no ejerce revisión, supervisión ni validación de la
  edición nueva. El agente nunca es revisor.
- **Imágenes:** Wikimedia Commons (página `File:`) o ilustración original con autor humano.
  Nunca fotografías de pacientes de las ediciones anteriores ni imágenes generadas con IA.
- **Estados:** en un `borrador` las faltas son alertas; desde `revisado` bloquean.
- **Verificación con red:** `uv run python -m lecciones citas`, fuera de los gates (como
  `topics:check`).

## Plan

| Fase | Entregable |
|:-|:-|
| 0 | Este contrato: plantilla, validador, verificador de citas, tests y gates. |
| 1 | Piloto vertical: «Examen neurológico del recién nacido» (cap. I, 1993), con sus conceptos y condiciones en la db; la misma lección compila como artículo y como capítulo. |
| 2 | Los 13 módulos de neurología reconstruidos como lecciones (agrupación por decidir módulo a módulo), con su evidencia. Los HTML no se tocan. |
| 3 | Neuropediatría (resto de la obra de 1993). Revisor: Alcy Ramiro Torres Guerrero. |
| 4 | Neuroftalmología. Revisora: Gladys Torres Guerrero. |
| 5 | `tools/libro` lee el manifiesto; se retira `modulos.yaml`; créditos, licencia, DOI e ISBN. |

## Consecuencias

- Hay un solo lugar donde corregir un texto y un solo lugar donde corregir una cifra (la db).
- El libro hereda el rigor de biosemiotics: ninguna lección pasa de borrador sin revisor
  humano ni con cifras sin fuente.
- Durante la migración conviven el libro actual (PR #33) y las lecciones. El libro no cambia
  hasta la fase 5.
