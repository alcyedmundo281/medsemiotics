"""Genera ``medicina_y_datos.html``, la guía de 16 sesiones, desde ``classroom/curso-*.yaml``.

Las fechas, los casos ancla y las evaluaciones salen del plan: no se escriben a mano en el HTML.
Las tareas marcadas ``propuesta`` no se muestran a los estudiantes hasta que el docente confirme.
"""

from __future__ import annotations

import json
import re
from html import escape
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

    from casos.articulo import Articulo
    from classroom.modelo import Plan, Sesion

MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
TITULO = re.compile(r"<title>(.*?)</title>", re.S)

MOMENTOS = [
    ("0–10", "Caso socrático", "Estimas la probabilidad pretest sin ver el cociente."),
    ("10–35", "Concepto", "Mini-clase anclada en el caso."),
    ("35–65", "Cálculo y debate", "Tabla 2×2, LR y postest en parejas."),
    ("65–80", "Autoevaluación", "Preguntas del Reto clínico."),
    ("80–90", "Cierre", "¿Qué cambia en la conducta?"),
]


def _preguntas(raiz: Path) -> dict[str, int]:
    """Preguntas del Reto por artículo, según el índice del blog (origen de los datos)."""
    indice = json.loads((raiz / "assets" / "data" / "blog-index.json").read_text(encoding="utf-8"))
    return {p["slug"]: int(p.get("quiz_count") or 0) for p in indice}


def _fecha(s: Sesion) -> str:
    return f"mié {s.fecha.day:02d} {MESES[s.fecha.month - 1]} {s.fecha.year}"


def _titulo_pagina(raiz: Path, recurso: str) -> str:
    texto = (raiz / recurso).read_text(encoding="utf-8")
    m = TITULO.search(texto)
    if not m:
        return recurso
    return " ".join(m.group(1).replace(" - Powersemiotics", "").split())


def _enlace(href: str, etiqueta: str, icono: str) -> str:
    return (
        f'<a href="{escape(href)}" class="inline-flex items-center text-sm text-indigo-700 '
        f'hover:text-indigo-500 font-semibold"><i class="fas {icono} mr-2"></i>'
        f"{escape(etiqueta)}</a>"
    )


def _tarjeta(plan: Plan, s: Sesion, raiz: Path, articulos: dict[str, Articulo]) -> str:
    preguntas = _preguntas(raiz)
    enlaces = [
        _enlace(
            f"post.html?slug={articulos[c].slug}",
            f"{articulos[c].condicion_nombre} · {preguntas.get(articulos[c].slug, 0)} preguntas del Reto",
            "fa-file-medical",
        )
        for c in s.condiciones
    ]
    enlaces += [
        _enlace(r, _titulo_pagina(raiz, r), "fa-arrow-up-right-from-square") for r in s.recursos
    ]
    insignias = []
    for t in plan.tareas:
        if not t.propuesta and t.sesion_entrega == s.n:
            insignias.append(f"Entrega: {t.titulo}")
    if s.evaluacion:
        peso = next(c.peso for c in plan.componentes if c.id == s.evaluacion)
        insignias.append(f"Evaluación · {peso} % de la nota")
    chips = "".join(
        '<span class="inline-block bg-yellow-100 text-yellow-800 text-xs font-bold px-2 py-1 '
        f'rounded-full mr-2 mb-2">{escape(i)}</span>'
        for i in insignias
    )
    cuerpo = "".join(f'<li class="mt-1">{e}</li>' for e in enlaces) or (
        '<li class="mt-1 text-sm text-gray-400">Recursos en Classroom.</li>'
    )
    return f"""
        <article id="sesion-{s.n}" class="bg-white p-6 rounded-xl shadow-lg border border-gray-200">
          <div class="flex items-baseline justify-between mb-2">
            <span class="text-sm font-bold text-indigo-700 uppercase tracking-wider">Sesión {s.n}</span>
            <time datetime="{s.fecha.isoformat()}" class="text-sm text-gray-500">{_fecha(s)}</time>
          </div>
          <h3 class="text-xl font-bold text-gray-800 mb-3">{escape(s.tema)}</h3>
          <div>{chips}</div>
          <p class="text-xs font-semibold text-gray-400 uppercase tracking-wider mt-2">Estudio individual</p>
          <ul>{cuerpo}</ul>
        </article>"""


def generar(plan: Plan, raiz: Path, articulos: dict[str, Articulo]) -> str:
    c = plan.curso
    ini, fin = plan.sesiones[0], plan.sesiones[-1]
    recesos = " y ".join(f"{r.day} de dic" for r in c.recesos)
    unidades = ""
    for u in plan.unidades:
        tarjetas = "".join(
            _tarjeta(plan, s, raiz, articulos) for s in plan.sesiones if s.unidad == u.id
        )
        unidades += f"""
      <section id="{u.id.lower()}" class="max-w-6xl mx-auto mb-16">
        <h2 class="text-3xl font-bold text-gray-900 mb-6">{escape(u.titulo)}</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">{tarjetas}
        </div>
      </section>"""
    momentos = "".join(
        f'<li class="flex"><span class="w-16 shrink-0 font-mono text-sm text-indigo-700">{m}</span>'
        f"<span><strong>{escape(t)}.</strong> {escape(d)}</span></li>"
        for m, t, d in MOMENTOS
    )
    pesos = "".join(
        f'<div class="bg-white p-6 rounded-xl shadow border border-gray-200 text-center">'
        f'<div class="text-4xl font-bold gradient-text">{k.peso} %</div>'
        f'<div class="text-gray-700 font-semibold mt-1">{escape(k.titulo)}</div></div>'
        for k in plan.componentes
    )
    rubrica = plan.rubricas[0]
    filas = "".join(
        f'<tr class="border-t border-gray-100"><td class="py-2 pr-4">{escape(k.titulo)}</td>'
        f'<td class="py-2 text-right font-bold">{k.puntos}</td></tr>'
        for k in rubrica.criterios
    )
    nav = "".join(
        f'<a href="#{u.id.lower()}" class="text-indigo-700 hover:text-indigo-500 font-semibold">'
        f"{escape(u.titulo.split(' · ')[0])}</a>"
        for u in plan.unidades
    )
    return f"""<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Medicina y Ciencia 2026-2027 - Powersemiotics</title>
    <link
      rel="canonical"
      href="https://powersemiotics.com/medsemiotics/medicina_y_datos.html"
    />
    <link rel="stylesheet" href="assets/vendor/fontawesome/css/all.min.css" />

    <link href="assets/tailwind.css" rel="stylesheet" />
  </head>

  <body class="font-sans bg-gray-50 text-gray-800">
    <header class="bg-white shadow-sm sticky top-0 z-50">
      <nav class="container mx-auto px-6 py-4 flex justify-between items-center">
        <a href="index.html" class="flex items-center space-x-2">
          <img src="assets/images/logo.png" alt="Logo de Powersemiotics" class="h-8 w-8" />
          <span class="text-2xl font-bold gradient-text">Powersemiotics</span>
        </a>
        <div class="hidden md:flex items-center space-x-6">{nav}<a href="#evaluacion" class="text-indigo-700 hover:text-indigo-500 font-semibold">Evaluación</a></div>
      </nav>
    </header>

    <main class="container mx-auto px-6 py-16">
      <div class="text-center mb-12">
        <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">{escape(c.nombre)}</h1>
        <p class="text-lg text-gray-600 max-w-3xl mx-auto">{escape(c.descripcion)}</p>
        <p class="mt-4 text-gray-600">
          <i class="fas fa-calendar-days mr-2"></i>Miércoles {c.hora_inicio}, {c.duracion_min} min ·
          {_fecha(ini)} a {_fecha(fin)} · {len(plan.sesiones)} sesiones (receso {recesos})
        </p>
        <p class="text-sm text-gray-500">{escape(c.seccion)}</p>
      </div>

      <section class="max-w-6xl mx-auto mb-16 grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="bg-white p-8 rounded-xl shadow-lg border border-gray-200">
          <h2 class="text-2xl font-bold text-gray-800 mb-3">La ruta de un hallazgo</h2>
          <ol class="list-decimal ml-5 text-gray-700 space-y-1">
            <li>¿Qué tan frecuente es? (probabilidad basal)</li>
            <li>¿Qué tan informativo es? (sens/esp → LR+ / LR−)</li>
            <li>¿Qué tan seguro es ese número? (IC 95 %, calidad del estudio)</li>
            <li>¿Cambia la conducta? (umbrales) y ¿cómo se lo digo al paciente?</li>
          </ol>
          <p class="text-sm text-gray-500 mt-4">Cada sesión usa una condición del blog como caso ancla; las cifras salen del artículo, no de memoria.</p>
        </div>
        <div class="bg-white p-8 rounded-xl shadow-lg border border-gray-200">
          <h2 class="text-2xl font-bold text-gray-800 mb-3">Cómo es cada clase</h2>
          <ul class="space-y-2 text-gray-700">{momentos}</ul>
          <p class="text-sm text-gray-500 mt-4">Antes: lee el artículo ancla. Después: autoevalúate en el <a href="reto.html" class="text-indigo-700 font-semibold">Reto clínico</a>. Los casos ancla salen del <a href="index.html" class="text-indigo-700 font-semibold">blog clínico</a> (48 condiciones).</p>
        </div>
      </section>
{unidades}
      <section id="evaluacion" class="max-w-4xl mx-auto mb-16">
        <h2 class="text-3xl font-bold text-gray-900 mb-6">Evaluación</h2>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-6 mb-8">{pesos}</div>
        <div class="bg-white p-8 rounded-xl shadow-lg border border-gray-200">
          <h3 class="text-xl font-bold text-gray-800 mb-3">Rúbrica: {escape(rubrica.titulo.lower())} (20 puntos)</h3>
          <table class="w-full text-gray-700">{filas}</table>
          <ul class="mt-6 text-sm text-gray-600 list-disc ml-5 space-y-1">
            <li>Todo dato de paciente va anonimizado: sin nombres, cédulas ni identificadores.</li>
            <li>Las cifras diagnósticas se citan con su referencia (PMID/DOI); un número sin fuente no puntúa.</li>
            <li>Declara el uso de IA generativa: su salida es un borrador, no una fuente.</li>
            <li>Las entregas se gestionan en Google Classroom.</li>
          </ul>
        </div>
      </section>
    </main>

    <footer class="bg-white mt-20">
      <div class="container mx-auto px-6 py-6 text-center text-gray-500">
        <p>&copy; 2024 Alcy Edmundo Torres Guerrero.</p>
        <p class="mt-2 text-sm">
          Contenido bajo licencia
          <a
            rel="license"
            href="https://creativecommons.org/licenses/by-sa/4.0/deed.es"
            class="font-semibold text-indigo-700 hover:text-indigo-500 transition-colors"
            >Creative Commons Atribución-CompartirIgual 4.0</a
          >.
        </p>
      </div>
    </footer>
  </body>
</html>
"""
