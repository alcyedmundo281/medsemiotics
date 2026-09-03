# medsemiotics

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22069641.svg)](https://doi.org/10.5281/zenodo.22069641)

DOI de concepto: cita siempre la última versión. La v1.0.0 quedó fija en
[10.5281/zenodo.22069642](https://doi.org/10.5281/zenodo.22069642).

Contenido escrito de **Powersemiotics**: los módulos educativos, autoevaluaciones,
presentaciones e infografías de medicina, separados del sitio corporativo.

Se publica en <https://powersemiotics.com/medsemiotics/>.

La raíz de `powersemiotics.com` vive en otro repositorio
([PowerSemiotics](https://github.com/alcyedmundo281/PowerSemiotics)) y es solo la
presentación corporativa de una página. Este repositorio reúne el contenido
educativo de Medsemiotics.

La farmacoterapia y los repositorios de medicamentos se mantienen en el portal
independiente [Farmacosemiotics](https://powersemiotics.com/farmacosemiotics/).
El árbol `farmacoterapia_racional/` y las páginas de medicamentos se retiraron de
este repositorio; la portada enlaza directamente a sus destinos externos.

El contenido clínico de POCUS evolucionó a un proyecto independiente:
[Biosemiotics](https://www.biosemiotics.net/), cuya fuente se mantiene en el
repositorio [biosemiotics](https://github.com/alcyedmundo281/biosemiotics). En
Medsemiotics permanece únicamente el análisis de implementación de POCUS en el
sistema sanitario.

## Publicación

GitHub Pages sirve la rama por defecto desde la raíz del repositorio. El sitio queda
bajo el subdirectorio `/medsemiotics/` del dominio, que es propiedad del repositorio
raíz.

- El `CNAME` **no** va aquí: lo declara el repositorio raíz, que es quien posee el
  dominio apex. Este repositorio depende de que aquel siga publicando
  `powersemiotics.com`.
- `.nojekyll` está presente para que Pages sirva los archivos tal cual, sin pasarlos
  por Jekyll.
- No hay paso de build en el despliegue: el HTML, el CSS compilado y los bundles de
  JavaScript están versionados y se sirven directamente.
- Los recursos compartidos incluyen fuentes, iconos, React y librerías alojadas
  en `assets/`. Todavía hay páginas con dependencias externas: por ejemplo,
  `neurologia/demencias.html` carga Google Fonts, Font Awesome y Tailwind desde
  servicios externos, y `reto.html` carga Google Fonts.

## Estructura del Sitio y Contenido

El portal principal (`index.html`) está organizado en tres zonas:

1. **Centro — Blog Clínico e Interactivo:** casos con referencias biomédicas,
   razonamiento bayesiano, búsqueda y filtros por especialidad, poder bayesiano,
   dificultad y disponibilidad de reto.
2. **Panel izquierdo — Lecturas Anteriores:** navegación por las cinco áreas
   locales y acceso al portal externo de Farmacosemiotics.
3. **Panel derecho — Herramientas y Recursos:** acceso al Reto Clínico
   (`reto.html`) y a las autoevaluaciones.

### Áreas Curriculares (Lecturas Anteriores)

| Área | Índice | Directorio de contenido |
| --- | --- | --- |
| Medicina y Datos | `medicina_y_datos.html` | `medicina_y_datos/` |
| Neurología | `neurologia.html` | `neurologia/` |
| Gastroenterología | `gastroenterologia.html` | `gastroenterologia/` |
| Inmunología Clínica | `inmunologia_clinica.html` | `inmunologia/` |
| Medicina e Implementación | `medicina_e_implementacion.html` | `medicina_e_implementacion/` |

Entradas y módulos destacados:

- `reto.html` — Reto Clínico (banco de autoevaluación dinámico indexado)
- `gastroenterologia-autoevaluacion.html` — Autoevaluación: ERGE
- `neurologia-autoevaluacion.html` — Autoevaluación de Neurología
- `post.html?slug=…` — Lectura de un artículo y su autoevaluación
- `blog.html` — Redirección a la portada `index.html`
- `neurologia/demencias.html` — Demencias y Trastornos Neurocognitivos
- `neurologia/trastornos-movimiento-1.html` — Atlas interactivo de Trastornos del Movimiento I
- `trastornos-movimiento-1.html` — Redirección al módulo dentro de Neurología

### Blog clínico y banco de preguntas

La **única fuente clínica** es
[medsemiotics-db](https://github.com/alcyedmundo281/medsemiotics-db): condiciones,
conceptos y referencias YAML. Cada condición debe tener un artículo en el blog,
incluidas las que no tienen LR medidos. `posts/*.md` contiene los artículos
derivados; no se corrigen allí los datos clínicos ni las preguntas.

Los bloques `grounding`, `evidencia` y `triada` conservan los hallazgos, rangos,
referencias, criterios y limitaciones del registro. `fuente` registra la revisión
del repositorio y hashes SHA-256 del texto fuente con finales de línea LF.
`assets/data/topic-images.json` aporta ilustraciones y su atribución, sin añadir
hechos clínicos.

Para reconstruir los JSON a partir de los Markdown ya sincronizados:

```bash
npm run build:blog
```

`tools/build-blog.mjs` genera los archivos que consume el navegador:

- `assets/data/blog-index.json` — Índice para la portada y sus filtros.
- `assets/data/posts/<slug>.json` — Contenido individual para `post.html`.
- `assets/data/quiz-bank.json` — Banco de preguntas para `reto.html` y los artículos.
- `assets/data/condition-posts.json` — Correspondencia condición → artículo → URL.

Los Markdown y JSON se versionan juntos. El build conserva el YAML anidado y
rechaza un LR numérico sin estado medido y referencia. Las calculadoras no
sustituyen datos ausentes por cero u otros valores, y no reducen rangos a una
estimación puntual. La validación bibliográfica pertenece a medsemiotics-db.

#### Generación desde medsemiotics-db

`tools/generate_topic.py` consulta el repositorio
[medsemiotics-db](https://github.com/alcyedmundo281/medsemiotics-db) en GitHub.
El flujo requiere Python, PyYAML y Node.js. Sin `--db-dir`, consulta GitHub y fija
la lectura a una revisión concreta al iniciar:

```bash
python -m pip install pyyaml
npm run topics:list
python tools/generate_topic.py --condition HM6011
npm run topics:sync
npm run topics:check
```

`topics:sync` **crea y actualiza todas las condiciones**, preservando los slugs y
fechas de los artículos existentes. `--condition` limita la actualización a un
identificador. Ambos regeneran los JSON. `topics:check` comprueba sin escribir la
cobertura, los artículos, sus JSON y las URLs de la base; falla ante diferencias.

Para trabajar con un checkout local (también configurable con
`MEDSEMIOTICS_DB_DIR`):

```bash
python tools/generate_topic.py --sync-all --db-dir ../medsemiotics-db
python tools/generate_topic.py --check --db-dir ../medsemiotics-db
```

En Windows se puede usar `py -3` en lugar de `python`.

#### Enlaces de vuelta a la base

Cada `condiciones/*.yaml` debe incluir en `url` la dirección del artículo:
`https://powersemiotics.com/medsemiotics/post.html?slug=<slug>`. Una dirección
existente se preserva; para un tema nuevo se usa la URL propuesta por la base o
se genera un slug estable. Después de publicar los artículos:

```bash
python tools/generate_topic.py --sync-all --db-dir ../medsemiotics-db --write-backlinks
```

Este comando comprueba el JSON servido en producción y su ID de condición antes
de modificar únicamente `url` en los registros locales de medsemiotics-db. Que
`post.html` responda HTTP 200 no demuestra que exista el artículo. Los cambios en
la base se revisan y publican desde ese repositorio; el comando no hace commits
ni pushes. La sincronización se ejecuta con estos comandos, no en segundo plano.

Pruebas del contrato y de la calculadora:

```bash
python -B -m unittest discover -s tools/tests -p test_topic_sync.py
npm run test:blog
```

### Sub-aplicaciones

Tres módulos incluyen un proyecto React/Vite con su propio `package.json`. El build
compilado está versionado; solo hay que reconstruirlo cuando cambia su fuente,
siguiendo los scripts del proyecto correspondiente. El build raíz no compila estas
sub-aplicaciones Vite.

- **`gastroenterologia/pancreatitis_reactor/`** — código fuente. Lo publicado es
  `gastroenterologia/pancreatitis_aguda/index.html`, que carga su propio
  `assets/index-*.js` y `assets/index-*.css`. El `index.html` del directorio
  `pancreatitis_reactor` es solo la entrada del servidor de desarrollo de Vite.
- **`neurologia/examen-neurologico/`** — código fuente y `dist/`. Quien consume el
  build es `neurologia/examen-neurologico-parte-1.html`, que carga
  `examen-neurologico/dist/assets/`. El `index.html` de la raíz del proyecto es la
  entrada de desarrollo.
- **`medicina_y_datos/estadisticos_descubiertos/`** — el `index.html` publicado es
  una página estática autónoma y es lo que enlaza
  `medicina_y_datos.html`. Los seis bundles de `assets/index-*.js` (~4 MB) son
  salida de build antigua y hoy no los referencia nada.

### Assets

`assets/` es compartido por todas las áreas: la hoja de estilos compilada, el logo,
las imágenes y los PDF descargables de los módulos.

## Estilos

`assets/tailwind.css` es un archivo **generado**. No se edita a mano.

La fuente es `assets/styles.css` (las tres directivas `@tailwind`) y la
configuración es `assets/tailwind.config.js`. Para regenerarlo tras cambiar clases
de Tailwind en cualquier página:

```bash
npm run build:css
```

Que equivale a:

```bash
npx tailwindcss -c assets/tailwind.config.js -i assets/styles.css -o assets/tailwind.css
```

El `content` recorre los directorios reales de contenido y los `.jsx` de los módulos
interactivos, excluyendo `node_modules` y los `dist/` de las sub-apps Vite. Los
`.bundle.js` no se escanean: las clases viven en el `.jsx` fuente.

## Sin backend

El sitio publicado sirve HTML, CSS, JavaScript y JSON estáticos. No requiere una
base de datos en ejecución, autenticación ni claves de API. La consulta a
`medsemiotics-db` pertenece al flujo de generación de contenido, no al uso del
sitio por los estudiantes. Algunas páginas sí dependen de recursos externos,
como se indica en la sección de publicación.

Las evaluaciones se corrigen en el navegador. Algunos módulos, como
`gastroenterologia/reflujo-gastroesofagico.html`, permiten descargar resultados en
JSON y CSV e imprimirlos. El Reto Clínico conserva estadísticas entre sesiones en
`localStorage`, bajo la clave
`medsemiotics_reto_stats`, y ofrece un botón para reiniciarlas.

## Módulos interactivos (React)

Ocho páginas incluyen un módulo interactivo en React. El JSX vive en un archivo
`.jsx` hermano de la página y es **la fuente**; el navegador solo recibe el
`.bundle.js` compilado. Babel ya no interviene en tiempo de ejecución.

```bash
npm run build:js
```

React y ReactDOM 18.3.1 se sirven desde `assets/vendor/react/` como globales UMD,
así que el bundle los deja como externos.

Para regenerar CSS, bundles React y los JSON del blog de una vez:

```bash
npm run build
```

## Desarrollo

Instalar dependencias:

```bash
npm install
```

Servidor estático local, que monta el sitio bajo `/medsemiotics/` igual que en
producción:

```bash
npm start
```

Abrir `http://localhost:3000/medsemiotics/`. El servidor permite configurar `PORT`
y `BASE_PATH`; abrir los HTML directamente con `file://` no reproduce las
peticiones de JSON ni las rutas del sitio publicado.

Formatear HTML y JavaScript:

```bash
npm run format
```

Lint de JavaScript:

```bash
npm run lint
```

`npm test` es todavía un marcador que termina con error; no hay una suite de
pruebas configurada en ese comando. Las comprobaciones específicas de navegación,
recursos y módulos interactivos se encuentran en `tools/verificacion/`.

## Herramientas

`tools/` contiene los compiladores de React y del blog, el generador de temas, el
servidor local y utilidades de verificación; ver [tools/README.md](tools/README.md).
No se necesita ejecutar estas herramientas para servir el sitio publicado.

Al añadir páginas, revisar sus enlaces y URL canónica, regenerar `sitemap.xml`
con `node tools/sitemap.mjs` y comprobar el resultado. El script parte de archivos
versionados y una lista fija de exclusiones; las nuevas redirecciones con
`noindex` requieren revisar esa lista.

## Migración y mantenimiento pendiente

[MIGRATION.md](MIGRATION.md) registra la migración del Google Site histórico,
los destinos canónicos y los recursos que deben recuperarse o compararse.
Entre los temas pendientes figuran epidemiología clínica y «¿Quién recibe el
dinero?», además de integraciones y auditorías de material incrustado.

El módulo de demencias todavía requiere incorporar una URL canónica y su entrada
en `sitemap.xml`, además de sustituir sus dependencias externas por recursos
locales.

## Convenciones de nombres

El árbol mezcla hoy `snake_case`, `kebab-case` y `PascalCase_Con_Guiones`. La
convención objetivo es **kebab-case** en minúsculas para directorios y archivos, pero
la unificación está pendiente: renombrar cambia URLs publicadas y exige
redirecciones.

## Licencia y cita

El contenido se publica bajo [Creative Commons Atribución-CompartirIgual 4.0
Internacional](https://creativecommons.org/licenses/by-sa/4.0/deed.es)
(CC BY-SA 4.0). El texto completo está en [LICENSE](LICENSE).

Puede reutilizarlo y adaptarlo, incluso con fines comerciales, siempre que dé
crédito y distribuya lo derivado bajo la misma licencia.

Para citar el trabajo, use los metadatos de [CITATION.cff](CITATION.cff); GitHub
genera desde ahí la cita en APA y BibTeX. `.zenodo.json` describe el depósito que
Zenodo crea en cada publicación etiquetada.
