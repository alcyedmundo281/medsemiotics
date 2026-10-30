"""Traduce el plan a operaciones de la API de Google Classroom (sin ejecutarlas)."""

from __future__ import annotations

from datetime import datetime, time, timedelta
from typing import TYPE_CHECKING, Any
from zoneinfo import ZoneInfo

if TYPE_CHECKING:
    from classroom.modelo import Plan, Sesion


def _vencimiento(plan: Plan, sesion: Sesion) -> str:
    zona = ZoneInfo(plan.curso.zona_horaria)
    hora, minuto = map(int, plan.curso.hora_inicio.split(":"))
    fin = datetime.combine(sesion.fecha, time(hora, minuto), zona) + timedelta(
        minutes=plan.curso.duracion_min
    )
    return fin.isoformat()


def construir(plan: Plan, slugs: dict[str, str]) -> dict[str, Any]:
    """Operaciones ordenadas: curso, temas (uno por sesión) y tareas con su rúbrica.

    ``slugs`` mapea ``HM:####`` al slug del artículo. Las tareas quedan en borrador
    (``DRAFT``) hasta que el docente las publique.
    """
    sesiones = {s.n: s for s in plan.sesiones}
    unidades = {u.id: u.titulo for u in plan.unidades}
    base = plan.curso.base_url
    temas = []
    for s in plan.sesiones:
        enlaces = [base + r for r in s.recursos]
        enlaces += [f"{base}post.html?slug={slugs[c]}" for c in s.condiciones]
        temas.append(
            {
                "name": f"S{s.n:02d} · {s.fecha.isoformat()} · {s.tema}",
                "unidad": unidades[s.unidad],
                "materiales": [{"link": {"url": url}} for url in enlaces],
            }
        )
    pesos = {c.id: c.peso for c in plan.componentes}
    rubricas = {r.id: r for r in plan.rubricas}
    tareas = [
        {
            "id": t.id,
            "title": t.titulo,
            "workType": "ASSIGNMENT",
            "state": "DRAFT",
            "maxPoints": 20,
            "categoria": {"id": t.componente, "peso": pesos[t.componente]},
            "topic": f"S{t.sesion_publicacion:02d}",
            "dueAt": _vencimiento(plan, sesiones[t.sesion_entrega]),
            "rubrica": rubricas[t.rubrica].model_dump() if t.rubrica else None,
            "propuesta": t.propuesta,
        }
        for t in plan.tareas
    ]
    return {
        "course": {
            "name": plan.curso.nombre,
            "section": plan.curso.seccion,
            "description": plan.curso.descripcion,
            "courseState": "PROVISIONED",
        },
        "topics": temas,
        "courseWork": tareas,
    }
