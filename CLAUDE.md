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
Un error de hecho se corrige y se documenta como error; una decisión válida
superada se conserva como antecedente.

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

## Repositorio de la obra

El libro se mantiene en [neurology](https://github.com/alcyedmundo281/neurology).
Para cada futura release de Medsemiotics, revisar que el paquete y los metadatos
describan únicamente la plataforma. El archivo histórico de la versión 1.1.0
conserva su DOI de versión y su corrección documentada.
