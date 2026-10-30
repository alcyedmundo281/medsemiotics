"""CLI del libro de Neurología: ``uv run python -m libro <orden>``.

Órdenes disponibles:
- ``qmd``: genera el proyecto Quarto (`.qmd`, `_quarto.yml`, preámbulo LaTeX y filtro Lua)
  en ``build/quarto``.
- ``build``: genera el proyecto Quarto, compila el PDF con ``quarto`` + ``lualatex`` y
  verifica su geometría de catálogo KDP/IngramSpark (170 × 244 mm = 6,69 × 9,61 in) con
  ``pdfinfo``.
- ``check``: verifica las fuentes del libro y, si existe el PDF compilado, comprueba
  ``libro.tex`` y ``pdfinfo``.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from libro import ALTO_MM, ALTO_PULGADAS, ANCHO_MM, ANCHO_PULGADAS
from libro.datos import RAIZ, leer_condiciones_neurologia
from libro.modulos import (
    obtener_banco_autoevaluacion,
    obtener_capitulos_modulos,
    verificar_fuentes_neurologia,
)
from libro.pdf import (
    compilar_libro_pdf,
    inspeccionar_pdf_con_pdfinfo,
    validar_info_pdf,
    validar_tex_libro,
)
from libro.qmd import generar_proyecto_quarto

RUTA_PROYECTO_DEFECTO = RAIZ / "build" / "quarto"
RUTA_PDF_DEFECTO = RAIZ / "build" / "libro-neurologia.pdf"


def _imprimir_resumen_pdf(
    ruta_proyecto: Path,
    ruta_pdf: Path,
) -> int:
    info = inspeccionar_pdf_con_pdfinfo(ruta_pdf)
    errores = validar_info_pdf(info)
    ruta_tex = ruta_proyecto / "libro.tex"
    if ruta_tex.is_file():
        errores.extend(validar_tex_libro(ruta_tex))

    for err in errores:
        print(f"ERROR: {err}", file=sys.stderr)

    print(
        f"PDF verificado con pdfinfo: {info.ruta}\n"
        f"  Páginas       : {info.paginas}\n"
        f"  Page size (pt): {info.ancho_pt:.2f} × {info.alto_pt:.2f} pts\n"
        f"  Formato (mm)  : {info.ancho_mm:.1f} × {info.alto_mm:.1f} mm "
        f"(catálogo {ANCHO_MM} × {ALTO_MM} mm)\n"
        f"  Formato (in)  : {info.ancho_in:.2f} × {info.alto_in:.2f} in "
        f"(catálogo KDP / IngramSpark {ANCHO_PULGADAS} × {ALTO_PULGADAS} in)\n"
        f"  Versión PDF   : {info.version_pdf} · Encriptado: {info.encriptado}\n"
        f"  Tamaño archivo: {info.tamano_bytes:,} bytes"
    )
    return 1 if errores else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="libro",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="orden", required=True)

    p_qmd = sub.add_parser("qmd", help="Genera el proyecto Quarto (.qmd) en build/quarto.")
    p_qmd.add_argument(
        "--proyecto",
        type=Path,
        default=RUTA_PROYECTO_DEFECTO,
        help="Carpeta donde se escribe el proyecto Quarto (por defecto: build/quarto).",
    )

    p_build = sub.add_parser(
        "build",
        help="Genera el proyecto Quarto, compila con lualatex y verifica con pdfinfo.",
    )
    p_build.add_argument(
        "--proyecto",
        type=Path,
        default=RUTA_PROYECTO_DEFECTO,
        help="Carpeta del proyecto Quarto (por defecto: build/quarto).",
    )
    p_build.add_argument(
        "--salida",
        type=Path,
        default=RUTA_PDF_DEFECTO,
        help="Ruta de salida del PDF compilado (por defecto: build/libro-neurologia.pdf).",
    )

    p_check = sub.add_parser(
        "check",
        help="Valida fuentes, proyecto Quarto y (si existe) el PDF con pdfinfo.",
    )
    p_check.add_argument(
        "--proyecto",
        type=Path,
        default=RUTA_PROYECTO_DEFECTO,
        help="Carpeta del proyecto Quarto.",
    )
    p_check.add_argument(
        "--pdf",
        type=Path,
        default=RUTA_PDF_DEFECTO,
        help="Ruta del PDF a inspeccionar con pdfinfo.",
    )
    p_check.add_argument(
        "--exigir-pdf",
        action="store_true",
        help="Falla si el archivo PDF aún no ha sido compilado.",
    )

    args = parser.parse_args(argv)

    if args.orden == "qmd":
        archivos = generar_proyecto_quarto(args.proyecto, raiz=RAIZ)
        print(f"Proyecto Quarto generado en {args.proyecto} ({len(archivos)} archivos).")
        return 0

    if args.orden == "build":
        compilar_libro_pdf(args.salida, args.proyecto, raiz=RAIZ)
        return _imprimir_resumen_pdf(args.proyecto, args.salida)

    # orden == "check"
    faltantes = verificar_fuentes_neurologia(RAIZ)
    if faltantes:
        for f in faltantes:
            print(f"ERROR: falta fuente de neurología: {f}", file=sys.stderr)
        return 1

    condiciones = leer_condiciones_neurologia(RAIZ)
    modulos = obtener_capitulos_modulos()
    preguntas = obtener_banco_autoevaluacion()
    print(
        f"Fuentes verificadas: {len(condiciones)} condiciones de medsemiotics-db, "
        f"{len(modulos)} capítulos de módulos clínicos y {len(preguntas)} casos de autoevaluación."
    )

    if args.pdf.is_file():
        return _imprimir_resumen_pdf(args.proyecto, args.pdf)
    if args.exigir_pdf:
        print(f"ERROR: no existe el PDF compilado en {args.pdf}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    try:
        sys.exit(main())
    except (ValueError, OSError, RuntimeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
