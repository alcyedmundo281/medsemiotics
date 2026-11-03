"""«Sobre los autores»: una semblanza por persona, aprobada por su titular antes de imprimirse."""

from __future__ import annotations

import shutil
from typing import TYPE_CHECKING

import pytest

from lecciones import mapa as m
from lecciones.semblanzas import problemas_de_semblanzas, separar, verificar
from libro.datos import RAIZ
from libro.qmd import generar_proyecto_quarto

if TYPE_CHECKING:
    from pathlib import Path

CLAVES = ["atc", "artg", "gtg", "aetg", "dtt"]
VIVOS = ["artg", "gtg", "aetg", "dtt"]


def _texto(aprobaciones: dict[str, tuple[list[str], str]], cuerpos: dict[str, str]) -> str:
    registro = "\n".join(
        f"  {k}: {{aprobada_por: {aprobaciones.get(k, ([], 'null'))[0]}, "
        f"fecha: {aprobaciones.get(k, ([], 'null'))[1]}}}"
        for k in CLAVES
    )
    secciones = "\n\n".join(
        f"### Nombre {k} {{#sobre-{k} .unnumbered}}\n\n{cuerpos.get(k, '')}" for k in CLAVES
    )
    return f"---\nsemblanzas:\n{registro}\n---\n\n## SOBRE LOS AUTORES {{.unnumbered}}\n\n{secciones}\n"


def _completo() -> str:
    aprobaciones = {k: ([k], "2026-11-03") for k in VIVOS} | {"atc": (VIVOS, "2026-11-03")}
    return _texto(aprobaciones, {k: f"Semblanza de {k}." for k in CLAVES})


def test_el_orden_del_paratexto_es_el_de_autoria() -> None:
    assert list(m.cargar().personas) == CLAVES


def test_la_semblanza_de_gtg_esta_pendiente_de_su_aprobacion() -> None:
    texto = (RAIZ / "lecciones" / "paratextos" / "autores.md").read_text(encoding="utf-8")
    datos, cuerpo = separar(texto)
    assert datos["semblanzas"]["gtg"] == {"aprobada_por": [], "fecha": None}
    assert "directora ejecutiva de VisionUno, en Quito" in cuerpo
    assert "Bascom Palmer" in cuerpo
    # Las demás siguen vacías hasta que las envíen sus titulares.
    assert all(f"{{#sobre-{k} .unnumbered}}\n\n###" in cuerpo or k == "dtt" for k in CLAVES if k != "gtg")


def test_afiliacion_de_gtg_en_el_mapa() -> None:
    assert m.cargar().personas["gtg"].afiliacion == "VisionUno, Quito"


def test_el_paratexto_del_repositorio_aun_no_se_puede_imprimir() -> None:
    problemas = verificar(RAIZ)
    assert any("Gladys Torres Guerrero" in p and "sin aprobar" in p for p in problemas)
    assert any("Daniela Torres Tobar" in p and "sin texto" in p for p in problemas)


def test_un_paratexto_completo_y_aprobado_no_da_problemas() -> None:
    assert problemas_de_semblanzas(_completo(), m.cargar()) == []


def test_la_de_un_autor_vivo_la_aprueba_su_titular_y_no_otro() -> None:
    texto = _completo().replace("gtg: {aprobada_por: ['gtg']", "gtg: {aprobada_por: ['aetg']")
    problemas = problemas_de_semblanzas(texto, m.cargar())
    assert problemas == ["semblanza de Gladys Torres Guerrero: sin aprobar por Gladys Torres Guerrero"]


def test_la_de_atc_la_aprueban_todos_los_autores_vivos() -> None:
    texto = _completo().replace(
        "atc: {aprobada_por: ['artg', 'gtg', 'aetg', 'dtt']", "atc: {aprobada_por: ['artg', 'aetg']"
    )
    (problema,) = problemas_de_semblanzas(texto, m.cargar())
    assert "Alcy Torres Catefort" in problema
    assert "Gladys Torres Guerrero" in problema
    assert "Daniela Torres Tobar" in problema


def test_aprobar_sin_fecha_no_basta() -> None:
    texto = _completo().replace("dtt: {aprobada_por: ['dtt'], fecha: 2026-11-03}", "dtt: {aprobada_por: ['dtt'], fecha: null}")
    assert problemas_de_semblanzas(texto, m.cargar()) == [
        "semblanza de Daniela Torres Tobar: falta la fecha de aprobación"
    ]


def test_el_orden_de_las_secciones_se_comprueba() -> None:
    texto = _completo().replace("#sobre-artg", "#sobre-tmp").replace("#sobre-gtg", "#sobre-artg")
    texto = texto.replace("#sobre-tmp", "#sobre-gtg")
    assert any("en el orden de autoría" in p for p in problemas_de_semblanzas(texto, m.cargar()))


def test_la_compilacion_falla_mientras_haya_semblanzas_sin_aprobar(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="Sobre los autores"):
        generar_proyecto_quarto(tmp_path, RAIZ)


def test_aprobado_el_paratexto_se_imprime_sin_su_frontmatter(tmp_path: Path) -> None:
    raiz = tmp_path / "repo"
    shutil.copytree(RAIZ / "lecciones", raiz / "lecciones", ignore=shutil.ignore_patterns("*.qmd"))
    for carpeta in ("posts", "casos"):
        if (RAIZ / carpeta).is_dir():
            shutil.copytree(RAIZ / carpeta, raiz / carpeta)
    shutil.copyfile(RAIZ / "CITATION.cff", raiz / "CITATION.cff")
    (raiz / "lecciones" / "paratextos" / "autores.md").write_text(_completo(), encoding="utf-8")
    salida = tmp_path / "quarto"
    generar_proyecto_quarto(salida, raiz)
    qmd = (salida / "P-autores.qmd").read_text(encoding="utf-8")
    assert "aprobada_por" not in qmd
    assert qmd.startswith("\n## SOBRE LOS AUTORES") or qmd.startswith("## SOBRE LOS AUTORES")
    assert "Semblanza de dtt." in qmd
