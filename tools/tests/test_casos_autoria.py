"""Autoría de casos y fichas: personas reales del mapa, no un nombre genérico (ADR-001)."""

from __future__ import annotations

import re
from typing import Any

import pytest
import yaml
from pydantic import ValidationError

from casos.__main__ import _autor
from casos.compilar import RAIZ, Rutas, leer_casos
from casos.errores import ErrorDeCaso
from casos.modelo import Autoria
from lecciones import mapa as mapa_libro

NOMBRE_GENERICO = "Dr. Alcy Torres"


def _personas() -> dict[str, Any]:
    return mapa_libro.cargar().personas


def _firma(persona: Any) -> str:
    return str(persona.nombre_bibliografico or persona.nombre)


# --- el modelo -----------------------------------------------------------------------------


def test_la_autoria_es_una_lista_de_autores_con_creditos() -> None:
    autoria = Autoria.model_validate(
        {
            "autores": [
                {
                    "nombre": "Alcy Ramiro Torres Guerrero",
                    "orcid": "0000-0001-5798-9161",
                    "credit": ["redaccion"],
                }
            ],
            "revisor": "Alcy Edmundo Torres Guerrero",
        }
    )
    assert autoria.autores[0].orcid == "0000-0001-5798-9161"
    assert autoria.autores[0].credit == ["redaccion"]


@pytest.mark.parametrize(
    ("autoria", "mensaje"),
    [
        ({"autores": [], "revisor": None}, "at least 1"),
        ({"autor": NOMBRE_GENERICO, "revisor": None}, "autores"),
        (
            {"autores": [{"nombre": "X", "credit": ["redaccion"]}], "revisor": "Claude"},
            "el agente nunca es revisor",
        ),
        (
            {
                "autores": [
                    {"nombre": "X", "orcid": "0000-0001-5798-" + "9162", "credit": ["redaccion"]}
                ]
            },
            "ORCID inválido",
        ),
        ({"autores": [{"nombre": "X", "credit": []}]}, "at least 1"),
    ],
)
def test_reglas_de_la_autoria(autoria: dict[str, Any], mensaje: str) -> None:
    with pytest.raises(ValidationError, match=mensaje):
        Autoria.model_validate(autoria)


def test_el_autor_de_un_caso_nuevo_es_una_persona_viva_del_mapa() -> None:
    assert _autor("artg")["nombre"] == "Alcy Ramiro Torres Guerrero"
    assert _autor("artg")["nombre_bibliografico"] == "Alcy R. Torres"
    with pytest.raises(ErrorDeCaso, match="no es una persona viva"):
        _autor("atc")  # fallecido
    with pytest.raises(ErrorDeCaso, match="no es una persona viva"):
        _autor("inventado")


# --- los casos existentes ------------------------------------------------------------------


def _casos() -> list[Any]:
    return leer_casos(Rutas(RAIZ))


def test_cada_autor_de_cada_caso_es_una_persona_del_mapa() -> None:
    personas = {p.nombre: p for p in _personas().values()}
    for leido in _casos():
        for autor in leido.caso.autoria.autores:
            persona = personas.get(autor.nombre)
            assert persona is not None, f"{leido.caso.condicion_id}: autor fuera del mapa"
            assert autor.orcid == persona.orcid
            assert autor.nombre_bibliografico == persona.nombre_bibliografico
            assert not persona.fallecido


def test_el_revisor_de_cada_caso_es_una_persona_del_mapa() -> None:
    nombres = {p.nombre for p in _personas().values() if not p.fallecido}
    for leido in _casos():
        revisor = leido.caso.autoria.revisor
        assert revisor is None or revisor in nombres, leido.caso.condicion_id


def test_ningun_caso_lleva_el_nombre_generico() -> None:
    for ruta in (RAIZ / "casos").glob("HM*.yaml"):
        assert NOMBRE_GENERICO not in ruta.read_text(encoding="utf-8"), ruta.name


def test_el_libro_muestra_los_autores_del_caso_no_none() -> None:
    from libro.datos import leer_condiciones_neurologia, renderizar_caso_qmd

    caso = next(c.caso for c in leer_condiciones_neurologia(RAIZ) if c.caso is not None)
    texto = renderizar_caso_qmd(caso)
    assert "Autoría: Alcy E. Torres-Guerrero" in texto
    ficha = texto.split("**Ficha del caso:**")[1].splitlines()[0]
    assert "None" not in ficha


# --- las fichas del blog ------------------------------------------------------------------


def _posts() -> dict[str, str]:
    salida: dict[str, str] = {}
    for ruta in sorted((RAIZ / "posts").glob("*.md")):
        cabecera = yaml.safe_load(re.split(r"^---\s*$", ruta.read_text("utf-8"), flags=re.M)[1])
        salida[cabecera["grounding"]["condicion_id"]] = cabecera["author"]
    return salida


def test_ninguna_ficha_muestra_el_nombre_generico() -> None:
    posts = _posts()
    assert posts
    assert NOMBRE_GENERICO not in posts.values()


def test_cada_ficha_la_firma_una_persona_viva_del_mapa() -> None:
    firmas = {_firma(p) for p in _personas().values() if not p.fallecido}
    for cid, autor in _posts().items():
        assert autor in firmas, f"{cid}: «{autor}» no es la firma de ninguna persona del mapa"


def test_la_ficha_muestra_el_mismo_autor_que_su_caso() -> None:
    posts = _posts()
    for leido in _casos():
        autores = ", ".join(a.nombre_bibliografico or a.nombre for a in leido.caso.autoria.autores)
        cid = leido.caso.condicion_id
        if cid in posts:
            assert posts[cid] == autores, f"{cid}: ficha «{posts[cid]}» ≠ caso «{autores}»"
