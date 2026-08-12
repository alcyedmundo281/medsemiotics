# tools/

Utilidades de desarrollo. **Nada de aquí forma parte del sitio publicado**: no se
enlaza desde ninguna página y no hace falta para servir el contenido.

## `build-js.mjs`

Compila con esbuild los módulos interactivos en React. Lee cada `.jsx` —que es la
fuente— y produce el `.bundle.js` hermano que carga la página. React y ReactDOM
llegan como globales UMD desde `assets/vendor/react/`, así que quedan fuera del
bundle.

```bash
npm run build:js
```

Hay que ejecutarlo tras cualquier cambio en un `.jsx`, porque GitHub Pages no
compila nada: publica lo que está commiteado.

## `local-server.js`

Servidor estático que monta el repositorio bajo el prefijo `/medsemiotics/`, igual
que en producción. Sin él, las rutas relativas se comportan distinto en local que en
`powersemiotics.com/medsemiotics/`.

```bash
npm start
```

Escucha en `http://localhost:3000/medsemiotics/`. Se puede cambiar con las variables
`PORT` y `BASE_PATH`.
