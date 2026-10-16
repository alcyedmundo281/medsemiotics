---
name: classroom-medicina-ciencia
description: Planifica y prepara el Google Classroom de Medicina y Ciencia 2026-2027 a partir del sílabo v3 (temas, tareas, rúbricas, fechas). Usar cuando se pida crear, actualizar o revisar el classroom, las tareas, las rúbricas o el calendario del curso.
---

# Classroom · Medicina y Ciencia 2026-2027

Fuente de verdad: `docs/silabo-medicina-y-ciencia-v3.md` (prosa) y
`classroom/curso-2026-2027.yaml` (datos). Se cambian juntos.

## Flujo

1. Editar el YAML (o el sílabo) y correr `uv run python -m classroom check`. Debe quedar sin errores;
   los `AVISO` son pendientes del docente, no fallos.
2. `uv run python -m classroom plan` imprime las operaciones de Classroom. Revisarlas con el docente.
3. Antes de `npm run gates` y de cada commit: gates en verde.

## Reglas

- Ponderaciones fijas: 40 % formativa, 60 % sumativa (25 + 35), escala sobre 20. No se cambian.
- Las tareas con `propuesta: true` no se publican sin confirmación del docente.
- Las tareas se crean en `DRAFT`; publicar es una acción del docente.
- Nunca se guardan en el repo (público) datos de estudiantes, entregas, calificaciones, tokens ni
  credenciales. La carpeta de Drive del curso anterior contiene entregas con nombre: leer en sesión, no copiar.
- Aplicar cambios a Classroom, enviar mensajes a estudiantes o archivar el curso anterior requiere
  confirmación explícita del docente en esa acción.
- Los casos socráticos de las sesiones siguen la skill `caso-socratico` (revisor humano nominado).
- La salida de un LLM es un borrador; las cifras diagnósticas vienen del artículo (medsemiotics-db).
