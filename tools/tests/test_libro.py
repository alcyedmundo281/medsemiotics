"""Pruebas unitarias y de integración del generador del libro de Neurología."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
import yaml

from libro import (
    ALTO_MM,
    ALTO_PT,
    ALTO_PULGADAS,
    ANCHO_MM,
    ANCHO_PT,
    ANCHO_PULGADAS,
    CONDICIONES_NEUROLOGIA,
)
from libro import (
    __main__ as cli_libro,
)
from libro.datos import (
    RAIZ,
    leer_condiciones_neurologia,
    leer_imagenes_condiciones,
    leer_metadatos,
    todos_los_hallazgos,
)
from libro.modulos import (
    obtener_banco_autoevaluacion,
    obtener_capitulos_modulos,
    verificar_fuentes_neurologia,
)
from libro.pdf import parsear_salida_pdfinfo, validar_info_pdf, validar_tex_libro
from libro.qmd import NOMBRES_QMD_CONDICIONES, generar_proyecto_quarto

if TYPE_CHECKING:
    from pathlib import Path


def test_dimensiones_catalogo_kdp_ingramspark() -> None:
    """Verifica que las dimensiones coincidan con el catálogo 6,69 × 9,61 in = 170 × 244 mm."""
    assert ANCHO_MM == 170
    assert ALTO_MM == 244
    assert pytest.approx(6.69, abs=0.01) == ANCHO_PULGADAS
    assert pytest.approx(9.61, abs=0.01) == ALTO_PULGADAS
    assert pytest.approx(170 * 72.0 / 25.4, abs=0.05) == ANCHO_PT
    assert pytest.approx(244 * 72.0 / 25.4, abs=0.05) == ALTO_PT


def test_fuentes_y_condiciones_neurologia() -> None:
    assert verificar_fuentes_neurologia(RAIZ) == []
    meta = leer_metadatos(RAIZ)
    assert "Neurología" in meta.titulo
    assert meta.doi.startswith("10.5281/zenodo.")

    condiciones = leer_condiciones_neurologia(RAIZ)
    assert tuple(c.condicion_id for c in condiciones) == CONDICIONES_NEUROLOGIA
    # HM:6004 tiene caso socrático publicado e imagen verificada
    hm6004 = next(c for c in condiciones if c.condicion_id == "HM:6004")
    assert hm6004.caso is not None
    assert hm6004.imagen is not None
    assert ":::" in hm6004.cuerpo_qmd
    assert "Kernig" in hm6004.cuerpo_qmd

    filas = todos_los_hallazgos(condiciones)
    assert len(filas) >= 15

    imagenes = leer_imagenes_condiciones(RAIZ)
    for cid in CONDICIONES_NEUROLOGIA:
        assert cid in imagenes


def test_generar_proyecto_quarto(tmp_path: Path) -> None:
    carpeta = tmp_path / "quarto"
    archivos = generar_proyecto_quarto(carpeta, raiz=RAIZ)
    assert (carpeta / "_quarto.yml").is_file()
    assert (carpeta / "index.qmd").is_file()
    assert (carpeta / "preambulo-libro.tex").is_file()
    assert (carpeta / "diseno-pdf.lua").is_file()
    assert (carpeta / "portada.svg").is_file()
    assert (carpeta / "libro-plano.md").is_file()
    assert len(archivos) >= 18

    cfg = yaml.safe_load((carpeta / "_quarto.yml").read_text(encoding="utf-8"))
    geometria = cfg["format"]["pdf"]["geometry"]
    assert "paperwidth=170mm" in geometria
    assert "paperheight=244mm" in geometria
    assert cfg["format"]["pdf"]["pdf-engine"] == "lualatex"
    assert cfg["format"]["pdf"]["documentclass"] == "scrbook"

    for nombre_qmd in NOMBRES_QMD_CONDICIONES.values():
        assert (carpeta / nombre_qmd).is_file()

    for cap in obtener_capitulos_modulos():
        assert (carpeta / cap.archivo_qmd).is_file()

    assert len(obtener_banco_autoevaluacion()) == 12


def test_parsear_y_validar_pdfinfo_170x244(tmp_path: Path) -> None:
    ruta_pdf = tmp_path / "libro.pdf"
    salida_simulada = (
        "Title:          Neurología Clínica y Semiología Basada en la Evidencia\n"
        "Author:         Alcy Montserrat\n"
        "Producer:       LuaHBTeX-1.24.0\n"
        "Pages:          64\n"
        "Encrypted:      no\n"
        "Page size:      481.89 x 691.65 pts\n"
        "File size:      245120 bytes\n"
        "PDF version:    1.5\n"
    )
    info = parsear_salida_pdfinfo(ruta_pdf, salida_simulada, tamano_bytes=245120)
    assert info.paginas == 64
    assert info.ancho_mm == pytest.approx(170.0, abs=0.2)
    assert info.alto_mm == pytest.approx(244.0, abs=0.2)
    assert info.ancho_in == pytest.approx(6.69, abs=0.02)
    assert info.alto_in == pytest.approx(9.61, abs=0.02)
    assert validar_info_pdf(info) == []


def test_rechaza_dimensiones_fuera_de_catalogo(tmp_path: Path) -> None:
    ruta_pdf = tmp_path / "libro-170x240.pdf"
    # 170 x 240 mm = 481.89 x 680.31 pts (no existe en KDP/IngramSpark)
    salida_240 = (
        "Pages:          50\n"
        "Encrypted:      no\n"
        "Page size:      481.89 x 680.31 pts\n"
        "PDF version:    1.5\n"
    )
    info = parsear_salida_pdfinfo(ruta_pdf, salida_240, tamano_bytes=100000)
    errores = validar_info_pdf(info)
    assert any("Alto de página incorrecto" in e for e in errores)


def test_validar_tex_detecta_faltantes(tmp_path: Path) -> None:
    ruta_tex = tmp_path / "incompleto.tex"
    ruta_tex.write_text(r"\documentclass{scrbook}", encoding="utf-8")
    errores = validar_tex_libro(ruta_tex)
    assert any("paperwidth=170mm" in e for e in errores)
    assert any("paperheight=244mm" in e for e in errores)


def test_cli_qmd_y_check(tmp_path: Path) -> None:
    carpeta = tmp_path / "quarto_cli"
    rc_qmd = cli_libro.main(["qmd", "--proyecto", str(carpeta)])
    assert rc_qmd == 0
    rc_check = cli_libro.main(
        ["check", "--proyecto", str(carpeta), "--pdf", str(tmp_path / "no-existe.pdf")]
    )
    assert rc_check == 0
