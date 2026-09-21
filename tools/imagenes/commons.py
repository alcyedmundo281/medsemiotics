"""Consulta a la API de Wikimedia Commons y decisión de licencia.

Solo se aceptan obras en dominio público: marcas ``PD-*`` y la dedicatoria CC0. Cualquier
licencia que exija atribución o compartir igual (CC BY, CC BY-SA, GFDL…) se rechaza.
"""

from __future__ import annotations

import html
import json
import re
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable

API = "https://commons.wikimedia.org/w/api.php"
AGENTE = "Medsemiotics-Imagenes/1.0 (https://powersemiotics.com/medsemiotics/)"
ANCHO_MINIATURA = 1280
MIMES = frozenset({"image/jpeg", "image/png", "image/svg+xml", "image/gif", "image/tiff"})


class LicenciaNoPermitida(ValueError):
    """La obra no está en dominio público."""


@dataclass(frozen=True)
class Imagen:
    titulo: str
    url: str
    miniatura: str
    pagina: str
    licencia: str
    codigo_licencia: str
    autor: str
    descripcion: str
    ancho: int
    alto: int
    mime: str


def descargar(url: str) -> dict[str, Any]:
    peticion = urllib.request.Request(url, headers={"User-Agent": AGENTE})
    with urllib.request.urlopen(peticion, timeout=30) as respuesta:
        datos: dict[str, Any] = json.loads(respuesta.read().decode("utf-8"))
        return datos


def _texto(valor: Any) -> str:
    """Los metadatos de Commons llegan como HTML: se deja solo el texto."""
    limpio = re.sub(r"<[^>]+>", " ", str(valor or ""))
    return re.sub(r"\s+", " ", html.unescape(limpio)).strip()


def _sin_consulta(url: Any) -> str:
    """Quita los parámetros de seguimiento (``utm_*``) que añade la API."""
    return str(url or "").split("?", 1)[0]


def es_dominio_publico(metadatos: dict[str, Any]) -> tuple[bool, str, str]:
    """Devuelve (aceptada, nombre legible, código) a partir de ``extmetadata``."""
    codigo = _texto((metadatos.get("License") or {}).get("value")).lower()
    nombre = _texto((metadatos.get("LicenseShortName") or {}).get("value"))
    corto = nombre.lower()
    if codigo == "cc0" or corto.startswith("cc0"):
        return True, "CC0", "cc0"
    if codigo.startswith("pd") or corto in {"public domain", "dominio público", "pd"}:
        return True, "Public domain", codigo or "pd"
    return False, nombre or codigo or "sin licencia declarada", codigo


def _imagen(pagina: dict[str, Any]) -> Imagen | None:
    info = (pagina.get("imageinfo") or [None])[0]
    if not info:
        return None
    metadatos = info.get("extmetadata") or {}
    aceptada, licencia, codigo = es_dominio_publico(metadatos)
    return Imagen(
        titulo=str(pagina["title"]),
        url=_sin_consulta(info["url"]),
        miniatura=_sin_consulta(info.get("thumburl") or info["url"]),
        pagina=_sin_consulta(info.get("descriptionurl")),
        licencia=licencia if aceptada else f"NO PERMITIDA: {licencia}",
        codigo_licencia=codigo,
        autor=_texto((metadatos.get("Artist") or {}).get("value")) or "Autor no declarado",
        descripcion=_texto((metadatos.get("ImageDescription") or {}).get("value"))[:300],
        ancho=int(info.get("width") or 0),
        alto=int(info.get("height") or 0),
        mime=str(info.get("mime") or ""),
    )


def _parametros(**extra: str) -> str:
    base = {
        "action": "query",
        "format": "json",
        "formatversion": "2",
        "prop": "imageinfo",
        "iiprop": "url|extmetadata|mime|size",
        "iiurlwidth": str(ANCHO_MINIATURA),
        "iiextmetadatafilter": "License|LicenseShortName|Artist|ImageDescription",
    }
    return API + "?" + urllib.parse.urlencode({**base, **extra})


def buscar(
    consulta: str, descargar_json: Callable[[str], dict[str, Any]] = descargar, limite: int = 40
) -> list[Imagen]:
    """Candidatas en dominio público para una consulta; las demás se descartan."""
    url = _parametros(
        generator="search",
        gsrnamespace="6",
        gsrlimit=str(limite),
        gsrsearch=f"{consulta} filetype:bitmap|drawing",
    )
    paginas = (descargar_json(url).get("query") or {}).get("pages") or []
    candidatas = [_imagen(p) for p in sorted(paginas, key=lambda p: p.get("index", 0))]
    return [
        c
        for c in candidatas
        if c is not None and not c.licencia.startswith("NO PERMITIDA") and c.mime in MIMES
    ]


def obtener(titulo: str, descargar_json: Callable[[str], dict[str, Any]] = descargar) -> Imagen:
    """Una imagen concreta; falla si no existe o no está en dominio público."""
    if not titulo.startswith("File:"):
        titulo = "File:" + titulo
    paginas = (descargar_json(_parametros(titles=titulo)).get("query") or {}).get("pages") or []
    imagen = _imagen(paginas[0]) if paginas else None
    if imagen is None:
        raise ValueError(f"No existe en Commons: {titulo}")
    if imagen.licencia.startswith("NO PERMITIDA"):
        raise LicenciaNoPermitida(f"{titulo}: {imagen.licencia}")
    if imagen.mime not in MIMES:
        raise ValueError(f"{titulo}: formato no admitido ({imagen.mime})")
    return imagen
