"""CLI: ``uv run python -m casos <orden>``.

- ``check``: valida todos los casos y falla si el JSON publicado está desactualizado.
- ``build``: valida y escribe ``assets/data/casos/*.json`` de los casos publicados.
- ``preview HM6003``: imprime el caso compilado en Markdown para revisión humana.
- ``nuevo HM6003``: crea el borrador ``casos/HM6003.yaml`` con los hallazgos de la base.
- ``estado``: tabla de artículos con y sin caso.
"""

from __future__ import annotations

import argparse
import sys
from datetime import date

from casos.articulo import leer_articulos
from casos.compilar import RAIZ, Rutas, compilar, construir, esqueleto, leer_casos, nombre_archivo
from casos.errores import ErrorDeCaso
from casos.presentacion import markdown


def _condicion(valor: str) -> str:
    valor = valor.strip().upper().replace("HM:", "HM")
    if not valor.startswith("HM") or not valor[2:].isdigit():
        raise ErrorDeCaso(f"Condición no válida: {valor} (ejemplo: HM6003)")
    return "HM:" + valor[2:]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="casos", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ordenes = parser.add_subparsers(dest="orden", required=True)
    ordenes.add_parser("check")
    ordenes.add_parser("build")
    ordenes.add_parser("estado")
    vista = ordenes.add_parser("preview")
    vista.add_argument("condicion")
    nuevo = ordenes.add_parser("nuevo")
    nuevo.add_argument("condicion")
    nuevo.add_argument("--autor", default="Dr. Alcy Torres")
    args = parser.parse_args(argv)
    rutas = Rutas(RAIZ)
    hoy = date.today()

    if args.orden in ("check", "build"):
        pendientes = construir(rutas, hoy, solo_comprobar=args.orden == "check")
        for ruta in pendientes:
            print(("DESACTUALIZADO: " if args.orden == "check" else "ACTUALIZADO: ") + ruta)
        if args.orden == "check" and pendientes:
            print("Ejecute: npm run casos:build", file=sys.stderr)
            return 1
        casos = leer_casos(rutas)
        publicados = sum(c.caso.estado == "publicado" for c in casos)
        print(f"Casos válidos: {len(casos)}. Publicados: {publicados}.")
        return 0

    if args.orden == "estado":
        por_condicion = {c.caso.condicion_id: c.caso for c in leer_casos(rutas)}
        for cid, articulo in leer_articulos(rutas.posts).items():
            caso = por_condicion.get(cid)
            estado = caso.estado if caso else "sin caso"
            fecha = caso.publicacion.fecha if caso and caso.publicacion.fecha else "—"
            print(f"{cid:9} {estado:12} {fecha!s:10} {articulo.slug}")
        return 0

    condicion = _condicion(args.condicion)
    if args.orden == "nuevo":
        encontrado = leer_articulos(rutas.posts).get(condicion)
        if encontrado is None:
            raise ErrorDeCaso(f"No hay artículo para {condicion}.")
        destino = rutas.casos / nombre_archivo(condicion)
        if destino.exists():
            raise ErrorDeCaso(
                f"Ya existe {destino.relative_to(RAIZ).as_posix()}; no se sobrescribe."
            )
        rutas.casos.mkdir(exist_ok=True)
        destino.write_text(esqueleto(encontrado, args.autor), encoding="utf-8", newline="\n")
        print(f"Borrador creado: {destino.relative_to(RAIZ).as_posix()}")
        return 0

    leido = next((c for c in leer_casos(rutas) if c.caso.condicion_id == condicion), None)
    if leido is None:
        raise ErrorDeCaso(f"No existe casos/{nombre_archivo(condicion)}.")
    print(markdown(compilar(leido, hoy)))
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        sys.exit(main())
    except ErrorDeCaso as error:
        print(f"ERROR:\n{error}", file=sys.stderr)
        sys.exit(1)
