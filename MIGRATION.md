# Migración desde el Google Site histórico

Este registro controla la migración desde
<https://sites.google.com/view/club-de-mbe/home>. La unidad de migración es el
**tema**, no la página antigua: varias páginas pueden consolidarse en un solo
módulo y una página antigua puede tener un sucesor en otro proyecto.

## Estados

- **Cubierto:** existe un sucesor suficiente; no se crea otra página.
- **Integrar:** solo se trasladan piezas únicas al módulo indicado.
- **Migrar:** merece un módulo nuevo en Medsemiotics.
- **Biosemiotics:** su sucesor canónico está fuera de este repositorio.
- **Archivar:** se conserva como fuente docente o histórica, sin publicarlo como
  módulo principal.
- **Auditar:** el contenido incrustado debe exportarse antes de decidir.

## Decisiones aprobadas

| Material histórico                                      | Estado       | Destino canónico                                                          | Acción                                                                                                |
| ------------------------------------------------------- | ------------ | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Introducción a POCUS y partes 1–6                       | Biosemiotics | <https://www.biosemiotics.net/>                                           | Auditar conceptos, signos, casos, imágenes y referencias; no copiar páginas completas a Medsemiotics. |
| Implementación de POCUS                                 | Cubierto     | `medicina_e_implementacion/POCUS-implementacion.html`                     | Mantener la monografía y enlazar el atlas clínico externo.                                            |
| Medidas de frecuencia, asociación e impacto             | Migrar       | `medicina_y_datos/epidemiologia-clinica.html`                             | Consolidar las tres páginas después de exportar los incrustados.                                      |
| Razonamiento clínico: Peirce, Foucault y mirada clínica | Migrado      | `medicina_y_datos/fundamentos-semioticos.html`                            | Tarjeta nueva; enfoque histórico y filosófico preservado sin repetir el módulo computacional.         |
| Introducción al razonamiento clínico y ciencia de datos | Integrar     | `medicina_y_datos/razonamiento_clinico/`                                  | Incorporar solo ejemplos o recursos ausentes.                                                         |
| Estadísticos al descubierto                             | Integrar     | `medicina_y_datos/estadisticos_descubiertos/`                             | Comparar la presentación y los documentos; conservar únicamente material diferencial.                 |
| Probabilidad y estadística                              | Cubierto     | `medicina_y_datos/probabilidad_estadistica/`                              | No crear duplicado.                                                                                   |
| Comunicación efectiva                                   | Cubierto     | `medicina_y_datos/razonamiento_clinico/comunicacion_y_visualizacion.html` | No crear duplicado.                                                                                   |
| Código de conducta ético                                | Auditar      | Por definir dentro de Medicina y Datos                                    | Exportar el incrustado y comparar con `razonamiento_clinico/Etica_y_Sesgos/`.                         |
| Acute Hepatitis, Hepatitis Viral A y Hepatitis A        | Migrado      | `gastroenterologia/hepatitis-viral-aguda.html`                            | Tres fuentes consolidadas en HTML autónomo y actualizadas con referencias clínicas.                   |
| Gastroenterología Semana 2                              | Integrar     | `gastroenterologia/helicobacter_pylori.html`                              | Los cinco incrustados corresponden a _H. pylori_; integrar solo actividades o recursos ausentes.      |
| Síndrome de intestino irritable                         | Migrado      | `gastroenterologia/sindrome-intestino-irritable.html`                     | Ruta heredada como módulo HTML autónomo; el antiguo embed ya no responde.                             |
| ERGE                                                    | Cubierto     | `gastroenterologia/reflujo-gastroesofagico.html`                          | No crear duplicado.                                                                                   |
| Gastroenteropatía por AINEs                             | Cubierto     | `gastroenterologia/gastroenteropatias-aines.html`                         | No crear duplicado.                                                                                   |
| Sílabo de Gastroenterología                             | Archivar     | Archivo docente                                                           | Publicar solo si continúa vigente.                                                                    |
| Neurología Semana 1                                     | Integrar     | `neurologia/examen-neurologico-parte-1.html` y `parte-2.html`             | Conservar únicamente actividades o recursos ausentes.                                                 |
| Enfermedad cerebrovascular 1 y ACV parte II             | Cubierto     | `neurologia/acv.html` y `neurologia/acv-isquemico.html`                   | No crear duplicados.                                                                                  |
| Epilepsia I                                             | Integrar     | `neurologia/epilepsia-ii/`                                                | Revisar si contiene fundamentos que no estén presentes.                                               |
| ¿Quién recibe el dinero? y sus ocho secciones           | Migrar       | `medicina_e_implementacion/quien-recibe-el-dinero.html`                   | Consolidar después de recuperar íntegramente los incrustados.                                         |
| Página histórica “Webpage”                              | Auditar      | Por definir                                                               | Identificar el incrustado antes de descartarla.                                                       |

## Regla de publicación

Un contenido clínico no se publica únicamente porque exista en el sitio antiguo.
Antes debe:

1. recuperarse íntegramente, incluidos archivos e incrustados;
2. compararse con los módulos actuales por concepto y no solo por título;
3. verificar las afirmaciones clínicas y actualizar las referencias;
4. registrar procedencia, autoría y licencia de cada recurso multimedia;
5. asignar una sola URL canónica y añadirla a `sitemap.xml`;
6. comprobar navegación, accesibilidad básica y enlaces locales.

## Inventario de recursos externos conocido

Los trece documentos o presentaciones de Google incrustados están accesibles en el
Drive de origen. No deben considerarse vacíos ni descartarse porque su contenido no
aparezca en el HTML exterior de Google Sites.

| Grupo histórico              | Tipo         | Título en Drive                                                                       | ID                                             |
| ---------------------------- | ------------ | ------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Estadísticos al descubierto  | Presentación | Razonamiento Clínico y Método Científico                                              | `1Mk32YhzkwrF7tb9Wr6broaOhBpgf7CeYONDZro6ZgG4` |
| Estadísticos al descubierto  | Documento    | Actividad Interactiva para el Aula: “Estadísticos al Descubierto”                     | `1byZ3RdMIwugO2EmP69Umcz5HlRukkRt12lV5kmkC9gk` |
| Estadísticos al descubierto  | Documento    | Plan de Clase Semana 2                                                                | `1DjdAJl4u5MZXJh6wGl9QP5e0x79TrADhN64JnkJxccI` |
| Razonamiento clínico         | Documento    | Semana 3: La Base del Razonamiento Clínico — Datos de Calidad y Comunicación Efectiva | `1zJUkMBMS72-4LCj8IdjPbbbON1Rp1ysTGYgvREhweZE` |
| Razonamiento clínico         | Documento    | Materiales Educativos: Medicina y Ciencia (Razonamiento Clínico) — Semana 3           | `1YCd5YyM1FsiWvNcdkPClZ_k0ox1kTGg1Q2xqjdtarms` |
| Razonamiento clínico         | Documento    | Medicina y Ciencia (Razonamiento Clínico) — Semana 3: Puntos Clave para el Estudio    | `1Fghc-8mId1V6ibuwf_gilVfWhWy6L-xRVI6T2Z9po1k` |
| Razonamiento clínico         | Documento    | Materiales Educativos: Medicina y Ciencia (Razonamiento Clínico) — Semana 3           | `1es7uU2MP40Vgzhirkmt5-pZh8JQl6xSV4h1hCh1ZwmQ` |
| Gastroenterología Semana 2   | Presentación | Infección por _Helicobacter pylori_                                                   | `16hOAEf9tpD1NuReYNfOaupJWQI-JkHSLlz_HGEP9vE8` |
| Gastroenterología Semana 2   | Documento    | Taller: “Descifrando las Pistas de H…”                                                | `1cBeuIJFFgPhz7XdzExRE2Ez9-_SmcE-jKH0GQVrzfCs` |
| Gastroenterología Semana 2   | Documento    | Hoja de Datos Clave: _Helicobacter pylori_                                            | `1DLzux5au0M8sQJD-bv5zCyJU9bWBB6FUtGd7zyI36SA` |
| Gastroenterología Semana 2   | Documento    | Cuestionario de Autoevaluación: _Helicobacter pylori_                                 | `1bBupigO7lXfI8kzRZ1ZDKmSeNPr9_suecRaSZqtr5wk` |
| Gastroenterología Semana 2   | Documento    | Materiales para el Profesor                                                           | `1m4DuX-IJxQyXemuOO7c8wBzQ9rMCdxX6deFEdotaJoA` |
| Enfermedad cerebrovascular 1 | Documento    | Materiales Educativos: Neurología — Enfermedad Cerebrovascular (Parte 1)              | `1zKuFrH_hsh7hz4ibGDqwHqOwZDMWiL143FBRBkAAncQ` |

El siguiente paso es leer y comparar su contenido antes de exportar únicamente las
fuentes que aporten material diferencial. Las exportaciones se conservarán en un
formato abierto o estable antes de retirar el sitio histórico.
