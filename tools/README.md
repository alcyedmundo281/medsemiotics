# tools/

Utilidades de desarrollo. **Nada de aquí forma parte del sitio publicado**: no se
enlaza desde ninguna página y no hace falta para servir el contenido.

## Recurrentes

### `build-js.mjs`

Compila con esbuild los módulos interactivos en React. Lee cada `.jsx` —que es la
fuente— y produce el `.bundle.js` hermano que carga la página. React y ReactDOM
llegan como globales UMD desde `assets/vendor/react/`, así que quedan fuera del
bundle.

```bash
npm run build:js
```

Hay que ejecutarlo tras cualquier cambio en un `.jsx`, porque GitHub Pages no
compila nada: publica lo que está commiteado.

### `local-server.js`

Servidor estático que monta el repositorio bajo el prefijo `/medsemiotics/`, igual
que en producción. Sin él, las rutas relativas se comportan distinto en local que en
`powersemiotics.com/medsemiotics/`.

```bash
npm start
```

Escucha en `http://localhost:3000/medsemiotics/`. Se puede cambiar con las variables
`PORT` y `BASE_PATH`.

### `sitemap.mjs`

Regenera `sitemap.xml` a partir de las páginas versionadas, con URLs absolutas y la
fecha del último commit que tocó cada archivo.

```bash
node tools/sitemap.mjs
```

Excluye los seis índices de sección: llevan `noindex` por ser redirecciones, y
anunciar en el sitemap una URL que pide no ser indexada es una contradicción que
Search Console marca como incidencia.

---

## `migracion/`

Scripts de un solo uso, ya ejecutados. Se conservan porque documentan **cómo** se
transformó el sitio; volver a ejecutarlos sobre el árbol actual no tiene sentido.

| Script | Qué hizo |
|---|---|
| `rewrite-cdn.mjs` | Sustituyó toda referencia a CDN por rutas locales relativas |
| `fetch-fonts.mjs` | Descargó los woff2 de Google Fonts, subconjuntos latin y latin-ext, y generó los `@font-face` |
| `fix-fonts.mjs` | Cambió las utilidades de fuente para preservar la tipografía de cada página tras la migración |
| `swap-mono.mjs` | Lo mismo para las monoespaciadas |
| `migrate-tw.mjs` | Sustituyó el `<script>` del CDN de Tailwind por el `tailwind.css` local |
| `extract-jsx.mjs` | Extrajo el `<script type="text/babel">` de cada página a un `.jsx` fuente |
| `inventory.mjs` | Inventarió los `tailwind.config` en línea de las 23 páginas y detectó las colisiones entre ellos |
| `canonical.mjs` | Insertó el `<link rel="canonical">` absoluto en las 107 páginas |
| `licencia-pie.mjs` | Sustituyó el «todos los derechos reservados» del pie por el aviso CC BY-SA |
| `fix-eol.mjs` | Comparó el fin de línea de cada archivo modificado contra su versión en `HEAD` |

Ese último tiene su historia: dos scripts convirtieron archivos CRLF a LF sin
querer, y el diff resultante marcaba el archivo entero como modificado. Comprobar el
EOL antes de commitear dejó de ser opcional.

## `verificacion/`

Comprobaciones contra un navegador real o contra producción. Se reejecutan cuando
haga falta.

| Script | Qué comprueba |
|---|---|
| `crawl-prod.mjs` | Extrae toda referencia local de las páginas y la pide a producción. Es la prueba real de enlaces rotos y de caja de nombres |
| `case-audit.mjs` | Caja de nombres en estático: Windows no distingue mayúsculas, Pages sí |
| `prod-browser.mjs` | Peticiones externas, errores de consola y fuentes realmente aplicadas |
| `interact.mjs` · `interact2.mjs` | Que los módulos React monten y respondan. **Usa el segundo**: el primero pulsaba el primer control, que suele ser la pestaña ya activa, y daba falsos negativos en 7 de 8 páginas |
| `compare.mjs` | Render antes y después de una migración, sobre dos servidores |
| `diff.mjs` · `diff2.mjs` | Diff de estilos computados. **Usa el segundo**: alinea por selector en vez de por índice, que es lo que hace comparables dos árboles distintos |
| `typo.mjs` | Tipografía computada de `body` y encabezados, página por página |
| `shots.mjs` | Capturas para comparación visual |
| `check-classes.mjs` · `check2`–`check6` | Iteraciones sucesivas de la misma pregunta: qué clases usadas en las páginas no están en el `tailwind.css` generado. **`check6` es la versión buena**; recoge la clase en cualquier posición del selector, incluidas `group-hover:` y las variantes escapadas. Las anteriores se quedan como registro de por qué hicieron falta seis intentos |

## Lo que no está aquí

Las herramientas que prueban el `404.html` y las fuentes de la portada viven en el
repositorio del sitio de usuario
([alcyedmundo281.github.io](https://github.com/alcyedmundo281/alcyedmundo281.github.io)),
que es a quien pertenecen.
