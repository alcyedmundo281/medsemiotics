"""CLI: ``uv run python -m classroom <orden>``.

- ``check``: valida ``classroom/curso-2026-2027.yaml`` contra el sitio y los artículos.
- ``portal [--check]``: genera (o comprueba) ``medicina_y_datos.html`` desde el plan.
- ``plan``: imprime en JSON las operaciones de Classroom (borradores); no llama a ninguna API.
"""

from __future__ import annotations

import argparse
import json
import sys

from casos.articulo import leer_articulos
from casos.compilar import RAIZ, Rutas, leer_casos
from classroom.plan import construir
from classroom.portal import generar
from classroom.validar import avisos, cargar, contraste_silabo, errores

CURSO = RAIZ / "classroom" / "curso-2026-2027.yaml"
PORTAL = RAIZ / "medicina_y_datos.html"
SILABO = RAIZ / "docs" / "silabo-medicina-y-ciencia-v3.md"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="classroom", description=__doc__)
    ordenes = parser.add_subparsers(dest="orden", required=True)
    ordenes.add_parser("check")
    ordenes.add_parser("plan")
    portal = ordenes.add_parser("portal")
    portal.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)

    plan = cargar(CURSO)
    rutas = Rutas(RAIZ)
    articulos = leer_articulos(rutas.posts)
    fallos = errores(plan, RAIZ, set(articulos))
    fallos += contraste_silabo(plan, SILABO.read_text(encoding="utf-8"))
    if fallos:
        print("\n".join(fallos), file=sys.stderr)
        return 1
    if args.orden == "check":
        con_caso = {c.caso.condicion_id for c in leer_casos(rutas) if c.caso.estado == "publicado"}
        for aviso in avisos(plan, con_caso):
            print("AVISO: " + aviso)
        print(f"Plan válido: {len(plan.sesiones)} sesiones, {len(plan.tareas)} tareas.")
        return 0
    if args.orden == "portal":
        html = generar(plan, RAIZ, articulos)
        if args.check:
            # splitlines ignora si el archivo quedó con CRLF o LF.
            if PORTAL.read_text(encoding="utf-8").splitlines() != html.splitlines():
                print(
                    "DESACTUALIZADO: medicina_y_datos.html (npm run classroom:portal)",
                    file=sys.stderr,
                )
                return 1
            return 0
        with PORTAL.open("w", encoding="utf-8", newline="") as f:
            f.write("\n".join(html.splitlines()) + "\n")
        print("Escrito: medicina_y_datos.html")
        return 0
    slugs = {cid: a.slug for cid, a in articulos.items()}
    print(json.dumps(construir(plan, slugs), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
