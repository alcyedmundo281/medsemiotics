"""Comprobaciones del plan contra el sílabo, el sitio y los artículos."""

from __future__ import annotations

from datetime import timedelta
from typing import TYPE_CHECKING

import yaml

from classroom.modelo import Plan

if TYPE_CHECKING:
    from pathlib import Path

MIERCOLES = 2
PUNTOS_RUBRICA = 20


def cargar(ruta: Path) -> Plan:
    return Plan.model_validate(yaml.safe_load(ruta.read_text(encoding="utf-8")))


def errores(plan: Plan, raiz: Path, condiciones_publicadas: set[str]) -> list[str]:
    """Devuelve los errores bloqueantes; lista vacía = el plan es coherente."""
    fallos: list[str] = []
    sesiones = {s.n: s for s in plan.sesiones}
    if sorted(sesiones) != list(range(1, 17)):
        fallos.append("Se esperan 16 sesiones numeradas 1–16.")
    previa = None
    for s in plan.sesiones:
        if s.fecha.weekday() != MIERCOLES:
            fallos.append(f"Sesión {s.n}: {s.fecha} no es miércoles.")
        if previa is not None:
            esperada = previa + timedelta(days=7)
            while esperada in plan.curso.recesos:
                esperada += timedelta(days=7)
            if s.fecha != esperada:
                fallos.append(f"Sesión {s.n}: fecha {s.fecha}, se esperaba {esperada}.")
        previa = s.fecha
        fallos += [
            f"Sesión {s.n}: {c} no tiene artículo en posts/."
            for c in s.condiciones
            if c not in condiciones_publicadas
        ]
        fallos += [
            f"Sesión {s.n}: recurso inexistente {r}" for r in s.recursos if not (raiz / r).exists()
        ]
    if sum(c.peso for c in plan.componentes) != 100:
        fallos.append("Las ponderaciones no suman 100.")
    formativa = sum(c.peso for c in plan.componentes if c.id == "formativa")
    if formativa != 40:
        fallos.append(f"Formativa debe pesar 40 % (pesa {formativa} %).")
    for r in plan.rubricas:
        if sum(c.puntos for c in r.criterios) != PUNTOS_RUBRICA:
            fallos.append(f"Rúbrica {r.id}: los criterios no suman {PUNTOS_RUBRICA}.")
    ids_c = {c.id for c in plan.componentes}
    ids_r = {r.id for r in plan.rubricas}
    for t in plan.tareas:
        if t.componente not in ids_c:
            fallos.append(f"Tarea {t.id}: componente desconocido {t.componente}.")
        if t.rubrica and t.rubrica not in ids_r:
            fallos.append(f"Tarea {t.id}: rúbrica desconocida {t.rubrica}.")
        if t.sesion_publicacion not in sesiones or t.sesion_entrega not in sesiones:
            fallos.append(f"Tarea {t.id}: sesión inexistente.")
        elif t.sesion_entrega < t.sesion_publicacion:
            fallos.append(f"Tarea {t.id}: se entrega antes de publicarse.")
    for c in plan.componentes:
        if c.sesion and c.sesion in sesiones and sesiones[c.sesion].evaluacion != c.id:
            fallos.append(f"Componente {c.id}: la sesión {c.sesion} no la declara.")
    return fallos


def avisos(plan: Plan, condiciones_con_caso: set[str]) -> list[str]:
    """Pendientes no bloqueantes: lo que el docente debe decidir o redactar."""
    sin_caso = [
        f"Sesión {s.n}: {c} sin caso socrático publicado (skill caso-socratico)."
        for s in plan.sesiones
        for c in s.condiciones
        if c not in condiciones_con_caso
    ]
    propuestas = [
        f"Tarea {t.id}: propuesta, confirmar con el docente." for t in plan.tareas if t.propuesta
    ]
    return sin_caso + propuestas
