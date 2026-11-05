# Separación del libro de neurología — plan sin ejecutar

**Estado: pendiente de decisión con Alcy, no antes del 13/11/2026.** No se
crean repositorios, se trasladan archivos ni se reservan DOI desde este plan.
La semana de congelamiento de biosemiotics tiene prioridad.
La corrección ya realizada de Zenodo v1.1.0 es independiente de esta migración.

## Objetivo y regla transitoria

El libro tendrá repositorio, autoría, bibliografía, licencia y depósito propios.
La plataforma medsemiotics sin el trabajo del libro conservará CC BY-SA 4.0
y su atribución correspondiente, sin acreditar como autores de toda la
plataforma a titulares cuyo trabajo ya no estará en ella.

**No publicar ningún release nuevo de medsemiotics hasta que `lecciones/`
esté fuera.** Los metadatos activos se revisarán una sola vez al terminar,
contra el contenido real del paquete. No hay una ventana de publicación
intermedia con metadatos heredados defectuosos.

## Inventario observado y destino propuesto

Inventario del árbol base `1cea81909ba9a31ad9606758807470a3b7fc38f9`, excluidos
cachés: 11 archivos en `lecciones/` (1.438 líneas), 12 módulos en
`tools/lecciones/` (1.845 líneas), 6 en `tools/libro/` (1.842 líneas) y 4 en
`assets/libro/` (1.517 líneas). Hay diez archivos de pruebas de autoría,
lecciones y libro que deben repartirse; no todos pertenecen exclusivamente
al libro. Son medidas del código actual, no una previsión de páginas terminadas.

| Conjunto | Qué se propone hacer | Precaución |
|---|---|---|
| `lecciones/` completo | Trasladar mapa, lección `.qmd`, evidencia reservada, `refs.bib`, licencia, declaración IA, paratextos, dedicatoria y semblanzas con trazabilidad | No cambiar texto clínico ni estados para facilitar la mudanza |
| `assets/plantilla-leccion.qmd` y `mapa-maestro-libro.md` | Llevar plantilla y mapa derivado; regenerar este último desde el mapa fuente | No crear dos mapas fuente |
| `tools/libro/`, `assets/libro/` | Dar al nuevo proyecto compilación y diseño propios, incluida la geometría de impresión | Separar el modo opcional `--material-previo` y los módulos antiguos de la plataforma |
| `tools/lecciones/` | Trasladar las funciones exclusivas de lecciones; extraer primero lo que usa la plataforma | No romper los tipos de autoría que consumen los casos |
| Imágenes efectivamente usadas por el libro | Inventariar archivos, fuente Commons, crédito, licencia y hash; trasladar solo las necesarias | No copiar `assets/` entero ni cambiar licencias de terceros |
| Pruebas `test_lecciones*`, `test_libro.py`, autoría y fixtures | Repartir por responsabilidad después de desacoplar | Parte de `test_autoria.py`, `test_casos_autoria.py` y `conftest.py` protege también la plataforma |
| Blog, `posts/`, `casos/`, módulos HTML, Classroom y datos publicados de la plataforma | Permanecer en medsemiotics | El libro no se convierte en una copia completa del sitio |

El traslado preservará la historia o dejará un manifiesto origen→destino con
commit y hashes; no reescribirá tags, ZIP ni DOI históricos. El nombre del
repositorio nuevo se decide con Alcy, no se presupone aquí.

## Qué se rompe si solo se quita `lecciones/`

| Dependencia real | Efecto de una retirada directa | Trabajo previo necesario |
|---|---|---|
| `tools/generate_topic.py`: `MAPA`, `read_authors()` | Pierde `lecciones/mapa.yaml`, registro de personas usado para firmar el blog | Extraer el registro compartido a una fuente neutral y mantener las firmas bibliográficas |
| `tools/generate_topic.py`: `EVIDENCE`, `topics:sync` | Sigue intentando escribir evidencia reservada en `lecciones/evidencia/` | Separar la salida de evidencia del blog y la del libro, con revisión de medsemiotics-db fijada |
| `tools/autores-fichas.yaml` | Sus claves remiten a personas del mapa del libro | Apuntar al registro neutral sin cambiar autores ya atribuidos a artículos |
| `tools/casos/__main__.py` | Importa `lecciones.mapa` y carga personas para crear casos | Cambiar la dependencia de autoría antes de retirar el módulo |
| `tools/casos/modelo.py` | Importa `AGENTES` y `Autor` de `lecciones.modelo` | Extraer los tipos compartidos; retirar todo `tools/lecciones/` ahora rompería importaciones |
| `package.json`: `gates`, `libro:*`, `lecciones:*` | La CI actual ejecuta incondicionalmente controles de libro y lecciones | Repartir comandos y conservar gates de blog/casos/imágenes/Classroom en la plataforma |
| `pyproject.toml`: paquetes, mypy, Ruff y pruebas | Sigue enumerando paquetes y rutas que ya no existirán | Actualizar empaquetado, alcance de analizadores y fixtures, sin quitar controles para ocultar fallos |
| `tools/libro/datos.py` y `qmd.py` | Leen mapa y `lecciones/refs.bib`; también importan utilidades de `casos.*` | Dar al libro raíces y contratos propios; evitar arrastrar el blog completo |
| `tools/lecciones/evidencia.py` | Combina `posts/` y evidencia reservada de una misma revisión de la base | Crear un suministro acotado y versionado de evidencia; prohibir ramas vivas y mezclas de revisiones |
| `libro.datos.MetadatosLibro` | Lee enlaces y DOI de plataforma desde el CFF raíz | Distinguir explícitamente DOI propio del libro de DOI de procedencia |
| Documentación, skill de casos, enlaces de lecciones y material previo | Conservan rutas al mapa o a los archivos movidos | Actualizar enlaces y contratos; mantener referencias al archivo histórico |

Los HTML ya construidos pueden seguir sirviéndose, pero eso no demuestra que
su reconstrucción, la CLI de casos ni la CI sobrevivan a la retirada.

Los módulos `tools/lecciones/` importan `casos.articulo`, `casos.errores` y
`casos.evidencia`; `tools/libro/datos.py` importa además `casos.compilar` y
`casos.presentacion`. No es una mudanza de carpeta aislada. Debe decidirse
qué contrato común se extrae a una dependencia versionada y qué código es
exclusivo del libro. El código fuera de `lecciones/` tiene su licencia propia:
no se lo convierte automáticamente en NC-SA al copiarlo. Si se incorpora
código BY-SA, se conserva su licencia o se acuerda previamente otra autorización
con sus titulares; otra opción técnica es consumir el motor como dependencia
externa fijada. Esta decisión evita recrear la misma ambigüedad en el nuevo ZIP.

## Qué necesita el repositorio nuevo

- **`CLAUDE.md` y `AGENTS.md`:** fuente `.qmd` única, cinco personas y roles,
  fundador fallecido sin revisión actual, aprobación clínica/editorial humana,
  política de autorías, licencias por material y prohibición de identificadores
  o fechas inventados. Procedencia y reglas de publicación explícitas.
- **Identidad editorial:** título y subtítulo del mapa, cinco titulares,
  `LICENSE` NC-SA para el libro, `CITATION.cff` y `.zenodo.json` propios.
  Gladys y Daniela sin ORCID hasta verificarlo; fundador sin ORCID. Comprobar
  los ISBN completos y su asignación a formatos a partir del documento original;
  no completar de memoria los bloques `979-8-953844-10` y `-11`.
- **`refs.bib` propio:** conservar claves y registros de `lecciones/refs.bib`,
  con procedencia por versión. Ninguna dependencia implícita del BibTeX o de
  la rama viva de medsemiotics. El traslado de ubicación no obliga a reescribir
  las citas dentro de las lecciones.
- **Verificación de citas:** adaptar `tools/lecciones/citas.py` para ese BibTeX;
  comprobar correspondencia PMID↔DOI con PubMed y Crossref, cobertura de claves
  y títulos. Revisar qué controles de año/retractación faltan antes de declarar
  equivalencia con el contrato editorial del atlas. Discrepancia o servicio
  no disponible bloquean la publicación; no se considera revisión clínica.
- **CI y dependencias:** Python 3.12+ con `uv.lock`, Ruff, mypy, pytest, contratos
  de mapa/autoría/estado/medios y citas. Motor Quarto + LuaLaTeX y fuentes
  reproducibles; verificar PDF, geometría y glifos. Si se incluye EPUB, añadir
  su generación y epubcheck. No dar por disponible un pipeline EPUB que hoy
  la CLI `libro` no ofrece.
- **Artefactos y permisos:** fuente reproducible, manifiesto y hashes; PDF/EPUB
  solo de una edición aprobada. Revisión de archivos de terceros. Elegir si
  Zenodo recibe fuentes, binarios o ambos; un asset de GitHub no se da por
  incorporado automáticamente al ZIP de integración.

## Identificador y linaje del futuro depósito

El libro es una obra distinta y requiere **un DOI de concepto nuevo**, además
del DOI de versión que Zenodo asigne a cada edición depositada. No será una
versión de `22069641` ni compartirá su concepto.

El registro nuevo debe llevar como identificador relacionado de procedencia:

- identificador: **`10.5281/zenodo.23862211`**;
- esquema: `doi`;
- relación desde el libro: `isDerivedFrom`.

Se usa la versión exacta v1.1.0, no solo el DOI de concepto `22069641`: esta
última dirección puede resolver en el futuro a una plataforma que ya no
contenga las lecciones. El ZIP de v1.1.0 queda como el archivo de las lecciones
tempranas; el registro nuevo reconoce ese linaje sin sustituirlo. Se podrán
conservar adicionalmente commit y hash de origen. No usar `isVersionOf` ni
`isIdenticalTo` para equiparar estas obras distintas.

## Secuencia propuesta, después de la decisión

1. Cerrar perímetro, registro neutral de personas y contrato común de evidencia.
2. Preparar y probar el desacoplamiento en medsemiotics, aún sin release.
3. Crear el repositorio del libro y migrar fuentes/historia con inventario.
4. Hacer funcionar en ambos repositorios su CI, bibliografía y construcción.
5. Comprobar que el paquete de medsemiotics ya no incluye el libro; solo entonces
   revisar una vez sus metadatos futuros, BY-SA y autoría de la plataforma.
6. Con aprobación de la edición, preparar el depósito propio del libro,
   reservar/publicar su identificador real y declarar `isDerivedFrom` a v1.1.0.
7. Leer el ZIP y los metadatos publicados para verificar objeto, licencia,
   autores, DOI nuevo, procedencia y artefactos. Documentar el cierre.

No hay releases transitorios. El congelamiento se levanta solo después de
comprobar la salida de `lecciones/` y la coherencia del paquete final.

## Estimación de trabajo — PENDIENTE DE REVISIÓN

**PENDIENTE DE REVISIÓN.** Las cifras de **24–40 horas** y su desglose se
conservan como antecedente cuestionado, no como estimación aprobada ni base
para planificar trabajo. Alcy aporta el precedente de una mudanza comparable
de farmacosemiotics que tomó diez minutos. La comparación y los supuestos
se revisarán con él; no se recalculan en este PR.

La actualización debe expresar el trabajo en **ciclos de revisión y riesgo**,
no en horas de ingeniería. Se hará después del 13/11/2026, con las decisiones
nuevas de arquitectura editorial que todavía no están en el repositorio.
Una sesión posterior no debe dar por válido el rango conservado aquí.

Estimación previa de ingeniería, basada en el inventario y acoplamientos anteriores,
no un plazo de entrega comprometido. Para una persona con revisión de Alcy:

| Trabajo | Horas estimadas |
|---|---:|
| Inventario final, perímetro e historia | 2–3 |
| Desacoplar autoría, tipos y evidencia | 6–10 |
| Repositorio nuevo, CI, citas y BibTeX propio | 6–8 |
| Migración y ajustes de plataforma/documentación/enlaces | 4–6 |
| Pruebas en ambos lados y verificación de artefactos | 5–8 |
| Preparación del depósito y verificación del linaje | 1–2 |
| **Total previo — PENDIENTE DE REVISIÓN** | **24–37 horas; reservar 24–40 (3–5 jornadas)** |

No incluye escribir/revisar las 54 lecciones, conseguir ORCID/ISBN, tiempos de
respuesta de terceros ni aprobación editorial de una edición. El alcance EPUB,
la extracción de código común o problemas de derechos de recursos reutilizados
pueden ampliar el trabajo. La corrección de metadatos del registro existente
no depende de esperar esta migración y ya se completó por separado.
