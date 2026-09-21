"""``assets/data/topic-images.json``: una imagen destacada por condición, en dominio público.

``build-blog.mjs`` lee este archivo y rechaza cualquier entrada que no cumpla la política.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from datetime import date

    from imagenes.commons import Imagen

RAIZ = Path(__file__).resolve().parents[2]
ARCHIVO = RAIZ / "assets" / "data" / "topic-images.json"
LICENCIAS = frozenset({"Public domain", "CC0"})
CAMPOS = ("title", "url", "thumb", "license", "license_code", "author", "alt", "source", "verified")
CLAVE = re.compile(r"^HM\d+$")
SERVIDORES = ("https://upload.wikimedia.org/", "https://thumb.wikimedia.org/")


def leer(archivo: Path = ARCHIVO) -> dict[str, dict[str, Any]]:
    if not archivo.exists():
        return {}
    datos: dict[str, dict[str, Any]] = json.loads(archivo.read_text(encoding="utf-8"))
    return datos


def escribir(registro: dict[str, dict[str, Any]], archivo: Path = ARCHIVO) -> None:
    ordenado = {clave: registro[clave] for clave in sorted(registro)}
    texto = json.dumps(ordenado, ensure_ascii=False, indent=2) + "\n"
    archivo.write_text(texto, encoding="utf-8", newline="\n")


def entrada(imagen: Imagen, alt: str, hoy: date) -> dict[str, Any]:
    return {
        "title": imagen.titulo,
        "url": imagen.url,
        "thumb": imagen.miniatura,
        "license": imagen.licencia,
        "license_code": imagen.codigo_licencia,
        "author": imagen.autor,
        "alt": alt.strip(),
        "source": imagen.pagina,
        "verified": hoy.isoformat(),
    }


def problemas(clave: str, datos: dict[str, Any]) -> list[str]:
    """Incumplimientos de la política en una entrada, sin consultar la red."""
    errores: list[str] = []
    if not CLAVE.match(clave):
        errores.append(f"{clave}: la clave debe ser el ID de condición sin dos puntos (HM6003).")
    faltan = [c for c in CAMPOS if not str(datos.get(c) or "").strip()]
    if faltan:
        errores.append(f"{clave}: faltan campos {faltan}.")
    if datos.get("license") not in LICENCIAS:
        errores.append(f"{clave}: licencia «{datos.get('license')}» no es dominio público ni CC0.")
    for campo in ("url", "thumb"):
        if not str(datos.get(campo, "")).startswith(SERVIDORES):
            errores.append(f"{clave}: {campo} no apunta a los servidores de Wikimedia.")
    if not str(datos.get("source", "")).startswith("https://commons.wikimedia.org/wiki/File:"):
        errores.append(f"{clave}: source no es una página de archivo de Wikimedia Commons.")
    if len(str(datos.get("alt") or "")) < 15:
        errores.append(f"{clave}: el texto alternativo debe describir la imagen (≥ 15 caracteres).")
    return errores
