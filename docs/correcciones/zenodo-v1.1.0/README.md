# Corrección de metadatos de medsemiotics v1.1.0

**Publicada el 04/11/2026**, por autorización explícita de Alcy, en
[Zenodo 23862211](https://zenodo.org/records/23862211). El PR #55 registra el
episodio, su corrección y el congelamiento de releases. Permanece sin fusionar.

No fue una licencia correcta que cambiara después: el metadato global era
incorrecto desde el origen para el agregado que se archivó. Por eso se corrige
el hecho, conservando los archivos y explicando qué se declaraba antes.

| Campo | Antes | Después |
|---|---|---|
| Licencia global del registro | CC BY-SA 4.0 | CC BY-NC-SA 4.0, la más restrictiva presente en este ZIP mixto |
| Creadores | Solo Alcy Edmundo Torres Guerrero | Alcy Torres Catefort (†), Alcy Ramiro Torres Guerrero, Gladys Torres Guerrero, Alcy Edmundo Torres Guerrero y Daniela Torres Tobar |
| Descripción | Excepción NC mencionada, sin explicar el error global ni su corrección | Descripción original conservada, seguida de una única nota de alcance y corrección fechada |
| ORCID de Gladys y Daniela | Sin identificador | Sin identificador, pendientes de verificación; no se afirma su inexistencia |
| DOI, versión y fecha original | `10.5281/zenodo.23862211`, 1.1.0, 01/11/2026 | Idénticos |
| ZIP | 17.024.234 bytes; MD5 `24f8101a68b0417b32c79dd00ccc0b8b` | Idéntico |

La nota deja claro que la plataforma fuera de `lecciones/` conserva BY-SA y
los terceros sus licencias. La etiqueta NC del agregado no añade restricciones
a esas partes ni pretende revocar permisos previos. El autor fallecido conserva
su atribución, no recibe ORCID ni revisión actual.

La inspección histórica de los ZIP está en [alcance-archivo.json](alcance-archivo.json).
Su estado se marcó expresamente como **anterior a la corrección**, para no
confundirlo con los metadatos vigentes. El LICENSE dentro del ZIP enumera a
cuatro titulares; no se le atribuye retrospectivamente la mención de Daniela
que sí aparece en la fuente actual. No se reemplaza el ZIP para cambiarlo.
v1.0.0 (`22069642`) no contenía `lecciones/` y no se modifica.

## Evidencia reproducible

- [antes.json](antes.json): licencia, autores, descripción y archivo antes.
- [despues.json](despues.json): los mismos campos leídos de la API pública después.
- [nota-alcance.html](nota-alcance.html): nota que se añadió una sola vez.
- [descripcion-corregida.html](descripcion-corregida.html): preparación del texto
  completo; Zenodo puede normalizar entidades y espacios en su exportación.
- [autores-invenio.json](autores-invenio.json): cinco personas importadas mediante
  el formulario, con solo los dos ORCID verificados en las fuentes.

La publicación se hizo por la interfaz autenticada de Zenodo. La comprobación
posterior usó `GET https://zenodo.org/api/records/23862211`: licencia NC-SA,
cinco creadores, nota única, fecha de corrección y ausencia de ORCID en los
nombres pendientes. Las entidades HTML se normalizaron antes de comparar el
texto. Los campos de identidad y el inventario/checksum del archivo coinciden
con el estado anterior.

## Futuro detenido

Los `CITATION.cff` y `.zenodo.json` activos de medsemiotics **no se editan**
en este PR. Se retiraron también sus borradores futuros, para que no se apliquen
antes de separar el libro. No habrá nuevo release hasta que `lecciones/` esté
fuera y los metadatos y el paquete final describan solo la plataforma.

El [plan de separación](../../planes/separacion-libro-neurologia.md) es un
documento aparte, sin ejecutar. La decisión se toma con Alcy no antes del
13/11/2026; la semana de congelamiento de biosemiotics se respeta.
