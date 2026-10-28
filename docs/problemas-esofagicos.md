# Complemento de la última clase: problemas esofágicos

Página: `gastroenterologia/problemas-esofagicos.html`. Entrada desde una tarjeta
de `gastroenterologia.html`. No modifica el sílabo ni el banco del blog.

El usuario autorizó expresamente el uso directo de guías médicas para este módulo
el 28 de octubre de 2026, después de comprobar que medsemiotics-db, revisión
`af44eec90966a41d8052c3605c90a480ad042299`, no contiene estos temas. Esta excepción
se limita a este complemento. Las cinco guías y sus DOI aparecen en la página;
las preguntas y el comparador remiten a ellas. El material permanece identificado
como borrador pendiente de revisión clínica. No se atribuye revisión humana.

## Recursos y mantenimiento

- HTML, CSS y JavaScript autónomos; no necesitan compilación ni servicios externos.
- Ilustración local `assets/images/esofago-anatomia.jpg`, original de Wikimedia
  Commons en dominio público (SEER / NCI). Los rótulos originales están en inglés.
- Registro verificable en `assets/data/module-images.json`, separado del blog.
  La CLI admite páginas existentes de un nivel mediante `--modulo`:

  ```sh
  uv run python -m imagenes asignar gastroenterologia/problemas-esofagicos.html "File:Illu esophagus.jpg" --modulo --alt "Ilustración anatómica del esófago: trayecto desde la faringe hasta el estómago, con rótulos en inglés"
  ```

- `imagenes check` comprueba también las licencias, rutas y metadatos de módulos;
  `--online` vuelve a consultar Commons. No se inventa un identificador HM.
- Si cambia la imagen, actualizar la copia local, el `alt` y la atribución del HTML
  junto con el registro. Las guías conservan sus propias licencias.

## Verificación

Ejecutar `npm run gates`. Comprobar en navegador la tarjeta del hub, las tres
selecciones del comparador, los desplegables, la validación de preguntas sin
responder, corrección con aciertos y errores, cambio de selección y reinicio.
El resultado anterior debe desaparecer al cambiar una respuesta. Comprobar
enlaces, impresión y ausencia de desbordamiento a 320 y 390 px.

El sitemap se regenera con `node tools/sitemap.mjs` después de registrar el HTML
en Git. La autoevaluación se corrige localmente y no almacena datos del alumno.
