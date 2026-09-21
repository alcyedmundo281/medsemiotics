"""Tokens de evidencia: la única vía por la que una cifra de la base entra en el texto del caso.

Sintaxis: ``{{tipo HM:####}}``. Tipos:

- ``lr+`` / ``lr-``: cociente de verosimilitud positivo o negativo, con IC 95 % o rango.
- ``sens`` / ``esp``: sensibilidad o especificidad registradas.
- ``hallazgo``: nombre del hallazgo.
- ``estado``: estado del LR (medido, no medido, no medible, sin efecto).

Fuera de los tokens, el texto no puede escribir cocientes, sensibilidades, IC ni
identificadores: así una corrección en medsemiotics-db se propaga sola al caso.
"""

from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any

from casos.errores import ErrorDeCaso

if TYPE_CHECKING:
    from collections.abc import Collection

    from casos.articulo import Articulo

TOKEN = re.compile(r"\{\{\s*(?P<tipo>[a-z+\-]+)\s+(?P<id>HM:\d+)\s*\}\}")
LLAVES = re.compile(r"\{\{.*?\}\}|\{\{|\}\}")
TIPOS = frozenset({"lr+", "lr-", "sens", "esp", "hallazgo", "estado"})

ESTADOS = {
    "medido": "LR medido",
    "no_medido": "LR no medido",
    "no_medible": "LR no medible",
    "sin_efecto": "sin efecto discriminativo",
}
ROLES = {
    "manifestacion": "Manifestación",
    "prueba_sensible": "Prueba sensible",
    "prueba_especifica": "Prueba específica",
    "apoyo": "Apoyo diagnóstico",
    "imagen": "Imagen",
    "bandera_roja": "Signo de alarma",
}

# Cifras de rendimiento diagnóstico escritas a mano. La lista es deliberadamente amplia:
# un falso positivo se resuelve con un token; un falso negativo publica una cifra huérfana.
PROHIBIDOS: tuple[tuple[re.Pattern[str], str], ...] = (
    (
        re.compile(r"\bLR\s*[+\-−]?\s*(?:positivo|negativo)?\s*(?:de|=|:|≈|~)?\s*\d", re.I),
        "cociente de verosimilitud escrito a mano; use {{lr+ HM:…}} o {{lr- HM:…}}",
    ),
    (
        re.compile(
            r"(?:cocientes? de (?:verosimilitud|probabilidad)|likelihood ratios?)"
            r"[^.\n]{0,30}?\d",
            re.I,
        ),
        "cociente de verosimilitud escrito a mano; use {{lr+ HM:…}} o {{lr- HM:…}}",
    ),
    (
        re.compile(r"\b(?:sensibilidad|especificidad)\b[^.\n]{0,25}?\d", re.I),
        "sensibilidad o especificidad escrita a mano; use {{sens HM:…}} o {{esp HM:…}}",
    ),
    (
        re.compile(r"\b(?:VPP|VPN|valores? predictivos?)\b[^.\n]{0,25}?\d", re.I),
        "valor predictivo escrito a mano: la base no lo registra",
    ),
    (re.compile(r"\bIC\s*(?:del?\s*)?95", re.I), "intervalo de confianza escrito a mano"),
    (re.compile(r"\bpmid\b", re.I), "referencia escrita a mano: se deriva de la evidencia"),
    (re.compile(r"\bHM:\d+"), "identificador fuera de token; use {{hallazgo HM:…}}"),
)


def _numero(valor: Any) -> bool:
    return isinstance(valor, int | float) and not isinstance(valor, bool)


def _cociente(etiqueta: str, bloque: Any, concepto: str) -> str:
    if not isinstance(bloque, dict):
        raise ErrorDeCaso(f"{concepto}: la base no registra {etiqueta}.")
    ic95 = bloque.get("ic95")
    rango = bloque.get("rango")
    if _numero(bloque.get("valor")):
        texto = f"{etiqueta} {bloque['valor']}"
        if isinstance(ic95, list) and len(ic95) == 2:
            texto += f" (IC 95 %: {ic95[0]}–{ic95[1]})"
    elif isinstance(rango, list) and len(rango) == 2:
        texto = (
            f"{etiqueta} entre {rango[0]} y {rango[1]} "
            "(rango entre estudios, sin estimación puntual)"
        )
    else:
        raise ErrorDeCaso(f"{concepto}: {etiqueta} sin valor ni rango en la base.")
    if bloque.get("umbral"):
        texto += f", con umbral «{bloque['umbral']}»"
    return texto


def _proporcion(nombre: str, valor: Any, concepto: str) -> str:
    if not _numero(valor) or not 0 <= valor <= 1:
        raise ErrorDeCaso(f"{concepto}: la base no registra {nombre} numérica.")
    return f"{nombre} {valor}"


def resolver_token(tipo: str, concepto: str, articulo: Articulo) -> str:
    if tipo not in TIPOS:
        raise ErrorDeCaso(f"Token desconocido «{tipo}»; tipos válidos: {sorted(TIPOS)}")
    item = articulo.evidencia.get(concepto)
    if item is None:
        raise ErrorDeCaso(
            f"{concepto} no está en la evidencia de {articulo.condicion_id} en medsemiotics-db."
        )
    if tipo == "hallazgo":
        return articulo.nombres[concepto]
    if tipo == "estado":
        return ESTADOS.get(str(item.get("estado_lr")), str(item.get("estado_lr")))
    if tipo in ("lr+", "lr-"):
        if item.get("estado_lr") != "medido":
            raise ErrorDeCaso(f"{concepto}: no hay LR medido que citar ({item.get('estado_lr')}).")
        campo, etiqueta = ("lr_positivo", "LR+") if tipo == "lr+" else ("lr_negativo", "LR−")
        return _cociente(etiqueta, item.get(campo), concepto)
    campo, nombre = (
        ("sensibilidad", "sensibilidad") if tipo == "sens" else ("especificidad", "especificidad")
    )
    return _proporcion(nombre, item.get(campo), concepto)


def conceptos_citados(texto: str) -> set[str]:
    return {m["id"] for m in TOKEN.finditer(texto)}


def resolver(texto: str, articulo: Articulo, permitidos: Collection[str], donde: str) -> str:
    """Sustituye los tokens tras comprobar que el texto no trae cifras propias.

    ``permitidos`` son los hallazgos ya revelados en ese punto del caso: un token no puede
    adelantar evidencia que el estudiante todavía no tiene.
    """
    sin_tokens = TOKEN.sub(" ", texto)
    malformado = LLAVES.search(sin_tokens)
    if malformado:
        raise ErrorDeCaso(f"{donde}: token mal formado: {malformado[0]!r}")
    errores = [
        f"{donde}: {motivo} («{m[0]}»)"
        for patron, motivo in PROHIBIDOS
        for m in patron.finditer(sin_tokens)
    ]
    for concepto in sorted(conceptos_citados(texto) - set(permitidos)):
        errores.append(f"{donde}: {concepto} se cita antes de revelarse en una etapa.")
    if errores:
        raise ErrorDeCaso("\n".join(errores))
    return TOKEN.sub(lambda m: resolver_token(m["tipo"], m["id"], articulo), texto)


def resumen(concepto: str, articulo: Articulo) -> dict[str, Any]:
    """Ficha de un hallazgo tal como la registra la base, para mostrarla dentro del caso."""
    item = articulo.evidencia[concepto]
    estado = str(item.get("estado_lr"))
    cifras: list[str] = []
    if estado == "medido":
        for tipo, campo in (("lr+", "lr_positivo"), ("lr-", "lr_negativo")):
            if item.get(campo):
                cifras.append(resolver_token(tipo, concepto, articulo))
    for tipo, campo in (("sens", "sensibilidad"), ("esp", "especificidad")):
        if _numero(item.get(campo)):
            cifras.append(resolver_token(tipo, concepto, articulo))
    return {
        "id": concepto,
        "nombre": articulo.nombres[concepto],
        "rol": ROLES.get(str(item.get("rol")), str(item.get("rol") or "")),
        "estado_lr": estado,
        "estado": ESTADOS.get(estado, estado),
        "cifras": cifras,
        "decision": item.get("decision"),
        "motivo": item.get("motivo"),
        "advertencia": item.get("advertencia"),
        "referencias": sorted(referencias_de(item)),
    }


def referencias_de(item: dict[str, Any]) -> set[str]:
    encontrados: set[str] = set()

    def recorrer(valor: Any) -> None:
        if isinstance(valor, dict):
            for clave, contenido in valor.items():
                if clave == "ref" and isinstance(contenido, str):
                    encontrados.add(contenido)
                else:
                    recorrer(contenido)
        elif isinstance(valor, list):
            for contenido in valor:
                recorrer(contenido)

    recorrer(item)
    return encontrados
