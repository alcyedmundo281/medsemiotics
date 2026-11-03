"""Autoevaluaciones: forma, autoría contra el mapa, tokens que resuelven y revisión humana."""

from __future__ import annotations

import copy
from typing import Any

import pytest
import yaml

from lecciones import autoevaluacion as ae
from lecciones.evidencia import cargar_articulos
from lecciones.fuente import RAIZ, archivos
from lecciones.mapa import cargar as cargar_mapa

ID = "leccion-examen-neurologico-recien-nacido"
ARCHIVO = RAIZ / "lecciones" / "autoevaluaciones" / f"{ID}.yaml"
MAPA = cargar_mapa()
LECCIONES = ae.lecciones_por_id(archivos())
ARTICULOS = cargar_articulos()


def _original() -> dict[str, Any]:
    datos = yaml.safe_load(ARCHIVO.read_text(encoding="utf-8"))
    assert isinstance(datos, dict)
    return datos


def _problemas(datos: dict[str, Any], nombre: str = f"{ID}.yaml") -> list[str]:
    return ae.problemas_de_datos(nombre, datos, MAPA, LECCIONES, ARTICULOS)


def _con(**cambios: Any) -> dict[str, Any]:
    datos = copy.deepcopy(_original())
    datos.update(cambios)
    return datos


def _pregunta(i: int = 0, **cambios: Any) -> dict[str, Any]:
    datos = copy.deepcopy(_original())
    datos["preguntas"][i].update(cambios)
    return datos


def test_la_autoevaluacion_del_repositorio_es_valida() -> None:
    assert _problemas(_original()) == []
    assert ae.problemas_de_autoevaluaciones(RAIZ, MAPA, LECCIONES, ARTICULOS) == []


def test_la_leccion_debe_existir() -> None:
    datos = _con(leccion="leccion-que-no-existe")
    problemas = _problemas(datos, "leccion-que-no-existe.yaml")
    assert any("no existe en lecciones/" in p for p in problemas)


def test_el_archivo_se_llama_como_su_leccion() -> None:
    assert any("debe llamarse" in p for p in _problemas(_original(), "otro.yaml"))


def test_los_autores_son_claves_del_mapa_y_de_las_autoevaluaciones() -> None:
    assert any("«nadie» no está" in p for p in _problemas(_con(autores=["nadie"])))
    assert any("no figura entre los autores" in p for p in _problemas(_con(autores=["gtg"])))


def test_el_revisor_es_el_del_mapa() -> None:
    assert any("«nadie» no está" in p for p in _problemas(_con(revisor="nadie")))
    assert any("no es el revisor" in p for p in _problemas(_con(revisor="artg")))
    assert any("no es el revisor" in p for p in _problemas(_con(revisor="dtt")))


def test_una_pregunta_tiene_cuatro_opciones() -> None:
    datos = copy.deepcopy(_original())
    del datos["preguntas"][0]["opciones"]["D"]
    assert any("A, B, C y D" in p for p in _problemas(datos))
    datos = copy.deepcopy(_original())
    datos["preguntas"][0]["opciones"]["E"] = "Otra"
    assert _problemas(datos)


def test_dos_opciones_no_dicen_lo_mismo() -> None:
    datos = copy.deepcopy(_original())
    opciones = datos["preguntas"][0]["opciones"]
    opciones["B"] = opciones["A"]
    assert any("dicen lo mismo" in p for p in _problemas(datos))


def test_hay_una_sola_correcta_y_es_una_de_las_opciones() -> None:
    assert _problemas(_pregunta(correcta="E"))
    assert _problemas(_pregunta(correcta=["A", "B"]))
    assert _problemas(_pregunta(correcta=None))


def test_los_ids_de_pregunta_no_se_repiten() -> None:
    datos = copy.deepcopy(_original())
    datos["preguntas"][1]["id"] = datos["preguntas"][0]["id"]
    assert any("id repetido" in p for p in _problemas(datos))


def test_un_token_que_no_resuelve_es_un_error() -> None:
    malo = _pregunta(enunciado="Dato: {{lr+ HM:9999999}}.")
    assert any("HM:9999999" in p for p in _problemas(malo))


def test_un_token_de_un_concepto_ajeno_a_la_leccion_es_un_error() -> None:
    ajeno = _pregunta(explicacion="Dato: {{lr+ HM:3012}}.")
    assert any("no figura en «conceptos»" in p for p in _problemas(ajeno))


@pytest.mark.parametrize(
    "texto",
    [
        "El cociente de verosimilitud positivo es 8 para este signo.",
        "La sensibilidad fue de 85 % en la serie.",
        "Su LR+ es de 3,5.",
    ],
)
def test_ninguna_cifra_de_rendimiento_sin_token(texto: str) -> None:
    problemas = _problemas(_pregunta(explicacion=texto))
    assert any("escrito a mano" in p or "escrita a mano" in p for p in problemas)


def test_una_cifra_de_datos_del_paciente_no_exige_token() -> None:
    assert _problemas(_pregunta(enunciado="Un recién nacido de 38 semanas llora sin parar.")) == []


def test_revisado_requiere_revisor_humano_y_fecha() -> None:
    sin_revisor = _con(estado="revisado", revisor=None, fecha_revision="2026-11-03")
    assert any("requiere un revisor" in p for p in _problemas(sin_revisor))
    sin_fecha = _con(estado="revisado", revisor="aetg", fecha_revision=None)
    assert any("requiere fecha_revision" in p for p in _problemas(sin_fecha))
    agente = _con(estado="revisado", revisor="Claude", fecha_revision="2026-11-03")
    assert any("el agente nunca es revisor" in p for p in _problemas(agente))
    humano = _con(estado="revisado", revisor="aetg", fecha_revision="2026-11-03")
    assert _problemas(humano) == []


def test_un_yaml_invalido_se_informa_sin_romper(tmp_path: Any) -> None:
    carpeta = tmp_path / "lecciones" / "autoevaluaciones"
    carpeta.mkdir(parents=True)
    (carpeta / "x.yaml").write_text("a: [sin cerrar", encoding="utf-8")
    problemas = ae.problemas_de_autoevaluaciones(tmp_path, MAPA, LECCIONES, ARTICULOS)
    assert any("YAML inválido" in p for p in problemas)
