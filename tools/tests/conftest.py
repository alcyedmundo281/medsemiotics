"""Artículo sintético con la forma exacta que produce ``generate_topic.py``."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

import pytest
import yaml

if TYPE_CHECKING:
    from pathlib import Path

HOY = date(2026, 9, 21)

FRONTMATTER: dict[str, Any] = {
    "id": "HM9999-01",
    "slug": "tema-de-prueba",
    "title": "Tema de prueba: hallazgos y evidencia clínica",
    "date": "2026-08-21",
    "author": "Dr. Alcy Torres",
    "fuente": {"repositorio": "alcyedmundo281/medsemiotics-db", "revision": "abc123"},
    "grounding": {
        "condicion_id": "HM:9999",
        "condicion_nombre": "Tema de prueba",
        "concepto_id": "HM:0001",
    },
    "evidencia": [
        {
            "concepto": "HM:0001",
            "rol": "prueba_especifica",
            "estado_lr": "medido",
            "especificidad": 0.87,
            "lr_positivo": {"valor": 3.1, "ic95": [1.6, 5.9], "ref": "pmid:111"},
            "decision": "aumenta la probabilidad",
        },
        {
            "concepto": "HM:0002",
            "rol": "prueba_sensible",
            "estado_lr": "medido",
            "sensibilidad": 0.91,
            "lr_negativo": {"rango": [0.23, 0.44], "ref": "pmid:111"},
            "decision": "su ausencia reduce la probabilidad",
        },
        {
            "concepto": "HM:0003",
            "rol": "manifestacion",
            "estado_lr": "sin_efecto",
            "motivo": "sensible pero inespecífico",
        },
    ],
}

CUERPO = """
# Tema de prueba

## Hallazgos clínicos

### Signo específico (HM:0001)

### Signo sensible (HM:0002)

### Síntoma inespecífico (HM:0003)

## Referencias y procedencia

**pmid:111:** Estudio de referencia. JAMA, 2016. DOI: 10.1/x.
"""

CASO: dict[str, Any] = {
    "condicion_id": "HM:9999",
    "estado": "borrador",
    "autoria": {"autor": "Dr. Alcy Torres", "revisor": None},
    "duracion_min": 45,
    "objetivos": ["Interpretar la adenopatía en un adolescente con odinofagia"],
    "vineta": {
        "titulo": "Un estudiante con dolor de garganta",
        "texto": "Varón de 18 años con odinofagia y fiebre de cuatro días.",
        "datos": [{"etiqueta": "Temperatura", "valor": "38.4 °C"}],
    },
    "etapas": [
        {
            "titulo": "Primeras hipótesis",
            "fase": "activacion",
            "preguntas": [
                {"pregunta": "¿Qué diagnósticos consideras?", "clave": "Faringitis viral y otras."}
            ],
        },
        {
            "titulo": "Exploración cervical",
            "fase": "exploracion",
            "hallazgos": ["HM:0001", "HM:0003"],
            "preguntas": [
                {
                    "pregunta": "¿Qué aporta {{hallazgo HM:0001}}?",
                    "clave": "Con {{lr+ HM:0001}} y {{esp HM:0001}}, aumenta la probabilidad.",
                }
            ],
        },
        {
            "titulo": "Lo que descarta",
            "fase": "discriminacion",
            "hallazgos": ["HM:0002"],
            "preguntas": [
                {
                    "pregunta": "¿Qué pasa si no hay {{hallazgo HM:0002}}?",
                    "clave": "Su ausencia tiene {{lr- HM:0002}} y {{sens HM:0002}}.",
                }
            ],
        },
        {
            "titulo": "Conducta",
            "fase": "decision",
            "preguntas": [
                {"pregunta": "¿Qué harías ahora?", "clave": "Confirmar con laboratorio."}
            ],
        },
    ],
    "cierre": {
        "sintesis": "Los hallazgos de la base orientan más que los síntomas.",
        "necesidades_aprendizaje": ["Revisar la fisiopatología"],
    },
}


@pytest.fixture
def raiz(tmp_path: Path) -> Path:
    (tmp_path / "posts").mkdir()
    (tmp_path / "casos").mkdir()
    texto = "---\n" + yaml.safe_dump(FRONTMATTER, allow_unicode=True) + "---\n" + CUERPO
    (tmp_path / "posts" / "HM9999-tema.md").write_text(texto, encoding="utf-8")
    return tmp_path


def escribir_caso(raiz: Path, caso: dict[str, Any]) -> None:
    texto = yaml.safe_dump(caso, allow_unicode=True, sort_keys=False)
    (raiz / "casos" / "HM9999.yaml").write_text(texto, encoding="utf-8")
