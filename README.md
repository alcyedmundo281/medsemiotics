# medsemiotics

Contenido escrito de **Powersemiotics**: los módulos educativos, autoevaluaciones,
presentaciones e infografías de medicina, separados del sitio corporativo.

Se publica en <https://powersemiotics.com/medsemiotics/>.

La raíz de `powersemiotics.com` vive en otro repositorio
([PowerSemiotics](https://github.com/alcyedmundo281/PowerSemiotics)) y es solo la
presentación corporativa de una página. Este repositorio contiene todo lo demás.

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
- No se carga nada desde ningún CDN: fuentes, iconos, React y las librerías de
  terceros están alojadas en `assets/`.

## Estructura del Sitio y Contenido

El portal principal (`index.html`) está diseñado como una aplicación de 3 zonas:
1. **Canvas Principal (Centro)**: El Blog Clínico e Interactivo con casos fundamentados en evidencia, discriminación bayesiana con cocientes de verosimilitud (LR), buscador en tiempo real y filtrado por especialidad.
2. **Panel Lateral Izquierdo (Lecturas Anteriores)**: Navegación estructurada en acordeones para las 6 áreas temáticas curriculares previas.
3. **Panel Lateral Derecho (Herramientas y Recursos)**: Acceso directo al Reto Clínico (`reto.html`), autoevaluaciones específicas y repositorios de medicamentos.

### Áreas Curriculares (Lecturas Anteriores)

| Área                      | Índice                           | Páginas                          |
| ------------------------- | -------------------------------- | -------------------------------- |
| Medicina y Datos          | `medicina_y_datos.html`          | `medicina_y_datos/` — 20         |
| Neurología                | `neurologia.html`                | `neurologia/` — 22               |
| Gastroenterología         | `gastroenterologia.html`         | `gastroenterologia/` — 23        |
| Farmacoterapia Racional   | `farmacoterapia_racional.html`   | `farmacoterapia_racional/` — 18  |
| Inmunología Clínica       | `inmunologia_clinica.html`       | `inmunologia/` — 5               |
| Medicina e Implementación | `medicina_e_implementacion.html` | `medicina_e_implementacion/` — 4 |

Además cuenta con herramientas de autoevaluación y repositorios rápidos:

- `reto.html` — Reto Clínico (banco de autoevaluación dinámico indexado)
- `gastroenterologia-autoevaluacion.html` — Autoevaluación: ERGE
- `neurologia-autoevaluacion.html` — Autoevaluación de Neurología
- `medicamentos_cronicos.html` — Repositorio de Medicamentos Crónicos
- `medicamentos_oncologicos.html` — Repositorio de Medicamentos Oncológicos
- `trastornos-movimiento-1.html` — Trastornos del movimiento (versión de raíz)

### Sub-aplicaciones

Tres módulos incluyen un proyecto React/Vite con su propio `package.json`. El build
compilado está versionado; no hace falta compilar nada para publicar.

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

El sitio es autosustentable: HTML, CSS y JavaScript estáticos, sin ningún servicio
que pueda darse de baja y llevarse funcionalidad por delante. No hay base de datos,
no hay autenticación y no hay claves de API.

Las evaluaciones se corrigen en el navegador y muestran el resultado en la propia
página. Para conservarlo, cada una ofrece descarga en JSON y CSV —generada con
`Blob` y `URL.createObjectURL`, sin salir del equipo— y una hoja de impresión. No se
pide nombre ni correo en ningún formulario, y nada se guarda entre sesiones.

## Módulos interactivos (React)

Ocho páginas incluyen un módulo interactivo en React. El JSX vive en un archivo
`.jsx` hermano de la página y es **la fuente**; el navegador solo recibe el
`.bundle.js` compilado. Babel ya no interviene en tiempo de ejecución.

```bash
npm run build:js
```

React y ReactDOM 18.3.1 se sirven desde `assets/vendor/react/` como globales UMD,
así que el bundle los deja como externos.

Para regenerar CSS y JS de una vez:

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

Formatear HTML y JavaScript:

```bash
npm run format
```

Lint de JavaScript:

```bash
npm run lint
```

## Herramientas

`tools/` contiene el compilador de los módulos React y el servidor local. Nada de
ahí forma parte del sitio publicado; ver [tools/README.md](tools/README.md).

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
