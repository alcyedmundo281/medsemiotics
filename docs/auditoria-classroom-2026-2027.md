# Auditoría: automatizar Classroom 2026-2027 desde el sílabo v3

Fecha: 16 oct 2026. Alcance: repo `medsemiotics-copilot`, carpeta de Drive del semestre anterior y
portal `medicina_y_datos.html`.

## Hallazgos

| # | Hallazgo | Consecuencia |
| - | -------- | ------------ |
| 1 | El repo **no contiene scripts de agente docente** ni de Classroom (solo `casos`, `imagenes`, `generate_topic`, `build-blog`). La skill única es `caso-socratico`. | Había que crear la capa de automatización; no se heredaba nada. |
| 2 | El sílabo v3 era prosa Markdown: no se podía validar ni leer por máquina. | Se creó `classroom/curso-2026-2027.yaml` como fuente estructurada y `python -m classroom check` la contrasta con el sílabo, el sitio y los artículos. |
| 3 | De las 12 condiciones ancla del cronograma, **ninguna tiene caso socrático** (`casos/` solo tiene HM6001–HM6006). Los primeros 10 min de cada clase dependen de ellos. | `check` lo avisa por sesión. Redactarlos exige la skill `caso-socratico` y un revisor humano nominado. |
| 4 | `medicina_y_datos.html` es un índice de 9 tarjetas por módulo (versión por herramientas). No sigue las 16 sesiones, ni enlaza artículos ancla, `reto.html` ni Classroom. No comparé a fondo cómo guían Gastroenterología y Neurología; el rediseño debe partir de esa revisión. | Rediseño pendiente, ver «Siguiente». |
| 5 | La carpeta de Drive del semestre anterior contiene **entregas de estudiantes con nombre** (PDF de Evaluación 1, hojas de calificación, formularios de asistencia, `chimborazo.sqlite`). | Nunca se copian al repo (público). El agente lee Drive solo en sesión, por ID de carpeta; en el repo solo van IDs de plantillas no personales. |
| 6 | El sílabo tiene pendientes del docente (§9) y no fija cuántos informes de caso hay. | Las 3 tareas `informe_caso_*` van marcadas `propuesta: true`; nada se publica sin confirmación. |
| 7 | No hay conector de Classroom en este entorno; `gcloud` está instalado, `gws`/`clasp` no. | La aplicación real necesita OAuth del docente (ver abajo). |

## Lo que ya queda automatizado

`npm run gates` incluye ahora tests del plan. Órdenes:

```bash
uv run python -m classroom check   # valida 16 sesiones, miércoles, receso, 40/60, rúbrica = 20 pts, enlaces
uv run python -m classroom plan    # JSON de operaciones: curso, 16 temas con enlaces, 5 tareas en borrador con vencimiento
```

El plan no llama a ninguna API y no contiene datos de estudiantes.

## Cómo se aplicará a Classroom (siguiente paso, requiere decisión del docente)

1. OAuth de escritorio con la cuenta docente (alcances `classroom.courses`, `classroom.coursework.students`,
   `classroom.topics`), con el token **fuera del repo** (`~/.config/…`). Un módulo `classroom apply`
   leerá el JSON de `plan`, será idempotente (marca cada recurso con su `id` del YAML) y por defecto en `--dry-run`.
2. Orden: curso → temas → tareas en `DRAFT` → rúbricas. Las rúbricas por API dependen de la licencia de
   Workspace for Education del dominio: verificar antes; si no, el plan las incluye como texto en la descripción.
3. Las ponderaciones se configuran como categorías de calificación (formativa 40, sumativa 1 25,
   final 35); si la API no las cubre, se fijan a mano una vez.
4. El curso anterior se archiva solo después de revisar el nuevo y con confirmación explícita.

## Siguiente

- Rediseñar `medicina_y_datos.html` como guía de 16 sesiones (tarjeta por sesión: caso ancla, recursos,
  autoevaluación del `Reto`, entrega), tomando `classroom/curso-2026-2027.yaml` como fuente para no duplicar fechas.
- Redactar los casos socráticos de las sesiones 3–7 primero (antes del 11 nov 2026).
- Decidir las tareas `propuesta` y el sílabo §9.
