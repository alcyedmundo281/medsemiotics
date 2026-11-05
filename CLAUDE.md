# Claude Code

Seguir [`AGENTS.md`](AGENTS.md) como contrato de ingeniería y de seguridad del repositorio.

Para editar un artículo del blog (caso socrático e imagen destacada), usar la skill
`caso-socratico` en `.claude/skills/caso-socratico/SKILL.md`: un artículo por vez, con
revisión humana antes de publicar y `npm run gates` en verde antes de cada commit.

## Error de metadatos de Zenodo v1.1.0 y corrección — 04/11/2026

v1.1.0 (`10.5281/zenodo.23862211`, concepto `10.5281/zenodo.22069641`)
archivó 622 archivos, incluido `lecciones/` con CC BY-NC-SA 4.0, pero el
registro se publicó con CC BY-SA 4.0 y un solo creador. Fue un **error de
hecho desde el origen**, no una decisión correcta superada después.
No se lo documenta como «cicatriz»: se documentan el error y su corrección.

Por decisión explícita de Alcy, el 04/11/2026 se corrigió el registro
publicado: licencia global CC BY-NC-SA 4.0 (la más restrictiva presente en
este ZIP mixto), cinco autores/titulares y nota fechada que conserva el
estado anterior y explica los ámbitos. La plataforma fuera de `lecciones/`
conserva CC BY-SA 4.0 y los terceros conservan sus propias licencias; la
etiqueta NC del agregado no les añade restricciones. No se pretende revocar
permisos previamente concedidos mediante un cambio de metadatos.

Los cinco nombres son Alcy Torres Catefort (†), Alcy Ramiro Torres Guerrero,
Gladys Torres Guerrero, Alcy Edmundo Torres Guerrero y Daniela Torres Tobar.
Gladys y Daniela quedan sin ORCID, **pendientes de verificación**; omitir un
identificador no afirma que sea inexistente. No se crea ni asigna ORCID al
autor fallecido ni se le atribuye revisión actual.

El ZIP sigue idéntico (MD5 `24f8101a68b0417b32c79dd00ccc0b8b`); DOI, versión
y fecha original también. Su LICENSE histórico enumera cuatro titulares y
no menciona a Daniela: no atribuirle un texto que no contiene. La corrección
se hace en los metadatos del registro, no dentro del archivo preservado.
v1.0.0 (`10.5281/zenodo.22069642`) no contenía `lecciones/` y no se modifica.
La evidencia anterior/posterior y la nota están en
`docs/correcciones/zenodo-v1.1.0/`.

## Congelamiento de releases hasta separar el libro

**Ningún release nuevo de medsemiotics mientras `lecciones/` siga en este
repositorio.** No crear etiquetas de publicación ni un depósito/versión nueva
que pueda heredar los metadatos globales incorrectos del agregado.
Los `CITATION.cff` y `.zenodo.json` activos describen depósitos futuros: quedan
sin cambios durante esta corrección. Se revisarán una sola vez, al concluir
la migración y verificar el paquete final. No ponerles ahora NC-SA y cinco
autores para una plataforma de la que ese trabajo va a salir. Los borradores
de metadatos futuros se retiraron del PR #55.

El plan independiente está en `docs/planes/separacion-libro-neurologia.md`.
No ejecutar la migración ni crear el repositorio o el depósito del libro.
La decisión se tomará con Alcy **no antes del 13/11/2026**; se respeta la semana
de congelamiento de biosemiotics. Este PR no se fusiona sin autorización.

El futuro libro es otra obra: tendrá un **DOI de concepto nuevo**. Debe declarar
como procedencia el DOI de versión `10.5281/zenodo.23862211` mediante un
identificador relacionado (`isDerivedFrom`), porque ese snapshot de v1.1.0
seguirá siendo el archivo de las lecciones tempranas. No usar solo el DOI de
concepto de medsemiotics, que puede pasar a resolver a una plataforma sin ellas.
