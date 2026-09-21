"""CLI: ``uv run python -m imagenes <orden>``.

- ``buscar HM6003 "infectious mononucleosis"``: candidatas de Commons en dominio público.
- ``asignar HM6003 "File:…" --alt "…"``: verifica la licencia en Commons y registra la imagen.
- ``check``: valida el registro sin red. Toda condición con caso publicado exige imagen.
  ``--estricto`` la exige en todos los artículos; ``--online`` vuelve a verificar la licencia.
"""

from __future__ import annotations

import argparse
import sys
from datetime import date
from typing import TYPE_CHECKING

from casos.compilar import Rutas, leer_casos
from imagenes import commons, registro

if TYPE_CHECKING:
    from pathlib import Path


def _clave(valor: str) -> str:
    clave = valor.strip().upper().replace(":", "")
    if not registro.CLAVE.match(clave):
        raise ValueError(f"Condición no válida: {valor} (ejemplo: HM6003)")
    return clave


def _articulos(raiz: Path) -> set[str]:
    return {ruta.name.split("-")[0] for ruta in (raiz / "posts").glob("HM*.md")}


def comprobar(raiz: Path, *, estricto: bool, online: bool) -> list[str]:
    datos = registro.leer(raiz / "assets" / "data" / "topic-images.json")
    articulos = _articulos(raiz)
    errores = [e for clave, entrada in datos.items() for e in registro.problemas(clave, entrada)]
    errores += [
        f"{clave}: imagen de una condición sin artículo."
        for clave in sorted(set(datos) - articulos)
    ]
    publicados = {
        c.caso.condicion_id.replace(":", "")
        for c in leer_casos(Rutas(raiz))
        if c.caso.estado == "publicado"
    }
    exigidos = articulos if estricto else publicados
    errores += [
        f"{clave}: artículo sin imagen destacada en dominio público."
        for clave in sorted(exigidos - set(datos))
    ]
    if online:
        for clave, entrada in sorted(datos.items()):
            try:
                imagen = commons.obtener(str(entrada.get("title")))
            except ValueError as error:
                errores.append(f"{clave}: {error}")
                continue
            if imagen.licencia != entrada.get("license"):
                errores.append(f"{clave}: Commons declara hoy «{imagen.licencia}».")
    return errores


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="imagenes", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ordenes = parser.add_subparsers(dest="orden", required=True)
    buscar = ordenes.add_parser("buscar")
    buscar.add_argument("condicion")
    buscar.add_argument("consulta")
    asignar = ordenes.add_parser("asignar")
    asignar.add_argument("condicion")
    asignar.add_argument("titulo")
    asignar.add_argument("--alt", required=True, help="Descripción de la imagen para lectores.")
    check = ordenes.add_parser("check")
    check.add_argument("--estricto", action="store_true")
    check.add_argument("--online", action="store_true")
    args = parser.parse_args(argv)

    if args.orden == "check":
        errores = comprobar(registro.RAIZ, estricto=args.estricto, online=args.online)
        for error in errores:
            print("ERROR:", error, file=sys.stderr)
        total = len(registro.leer())
        print(f"Imágenes registradas: {total}. Incumplimientos: {len(errores)}.")
        return 1 if errores else 0

    clave = _clave(args.condicion)
    if clave not in _articulos(registro.RAIZ):
        raise ValueError(f"No hay artículo para {clave}.")
    if args.orden == "buscar":
        candidatas = commons.buscar(args.consulta)
        if not candidatas:
            print(
                "Sin candidatas en dominio público; pruebe otra consulta (en inglés suele "
                "haber más resultados)."
            )
        for numero, imagen in enumerate(candidatas, 1):
            print(
                f"{numero:2}. {imagen.titulo}\n    {imagen.licencia} · {imagen.ancho}×"
                f"{imagen.alto} · {imagen.autor[:60]}\n    {imagen.descripcion[:160]}\n"
                f"    {imagen.pagina}"
            )
        return 0

    imagen = commons.obtener(args.titulo)
    datos = registro.leer()
    anterior = datos.get(clave, {}).get("title")
    datos[clave] = registro.entrada(imagen, args.alt, date.today())
    errores = registro.problemas(clave, datos[clave])
    if errores:
        raise ValueError("\n".join(errores))
    registro.escribir(datos)
    print(
        f"{clave}: {imagen.titulo} ({imagen.licencia})"
        + (f"; sustituye a {anterior}" if anterior and anterior != imagen.titulo else "")
    )
    print("Regenere el blog: npm run build:blog")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        sys.exit(main())
    except (ValueError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
