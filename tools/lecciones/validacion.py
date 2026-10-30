"""Contrato editorial de una lección. No sustituye la revisión clínica humana.

Un ``borrador`` puede estar incompleto: sus faltas se informan como alertas. A partir de
``revisado`` cada falta bloquea. Un frontmatter que no se puede leer bloquea siempre.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from pydantic import ValidationError

from casos.evidencia import LLAVES, PROHIBIDOS, TIPOS, TOKEN
from lecciones.fuente import RAIZ, ErrorDeFuente, leer, leer_bib
from lecciones.modelo import Leccion

if TYPE_CHECKING:
    from pathlib import Path

    from lecciones.fuente import EntradaBib

# Plantilla de la lección (norma editorial: prólogos de 1993 + rigor de biosemiotics).
SECCIONES: tuple[str, ...] = (
    "Cómo se explora",
    "Qué significa",
    "Por qué ocurre",
    "Qué hacer",
    "Cómo prevenir",
    "Nuestra realidad",
)

PENDIENTE = re.compile(r"\b(TODO|PENDIENTE)\b")
CITA = re.compile(r"\[[^\]]*@([A-Za-z][A-Za-z0-9_:\-]*)[^\]]*\]")
DIGITO = re.compile(r"\d")
LISTA_NUMERADA = re.compile(r"^\s*\d+[.)]\s")
BLOQUE = re.compile(r"(?ms)^:::\s*\{\.(?P<clase>[a-z-]+)\}\s*$.*?^:::\s*$")
CODIGO = re.compile(r"(?ms)^(`{3,}|~{3,}).*?^\1\s*$")
COMENTARIO = re.compile(r"(?s)<!--.*?-->")
CODIGO_EN_LINEA = re.compile(r"`[^`\n]+`")


# Además de las de los casos: «LR positivo es 3,5», «el LR fue de 8».
PROHIBIDOS_LECCION: tuple[tuple[re.Pattern[str], str], ...] = (
    *PROHIBIDOS,
    (
        re.compile(r"\bLR\b[^.\n{]{0,25}?\d", re.I),
        "cociente de verosimilitud escrito a mano; use {{lr+ HM:…}} o {{lr- HM:…}}",
    ),
)


@dataclass
class Resultado:
    errores: list[str] = field(default_factory=list)
    alertas: list[str] = field(default_factory=list)


def _limpio(cuerpo: str) -> str:
    return CODIGO_EN_LINEA.sub("", COMENTARIO.sub("", CODIGO.sub("", cuerpo)))


def problemas_de_cuerpo(cuerpo: str, leccion: Leccion | None) -> list[str]:
    """Secciones obligatorias, cifras sin token o sin cita, tokens fuera de la lección."""
    problemas: list[str] = []
    texto = _limpio(cuerpo)
    if PENDIENTE.search(texto):
        problemas.append("el cuerpo contiene TODO o PENDIENTE")

    encabezados = list(re.finditer(r"(?m)^##\s+(.+?)\s*$", texto))
    for seccion in SECCIONES:
        indices = [i for i, h in enumerate(encabezados) if h[1] == seccion]
        if len(indices) != 1:
            problemas.append(f"## {seccion}: debe aparecer exactamente una vez")
            continue
        i = indices[0]
        fin = encabezados[i + 1].start() if i + 1 < len(encabezados) else len(texto)
        contenido = re.sub(r"(?m)^#{1,6}\s+.*$", "", texto[encabezados[i].end() : fin])
        contenido = BLOQUE.sub("", contenido)
        if not contenido.strip():
            problemas.append(f"## {seccion}: sección vacía")

    clases = {m["clase"] for m in BLOQUE.finditer(texto)}
    if leccion is not None and leccion.legado is not None and "legado" not in clases:
        problemas.append("declara «legado» pero el cuerpo no tiene un bloque ::: {.legado}")

    # El bloque legado es una cita histórica literal: sus cifras no se reescriben ni se citan.
    prosa = BLOQUE.sub(lambda m: "" if m["clase"] == "legado" else m[0], texto)

    sin_tokens = TOKEN.sub(" ", prosa)
    malformado = LLAVES.search(sin_tokens)
    if malformado:
        problemas.append(f"token mal formado: {malformado[0]!r}")
    for patron, motivo in PROHIBIDOS_LECCION:
        for m in patron.finditer(sin_tokens):
            problemas.append(f"{motivo}: «{m[0]}»")

    declarados = set(leccion.conceptos) if leccion is not None else set()
    for m in TOKEN.finditer(prosa):
        if m["tipo"] not in TIPOS:
            problemas.append(f"token de tipo desconocido: {m[0]}")
        elif leccion is not None and m["id"] not in declarados:
            problemas.append(f"token {m[0]}: {m['id']} no figura en «conceptos»")

    refs = set(leccion.refs) if leccion is not None else set()
    for parrafo in re.split(r"\n\s*\n", sin_tokens):
        lineas = [
            LISTA_NUMERADA.sub("", ln)
            for ln in parrafo.splitlines()
            if not ln.lstrip().startswith(("#", ":::"))
        ]
        resto = CITA.sub("", "\n".join(lineas))
        if DIGITO.search(resto) and not CITA.search(parrafo):
            extracto = " ".join(resto.split())[:70]
            problemas.append(f"cifra sin cita [@clave] en el párrafo: «{extracto}…»")
        for clave in CITA.findall(parrafo):
            if leccion is not None and clave not in refs:
                problemas.append(f"cita [@{clave}] no declarada en «refs»")
    return problemas


def _textos(datos: object, ruta: str = "") -> list[tuple[str, str]]:
    """Pares (campo, texto) de todo el frontmatter, para buscar marcas sin redactar."""
    if isinstance(datos, str):
        return [(ruta, datos)]
    if isinstance(datos, dict):
        return [
            par for k, v in datos.items() for par in _textos(v, k if not ruta else f"{ruta}.{k}")
        ]
    if isinstance(datos, list):
        return [par for v in datos for par in _textos(v, ruta)]
    return []


def problemas_de_referencias(leccion: Leccion, bib: dict[str, EntradaBib]) -> list[str]:
    problemas: list[str] = []
    for clave in leccion.refs:
        entrada = bib.get(clave)
        if entrada is None:
            problemas.append(f"refs: «{clave}» no está en lecciones/refs.bib")
            continue
        if not re.fullmatch(r"[1-9]\d*", entrada.pmid):
            problemas.append(f"refs: «{clave}» sin PMID numérico en refs.bib")
        if not entrada.doi.startswith("10."):
            problemas.append(f"refs: «{clave}» sin DOI en refs.bib")
    return problemas


def problemas_de_archivos(leccion: Leccion, raiz: Path) -> list[str]:
    problemas: list[str] = []
    for medio in leccion.medios:
        if not (raiz / medio.archivo_local).is_file():
            problemas.append(f"medio {medio.id}: no existe {medio.archivo_local}")
    for modulo in leccion.modulos_html:
        if not modulo.endswith(".html") or not (raiz / modulo).is_file():
            problemas.append(f"modulos_html: no existe {modulo}")
    return problemas


def validar_archivo(
    ruta: Path, raiz: Path = RAIZ, bib: dict[str, EntradaBib] | None = None
) -> Resultado:
    resultado = Resultado()
    nombre = ruta.name
    try:
        archivo = leer(ruta)
        bib = leer_bib() if bib is None else bib
    except ErrorDeFuente as exc:
        resultado.errores.append(str(exc))
        return resultado

    borrador = archivo.datos.get("estado", "borrador") == "borrador"
    destino = resultado.alertas if borrador else resultado.errores

    try:
        leccion: Leccion | None = Leccion.model_validate(archivo.datos)
    except ValidationError as exc:
        leccion = None
        for e in exc.errors():
            lugar = ".".join(str(p) for p in e["loc"]) or "frontmatter"
            destino.append(f"{nombre}: {lugar}: {e['msg']}")

    marcas = sorted({clave for clave, valor in _textos(archivo.datos) if PENDIENTE.search(valor)})
    if marcas:
        destino.append(f"{nombre}: campos sin redactar (PENDIENTE/TODO): {', '.join(marcas)}")

    if leccion is not None:
        if ruta.stem != leccion.id:
            resultado.errores.append(f"{nombre}: el archivo debe llamarse {leccion.id}.qmd")
        destino.extend(f"{nombre}: {p}" for p in problemas_de_referencias(leccion, bib))
        destino.extend(f"{nombre}: {p}" for p in problemas_de_archivos(leccion, raiz))

    destino.extend(f"{nombre}: {p}" for p in problemas_de_cuerpo(archivo.cuerpo, leccion))
    return resultado


def validar_todo(rutas: list[Path], raiz: Path = RAIZ) -> Resultado:
    total = Resultado()
    try:
        bib = leer_bib()
    except ErrorDeFuente as exc:
        total.errores.append(str(exc))
        return total
    ids: dict[str, str] = {}
    orden: dict[tuple[str, int], str] = {}
    for ruta in rutas:
        r = validar_archivo(ruta, raiz, bib)
        total.errores.extend(r.errores)
        total.alertas.extend(r.alertas)
        try:
            datos = leer(ruta).datos
        except ErrorDeFuente:
            continue
        ident, parte, num = datos.get("id"), datos.get("parte"), datos.get("orden")
        if isinstance(ident, str):
            if ident in ids:
                total.errores.append(f"id repetido «{ident}»: {ids[ident]} y {ruta.name}")
            ids[ident] = ruta.name
        if isinstance(parte, str) and isinstance(num, int):
            if (parte, num) in orden:
                previo = orden[(parte, num)]
                total.errores.append(
                    f"orden {num} repetido en la parte «{parte}»: {previo} y {ruta.name}"
                )
            orden[(parte, num)] = ruta.name
    return total
