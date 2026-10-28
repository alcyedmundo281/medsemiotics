"""Política de imágenes: Wikimedia Commons, dominio público o CC0, verificadas."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import pytest
from conftest import HOY

from imagenes import commons, registro
from imagenes.__main__ import comprobar, main

if TYPE_CHECKING:
    from pathlib import Path


def pagina(licencia: str, nombre: str, mime: str = "image/jpeg") -> dict[str, Any]:
    return {
        "title": "File:Ejemplo.jpg",
        "index": 1,
        "imageinfo": [
            {
                "url": "https://upload.wikimedia.org/wikipedia/commons/a/ab/Ejemplo.jpg?utm_source=x",
                "thumburl": "https://thumb.wikimedia.org/wikipedia/commons/thumb/a/ab/Ejemplo.jpg/"
                "1280px-Ejemplo.jpg?utm_source=x",
                "descriptionurl": "https://commons.wikimedia.org/wiki/File:Ejemplo.jpg",
                "width": 2000,
                "height": 1500,
                "mime": mime,
                "extmetadata": {
                    "License": {"value": licencia},
                    "LicenseShortName": {"value": nombre},
                    "Artist": {"value": '<a href="//x">Autora <b>Ejemplo</b></a>'},
                    "ImageDescription": {"value": "Signo clínico &amp; exploración"},
                },
            }
        ],
    }


def api(*paginas: dict[str, Any]) -> Any:
    return lambda _url: {"query": {"pages": list(paginas)}}


@pytest.mark.parametrize(
    ("codigo", "nombre", "esperada"),
    [
        ("pd", "Public domain", "Public domain"),
        ("pd-usgov", "Public domain", "Public domain"),
        ("cc0", "CC0", "CC0"),
    ],
)
def test_acepta_dominio_publico(codigo: str, nombre: str, esperada: str) -> None:
    imagen = commons.obtener("Ejemplo.jpg", api(pagina(codigo, nombre)))
    assert imagen.licencia == esperada
    assert imagen.autor == "Autora Ejemplo"
    assert imagen.descripcion == "Signo clínico & exploración"
    assert "?" not in imagen.url and "?" not in imagen.miniatura


@pytest.mark.parametrize(
    ("codigo", "nombre"),
    [("cc-by-sa-4.0", "CC BY-SA 4.0"), ("cc-by-2.0", "CC BY 2.0"), ("", "GFDL"), ("", "")],
)
def test_rechaza_licencias_con_condiciones(codigo: str, nombre: str) -> None:
    with pytest.raises(commons.LicenciaNoPermitida):
        commons.obtener("Ejemplo.jpg", api(pagina(codigo, nombre)))
    assert commons.buscar("x", api(pagina(codigo, nombre))) == []


def test_busqueda_descarta_formatos_no_imagen() -> None:
    assert commons.buscar("x", api(pagina("pd", "Public domain", "application/pdf"))) == []


def test_registro_y_comprobacion(raiz: Path) -> None:
    imagen = commons.obtener("Ejemplo.jpg", api(pagina("cc0", "CC0")))
    entrada = registro.entrada(imagen, "Fotografía de la exploración del signo", HOY)
    assert registro.problemas("HM9999", entrada) == []
    assert entrada["verified"] == "2026-09-21"
    malo = {**entrada, "license": "CC BY-SA 4.0", "alt": "foto"}
    assert len(registro.problemas("HM9999", malo)) == 2

    archivo = raiz / "assets" / "data" / "topic-images.json"
    archivo.parent.mkdir(parents=True)
    archivo.write_text(json.dumps({}), encoding="utf-8")
    assert comprobar(raiz, estricto=False, online=False) == []
    assert comprobar(raiz, estricto=True, online=False) == [
        "HM9999: artículo sin imagen destacada en dominio público."
    ]
    registro.escribir({"HM9999": entrada, "HM1234": entrada}, archivo)
    assert comprobar(raiz, estricto=True, online=False) == [
        "HM1234: imagen de una condición sin artículo."
    ]


def test_autor_duplicado_o_desconocido() -> None:
    assert commons._autor("Unknown author Unknown author") == "Autor no declarado"
    assert commons._autor("CDC CDC") == "CDC"
    assert commons._autor("R. G. Wiener, Harlem Hospital") == "R. G. Wiener, Harlem Hospital"


def test_imagen_modulo_y_licencia(raiz: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    modulo = "gastroenterologia/esofago.html"
    pagina_html = raiz / modulo
    pagina_html.parent.mkdir(parents=True)
    pagina_html.write_text("<!doctype html>", encoding="utf-8")
    (raiz / "assets" / "data").mkdir(parents=True)
    monkeypatch.setattr(registro, "RAIZ", raiz)
    imagen = commons.obtener("Ejemplo.jpg", api(pagina("pd", "Public domain")))
    monkeypatch.setattr(commons, "obtener", lambda _: imagen)
    assert (
        main(
            [
                "asignar",
                modulo,
                "Ejemplo.jpg",
                "--modulo",
                "--alt",
                "Anatomía del esófago y su trayecto",
            ]
        )
        == 0
    )
    archivo = raiz / "assets" / "data" / registro.MODULOS
    assert registro.leer(archivo)[modulo]["license"] == "Public domain"
    assert comprobar(raiz, estricto=False, online=False) == []
    entrada = {**registro.leer(archivo)[modulo], "license": "CC BY-SA 4.0"}
    registro.escribir({modulo: entrada}, archivo)
    assert any("licencia" in error for error in comprobar(raiz, estricto=False, online=False))
    with pytest.raises(ValueError, match="ruta relativa"):
        main(
            [
                "asignar",
                "../fuera.html",
                "Ejemplo.jpg",
                "--modulo",
                "--alt",
                "Una descripción extensa",
            ]
        )
