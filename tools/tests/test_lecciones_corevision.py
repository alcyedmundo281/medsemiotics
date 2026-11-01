"""Revisión pediátrica: firma bibliográfica de artg y corevisión por lección (ADR-001)."""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any

import pytest
import yaml
from pydantic import ValidationError

from casos.articulo import Articulo
from lecciones import mapa as m
from lecciones.fuente import Archivo
from lecciones.modelo import Autor, Leccion
from lecciones.proyectar import linea_revision, proyectar

CON_COREVISION = {
    "leccion-infecciones-snc",
    "leccion-traumatismo-craneal-leve",
    "leccion-epilepsias",
    "leccion-estado-epileptico",
}


def _datos_mapa() -> dict[str, Any]:
    return yaml.safe_load(m.MAPA.read_text(encoding="utf-8"))  # type: ignore[no-any-return]


# --- firma bibliográfica -----------------------------------------------------------------------


def test_artg_firma_como_alcy_r_torres_pero_la_portada_usa_el_nombre_completo() -> None:
    mapa = m.cargar()
    artg = mapa.personas["artg"]
    assert artg.nombre == "Alcy Ramiro Torres Guerrero"
    assert artg.nombre_bibliografico == "Alcy R. Torres"
    assert all(p.nombre_bibliografico is None for k, p in mapa.personas.items() if k != "artg")


def test_la_firma_bibliografica_es_opcional() -> None:
    autor = Autor.model_validate({"nombre": "Alguien", "credit": ["redaccion"]})
    assert autor.nombre_bibliografico is None


def test_artg_revisa_las_partes_pediatricas() -> None:
    mapa = m.cargar()
    assert mapa.parte("neonato").revisor == "artg"
    assert mapa.parte("lactante-nino").revisor == "artg"


# --- el mapa asigna la corevisión --------------------------------------------------------------


def test_artg_corevisa_las_cuatro_lecciones_de_adulto() -> None:
    mapa = m.cargar()
    asignadas = {f.id for f in mapa.lecciones if f.corevisor == "artg"}
    assert asignadas == CON_COREVISION
    assert all(mapa.fila(i) is not None and mapa.fila(i).parte == "adulto" for i in CON_COREVISION)  # type: ignore[union-attr]
    assert not [f for f in mapa.lecciones if f.corevisor and f.id not in CON_COREVISION]


@pytest.mark.parametrize(
    ("corevisor", "mensaje"),
    [
        ("nadie", "corevisor desconocido"),
        ("atc", "fallecido"),
        ("aetg", "distinto del revisor"),  # aetg revisa la parte «adulto»
    ],
)
def test_el_mapa_rechaza_un_corevisor_invalido(corevisor: str, mensaje: str) -> None:
    datos = _datos_mapa()
    fila = next(f for f in datos["lecciones"] if f["id"] == "leccion-epilepsias")
    fila["corevisor"] = corevisor
    with pytest.raises(ValidationError, match=mensaje):
        m.Mapa.model_validate(datos)


# --- «revisado» exige la revisión de ambos -----------------------------------------------------


def _leccion(**cambios: Any) -> dict[str, Any]:
    base: dict[str, Any] = {
        "id": "leccion-prueba",
        "tipo": "leccion",
        "titulo": "Lección de prueba",
        "parte": "adulto",
        "orden": 1,
        "estado": "borrador",
        "autores": [
            {
                "nombre": "Alcy Edmundo Torres Guerrero",
                "orcid": "0000-0002-9742-375X",
                "credit": ["redaccion"],
            }
        ],
        "uso_ia": [],
        "pregunta_clinica": "¿Qué hacemos ante este paciente concreto?",
        "abstract": " ".join(["palabra"] * 50),
        "dialogo_clinico": "Un paciente de prueba con un problema clínico.",
        "indispensable": ["Una perla."],
        "limites": ["Un límite."],
    }
    return {**base, **cambios}


REVISADA = {
    "estado": "revisado",
    "revisor": "Alcy Edmundo Torres Guerrero",
    "fecha_revision": date(2026, 11, 2),
}


def test_un_borrador_puede_declarar_corevisor_sin_fecha() -> None:
    leccion = Leccion.model_validate(_leccion(corevisor="Alcy Ramiro Torres Guerrero"))
    assert leccion.fecha_corevision is None


def test_revisado_con_corevisor_exige_su_fecha() -> None:
    cambios = {**REVISADA, "corevisor": "Alcy Ramiro Torres Guerrero"}
    with pytest.raises(ValidationError, match="requiere fecha_corevision"):
        Leccion.model_validate(_leccion(**cambios))
    completa = {**cambios, "fecha_corevision": date(2026, 11, 3)}
    assert Leccion.model_validate(_leccion(**completa)).estado == "revisado"


def test_la_corevision_no_exigida_no_estorba() -> None:
    assert Leccion.model_validate(_leccion(**REVISADA)).corevisor is None


@pytest.mark.parametrize(
    ("corevisor", "mensaje"),
    [
        ("Alcy Edmundo Torres Guerrero", "distinta del revisor"),
        ("Claude", "el agente nunca revisa"),
    ],
)
def test_el_corevisor_es_otra_persona_nominada(corevisor: str, mensaje: str) -> None:
    cambios = {**REVISADA, "corevisor": corevisor, "fecha_corevision": date(2026, 11, 3)}
    with pytest.raises(ValidationError, match=mensaje):
        Leccion.model_validate(_leccion(**cambios))


def test_fecha_de_corevision_sin_corevisor_es_un_error() -> None:
    with pytest.raises(ValidationError, match="fecha_corevision sin corevisor"):
        Leccion.model_validate(_leccion(fecha_corevision=date(2026, 11, 3)))


# --- coherencia mapa ↔ lección -----------------------------------------------------------------


def _coherencia(corevisor: str | None) -> list[str]:
    mapa = m.cargar()
    fila = mapa.fila("leccion-epilepsias")
    assert fila is not None
    datos: dict[str, Any] = {
        "_archivo": "leccion-epilepsias.qmd",
        "titulo": fila.titulo,
        "parte": fila.parte,
        "orden": fila.orden,
        "modulos_html": list(fila.modulos_html),
        "condiciones": list(fila.condiciones),
        "legado": {},
        "autores": [{"nombre": mapa.personas["aetg"].nombre}],
        "corevisor": corevisor,
    }
    return m.coherencia(mapa, {"leccion-epilepsias": datos})


def test_la_leccion_debe_llevar_el_corevisor_del_mapa() -> None:
    assert any("corevisor «None» ≠ mapa" in e for e in _coherencia(None))
    assert not any("corevisor" in e for e in _coherencia("Alcy Ramiro Torres Guerrero"))


def test_una_leccion_no_inventa_un_corevisor_que_el_mapa_no_asigna() -> None:
    mapa = m.cargar()
    fila = mapa.fila("leccion-estado-epileptico")
    assert fila is not None
    datos: dict[str, Any] = {
        "_archivo": "x.qmd",
        "titulo": fila.titulo,
        "parte": fila.parte,
        "orden": fila.orden,
        "modulos_html": [],
        "condiciones": [],
        "legado": {},
        "autores": [{"nombre": mapa.personas["aetg"].nombre}],
        "corevisor": "Gladys Torres Guerrero",
    }
    errores = m.coherencia(mapa, {"leccion-estado-epileptico": datos})
    assert any("Gladys Torres Guerrero" in e and "≠ mapa" in e for e in errores)


def test_el_esqueleto_de_una_leccion_con_corevision_la_declara() -> None:
    texto = m.esqueleto(m.cargar(), "leccion-epilepsias")
    cabecera = yaml.safe_load(texto.split("---\n")[1])
    assert cabecera["corevisor"] == "Alcy Ramiro Torres Guerrero"
    assert cabecera["fecha_corevision"] is None
    assert "corevisor" not in yaml.safe_load(
        m.esqueleto(m.cargar(), "leccion-ecv-hemorragica").split("---\n")[1]
    )


# --- línea de revisión ---------------------------------------------------------------------


FIRMAS = {
    "Alcy Ramiro Torres Guerrero": "Alcy R. Torres",
    "Alcy Edmundo Torres Guerrero": "Alcy Edmundo Torres Guerrero",
}


def test_la_linea_de_revision_usa_la_firma_bibliografica() -> None:
    datos = {
        **REVISADA,
        "revisor": "Alcy Ramiro Torres Guerrero",
        "corevisor": "Alcy Edmundo Torres Guerrero",
        "fecha_corevision": date(2026, 11, 3),
    }
    linea = linea_revision(datos, FIRMAS)
    assert linea == (
        "*Revisión clínica: Alcy R. Torres (2026-11-02); "
        "corevisión: Alcy Edmundo Torres Guerrero (2026-11-03)*"
    )


def test_un_borrador_no_lleva_linea_de_revision() -> None:
    assert linea_revision({"estado": "borrador", "revisor": "x"}, FIRMAS) is None


def test_la_proyeccion_de_una_leccion_revisada_lleva_la_linea() -> None:
    articulo = Articulo(
        ruta=Path("posts/x.md"),
        condicion_id="HM:6004",
        condicion_nombre="x",
        slug="x",
        fecha="2026-11-01",
        revision_fuente="abc1234",
        concepto_principal=None,
        evidencia={},
        nombres={},
        referencias={},
    )
    datos = {
        **_leccion(),
        **REVISADA,
        "revisor": "Alcy Ramiro Torres Guerrero",
        "condiciones": [],
    }
    archivo = Archivo(Path("leccion-prueba.qmd"), datos, "## Qué significa\n\nTexto.\n")
    texto = proyectar(archivo, {"HM:6004": articulo}, firmas=FIRMAS)
    assert "Revisión clínica: Alcy R. Torres (2026-11-02)" in texto
    assert "Borrador" not in texto
