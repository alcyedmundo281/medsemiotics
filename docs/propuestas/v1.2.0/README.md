# Propuesta v1.2.0: licencia, atribución y objeto de depósito

**Estado: propuesta, sin alternativa elegida.** No se publica ni se fusiona
este PR. No se crean releases, repositorios de destino, depósitos o DOI.
No se editan registros publicados. No se modifica el contenido de lecciones,
libro, archivos de licencia actuales ni metadatos activos de la raíz.

## 1. Alcance de los registros históricos

La evidencia comprobada está en [alcance-zenodo.json](alcance-zenodo.json).
Los ZIP descargados se inspeccionaron en memoria y sus MD5 coinciden con
los suministrados por la API pública de Zenodo:

| DOI | Versión | ZIP | Contenido |
|---|---|---|---|
| `10.5281/zenodo.22069642` | v1.0.0, 23/08/2026 | 459 archivos, MD5 `98eed60208641d1a9faf991eed534794` | Instantánea del repositorio; sin `lecciones/` ni libro compilado |
| `10.5281/zenodo.23862211` | v1.1.0, 01/11/2026 | 622 archivos, MD5 `24f8101a68b0417b32c79dd00ccc0b8b` | Incluye los nueve archivos enumerados de `lecciones/`, pero no EPUB/PDF del libro compilado |

`10.5281/zenodo.22069641` es el DOI de concepto, no un tercer ZIP: al comprobarlo
el 04/11/2026 resolvía a v1.1.0. No confundir DOI de concepto con DOI de versión.

En v1.1.0 hay una contradicción verificable: licencia global CC BY-SA 4.0 y un
creador en el registro, frente a CC BY-NC-SA 4.0 en `lecciones/LICENSE.md` del
ZIP. La descripción del registro sí menciona la excepción NC. El LICENSE
archivado nombra a Alcy Torres Catefort (†) y sus herederos, Alcy Ramiro Torres
Guerrero, Gladys Torres Guerrero y Alcy Edmundo Torres Guerrero. **No nombra a
Daniela Torres Tobar**; la fuente actual sí. No corregir silenciosamente esa
diferencia histórica ni trasladar el diagnóstico a v1.0.0, que no contiene
la carpeta. Ambos registros siguen intactos.

## 2. ¿Puede editarse la licencia después de publicar?

**Sí, según la documentación técnica actual: no solo la descripción.**
Zenodo documenta que los metadatos de un registro publicado son editables y
que guardar/publicar esa edición no cambia su DOI. El formulario de licencias
permite cambiar una licencia y declarar varias en depósitos mixtos. Las fuentes
consultadas son las de Zenodo, no una inferencia basada en otro repositorio:

- [Editar registros publicados](https://help.zenodo.org/docs/deposit/manage-records/#edit).
- [Licencias y depósitos mixtos](https://help.zenodo.org/docs/deposit/describe-records/licenses/).
- [FAQ de edición posterior a publicación](https://support.zenodo.org/help/en-gb/1-upload-deposit/64-can-i-edit-records-after-they-have-been-published).

No se abrió un borrador de edición ni se hizo una prueba guardando cambios en
los depósitos del usuario. Esta conclusión documental no es una demostración
mediante una escritura en su cuenta. La capacidad técnica de cambiar un campo
no equivale a revocar permisos previos ni a borrar lo distribuido. Creative
Commons distingue esa irrevocabilidad en su [FAQ](https://creativecommons.org/faq/#what-if-i-change-my-mind-about-using-a-cc-license).

**Decisión de Alcy:** no editar v1.1.0. Se conserva como cicatriz en `CLAUDE.md`
y se prepara una versión que la supere. No ejecutar una modificación de
metadatos aunque la interfaz la permita.

### Nota histórica redactada, NO aplicada

Este texto queda preparado para la documentación de v1.2.0 o para una eventual
nota pública que Alcy autorice expresamente. No está autorizado pegarlo en el
registro antiguo:

> Antecedente de licencia y atribución: medsemiotics v1.1.0, DOI
> 10.5281/zenodo.23862211, fue archivada como una instantánea del repositorio.
> Sus metadatos globales indicaban CC BY-SA 4.0 y un único creador, Alcy Edmundo
> Torres Guerrero. El ZIP incluye lecciones/LICENSE.md, que declara CC BY-NC-SA
> 4.0 para lecciones/ y el libro derivado y nombra a Alcy Torres Catefort (†) y
> sus herederos, Alcy Ramiro Torres Guerrero, Gladys Torres Guerrero y Alcy
> Edmundo Torres Guerrero. Se conserva íntegro el archivo y su contexto
> histórico; esta nota no sustituye los archivos ni pretende revocar permisos
> anteriores. La fuente actual reconoce además a Daniela Torres Tobar. La
> licencia, autoría y alcance de versiones posteriores deben consultarse en
> sus propios metadatos. v1.0.0, DOI 10.5281/zenodo.22069642, no contenía
> lecciones/; no se le atribuye este mismo conflicto.

## 3. Las tres alternativas, sin elegir

| Alternativa | Objeto y etiqueta global | Ventaja | Límite que permanece | Trabajo pendiente |
|---|---|---|---|---|
| **a. Agregado NC** | Mantener el repositorio mixto y etiquetar el depósito CC BY-NC-SA 4.0 | La máquina ya no declara reutilización comercial de todo el agregado | Subdeclara las partes BY-SA y no puede imponerles retrospectivamente NC; la etiqueta única no describe los ámbitos por archivo | Revisar facultades sobre cada parte, describir los ámbitos y validar los cinco autores del agregado |
| **b. BY-SA con nota** | Mantener el agregado y la etiqueta CC BY-SA 4.0, con excepción NC explícita en descripción y notas | Conserva la identificación de la plataforma y hace visible la excepción a lectores humanos | La máquina sigue leyendo BY-SA; la nota no resuelve el defecto del campo global ni vuelve homogéneo el ZIP | Mantener una declaración por ámbitos y asumir/documentar el límite del importador heredado |
| **c. Separación estructural** | Plataforma BY-SA sin el libro; repositorio y depósito nuevos del libro NC-SA con sus cinco autores | Cada depósito coincide con un objeto y una licencia; separa sus citas y preserva la autoría del libro | No borra la historia de v1.1.0 ni por sí sola limpia dependencias, contenido duplicado o bibliografía compartida | Diseñar y revisar la migración, dependencias, enlaces y paquetes; publicar ambos objetos solo tras verificar su separación |

No se asignan puntuaciones ni se toma una decisión en este PR. Los controles
técnicos adicionales que ofrece la interfaz moderna de Zenodo no se presentan
como una cuarta alternativa decidida.

### Límites del formato de metadatos

El [formato heredado `.zenodo.json`](https://developers.zenodo.org/#deposit-metadata)
usa un solo campo `license`, aplicable a los archivos del depósito. No se
inventa una lista ni un valor SPDX compuesto que ese importador no admite.

En [CFF 1.2](https://raw.githubusercontent.com/citation-file-format/citation-file-format/main/schema.json),
una lista en `license` significa alternativas **OR**. No se usa para expresar
«BY-SA para plataforma y NC-SA para lecciones». Un mapa REUSE por rutas sería
una ayuda para un repositorio mixto, pero no cambia ese campo global de Zenodo,
no separa el objeto y **no se aplica en este PR**.

### Borradores revisables de los metadatos

- [a-agregado-nc/](a-agregado-nc/): `CITATION.cff` y `.zenodo.json` de v1.2.0
  con cinco autores, etiqueta global NC-SA y descripción de sus límites.
- [b-alcance-nota/](b-alcance-nota/): los mismos cinco autores, etiqueta BY-SA
  y nota expresa de alcance; se conserva visible el problema para máquinas.
- [c-separacion/](c-separacion/): plataforma tras la separación; la atribución
  a su autor actual no se sustituye automáticamente por la autoría del libro.
  En [c-separacion/libro/](c-separacion/libro/) están los metadatos distintos
  del libro, con sus cinco autores y NC-SA. El CFF del libro usa
  `preferred-citation` de tipo `book`, sin fingir un tipo raíz no admitido.

Son archivos de propuesta, no los activos en la raíz. No se declaran DOI de
v1.2.0 ni del libro que aún no existen; tampoco fecha futura de publicación.
El DOI de concepto existente solo se conserva para las versiones de la
plataforma. Los DOI de versiones anteriores no se usan como identificadores
de v1.2.0. Al preparar un release real se añaden sus datos verificados.

### Identidad y atribución

Orden preparado: Alcy Torres Catefort (†), Alcy Ramiro Torres Guerrero, Gladys
Torres Guerrero, Alcy Edmundo Torres Guerrero y Daniela Torres Tobar.

- CFF conserva el nombre del autor fallecido y añade `name-suffix: (†)`;
  Zenodo lleva `(†)` en el nombre. Las notas aclaran el carácter de autor
  fundador y excluyen atribuirle revisión actual. No se le asigna ORCID.
- Alcy Ramiro: ORCID `0000-0001-5798-9161`, tomado de `lecciones/mapa.yaml`.
- Alcy Edmundo: ORCID `0000-0002-9742-375X`, tomado de la misma fuente.
- Gladys y Daniela: sin ORCID, confirmado por Alcy. En los CFF hay comentarios
  en el lugar donde añadir `orcid` cuando exista. En JSON el campo se omite;
  no se escribe `null`, un identificador vacío ni un valor de ejemplo.

Los cinco titulares de lecciones/libro no se convierten por esta corrección
en autores de todos los módulos de la plataforma. La alternativa c conserva
esa separación en sus propios metadatos.

## 4. Plan del repositorio y depósito independiente del libro — NO ejecutar

1. **Decisión y perímetro.** Alcy elige el camino. Si elige c, confirma el nombre
   del repositorio nuevo y el alcance de la edición. No se crea nada en este PR.
2. **Inventario.** Enumerar `lecciones/`, su mapa, referencias, evidencia,
   paratextos, imágenes del libro, `assets/libro/`, `tools/libro/` y sus pruebas.
   Revisar dependencias sobre `tools/lecciones/`, módulos y datos clínicos.
   Elegir cuáles se trasladan, cuáles se referencian por versión y cuáles son
   compartidas. No copiar toda la plataforma dentro del libro.
3. **Preservación.** Migrar con trazabilidad de la historia y hashes; no reescribir
   tags, commits, ZIP ni DOI anteriores. Eliminar del árbol activo de la
   plataforma lo que pase al libro solo en una migración autorizada y revisada.
   Conservar enlaces de navegación y redirecciones necesarias.
4. **Identidad propia.** Título y subtítulo se toman del mapa actual. El libro
   tendrá su repositorio, `LICENSE` NC-SA, sus cinco autores y sus propios
   `CITATION.cff` y `.zenodo.json`. El sello no sustituye a los autores.
5. **ISBN.** Alcy informa los bloques `979-8-953844-10` y `979-8-953844-11`.
   No son aquí números ISBN-13 completos verificados. Antes del depósito se
   obtienen de la asignación original los números completos y qué formato
   corresponde a cada uno. En el checkout inspeccionado el generador aún dice
   «ISBN: pendiente»; este PR no lo corrige ni toca los créditos del libro.
6. **Nuevo objeto Zenodo.** Preparar una carga nueva del libro, no una versión
   del depósito medsemiotics ni un alias de `22069641`. Tipo publicación/libro,
   licencia `cc-by-nc-sa-4.0`, cinco autores y ORCID solo de quienes lo tengan.
   Reservar su DOI únicamente tras autorización; no se reserva en este PR.
   Zenodo distinguirá el concepto del libro de sus versiones; ninguno se
   confundirá con el concepto de la plataforma.
7. **Paquete.** Definir la edición y los archivos que realmente se archivarán:
   fuente reproducible y, si se acuerda, PDF/EPUB revisados. El ZIP de integración
   GitHub archiva el repositorio: un PDF/EPUB adjunto como asset de un release
   no se debe dar por incluido automáticamente. Verificar el inventario real.
8. **Relaciones.** Relacionar el libro con la plataforma mediante `isDerivedFrom`
   cuando corresponda, no `isVersionOf` ni `isIdenticalTo`. Incorporar los ISBN
   verificados a sus ediciones; no reutilizar un ISBN como DOI. Los borradores
   solo incluyen el DOI real de la plataforma como relación, nunca como DOI
   propio del libro.
9. **Verificación previa.** Autoría, licencia dentro de archivos y en metadatos,
   ISBN por formato, fuentes/derivados coherentes, exclusión del libro del
   paquete de plataforma y aprobación de la edición. Hoy `libro check` informa
   cero lecciones revisadas/publicadas: preparar un DOI no equivale a que el
   contenido esté listo para publicar.
10. **Publicación y comprobación, futuras.** Con autorización concreta, publicar
    y leer la API/exportación DataCite y el ZIP resultante: autores, licencia,
    relaciones, DOI propio e inventario. Registrar hashes, URL y versión. La
    propuesta actual no ejecuta ninguno de esos pasos externos.

## 5. Validación y límites de este PR

`npm run gates` pasó en el árbol base (230 pytest, 13 tests del blog y 26 de
sincronización, además de los validadores del repositorio). Los cuatro pares de borradores se validaron: CFF contra su esquema oficial;
Zenodo contra el esquema legacy enlazado en su documentación, comprobando
`version` y `language` por separado, porque ese esquema antiguo no incorpora
esos campos admitidos por la API desde 2017. No se presentan como una prueba
de aceptación por el servidor ni se enviaron a una API de escritura.
No se alteran las fuentes ni se renderiza o publica el libro para esta tarea.
El PR queda sin fusionar, con la elección a/b/c expresamente pendiente.
