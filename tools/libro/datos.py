"""Carga de metadatos, condiciones clínicas de medsemiotics-db, casos socráticos e imágenes."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

import yaml

from casos.articulo import Articulo, leer_articulo
from casos.compilar import CasoLeido, Rutas, compilar, leer_casos
from casos.evidencia import resumen
from libro import CONDICIONES_NEUROLOGIA

RAIZ = Path(__file__).resolve().parents[2]

_FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
_BLOQUE_SOCRATICO_RE = re.compile(
    r"<!--\s*CASO-SOCRATICO:INICIO\s*-->.*?<!--\s*CASO-SOCRATICO:FIN\s*-->\s*",
    re.DOTALL,
)
_COMENTARIO_HTML_RE = re.compile(r"<!--.*?-->\s*", re.DOTALL)
_SPAN_REF_RE = re.compile(r'<span\s+id="ref-\d+"\s*></span>\s*')
_LINK_REF_RE = re.compile(r"\[(\[\d+\])\]\(#ref-\d+\)")


@dataclass(frozen=True)
class MetadatosLibro:
    titulo: str
    subtitulo: str
    autor: str
    orcid: str
    afiliacion: str
    version: str
    doi: str
    fecha_publicacion: str
    licencia: str
    url_repositorio: str
    url_sitio: str


@dataclass(frozen=True)
class ImagenCondicion:
    condicion_id: str
    titulo_commons: str
    url: str
    licencia: str
    codigo_licencia: str
    autor: str
    alt: str
    fuente: str
    verificado: str


@dataclass(frozen=True)
class FilaHallazgo:
    condicion_id: str
    titulo_condicion: str
    hallazgo_id: str
    nombre: str
    rol: str
    sensibilidad: str
    especificidad: str
    lr_pos: str
    lr_neg: str


@dataclass(frozen=True)
class CondicionLibro:
    condicion_id: str
    slug: str
    titulo: str
    especialidad: str
    fecha: str
    descripcion: str
    cuerpo_qmd: str
    articulo: Articulo
    caso: CasoLeido | None
    imagen: ImagenCondicion | None


def leer_metadatos(raiz: Path = RAIZ) -> MetadatosLibro:
    ruta_cff = raiz / "CITATION.cff"
    datos_raw = yaml.safe_load(ruta_cff.read_text(encoding="utf-8"))
    if not isinstance(datos_raw, dict):
        raise ValueError(f"{ruta_cff}: CITATION.cff no contiene un mapa YAML válido")

    autores = datos_raw.get("authors", [])
    autor_principal = autores[0] if isinstance(autores, list) and autores else {}
    given = str(autor_principal.get("given-names", "Alcy")).strip()
    family = str(autor_principal.get("family-names", "Montserrat")).strip()
    orcid = str(autor_principal.get("orcid", "https://orcid.org/0009-0001-7627-9895")).strip()
    afiliacion = str(autor_principal.get("affiliation", "PowerSemiotics")).strip()

    return MetadatosLibro(
        titulo="Neurología Clínica y Semiología Basada en la Evidencia",
        subtitulo=(
            "Cocientes de verosimilitud, reglas de decisión clínica, aprendizaje basado en "
            "problemas y síndromes neurológicos de urgencia y consulta"
        ),
        autor=f"{given} {family}".strip(),
        orcid=orcid,
        afiliacion=afiliacion,
        version=str(datos_raw.get("version", "0.2.0")),
        doi=str(datos_raw.get("doi", "10.5281/zenodo.22069641")),
        fecha_publicacion=str(datos_raw.get("date-released", "2026-04-20")),
        licencia=str(datos_raw.get("license", "CC-BY-SA-4.0")),
        url_repositorio=str(
            datos_raw.get("repository-code", "https://github.com/alcyedmundo281/medsemiotics")
        ),
        url_sitio=str(datos_raw.get("url", "https://powersemiotics.com/medsemiotics/")),
    )


def leer_imagenes_condiciones(raiz: Path = RAIZ) -> dict[str, ImagenCondicion]:
    ruta = raiz / "assets" / "data" / "topic-images.json"
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    if not isinstance(datos, dict):
        raise ValueError(f"{ruta}: se esperaba un objeto JSON")
    resultado: dict[str, ImagenCondicion] = {}
    for clave, valor in datos.items():
        if not isinstance(valor, dict):
            continue
        cid = f"HM:{clave[2:]}" if clave.startswith("HM") and ":" not in clave else clave
        resultado[cid] = ImagenCondicion(
            condicion_id=cid,
            titulo_commons=str(valor.get("title", "")),
            url=str(valor.get("url", "")),
            licencia=str(valor.get("license", "")),
            codigo_licencia=str(valor.get("license_code", "")),
            autor=str(valor.get("author", "")),
            alt=str(valor.get("alt", "")),
            fuente=str(valor.get("source", "")),
            verificado=str(valor.get("verified", "")),
        )
    return resultado


def renderizar_caso_qmd(leido: CasoLeido) -> str:
    compilado: dict[str, Any] = compilar(leido, date.today())
    vineta = compilado["vineta"]
    autoria = compilado["autoria"]
    pub = compilado["publicacion"]
    revisor_txt = (
        f" · Revisión clínica: {autoria.get('revisor')} ({pub.get('fecha')})"
        if autoria.get("revisor") and pub.get("fecha")
        else " · Estado: borrador pendiente de revisión clínica"
    )

    lineas: list[str] = [
        "::: {.caso-socratico}",
        f"### Caso socrático (ABP dirigido): {vineta['titulo']}",
        "",
        (
            f"**Ficha del caso:** Condición `{compilado['condicion_id']}` · "
            f"Nivel: {compilado['nivel']} ({compilado['duracion_min']} min) · "
            f"Autoría: {autoria.get('autor')}{revisor_txt}."
        ),
        "",
        f"**Viñeta clínica inicial:** {vineta['texto']}",
        "",
    ]
    datos_vineta = vineta.get("datos") or []
    if datos_vineta:
        for d in datos_vineta:
            lineas.append(f"- **{d['etiqueta']}:** {d['valor']}")
        lineas.append("")

    for etapa in compilado["etapas"]:
        lineas.extend(
            [
                f"#### Etapa {etapa['numero']}. {etapa['titulo']} (*{etapa['fase_etiqueta']}*)",
                "",
            ]
        )
        if etapa.get("informacion"):
            lineas.extend([str(etapa["informacion"]), ""])
        for d in etapa.get("datos") or []:
            lineas.append(f"- **{d['etiqueta']}:** {d['valor']}")
        if etapa.get("datos"):
            lineas.append("")
        for p_idx, preg in enumerate(etapa.get("preguntas") or [], start=1):
            lineas.extend(
                [
                    f"**Pregunta {etapa['numero']}.{p_idx}:** *{preg['pregunta']}*",
                    "",
                    f"- **Razonamiento esperado:** {preg['clave']}",
                    "",
                ]
            )

    cierre = compilado["cierre"]
    lineas.extend(
        [
            f"**Síntesis clínica del caso:** {cierre['sintesis']}",
            "",
            "**Objetivos de aprendizaje:**",
            "",
        ]
    )
    for obj in compilado["objetivos"]:
        lineas.append(f"- {obj}")
    lineas.extend(["", ":::"])
    return "\n".join(lineas)


def _adaptar_tablas_evidencia(markdown_texto: str) -> str:
    """Añade anchos proporcionales a las tablas de 7 columnas de medsemiotics-db.

    Evita desbordes horizontales (Overfull \\hbox) en la caja de 132 mm (página 170 × 244 mm).
    """
    lineas = markdown_texto.splitlines()
    salida: list[str] = []
    en_tabla_7col = False
    for idx, linea in enumerate(lineas):
        if linea.startswith("| Signo o síntoma | Sensibilidad | Especificidad | LR+ | LR− |"):
            en_tabla_7col = True
        salida.append(linea)
        if en_tabla_7col:
            siguiente = lineas[idx + 1] if idx + 1 < len(lineas) else ""
            if not siguiente.startswith("|"):
                salida.append("")
                salida.append(': {tbl-colwidths="[22,12,12,11,11,20,12]"}')
                en_tabla_7col = False
    return "\n".join(salida)


def _transformar_post_a_qmd(
    texto_post: str,
    caso: CasoLeido | None,
    imagen: ImagenCondicion | None,
) -> str:
    cuerpo = _FRONTMATTER_RE.sub("", texto_post, count=1)
    if caso is not None:
        bloque_caso = renderizar_caso_qmd(caso)
        if _BLOQUE_SOCRATICO_RE.search(cuerpo):
            cuerpo = _BLOQUE_SOCRATICO_RE.sub(f"\n{bloque_caso}\n\n", cuerpo, count=1)
        else:
            cuerpo = f"{cuerpo.rstrip()}\n\n{bloque_caso}\n"
    else:
        cuerpo = _BLOQUE_SOCRATICO_RE.sub("", cuerpo)

    cuerpo = _COMENTARIO_HTML_RE.sub("", cuerpo)
    cuerpo = _SPAN_REF_RE.sub("", cuerpo)
    cuerpo = _LINK_REF_RE.sub(r"\1", cuerpo)

    lineas = cuerpo.lstrip().splitlines()
    if lineas and lineas[0].startswith("# "):
        lineas = lineas[1:]
    cuerpo_sin_h1 = "\n".join(lineas).strip()
    cuerpo_adaptado = _adaptar_tablas_evidencia(cuerpo_sin_h1)

    if imagen is not None:
        ficha_img = (
            "::: {.enlace-ficha}\n"
            f"**Iconografía clínica de referencia ({imagen.condicion_id}):** "
            f"*{imagen.alt}* — Wikimedia Commons (`{imagen.titulo_commons}`), "
            f"licencia {imagen.licencia}, autor: {imagen.autor}.\n"
            ":::\n\n"
        )
        return ficha_img + cuerpo_adaptado
    return cuerpo_adaptado


def leer_condiciones_neurologia(raiz: Path = RAIZ) -> list[CondicionLibro]:
    rutas_casos = Rutas(raiz)
    casos_por_id: dict[str, CasoLeido] = {
        leido.caso.condicion_id: leido for leido in leer_casos(rutas_casos)
    }
    imagenes = leer_imagenes_condiciones(raiz)

    condiciones: list[CondicionLibro] = []
    for cid in CONDICIONES_NEUROLOGIA:
        prefijo = cid.replace(":", "")
        coincidencias = sorted((raiz / "posts").glob(f"{prefijo}-*.md"))
        if len(coincidencias) != 1:
            raise ValueError(f"Se esperaba exactamente un post para {cid}: {coincidencias}")
        ruta_post = coincidencias[0]
        texto_post = ruta_post.read_text(encoding="utf-8")
        fm_match = _FRONTMATTER_RE.match(texto_post)
        if not fm_match:
            raise ValueError(f"{ruta_post}: falta frontmatter YAML")
        fm = yaml.safe_load(fm_match.group(1))
        if not isinstance(fm, dict):
            raise ValueError(f"{ruta_post}: frontmatter inválido")

        articulo = leer_articulo(ruta_post)
        caso = casos_por_id.get(cid)
        imagen = imagenes.get(cid)
        cuerpo_qmd = _transformar_post_a_qmd(texto_post, caso, imagen)

        condiciones.append(
            CondicionLibro(
                condicion_id=cid,
                slug=ruta_post.stem,
                titulo=str(fm.get("title", articulo.condicion_nombre)),
                especialidad=str(fm.get("specialty", "Neurología")),
                fecha=str(fm.get("date", "")),
                descripcion=str(fm.get("description", "")),
                cuerpo_qmd=cuerpo_qmd,
                articulo=articulo,
                caso=caso,
                imagen=imagen,
            )
        )
    return condiciones


def _formatear_proporcion(valor: Any) -> str:
    if isinstance(valor, int | float) and not isinstance(valor, bool):
        pct = round(float(valor) * 100, 1)
        return f"{int(pct)} %" if pct.is_integer() else f"{pct} %".replace(".", ",")
    return "—"


def _formatear_lr(bloque: Any) -> str:
    if not isinstance(bloque, dict):
        return "—"
    val = bloque.get("valor")
    rango = bloque.get("rango")
    if isinstance(val, int | float) and not isinstance(val, bool):
        return str(val).replace(".", ",")
    if isinstance(rango, list) and len(rango) == 2:
        return f"{rango[0]}–{rango[1]}".replace(".", ",")
    return "—"


def todos_los_hallazgos(condiciones: list[CondicionLibro]) -> list[FilaHallazgo]:
    """Devuelve la lista estructurada de hallazgos de todas las condiciones de neurología."""
    filas: list[FilaHallazgo] = []
    for cond in condiciones:
        art = cond.articulo
        for hid, items in art.evidencia.items():
            nombre = art.nombres.get(hid, hid)
            fichas = resumen(hid, art)
            rol = fichas[0]["rol"] if fichas else ""
            item0 = items[0] if items else {}
            sens = _formatear_proporcion(item0.get("sensibilidad"))
            esp = _formatear_proporcion(item0.get("especificidad"))
            lr_p = _formatear_lr(item0.get("lr_positivo"))
            lr_n = _formatear_lr(item0.get("lr_negativo"))
            filas.append(
                FilaHallazgo(
                    condicion_id=cond.condicion_id,
                    titulo_condicion=cond.titulo,
                    hallazgo_id=hid,
                    nombre=nombre,
                    rol=str(rol),
                    sensibilidad=sens,
                    especificidad=esp,
                    lr_pos=lr_p,
                    lr_neg=lr_n,
                )
            )
    return filas
