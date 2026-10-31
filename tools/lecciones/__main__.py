"""CLI: ``uv run python -m lecciones <orden>``.

- ``check``: contrato de todas las lecciones, coherencia con ``lecciones/mapa.yaml`` y
  ``mapa-maestro-libro.md`` al día (sin red; forma parte de ``npm run gates``).
- ``mapa``: regenera ``mapa-maestro-libro.md`` desde el mapa y el estado de las lecciones.
- ``nuevo <id>``: crea ``lecciones/<id>.qmd`` en borrador desde su fila del mapa.
- ``citas``: verifica ``lecciones/refs.bib`` contra PubMed y Crossref (requiere red).
"""

from __future__ import annotations

import argparse
import sys

from pydantic import ValidationError

from lecciones import mapa as mapa_libro
from lecciones.citas import verificar
from lecciones.fuente import CARPETA, RAIZ, ErrorDeFuente, archivos, leer_bib
from lecciones.validacion import validar_todo


def _cargar_mapa() -> mapa_libro.Mapa | None:
    try:
        return mapa_libro.cargar()
    except (ErrorDeFuente, ValidationError) as exc:
        print(f"✗ lecciones/mapa.yaml: {exc}")
        return None


def _check() -> int:
    rutas = archivos()
    resultado = validar_todo(rutas)
    errores = list(resultado.errores)
    mapa = _cargar_mapa()
    if mapa is None:
        return 1
    estados = mapa_libro.estados(rutas)
    errores += mapa_libro.coherencia(mapa, estados)
    esperado = mapa_libro.renderizar(mapa, estados)
    actual = mapa_libro.SALIDA.read_text(encoding="utf-8") if mapa_libro.SALIDA.is_file() else ""
    if actual != esperado:
        errores.append("mapa-maestro-libro.md desactualizado: uv run python -m lecciones mapa")
    for alerta in resultado.alertas:
        print(f"⚠ {alerta}")
    for error in errores:
        print(f"✗ {error}")
    if errores:
        print(f"lecciones: {len(errores)} errores en {len(rutas)} lecciones")
        return 1
    print(
        f"lecciones: {len(rutas)} de {len(mapa.lecciones)} lecciones del mapa conformes "
        f"({len(resultado.alertas)} alertas)"
    )
    return 0


def _mapa() -> int:
    mapa = _cargar_mapa()
    if mapa is None:
        return 1
    mapa_libro.SALIDA.write_text(
        mapa_libro.renderizar(mapa, mapa_libro.estados()), encoding="utf-8"
    )
    print(f"escrito {mapa_libro.SALIDA.relative_to(RAIZ)}")
    return 0


def _nuevo(ident: str) -> int:
    mapa = _cargar_mapa()
    if mapa is None:
        return 1
    destino = CARPETA / f"{ident}.qmd"
    if destino.exists():
        print(f"✗ ya existe {destino.relative_to(RAIZ)}: no se sobrescribe")
        return 1
    try:
        texto = mapa_libro.esqueleto(mapa, ident)
    except ErrorDeFuente as exc:
        print(f"✗ {exc}")
        return 1
    destino.write_text(texto, encoding="utf-8")
    print(f"creado {destino.relative_to(RAIZ)} (borrador); regenere el mapa con «mapa»")
    return 0


def _citas() -> int:
    try:
        bib = leer_bib()
    except ErrorDeFuente as exc:
        print(f"✗ {exc}")
        return 1
    informe = verificar(bib)
    for aviso in informe.avisos:
        print(f"⚠ {aviso}")
    for linea in informe.discrepancias:
        print(f"✗ {linea}")
    for linea in informe.incompletas:
        print(f"… {linea}")
    print(
        f"refs.bib: {len(informe.verificadas)}/{len(bib)} verificadas en PubMed y Crossref"
        + (" (INCOMPLETA)" if informe.incompletas else "")
    )
    return informe.codigo


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="lecciones", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ordenes = parser.add_subparsers(dest="orden", required=True)
    ordenes.add_parser("check")
    ordenes.add_parser("mapa")
    ordenes.add_parser("citas")
    nuevo = ordenes.add_parser("nuevo")
    nuevo.add_argument("id")
    args = parser.parse_args(argv)
    if args.orden == "check":
        return _check()
    if args.orden == "mapa":
        return _mapa()
    if args.orden == "nuevo":
        return _nuevo(args.id)
    return _citas()


if __name__ == "__main__":
    sys.exit(main())
