"""Mapa del libro (``lecciones/mapa.yaml``): plan editorial legible por máquina.

El mapa es la fuente del plan; cada lección es la fuente de su contenido y de su estado.
De aquí salen ``mapa-maestro-libro.md`` (generado, versionado y comprobado en los gates),
el esqueleto de cada lección nueva y, en la fase 5, el orden de los capítulos del libro.
"""

from __future__ import annotations

import re
from collections import Counter
from typing import TYPE_CHECKING, Annotated, Any, Literal, Self

import yaml
from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator

from lecciones.fuente import CARPETA, RAIZ, ErrorDeFuente, archivos, leer
from lecciones.modelo import Autor, HmId, Parte, Texto

if TYPE_CHECKING:
    from pathlib import Path

MAPA = CARPETA / "mapa.yaml"
SALIDA = RAIZ / "mapa-maestro-libro.md"
PLANTILLA = RAIZ / "assets" / "plantilla-leccion.qmd"
INDICE_MODULOS = RAIZ / "neurologia.html"

ICONOS = {
    "pendiente": "⬜ pendiente",
    "borrador": "✏️ borrador",
    "revisado": "🔎 revisado",
    "publicado": "✅ publicado",
}


class _Base(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class Obra(_Base):
    titulo_provisional: Texto
    licencia: Literal["CC BY-NC-SA 4.0"]
    legado: Texto
    fuentes_previas: list[Texto] = Field(default_factory=list)


class ParteMapa(_Base):
    clave: Parte
    titulo: Texto
    autores: list[str] = Field(min_length=1)
    revisor: str
    nota: Texto | None = None


class FilaMapa(_Base):
    id: Annotated[str, StringConstraints(pattern=r"^leccion-[a-z0-9]+(-[a-z0-9]+)*$")]
    titulo: Texto
    parte: Parte
    orden: int = Field(ge=1)
    fase: Literal[1, 2, 3, 4, 5]
    modulos_html: list[Texto] = Field(default_factory=list)
    legado_paginas: Annotated[str, StringConstraints(pattern=r"^\d+(-\d+)?$")] | None = None
    condiciones: list[HmId] = Field(default_factory=list)
    propuesta: bool = False


class Mapa(_Base):
    obra: Obra
    personas: dict[str, Autor]
    partes: list[ParteMapa] = Field(min_length=1)
    lecciones: list[FilaMapa]

    @model_validator(mode="after")
    def _integridad(self) -> Self:
        claves = [p.clave for p in self.partes]
        if len(set(claves)) != len(claves):
            raise ValueError("partes: clave repetida")
        for parte in self.partes:
            for alias in [*parte.autores, parte.revisor]:
                if alias not in self.personas:
                    raise ValueError(f"parte {parte.clave}: persona desconocida «{alias}»")
            if self.personas[parte.revisor].fallecido:
                raise ValueError(f"parte {parte.clave}: el revisor no puede ser el autor fallecido")
        repetidos = [i for i, n in Counter(f.id for f in self.lecciones).items() if n > 1]
        if repetidos:
            raise ValueError(f"lecciones: id repetido {repetidos}")
        orden = Counter((f.parte, f.orden) for f in self.lecciones)
        dobles = [k for k, n in orden.items() if n > 1]
        if dobles:
            raise ValueError(f"lecciones: orden repetido en {dobles}")
        for fila in self.lecciones:
            if fila.parte not in claves:
                raise ValueError(f"{fila.id}: parte «{fila.parte}» no declarada")
        modulos = Counter(m for f in self.lecciones for m in f.modulos_html)
        compartidos = [m for m, n in modulos.items() if n > 1]
        if compartidos:
            raise ValueError(f"módulos asignados a más de una lección: {compartidos}")
        return self

    def parte(self, clave: str) -> ParteMapa:
        return next(p for p in self.partes if p.clave == clave)

    def fila(self, ident: str) -> FilaMapa | None:
        return next((f for f in self.lecciones if f.id == ident), None)


def cargar(ruta: Path = MAPA) -> Mapa:
    if not ruta.is_file():
        raise ErrorDeFuente(f"no existe {ruta.relative_to(RAIZ)}")
    return Mapa.model_validate(yaml.safe_load(ruta.read_text(encoding="utf-8")))


def modulos_publicados(indice: Path = INDICE_MODULOS) -> list[str]:
    """Módulos de neurología enlazados desde su página índice (los que se usan en clase)."""
    if not indice.is_file():
        return []
    enlaces = re.findall(r'href="(neurologia/[^"#?]+\.html)"', indice.read_text(encoding="utf-8"))
    return sorted(set(enlaces))


def estados(rutas: list[Path] | None = None) -> dict[str, dict[str, Any]]:
    """Frontmatter de cada lección existente, por id (lo ilegible lo informa ``check``)."""
    salida: dict[str, dict[str, Any]] = {}
    for ruta in archivos() if rutas is None else rutas:
        try:
            datos = leer(ruta).datos
        except ErrorDeFuente:
            continue
        if isinstance(datos.get("id"), str):
            salida[datos["id"]] = {**datos, "_archivo": ruta.name}
    return salida


def coherencia(mapa: Mapa, lecciones: dict[str, dict[str, Any]], raiz: Path = RAIZ) -> list[str]:
    errores: list[str] = []
    for fila in mapa.lecciones:
        for modulo in fila.modulos_html:
            if not (raiz / modulo).is_file():
                errores.append(f"mapa: {fila.id}: no existe {modulo}")
    asignados = {m for f in mapa.lecciones for m in f.modulos_html}
    for modulo in modulos_publicados(raiz / "neurologia.html"):
        if modulo not in asignados:
            errores.append(f"mapa: el módulo de clase {modulo} no está asignado a ninguna lección")

    for ident, datos in lecciones.items():
        archivo = datos["_archivo"]
        plan = mapa.fila(ident)
        if plan is None:
            errores.append(f"{archivo}: la lección no figura en lecciones/mapa.yaml")
            continue
        for campo in ("titulo", "parte", "orden"):
            if datos.get(campo) != getattr(plan, campo):
                errores.append(
                    f"{archivo}: {campo} «{datos.get(campo)}» ≠ mapa «{getattr(plan, campo)}»"
                )
        if sorted(datos.get("modulos_html") or []) != sorted(plan.modulos_html):
            errores.append(f"{archivo}: modulos_html no coincide con el mapa")
        faltan = set(plan.condiciones) - set(datos.get("condiciones") or [])
        if faltan:
            errores.append(f"{archivo}: faltan condiciones del mapa {sorted(faltan)}")
        legado = datos.get("legado") or {}
        if (legado.get("paginas") if isinstance(legado, dict) else None) != plan.legado_paginas:
            errores.append(f"{archivo}: legado.paginas no coincide con el mapa")
        nombres = {a.get("nombre") for a in datos.get("autores") or [] if isinstance(a, dict)}
        for alias in mapa.parte(plan.parte).autores:
            if mapa.personas[alias].nombre not in nombres:
                nombre = mapa.personas[alias].nombre
                errores.append(f"{archivo}: falta el autor de la parte «{nombre}»")
    return errores


def _celda_fuente(fila: FilaMapa) -> str:
    partes: list[str] = []
    if fila.legado_paginas:
        partes.append(f"1993, pp. {fila.legado_paginas}")
    partes += [f"`{m.removeprefix('neurologia/')}`" for m in fila.modulos_html]
    partes += [f"db `{c}`" for c in fila.condiciones]
    return " · ".join(partes) or "nueva"


def renderizar(mapa: Mapa, lecciones: dict[str, dict[str, Any]], raiz: Path = RAIZ) -> str:
    total = Counter(lecciones.get(f.id, {}).get("estado", "pendiente") for f in mapa.lecciones)
    lineas = [
        "# Mapa maestro del libro",
        "",
        "<!-- GENERADO desde lecciones/mapa.yaml y lecciones/*.qmd con "
        "`uv run python -m lecciones mapa`. No editar a mano. -->",
        "",
        f"**Obra:** {mapa.obra.titulo_provisional}  ",
        f"**Legado:** {mapa.obra.legado}  ",
        f"**Licencia:** {mapa.obra.licencia} (lecciones y libro)",
        "",
        "Cada fila es una lección: una fuente única (`lecciones/<id>.qmd`) de la que salen el "
        "artículo del blog y el capítulo del libro. Todo el texto se reconstruye desde cero; "
        "los módulos de clase y la obra de 1993 son fuentes, no texto que se copia. El estado "
        "se lee de cada lección. Contrato: `docs/adr/ADR-001-arquitectura-libro.md`.",
        "",
        "**Estado:** "
        + " · ".join(f"{ICONOS[k]}: {total.get(k, 0)}" for k in ICONOS)
        + f" · total {len(mapa.lecciones)}",
        "",
        "**Fases:** 1 piloto · 2 módulos de clase · 3 neuropediatría · 4 neuroftalmología · "
        "5 libro. «(propuesta)» marca una agrupación de módulos pendiente de decisión.",
        "",
    ]
    for numero, parte in enumerate(mapa.partes, 1):
        autores = ", ".join(
            mapa.personas[a].nombre + (" †" if mapa.personas[a].fallecido else "")
            for a in parte.autores
        )
        lineas += [
            f"## {numero}. {parte.titulo}",
            "",
            f"Autores: {autores} · Revisión: {mapa.personas[parte.revisor].nombre}",
            "",
        ]
        if parte.nota:
            lineas += [f"*{parte.nota}*", ""]
        filas = sorted((f for f in mapa.lecciones if f.parte == parte.clave), key=lambda f: f.orden)
        if not filas:
            lineas += ["*Sin lecciones planificadas todavía.*", ""]
            continue
        lineas += ["| # | Lección | Fase | Fuentes | Estado |", "|:-|:-|:-|:-|:-|"]
        for f in filas:
            estado = ICONOS.get(str(lecciones.get(f.id, {}).get("estado", "pendiente")), "?")
            titulo = f.titulo + (" *(propuesta)*" if f.propuesta else "")
            lineas.append(
                f"| {f.orden} | {titulo}<br>`{f.id}` | {f.fase} | {_celda_fuente(f)} | {estado} |"
            )
        lineas.append("")

    asignacion = {m: f for f in mapa.lecciones for m in f.modulos_html}
    publicados = modulos_publicados(raiz / "neurologia.html")
    lineas += [
        "## Cobertura de los módulos de clase",
        "",
        f"{len(publicados)} módulos enlazados desde `neurologia.html`. Los HTML se conservan "
        "íntegros para la docencia; cada lección los enlaza.",
        "",
        "| Módulo | Lección |",
        "|:-|:-|",
    ]
    for modulo in publicados:
        fila = asignacion.get(modulo)
        lineas.append(f"| `{modulo}` | {fila.titulo if fila else '**sin asignar**'} |")
    lineas.append("")
    return "\n".join(lineas)


def esqueleto(mapa: Mapa, ident: str) -> str:
    """Lección nueva en borrador, con todo lo que el mapa ya sabe de ella."""
    fila = mapa.fila(ident)
    if fila is None:
        raise ErrorDeFuente(f"{ident} no figura en lecciones/mapa.yaml")
    parte = mapa.parte(fila.parte)
    pendiente = "PENDIENTE de redacción."
    datos: dict[str, Any] = {
        "id": fila.id,
        "tipo": "leccion",
        "titulo": fila.titulo,
        "parte": fila.parte,
        "orden": fila.orden,
        "estado": "borrador",
        "fecha_revision": None,
        "revisor": None,
        "autores": [
            mapa.personas[a].model_dump(exclude_defaults=True, exclude_none=True)
            for a in parte.autores
        ],
    }
    if fila.legado_paginas:
        datos["legado"] = {"obra": mapa.obra.legado, "paginas": fila.legado_paginas}
    datos |= {
        "pregunta_clinica": pendiente,
        "abstract": pendiente,
        "dialogo_clinico": pendiente,
        "indispensable": [pendiente],
        "limites": [pendiente],
        "condiciones": list(fila.condiciones),
        "conceptos": [],
        "refs": [],
        "medios": [],
        "modulos_html": list(fila.modulos_html),
    }
    plantilla = PLANTILLA.read_text(encoding="utf-8")
    cuerpo = plantilla.split("\n---\n", 2)[-1]
    if not fila.legado_paginas:
        cuerpo = re.sub(r"(?ms)^::: \{\.legado\}.*?^:::\s*$\n?", "", cuerpo)
    encabezado = yaml.safe_dump(datos, allow_unicode=True, sort_keys=False, width=100)
    return f"---\n{encabezado}---\n{cuerpo}"
