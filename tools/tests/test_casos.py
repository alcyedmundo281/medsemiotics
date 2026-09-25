"""Contrato de los casos socráticos: la evidencia de la base es el eje y no se reescribe."""

from __future__ import annotations

import copy
import json
from datetime import date
from typing import TYPE_CHECKING, Any

import pytest
import yaml
from conftest import CASO, CUERPO, FRONTMATTER, HOY, escribir_caso

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
    assert exploracion["preguntas"][0]["pregunta"] == "¿Qué aporta signo específico?"
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


def test_hallazgo_medido_en_varias_poblaciones(raiz: Path) -> None:
    frontmatter = copy.deepcopy(FRONTMATTER)
    primera = frontmatter["evidencia"][0]
    primera["poblacion"] = "escolares"
    frontmatter["evidencia"].append(
        {
            **copy.deepcopy(primera),
            "poblacion": "gestantes",
            "lr_positivo": {"valor": 4.7, "ic95": [3.6, 6.0], "ref": "pmid:111"},
        }
    )
    texto = "---\n" + yaml.safe_dump(frontmatter, allow_unicode=True) + "---\n" + CUERPO
    (raiz / "posts" / "HM9999-tema.md").write_text(texto, encoding="utf-8")
    datos = caso()
    datos["etapas"][1]["preguntas"][0]["clave"] = "Todas: {{lr+ HM:0001}}. Solo: {{lr+ HM:0001@2}}."
    resultado = compilado(raiz, datos)
    clave = resultado["etapas"][1]["preguntas"][0]["clave"]
    assert "LR+ 3.1 (IC 95 %: 1.6–5.9) (escolares); LR+ 4.7 (IC 95 %: 3.6–6.0) (gestantes)" in clave
    assert clave.endswith("Solo: LR+ 4.7 (IC 95 %: 3.6–6.0).")
    fichas = [f for f in resultado["etapas"][1]["hallazgos"] if f["id"] == "HM:0001"]
    assert [f["poblacion"] for f in fichas] == ["escolares", "gestantes"]
    datos["etapas"][1]["preguntas"][0]["clave"] = "Fuera de rango: {{lr+ HM:0001@3}}."
    with pytest.raises(ErrorDeCaso, match="2 medición"):
        compilado(raiz, datos)


def _con_tramos(raiz: Path) -> None:
    """HM:0001 como la palpación del aneurisma: una prueba evaluada contra dos definiciones."""
    frontmatter = copy.deepcopy(FRONTMATTER)
    primera = frontmatter["evidencia"][0]
    primera["lr_positivo"]["umbral_condicion"] = "aneurisma de 3.0 cm o mayor"
    primera["lr_negativo"] = {"valor": 0.72, "ic95": [0.65, 0.81], "ref": "pmid:111"}
    primera["advertencia"] = "no excluye el aneurisma"
    primera["graduacion"] = {"parametro": "Diámetro", "unidad": "cm", "lectura": "acumulativo"}
    primera["tramos"] = [
        {
            "umbral_condicion": "aneurisma de 3.0 cm o mayor",
            "lr_positivo": 12.0,
            "ic95": [7.4, 19.5],
            "lr_negativo": 0.72,
            "ic95_negativo": [0.65, 0.81],
            "ref": "pmid:111",
        },
        {
            "umbral": "diámetro palpado ≥ 4 cm",
            "lr_positivo": 15.6,
            "especificidad": 0.95,
            "ref": "pmid:111",
        },
    ]
    texto = "---\n" + yaml.safe_dump(frontmatter, allow_unicode=True) + "---\n" + CUERPO
    (raiz / "posts" / "HM9999-tema.md").write_text(texto, encoding="utf-8")


def test_el_cociente_dice_contra_que_diagnostico_se_mide(raiz: Path) -> None:
    _con_tramos(raiz)
    resultado = compilado(raiz, caso())
    clave = resultado["etapas"][1]["preguntas"][0]["clave"]
    assert "LR+ 3.1 (IC 95 %: 1.6–5.9), para el diagnóstico «aneurisma de 3.0 cm o mayor»" in clave


def test_tramos_por_token(raiz: Path) -> None:
    _con_tramos(raiz)
    datos = caso()
    datos["etapas"][1]["preguntas"][0]["clave"] = (
        "Uno: {{lr- HM:0001#1}}. Dos: {{lr+ HM:0001#2}}, {{esp HM:0001#2}}."
    )
    clave = compilado(raiz, datos)["etapas"][1]["preguntas"][0]["clave"]
    assert "Uno: LR− 0.72 (IC 95 %: 0.65–0.81), para el diagnóstico «aneurisma de 3.0 cm" in clave
    assert "Dos: LR+ 15.6, con umbral «diámetro palpado ≥ 4 cm»" in clave
    assert "especificidad 0.95, con umbral «diámetro palpado ≥ 4 cm»" in clave


@pytest.mark.parametrize(
    ("token", "mensaje"),
    [
        ("{{lr+ HM:0001#3}}", "2 tramo"),
        ("{{lr- HM:0001#2}}", "no registra LR−"),
        ("{{hallazgo HM:0001#1}}", "no admite tramo"),
        ("{{lr+ HM:0002#1}}", "0 tramo"),
    ],
)
def test_tramos_inexistentes(raiz: Path, token: str, mensaje: str) -> None:
    _con_tramos(raiz)
    datos = caso()
    datos["etapas"][2]["preguntas"][0]["clave"] = f"Cita {token}."
    with pytest.raises(ErrorDeCaso, match=mensaje):
        compilado(raiz, datos)


def test_un_tramo_con_varias_mediciones_exige_elegir_la_medicion(raiz: Path) -> None:
    _con_tramos(raiz)
    ruta = raiz / "posts" / "HM9999-tema.md"
    _, frontmatter_texto, cuerpo = ruta.read_text(encoding="utf-8").split("---\n", 2)
    frontmatter = yaml.safe_load(frontmatter_texto)
    frontmatter["evidencia"][0]["poblacion"] = "cribado"
    frontmatter["evidencia"].append({**frontmatter["evidencia"][0], "poblacion": "urgencias"})
    texto = "---\n" + yaml.safe_dump(frontmatter, allow_unicode=True) + "---\n" + cuerpo
    ruta.write_text(texto, encoding="utf-8")
    datos = caso()
    datos["etapas"][1]["preguntas"][0]["clave"] = "Cita {{lr+ HM:0001#2}}."
    with pytest.raises(ErrorDeCaso, match="@n#2"):
        compilado(raiz, datos)
    datos["etapas"][1]["preguntas"][0]["clave"] = "Cita {{lr+ HM:0001@2#2}}."
    assert "LR+ 15.6" in compilado(raiz, datos)["etapas"][1]["preguntas"][0]["clave"]


def test_la_ficha_muestra_tramos_y_advertencia(raiz: Path) -> None:
    from casos.presentacion import markdown

    _con_tramos(raiz)
    resultado = compilado(raiz, caso())
    ficha = resultado["etapas"][1]["hallazgos"][0]
    assert ficha["advertencia"] == "no excluye el aneurisma"
    assert ficha["graduacion"].startswith("Diámetro (cm), lectura acumulativa")
    assert ficha["tramos"] == [
        {
            "etiqueta": "aneurisma de 3.0 cm o mayor",
            "cifras": ["LR+ 12.0 (IC 95 %: 7.4–19.5)", "LR− 0.72 (IC 95 %: 0.65–0.81)"],
        },
        {"etiqueta": "diámetro palpado ≥ 4 cm", "cifras": ["LR+ 15.6", "especificidad 0.95"]},
    ]
    vista = markdown(resultado)
    assert "**Advertencia:** no excluye el aneurisma" in vista
    assert "  2. diámetro palpado ≥ 4 cm: LR+ 15.6; especificidad 0.95" in vista
    # Sin tramos, la ficha lo dice con una lista vacía, no con una clave ausente.
    assert resultado["etapas"][2]["hallazgos"][0]["tramos"] == []


def test_nombres_en_minuscula_dentro_de_la_oracion() -> None:
    from casos.evidencia import _inicio_de_oracion, _minuscula_inicial

    assert _minuscula_inicial("Fiebre") == "fiebre"
    assert _minuscula_inicial("ECG con elevación del ST") == "ECG con elevación del ST"
    assert _inicio_de_oracion("Hola. ", 6)
    assert _inicio_de_oracion("", 0)
    assert not _inicio_de_oracion("Se observa ", 11)
