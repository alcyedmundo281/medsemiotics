"""El plan de Classroom debe ser coherente con el sílabo, el sitio y los artículos."""

from __future__ import annotations

from casos.articulo import leer_articulos
from casos.compilar import RAIZ, Rutas
from classroom.__main__ import CURSO
from classroom.plan import construir
from classroom.validar import cargar, errores


def test_plan_real_es_coherente() -> None:
    plan = cargar(CURSO)
    articulos = leer_articulos(Rutas(RAIZ).posts)
    assert errores(plan, RAIZ, set(articulos)) == []


def test_plan_detecta_fecha_fuera_de_miercoles() -> None:
    plan = cargar(CURSO)
    roto = plan.model_copy(
        update={
            "sesiones": [
                plan.sesiones[0].model_copy(
                    update={"fecha": plan.sesiones[1].fecha.replace(day=19)}
                ),
                *plan.sesiones[1:],
            ]
        }
    )
    assert any("no es miércoles" in e for e in errores(roto, RAIZ, {"HM:6009"}))


def test_tareas_quedan_en_borrador_con_vencimiento_local() -> None:
    plan = cargar(CURSO)
    slugs = {c: "x" for s in plan.sesiones for c in s.condiciones}
    ops = construir(plan, slugs)
    assert all(t["state"] == "DRAFT" for t in ops["courseWork"])
    assert ops["courseWork"][-1]["dueAt"] == "2027-03-10T21:30:00-05:00"
