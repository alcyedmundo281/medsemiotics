"""Contrato de los casos socráticos: la evidencia de la base es el eje y no se reescribe."""

from __future__ import annotations

import copy
import json
from datetime import date
from typing import TYPE_CHECKING, Any

import pytest
from conftest import CASO, HOY, escribir_caso

from casos.compilar import Rutas, compilar, construir, leer_casos
from casos.errores import ErrorDeCaso

if TYPE_CHECKING:
    from pathlib import Path


def caso(**cambios: Any) -> dict[str, Any]:
    datos = copy.deepcopy(CASO)
    datos.update(cambios)
    return datos


def compilado(raiz: Path, datos: dict[str, Any]) -> dict[str, Any]:
    escribir_caso(raiz, datos)
    (leido,) = leer_casos(Rutas(raiz))
    return compilar(leido, HOY)


def test_las_cifras_llegan_desde_la_base_con_su_incertidumbre(raiz: Path) -> None:
    resultado = compilado(raiz, caso())
    exploracion, discriminacion = resultado["etapas"][1], resultado["etapas"][2]
    clave = exploracion["preguntas"][0]["clave"]
    assert "LR+ 3.1 (IC 95 %: 1.6–5.9)" in clave
    assert "especificidad 0.87" in clave
    assert exploracion["preguntas"][0]["pregunta"] == "¿Qué aporta Signo específico?"
    # Un rango nunca se convierte en estimación puntual.
    assert "LR− entre 0.23 y 0.44 (rango entre estudios" in discriminacion["preguntas"][0]["clave"]
    ficha = exploracion["hallazgos"][0]
    assert ficha["nombre"] == "Signo específico"
    assert ficha["cifras"] == ["LR+ 3.1 (IC 95 %: 1.6–5.9)", "especificidad 0.87"]
    assert ficha["referencias"] == ["pmid:111"]
    assert exploracion["hallazgos"][1]["estado"] == "sin efecto discriminativo"
    assert resultado["referencias"] == [
        {"id": "pmid:111", "cita": "Estudio de referencia. JAMA, 2016. DOI: 10.1/x."}
    ]
    assert resultado["fuente_revision"] == "abc123"


@pytest.mark.parametrize(
    "texto",
    [
        "El LR+ de 3.1 lo convierte en útil.",
        "Tiene una sensibilidad del 91 %.",
        "Especificidad: 0.87",
        "El cociente de verosimilitud positivo es 3.1",
        "IC 95 % 1.6 a 5.9",
        "Según PMID 111",
        "Ver HM:0001",
    ],
)
def test_prohibe_cifras_escritas_a_mano(raiz: Path, texto: str) -> None:
    datos = caso()
    datos["etapas"][1]["preguntas"][0]["clave"] = texto
    with pytest.raises(ErrorDeCaso):
        compilado(raiz, datos)


def test_la_vineta_admite_datos_clinicos_con_numeros(raiz: Path) -> None:
    resultado = compilado(raiz, caso())
    assert resultado["vineta"]["datos"] == [{"etiqueta": "Temperatura", "valor": "38.4 °C"}]


def test_no_se_adelanta_evidencia_no_revelada(raiz: Path) -> None:
    datos = caso()
    datos["etapas"][1]["preguntas"][0]["clave"] = "Compárelo con {{lr- HM:0002}}."
    with pytest.raises(ErrorDeCaso, match="antes de revelarse"):
        compilado(raiz, datos)


def test_la_vineta_no_cita_evidencia(raiz: Path) -> None:
    datos = caso()
    datos["vineta"]["texto"] = "Paciente con {{hallazgo HM:0001}} desde hace días."
    with pytest.raises(ErrorDeCaso, match="antes de revelarse"):
        compilado(raiz, datos)


def test_ningun_hallazgo_de_la_base_desaparece_sin_motivo(raiz: Path) -> None:
    datos = caso()
    datos["etapas"][1]["hallazgos"] = ["HM:0001"]
    with pytest.raises(ErrorDeCaso, match=r"HM:0003 \(Síntoma inespecífico\)"):
        compilado(raiz, datos)
    datos["omitidos"] = [{"hallazgo": "HM:0003", "motivo": "No aporta al razonamiento del caso."}]
    assert compilado(raiz, datos)["omitidos"][0]["nombre"] == "Síntoma inespecífico"


def test_el_hallazgo_principal_debe_revelarse(raiz: Path) -> None:
    datos = caso()
    datos["etapas"][1]["hallazgos"] = ["HM:0003"]
    datos["omitidos"] = [{"hallazgo": "HM:0001", "motivo": "Se estudia en otro caso distinto."}]
    datos["etapas"][1]["preguntas"][0] = {
        "pregunta": "¿Qué ves en el cuello?",
        "clave": "Nada. Sigue explorando.",
    }
    with pytest.raises(ErrorDeCaso, match="hallazgo principal"):
        compilado(raiz, datos)


def test_no_se_cita_lr_de_un_hallazgo_sin_lr_medido(raiz: Path) -> None:
    datos = caso()
    datos["etapas"][1]["preguntas"][0]["clave"] = "Su cociente es {{lr+ HM:0003}}."
    with pytest.raises(ErrorDeCaso, match="no hay LR medido"):
        compilado(raiz, datos)


def test_hallazgo_ajeno_a_la_condicion(raiz: Path) -> None:
    datos = caso()
    datos["etapas"][2]["hallazgos"] = ["HM:0002", "HM:0404"]
    with pytest.raises(ErrorDeCaso, match="HM:0404 no está en la evidencia"):
        compilado(raiz, datos)


@pytest.mark.parametrize(
    ("fases", "mensaje"),
    [
        (["exploracion", "exploracion", "discriminacion", "decision"], "empezar"),
        (["activacion", "discriminacion", "exploracion", "decision"], "orden"),
        (["activacion", "exploracion", "exploracion", "decision"], "discriminacion"),
    ],
)
def test_secuencia_abp(raiz: Path, fases: list[str], mensaje: str) -> None:
    datos = caso()
    for etapa, fase in zip(datos["etapas"], fases, strict=True):
        etapa["fase"] = fase
        etapa.setdefault("hallazgos", [])
    datos["etapas"][0]["hallazgos"] = datos["etapas"][0]["hallazgos"] or ["HM:0003"]
    datos["etapas"][1]["hallazgos"] = ["HM:0001"]
    with pytest.raises(ErrorDeCaso, match=mensaje):
        compilado(raiz, datos)


def test_publicar_exige_revisor_humano_y_fecha(raiz: Path) -> None:
    with pytest.raises(ErrorDeCaso, match="revisor humano"):
        compilado(raiz, caso(estado="publicado", publicacion={"fecha": date(2026, 9, 20)}))
    datos = caso(estado="publicado")
    datos["autoria"] = {"autor": "Dr. Alcy Torres", "revisor": "Dr. Alcy Torres"}
    with pytest.raises(ErrorDeCaso, match=r"publicacion\.fecha"):
        compilado(raiz, datos)
    with pytest.raises(ErrorDeCaso, match="no puede tener fecha"):
        compilado(raiz, caso(publicacion={"fecha": date(2026, 9, 20)}))


def publicado(**publicacion: Any) -> dict[str, Any]:
    datos = caso(estado="publicado", publicacion=publicacion)
    datos["autoria"] = {"autor": "Dr. Alcy Torres", "revisor": "Dr. Alcy Torres"}
    return datos


def test_fechas_de_publicacion_y_revisiones(raiz: Path) -> None:
    resultado = compilado(
        raiz,
        publicado(
            fecha=date(2026, 9, 1),
            revisiones=[{"fecha": date(2026, 9, 15), "nota": "Actualiza la etapa de decisión."}],
        ),
    )
    assert resultado["publicacion"] == {
        "fecha": "2026-09-01",
        "version": 2,
        "ultima_revision": "2026-09-15",
        "revisiones": [{"fecha": "2026-09-15", "nota": "Actualiza la etapa de decisión."}],
    }
    with pytest.raises(ErrorDeCaso, match="futura"):
        compilado(raiz, publicado(fecha=date(2026, 10, 1)))
    with pytest.raises(ErrorDeCaso, match="no es posterior"):
        compilado(
            raiz,
            publicado(
                fecha=date(2026, 9, 10),
                revisiones=[{"fecha": date(2026, 9, 5), "nota": "Revisión fuera de orden."}],
            ),
        )


def test_solo_los_publicados_llegan_al_sitio(raiz: Path) -> None:
    rutas = Rutas(raiz)
    escribir_caso(raiz, caso())
    assert construir(rutas, HOY, solo_comprobar=False) == []
    assert not list(rutas.salida.glob("*.json"))
    escribir_caso(raiz, publicado(fecha=date(2026, 9, 20)))
    assert construir(rutas, HOY, solo_comprobar=True) == ["assets/data/casos/tema-de-prueba.json"]
    construir(rutas, HOY, solo_comprobar=False)
    assert construir(rutas, HOY, solo_comprobar=True) == []
    datos = json.loads((rutas.salida / "tema-de-prueba.json").read_text(encoding="utf-8"))
    assert datos["slug"] == "tema-de-prueba"
    # Si vuelve a borrador, el JSON publicado se retira.
    escribir_caso(raiz, caso())
    assert construir(rutas, HOY, solo_comprobar=False) == ["assets/data/casos/tema-de-prueba.json"]
    assert not (rutas.salida / "tema-de-prueba.json").exists()


def test_esquema_estricto(raiz: Path) -> None:
    with pytest.raises(ErrorDeCaso, match="campo_inventado"):
        compilado(raiz, caso(campo_inventado=True))
    with pytest.raises(ErrorDeCaso, match="debe poner en juego"):
        datos = caso()
        datos["etapas"][2]["hallazgos"] = []
        compilado(raiz, datos)


def test_nombre_de_archivo_coherente(raiz: Path) -> None:
    escribir_caso(raiz, caso())
    (raiz / "casos" / "HM9999.yaml").rename(raiz / "casos" / "HM1234.yaml")
    with pytest.raises(ErrorDeCaso, match=r"debe llamarse HM9999.yaml"):
        leer_casos(Rutas(raiz))
