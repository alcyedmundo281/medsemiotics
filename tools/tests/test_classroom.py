"""El plan de Classroom debe ser coherente con el sílabo, el sitio y los artículos."""

from __future__ import annotations

from casos.articulo import leer_articulos
from casos.compilar import RAIZ, Rutas
from classroom.__main__ import CURSO, SILABO
from classroom.plan import construir
from classroom.validar import cargar, contraste_silabo, errores


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


def test_plan_coincide_con_el_silabo() -> None:
    plan = cargar(CURSO)
    assert contraste_silabo(plan, SILABO.read_text(encoding="utf-8")) == []


def test_contraste_detecta_fecha_y_caso_distintos() -> None:
    plan = cargar(CURSO)
    silabo = SILABO.read_text(encoding="utf-8")
    roto = silabo.replace("| 3 · 25 nov 2026", "| 3 · 26 nov 2026").replace("HM6044", "HM6099")
    fallos = contraste_silabo(plan, roto)
    assert any("Sesión 3" in f and "2026-11-26" in f for f in fallos)
    assert any("Sesión 7" in f for f in fallos)


def test_detecta_entregas_distintas_en_el_silabo() -> None:
    plan = cargar(CURSO)
    silabo = SILABO.read_text(encoding="utf-8")
    roto = silabo.replace("09 dic 2026 (s5)", "09 dic 2026 (s6)")
    fallos = contraste_silabo(plan, roto)
    assert any("informe_caso_u1" in f for f in fallos)
    sin_tabla = silabo.replace("| Proyecto integrador (parejas)", "| Otro nombre")
    assert any("proyecto_integrador" in f for f in contraste_silabo(plan, sin_tabla))
