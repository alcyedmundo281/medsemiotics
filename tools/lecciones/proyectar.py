"""Proyección de una lección: tokens resueltos, lista para Quarto (artículo o capítulo).

La lección (``lecciones/<id>.qmd``) es la fuente única. Aquí se proyecta a un ``.qmd`` donde
cada token ``{{lr+ HM:…}}`` ya es la cifra de la base y las citas ``[@clave]`` las resuelve
Quarto con ``refs.bib``. Un token sin resolver aborta: nunca sale texto crudo.

- ``autonomo``: documento independiente (título en el frontmatter), para el blog y la vista previa.
- ``capitulo``: capítulo de un libro Quarto (título como encabezado de primer nivel).
"""

from __future__ import annotations

import shutil
from typing import TYPE_CHECKING, Literal

import yaml

from lecciones import mapa as mapa_libro
from lecciones.fuente import BIB, CARPETA, RAIZ, archivos, leer
from lecciones.tokens import problemas_de_tokens, resolver_texto
from lecciones.validacion import CAMPOS_CLINICOS, _limpio

if TYPE_CHECKING:
    from collections.abc import Mapping
    from pathlib import Path

    from casos.articulo import Articulo
    from lecciones.fuente import Archivo

Modo = Literal["autonomo", "capitulo"]


def problemas_de_resolucion(archivo: Archivo, articulos: Mapping[str, Articulo]) -> list[str]:
    """Tokens que no resuelven y condiciones declaradas sin artículo sincronizado (sin red)."""
    declaradas = archivo.datos.get("condiciones") or []
    problemas = [
        f"condición {c} declarada pero sin artículo en posts/: ejecute topics:sync"
        for c in declaradas
        if c not in articulos
    ]
    textos = [_limpio(archivo.cuerpo)]
    for campo in CAMPOS_CLINICOS:
        valor = archivo.datos.get(campo) or []
        textos += valor if isinstance(valor, list) else [valor]
    for texto in textos:
        if isinstance(texto, str):
            problemas += problemas_de_tokens(texto, declaradas, articulos)
    return problemas


def proyectar(archivo: Archivo, articulos: Mapping[str, Articulo], modo: Modo = "capitulo") -> str:
    """El ``.qmd`` proyectado de una lección, con todos sus tokens resueltos."""
    datos = archivo.datos
    declaradas = datos.get("condiciones") or []

    def resolver(texto: str) -> str:
        return resolver_texto(str(texto).strip(), declaradas, articulos)

    titulo = str(datos["titulo"])
    partes: list[str] = []
    if modo == "autonomo":
        cabecera: dict[str, object] = {"title": titulo, "lang": "es", "bibliography": "refs.bib"}
        if datos.get("subtitulo"):
            cabecera["subtitle"] = str(datos["subtitulo"])
        partes.append("---\n" + yaml.safe_dump(cabecera, allow_unicode=True) + "---")
    else:
        partes.append(f"# {titulo} {{#sec-{datos['id']}}}")
    partes.append(f"*{resolver(datos['abstract'])}*")
    partes.append(
        "::: {.caso-socratico}\n**Diálogo clínico.** "
        + resolver(datos["dialogo_clinico"])
        + "\n:::"
    )
    partes.append(resolver(archivo.cuerpo))
    limites = "\n".join(f"- {resolver(x)}" for x in datos["limites"])
    partes.append("## Dónde no confiar\n\n" + limites)
    perlas = "\n".join(f"- {resolver(x)}" for x in datos["indispensable"])
    partes.append("::: {.perlas-clinicas}\n**Lo indispensable**\n\n" + perlas + "\n:::")
    return "\n\n".join(p.strip() for p in partes) + "\n"


def escribir_proyeccion(
    ruta: Path, carpeta: Path, articulos: Mapping[str, Articulo], modo: Modo = "autonomo"
) -> Path:
    """Escribe ``<id>.qmd`` y ``refs.bib`` en ``carpeta``; devuelve el ``.qmd``."""
    archivo = leer(ruta)
    texto = proyectar(archivo, articulos, modo)
    carpeta.mkdir(parents=True, exist_ok=True)
    destino = carpeta / f"{ruta.stem}.qmd"
    destino.write_text(texto, encoding="utf-8")
    shutil.copyfile(BIB, carpeta / "refs.bib")
    return destino


def lecciones_por_parte(raiz: Path = RAIZ) -> list[tuple[str, list[Path]]]:
    """Lecciones existentes agrupadas por parte del mapa, en el orden del mapa."""
    carpeta = raiz / CARPETA.relative_to(RAIZ)
    mapa = mapa_libro.cargar(carpeta / "mapa.yaml")
    existentes: dict[str, tuple[str, int, Path]] = {}
    for ruta in archivos(carpeta):
        datos = leer(ruta).datos
        existentes[ruta.stem] = (str(datos.get("parte")), int(datos.get("orden", 0)), ruta)
    salida: list[tuple[str, list[Path]]] = []
    for parte in mapa.partes:
        propias = sorted((o, r) for p, o, r in existentes.values() if p == parte.clave)
        if propias:
            salida.append((parte.titulo, [r for _, r in propias]))
    return salida
