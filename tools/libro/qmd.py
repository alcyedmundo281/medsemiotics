"""Generador del proyecto Quarto (.qmd) del libro de Neurología (170 × 244 mm)."""

from __future__ import annotations

import shutil
from typing import TYPE_CHECKING

import yaml

from libro import ALTO_MM, ALTO_PULGADAS, ANCHO_MM, ANCHO_PULGADAS
from libro.datos import (
    RAIZ,
    CondicionLibro,
    MetadatosLibro,
    leer_condiciones_neurologia,
    leer_metadatos,
    todos_los_hallazgos,
)
from libro.modulos import (
    CapituloModulo,
    obtener_banco_autoevaluacion,
    obtener_capitulos_modulos,
)

if TYPE_CHECKING:
    from collections.abc import Sequence
    from pathlib import Path

RUTA_PREAMBULO = RAIZ / "assets" / "libro" / "preambulo.tex"
RUTA_FILTRO_LUA = RAIZ / "assets" / "libro" / "diseno-pdf.lua"

NOMBRES_QMD_CONDICIONES: dict[str, str] = {
    "HM:6004": "01-hm6004-meningitis-aguda.qmd",
    "HM:6015": "02-hm6015-enfermedad-parkinson.qmd",
    "HM:6023": "03-hm6023-conmocion-cerebral-pediatrica.qmd",
    "HM:6038": "04-hm6038-traumatismo-craneal-leve.qmd",
}


def _generar_index_qmd(
    meta: MetadatosLibro,
    condiciones: Sequence[CondicionLibro],
    modulos: Sequence[CapituloModulo],
) -> str:
    total_hallazgos = sum(len(c.articulo.evidencia) for c in condiciones)
    total_casos = sum(1 for c in condiciones if c.caso is not None)
    total_preguntas = len(obtener_banco_autoevaluacion())
    tamano_str = (
        f"{ANCHO_MM} × {ALTO_MM} mm ({ANCHO_PULGADAS:.2f} × {ALTO_PULGADAS:.2f} pulgadas)".replace(
            ".", ","
        )
    )

    lineas: list[str] = [
        "```{=latex}",
        "\\portadalibro",
        "```",
        "",
        "::: {.portadilla-pdf}",
        f"# {meta.titulo} {{.unnumbered .unlisted}}",
        "",
        f"*{meta.subtitulo}*",
        "",
        f"**{meta.autor}**  ",
        f"{meta.afiliacion} · ORCID: `{meta.orcid}`",
        ":::",
        "",
        "::: {.creditos-pdf}",
        f"**{meta.titulo}**  ",
        f"*{meta.subtitulo}*",
        "",
        f"Primera edición · Versión `{meta.version}` ({meta.fecha_publicacion}).  ",
        f"Autoría y dirección académica: **{meta.autor}** ({meta.afiliacion}).  ",
        f"ORCID: <{meta.orcid}>  ",
        f"DOI de la obra: `https://doi.org/{meta.doi}`  ",
        f"Repositorio fuente: <{meta.url_repositorio}>  ",
        f"Plataforma interactiva: <{meta.url_sitio}>",
        "",
        (
            "**Fuente clínica única verificada:** las cifras diagnósticas de sensibilidad, "
            "especificidad y cocientes de verosimilitud (LR+ y LR−) de la Parte I proceden "
            "íntegramente de la base estructurada `medsemiotics-db` y sus fuentes primarias "
            "indexadas en PubMed/DOI."
        ),
        "",
        (
            f"**Especificaciones de imprenta (catálogo KDP e IngramSpark):** formato de corte "
            f"{tamano_str}, composición tipográfica a dos caras en KOMA-Script (`scrbook` 10,5 pt) "
            "con la familia *Libertinus Serif* y motor LuaLaTeX."
        ),
        "",
        (
            f"**Licencia de publicación:** obra distribuida bajo licencia abierta "
            f"**Creative Commons Atribución-CompartirIgual 4.0 Internacional ({meta.licencia})**. "
            "Las imágenes clínicas registradas proceden de Wikimedia Commons en dominio público "
            "(PD) o dedicación CC0."
        ),
        "",
        "::: {.alerta-ficha}",
        "**Aviso médico-legal y docente:** Esta obra tiene carácter exclusivamente educativo y "
        "científico para estudiantes de medicina, residentes y profesionales de la salud. Ningún "
        "algoritmo, cociente de verosimilitud o protocolo sustituye el juicio clínico individual "
        "frente al paciente ni las guías oficiales de cada institución sanitaria.",
        ":::",
        ":::",
        "",
        "```{=latex}",
        "\\tableofcontents",
        "\\cleardoublepage",
        "```",
        "",
        "# Prefacio y arquitectura metodológica {.unnumbered}",
        "",
        (
            "La neurología clínica es la disciplina médica donde la anamnesis dirigida y la "
            "exploración física conservan su mayor poder resolutivo. Sin embargo, durante décadas "
            "la enseñanza tradicional de la semiología neurológica transmitió maniobras epónimas "
            "sin explicitar su rendimiento diagnóstico cuantitativo real en estudios prospectivos. "
            "El proyecto **PowerSemiotics (`medsemiotics`)** une dos tradiciones complementarias: "
            "la **anatomía clínica localizadora** (que responde *dónde* se asienta la lesión) y "
            "la **medicina basada en la evidencia bayesiana** (que cuantifica *cuánto* modifica "
            "cada signo o regla de decisión la probabilidad de enfermedad)."
        ),
        "",
        "## Fundamento bayesiano de la semiología neurológica {.unnumbered}",
        "",
        (
            "Todo hallazgo semiológico actúa como una prueba diagnóstica que transforma una "
            "**probabilidad preprueba ($P_0$)** en una **probabilidad posprueba ($P_1$)** a través "
            "de sus **cocientes de verosimilitud (*likelihood ratios*, LR)**:"
        ),
        "",
        "$$",
        "\\text{Odds}_{\\text{posprueba}} = \\text{Odds}_{\\text{preprueba}} \\times \\text{LR}, "
        "\\qquad \\text{donde } \\text{Odds} = \\frac{P}{1 - P}",
        "$$",
        "",
        "$$",
        "\\text{LR}^+ = \\frac{\\text{Sensibilidad}}{1 - \\text{Especificidad}}, "
        "\\qquad "
        "\\text{LR}^- = \\frac{1 - \\text{Sensibilidad}}{\\text{Especificidad}}",
        "$$",
        "",
        (
            "- Un **$\\text{LR}^+ \\ge 10$** produce un incremento grande y a menudo concluyente "
            "en la probabilidad de la condición (por ejemplo, el cumplimiento de los criterios MDS "
            "para enfermedad de Parkinson clínicamente establecida con $\\text{LR}^+ = 24{,}5$)."
        ),
        (
            "- Un **$\\text{LR}^- \\le 0{,}10$** produce una reducción drástica que permite "
            "**descartar (*rule out*)** la condición con alto margen de seguridad (por ejemplo, "
            "la *Canadian CT Head Rule* negativa con $\\text{LR}^- = 0{,}04\\text{–}0{,}06$)."
        ),
        (
            "- Un **$\\text{LR}$ cercano a $1{,}0$** carece de poder discriminativo (por ejemplo, "
            "la ausencia aislada de los signos de Kernig o Brudzinski con $\\text{LR}^- = "
            "0{,}95\\text{–}0{,}97$, que jamás descarta una meningitis aguda)."
        ),
        "",
        "## Estructura de esta edición impresa {.unnumbered}",
        "",
        f"Esta obra integra **{len(condiciones)} condiciones verificadas** de `medsemiotics-db` "
        f"(con **{total_hallazgos} hallazgos semiológicos cuantificados** y **{total_casos} caso "
        f"socrático de aprendizaje basado en problemas**), **{len(modulos)} módulos clínicos "
        f"sistemáticos** y **{total_preguntas} problemas integradores de autoevaluación**:",
        "",
        (
            "1. **Parte I — Semiología Neurológica Basada en la Evidencia (`medsemiotics-db`) y "
            "Casos Socráticos:** aborda la meningitis aguda (`HM:6004`), la enfermedad de "
            "Parkinson según criterios MDS (`HM:6015`), la conmoción cerebral pediátrica y reglas "
            "PECARN (`HM:6023`), y la lesión intracraneal en el traumatismo craneal leve del "
            "adulto (`HM:6038`)."
        ),
        (
            "2. **Parte II — Síndromes Clínicos y Protocolos en Neurología:** desarrolla la "
            "exploración neurológica sistemática, cefaleas y banderas rojas SNOOP10, epilepsias y "
            "estado epiléptico, enfermedad cerebrovascular y Código Ictus, trastornos del "
            "movimiento hipo e hipercinéticos, enfermedades desmielinizantes del SNC, patología de "
            "la unión neuromuscular y miopatías, neuropatías periféricas y síndrome de "
            "Guillain-Barré, y demencias."
        ),
        (
            "3. **Apéndices:** banco de autoevaluación clínica integradora con justificación "
            "pedagógica detallada, índice maestro de precisión diagnóstica e inventario de "
            "iconografía abierta."
        ),
        "",
    ]
    return "\n".join(lineas)


def _generar_capitulo_condicion(cond: CondicionLibro) -> str:
    lineas: list[str] = [
        f"# {cond.titulo} (`{cond.condicion_id}`)",
        "",
        "::: {.enlace-ficha}",
        (
            f"**Condición verificada en `medsemiotics-db`:** `{cond.condicion_id}` · "
            f"Especialidad: {cond.especialidad} · Fecha de compilación: `{cond.fecha}` · "
            f"Archivo derivado: `posts/{cond.slug}.md`."
        ),
        ":::",
        "",
        cond.cuerpo_qmd.strip(),
        "",
    ]
    return "\n".join(lineas)


def _generar_capitulo_modulo(cap: CapituloModulo) -> str:
    lineas: list[str] = [
        f"# {cap.titulo}",
        "",
        f"*{cap.subtitulo}*",
        "",
        cap.cuerpo_qmd.strip(),
        "",
    ]
    return "\n".join(lineas)


def _generar_apendice_autoevaluacion() -> str:
    preguntas = obtener_banco_autoevaluacion()
    lineas: list[str] = [
        "# Autoevaluación Clínica Integradora y Respuestas Razonadas",
        "",
        (
            "Este apéndice reúne doce escenarios clínicos de selección múltiple extraídos de los "
            "módulos interactivos de evaluación del repositorio (`neurologia-autoevaluacion.html`, "
            "`cefaleas-autoevaluacion.html`, `epilepsia-2-autoevaluacion.html`, "
            "`neuromusculares.html` y `neuropatias.html`) y de las condiciones de "
            "`medsemiotics-db`. Se presenta primero el bloque de enunciados para resolución "
            "autónoma y, a continuación, la clave razonada."
        ),
        "",
        "## Enunciados de los casos clínicos",
        "",
    ]
    for p in preguntas:
        lineas.extend(
            [
                f"### Caso {p.numero}. {p.dominio}",
                "",
                p.enunciado,
                "",
            ]
        )
        for idx, op in enumerate(p.opciones):
            letra = chr(ord("A") + idx)
            lineas.append(f"- **{letra}.** {op}")
        lineas.append("")

    lineas.extend(
        [
            "---",
            "",
            "## Clave de respuestas y justificación fisiopatológica y bayesiana",
            "",
        ]
    )
    for p in preguntas:
        letra_ok = chr(ord("A") + p.indice_correcto)
        texto_ok = p.opciones[p.indice_correcto]
        lineas.extend(
            [
                "::: {.perlas-clinicas}",
                f"**Caso {p.numero} ({p.dominio}) — Respuesta correcta: {letra_ok}** "
                f"(*{texto_ok}*).",
                "",
                f"{p.justificacion}",
                "",
                f"*Fuente en el repositorio:* `{p.fuente}`.",
                ":::",
                "",
            ]
        )
    return "\n".join(lineas)


def _generar_apendice_evidencia(condiciones: Sequence[CondicionLibro]) -> str:
    filas = todos_los_hallazgos(list(condiciones))
    lineas: list[str] = [
        "# Síntesis de Evidencia Diagnóstica e Iconografía Abierta",
        "",
        "## Tabla maestra de hallazgos neurológicos (`medsemiotics-db`)",
        "",
        (
            "La siguiente tabla consolida los parámetros de sensibilidad, especificidad y "
            "cocientes de verosimilitud positivo ($\\text{LR}^+$) y negativo ($\\text{LR}^-$) de "
            "las condiciones neurológicas verificadas en la Parte I."
        ),
        "",
        "| Código | Condición | Signo, síntoma o regla | Sens. | Esp. | LR+ | LR− |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for h in filas:
        titulo_corto = h.titulo_condicion.split(":")[0].strip()
        lineas.append(
            f"| `{h.condicion_id}` | {titulo_corto} | {h.nombre} (`{h.hallazgo_id}`) | "
            f"{h.sensibilidad} | {h.especificidad} | {h.lr_pos} | {h.lr_neg} |"
        )
    lineas.extend(
        [
            "",
            ': {tbl-colwidths="[11,22,31,9,9,9,9]"}',
            "",
            "## Registro de iconografía clínica en dominio público (Wikimedia Commons)",
            "",
            (
                "Todas las imágenes asociadas a las condiciones neurológicas del repositorio han "
                "sido verificadas mediante `uv run python -m imagenes check` contra la API de "
                "Wikimedia Commons en dominio público (`pd`) o dedicación `cc0`:"
            ),
            "",
            "| Código | Archivo en Wikimedia Commons | Licencia | Autoría | Descripción clínica |",
            "| :--- | :--- | :--- | :--- | :--- |",
        ]
    )
    for cond in condiciones:
        if cond.imagen is not None:
            img = cond.imagen
            lineas.append(
                f"| `{cond.condicion_id}` | `{img.titulo_commons}` | {img.licencia} | "
                f"{img.autor} | {img.alt} |"
            )
    lineas.extend(
        [
            "",
            ': {tbl-colwidths="[11,26,13,20,30]"}',
            "",
        ]
    )
    return "\n".join(lineas)


def _generar_portada_svg(meta: MetadatosLibro) -> str:
    """Genera portada vectorial SVG 1700 × 2440 (proporción exacta 170 × 244 mm)."""
    lineas = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'viewBox="0 0 1700 2440" width="170mm" height="244mm">',
        '  <rect width="1700" height="2440" fill="#0D1B2A" />',
        '  <rect x="96" y="96" width="1508" height="2248" fill="none" '
        'stroke="#F8F6F1" stroke-opacity="0.25" stroke-width="2" />',
        '  <rect x="114" y="114" width="1472" height="2212" fill="none" '
        'stroke="#C69C6D" stroke-opacity="0.55" stroke-width="3" />',
        '  <text x="164" y="210" fill="#C69C6D" '
        'font-family="Libertinus Sans, sans-serif" font-size="24" font-weight="bold">',
        "    COLECCIÓN POWERSEMIOTICS · MEDICINA BASADA EN LA EVIDENCIA",
        "  </text>",
        '  <line x1="164" y1="238" x2="820" y2="238" stroke="#C69C6D" stroke-width="3" />',
        '  <text x="164" y="345" fill="#F8F6F1" '
        'font-family="Libertinus Serif Display, serif" font-size="68" font-weight="bold">',
        '    <tspan x="164" dy="0">Neurología Clínica y</tspan>',
        '    <tspan x="164" dy="82">Semiología Basada</tspan>',
        '    <tspan x="164" dy="82">en la Evidencia</tspan>',
        "  </text>",
        '  <text x="164" y="610" fill="#F8F6F1" fill-opacity="0.88" '
        'font-family="Libertinus Serif, serif" font-size="30" font-style="italic">',
        '    <tspan x="164" dy="0">Cocientes de verosimilitud, reglas de decisión clínica, '
        "casos socráticos</tspan>",
        '    <tspan x="164" dy="42">y síndromes neurológicos de urgencia y consulta '
        "(170 × 244 mm)</tspan>",
        "  </text>",
        '  <line x1="164" y1="705" x2="1536" y2="705" '
        'stroke="#C69C6D" stroke-opacity="0.65" stroke-width="2" />',
        '  <g transform="translate(850,1280)">',
        '    <circle cx="0" cy="0" r="390" fill="none" '
        'stroke="#F8F6F1" stroke-opacity="0.10" stroke-width="2" />',
        '    <circle cx="0" cy="0" r="280" fill="none" '
        'stroke="#C69C6D" stroke-opacity="0.30" stroke-width="3" stroke-dasharray="12,10" />',
        '    <circle cx="0" cy="0" r="160" fill="none" '
        'stroke="#F8F6F1" stroke-opacity="0.16" stroke-width="2" />',
        '    <polyline points="-380,30 -210,30 -175,-20 -140,60 -95,-220 '
        '-45,150 5,-45 55,30 380,30" '
        'fill="none" stroke="#C69C6D" stroke-width="6" />',
        "  </g>",
        '  <text x="164" y="2165" fill="#F8F6F1" '
        'font-family="Libertinus Sans, sans-serif" font-size="38" font-weight="bold">',
        f"    {meta.autor}",
        "  </text>",
        '  <text x="164" y="2225" fill="#C69C6D" '
        'font-family="Libertinus Sans, sans-serif" font-size="24">',
        f"    PowerSemiotics · Licencia {meta.licencia} · DOI {meta.doi}",
        "  </text>",
        "</svg>",
        "",
    ]
    return "\n".join(lineas)


def _configuracion_quarto(
    meta: MetadatosLibro,
    archivos_parte_1: list[str],
    archivos_parte_2: list[str],
    archivos_apendices: list[str],
) -> dict[str, object]:
    return {
        "project": {
            "type": "book",
            "output-dir": "_book",
        },
        "book": {
            "title": meta.titulo,
            "subtitle": meta.subtitulo,
            "author": meta.autor,
            "date": meta.fecha_publicacion,
            "output-file": "libro",
            "chapters": [
                "index.qmd",
                {
                    "part": (
                        "Parte I · Semiología Neurológica Basada en la Evidencia "
                        "(medsemiotics-db) y Casos Socráticos"
                    ),
                    "chapters": archivos_parte_1,
                },
                {
                    "part": "Parte II · Síndromes Clínicos y Protocolos en Neurología",
                    "chapters": archivos_parte_2,
                },
                {
                    "part": "Apéndices · Autoevaluación y Tablas Maestras",
                    "chapters": archivos_apendices,
                },
            ],
        },
        "lang": "es",
        "format": {
            "pdf": {
                "documentclass": "scrbook",
                "classoption": ["twoside", "open=any", "fontsize=10.5pt"],
                "keep-tex": True,
                "pdf-engine": "lualatex",
                "toc": False,
                "number-sections": True,
                "colorlinks": True,
                "linkcolor": "libroprimario",
                "urlcolor": "libroacento",
                "citecolor": "libroprimario",
                "mainfont": "Libertinus Serif",
                "sansfont": "Libertinus Sans",
                "monofont": "Libertinus Mono",
                "geometry": [
                    f"paperwidth={ANCHO_MM}mm",
                    f"paperheight={ALTO_MM}mm",
                    "inner=20mm",
                    "outer=18mm",
                    "top=24mm",
                    "bottom=24mm",
                    "headsep=7mm",
                    "footskip=11mm",
                ],
                "include-in-header": "preambulo-libro.tex",
                "filters": ["diseno-pdf.lua"],
            },
        },
    }


def generar_proyecto_quarto(
    carpeta_salida: Path,
    raiz: Path = RAIZ,
) -> list[Path]:
    """Genera todos los archivos del proyecto Quarto en ``carpeta_salida``."""
    carpeta_salida.mkdir(parents=True, exist_ok=True)
    meta = leer_metadatos(raiz)
    condiciones = leer_condiciones_neurologia(raiz)
    modulos = obtener_capitulos_modulos()

    shutil.copyfile(RUTA_PREAMBULO, carpeta_salida / "preambulo-libro.tex")
    shutil.copyfile(RUTA_FILTRO_LUA, carpeta_salida / "diseno-pdf.lua")

    ruta_portada_svg = carpeta_salida / "portada.svg"
    ruta_portada_svg.write_text(_generar_portada_svg(meta), encoding="utf-8")

    generados: list[Path] = [
        carpeta_salida / "preambulo-libro.tex",
        carpeta_salida / "diseno-pdf.lua",
        ruta_portada_svg,
    ]
    secciones_planas: list[str] = []

    # 1. index.qmd
    texto_index = _generar_index_qmd(meta, condiciones, modulos)
    ruta_index = carpeta_salida / "index.qmd"
    ruta_index.write_text(texto_index, encoding="utf-8")
    generados.append(ruta_index)
    secciones_planas.append(texto_index)

    # 2. Parte I: Condiciones de medsemiotics-db + casos socráticos
    archivos_parte_1: list[str] = []
    for cond in condiciones:
        nombre_qmd = NOMBRES_QMD_CONDICIONES[cond.condicion_id]
        archivos_parte_1.append(nombre_qmd)
        texto_cap = _generar_capitulo_condicion(cond)
        ruta_cap = carpeta_salida / nombre_qmd
        ruta_cap.write_text(texto_cap, encoding="utf-8")
        generados.append(ruta_cap)
        secciones_planas.append(texto_cap)

    # 3. Parte II: Módulos clínicos de neurologia/
    archivos_parte_2: list[str] = []
    for mod in modulos:
        archivos_parte_2.append(mod.archivo_qmd)
        texto_mod = _generar_capitulo_modulo(mod)
        ruta_mod = carpeta_salida / mod.archivo_qmd
        ruta_mod.write_text(texto_mod, encoding="utf-8")
        generados.append(ruta_mod)
        secciones_planas.append(texto_mod)

    # 4. Apéndices
    nombre_autoeval = "14-autoevaluacion.qmd"
    texto_autoeval = _generar_apendice_autoevaluacion()
    ruta_autoeval = carpeta_salida / nombre_autoeval
    ruta_autoeval.write_text(texto_autoeval, encoding="utf-8")
    generados.append(ruta_autoeval)
    secciones_planas.append(texto_autoeval)

    nombre_evidencia = "15-indice-evidencia-referencias.qmd"
    texto_evidencia = _generar_apendice_evidencia(condiciones)
    ruta_evidencia = carpeta_salida / nombre_evidencia
    ruta_evidencia.write_text(texto_evidencia, encoding="utf-8")
    generados.append(ruta_evidencia)
    secciones_planas.append(texto_evidencia)

    archivos_apendices = [nombre_autoeval, nombre_evidencia]

    # 5. _quarto.yml
    cfg = _configuracion_quarto(meta, archivos_parte_1, archivos_parte_2, archivos_apendices)
    ruta_quarto_yml = carpeta_salida / "_quarto.yml"
    ruta_quarto_yml.write_text(
        yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    generados.append(ruta_quarto_yml)

    # 6. Manuscrito plano unificado
    manuscrito = "\n\n---\n\n".join(secciones_planas)
    ruta_plano = carpeta_salida / "libro-plano.md"
    ruta_plano.write_text(manuscrito, encoding="utf-8")
    generados.append(ruta_plano)

    return generados
