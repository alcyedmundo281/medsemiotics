#!/usr/bin/env python3
"""Motor de Generación y Publicación de Temas Clínicos para MedSemiotics.
---------------------------------------------------------------------
Conecta directamente con medsemiotics-db (GitHub / local), extrae entidades
validadas (conceptos, condiciones, referencias) y genera publicaciones
interactivas en Markdown con estricto apego a la Ley de Grounding Absoluta.

Uso:
  python tools/generate_topic.py --list
  python tools/generate_topic.py --condition HM6011
  python tools/generate_topic.py --condition HM6012
  python tools/generate_topic.py --sync-all

Regla que este script no rompe: si una condición no tiene ningún signo con
estado_lr: medido y referencia resoluble, NO se genera un post con números de
relleno. Se informa y se omite. Un post con un cociente y un PMID inventados
es peor que no tener post.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
import urllib.error
from pathlib import Path

# Fix Windows console encoding
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

try:
    import yaml
except ImportError:
    print("Error: PyYAML no está instalado. Ejecuta: pip install pyyaml")
    sys.exit(1)

ROOT_DIR = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT_DIR / "posts"
DATA_DIR = ROOT_DIR / "assets" / "data"

DB_RAW_BASE = "https://raw.githubusercontent.com/alcyedmundo281/medsemiotics-db/main"
DB_API_CONTENTS = "https://api.github.com/repos/alcyedmundo281/medsemiotics-db/contents"

# Mapeo de taxonomía clínica real
SPECIALTY_MAP = {
    "meningitis": ("neurologia", "Neurología"),
    "parkinson": ("neurologia", "Neurología"),
    "cefalea": ("neurologia", "Neurología"),
    "acv": ("neurologia", "Neurología"),
    "epilepsia": ("neurologia", "Neurología"),
    "coronario": ("cardiologia", "Cardiología"),
    "sincope": ("cardiologia", "Cardiología y Urgencias"),
    "aorta": ("vascular", "Medicina Vascular y Cirugía"),
    "aneurisma": ("vascular", "Medicina Vascular y Cirugía"),
    "hipovolemia": ("urgencias", "Medicina de Urgencias y Críticos"),
    "shock": ("urgencias", "Medicina de Urgencias y Críticos"),
    "urgencias": ("urgencias", "Medicina de Urgencias y Críticos"),
    "pleural": ("neumologia", "Neumología y Medicina Interna"),
    "neumonia": ("neumologia", "Neumología y Medicina Interna"),
    "faringitis": ("infectologia", "Infectología y Atención Primaria"),
    "mononucleosis": ("infectologia", "Infectología y Medicina Interna"),
    "vih": ("infectologia", "Infectología y Medicina Interna"),
    "hepatitis": ("gastroenterologia", "Gastroenterología y Hepatología"),
    "pancreatitis": ("gastroenterologia", "Gastroenterología y Hepatología"),
    "intestino": ("gastroenterologia", "Gastroenterología"),
    "cadera": ("reumatologia", "Reumatología y Traumatología"),
    "manguito": ("traumatologia", "Traumatología y Medicina Deportiva"),
}

# Bandas de interpretación de McGee S. Simplifying likelihood ratios.
# J Gen Intern Med. 2002;17(8):646-9. Es una convención general de lectura,
# no un dato de la condición: se cita aparte y nunca sustituye al LR con ref.
LR_POS_BANDS = [
    (10, "cambia mucho la probabilidad: suele bastar por sí solo para confirmar"),
    (5, "cambia moderadamente la probabilidad: evidencia útil"),
    (2, "cambia poco la probabilidad: evidencia débil"),
    (0, "prácticamente no cambia la probabilidad"),
]
LR_NEG_BANDS = [
    (0.1, "cambia mucho la probabilidad: suele bastar por sí solo para descartar"),
    (0.2, "cambia moderadamente la probabilidad"),
    (0.5, "cambia poco la probabilidad"),
    (float("inf"), "prácticamente no cambia la probabilidad"),
]


def interpret_lr_positive(lr):
    if not isinstance(lr, (int, float)):
        return None
    for umbral, texto in LR_POS_BANDS:
        if lr >= umbral:
            return texto
    return LR_POS_BANDS[-1][1]


def interpret_lr_negative(lr):
    if not isinstance(lr, (int, float)):
        return None
    for umbral, texto in LR_NEG_BANDS:
        if lr <= umbral:
            return texto
    return LR_NEG_BANDS[-1][1]


def fetch_url_text(url: str) -> str:
    """Descarga texto de una URL con User-Agent seguro."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "MedSemiotics-TopicEngine/1.0 (https://powersemiotics.com)"}
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read().decode("utf-8")


def fetch_url_json(url: str):
    """Descarga JSON de una URL."""
    text = fetch_url_text(url)
    return json.loads(text)


def list_remote_conditions():
    """Obtiene la lista de condiciones disponibles en medsemiotics-db."""
    url = f"{DB_API_CONTENTS}/condiciones"
    try:
        items = fetch_url_json(url)
        conditions = [item["name"] for item in items if item["name"].endswith(".yaml")]
        return sorted(conditions)
    except Exception as e:
        print(f"[!] Error al listar condiciones remotas: {e}")
        return []


def fetch_condition_yaml(filename_or_id: str) -> dict:
    """Obtiene y parsea el YAML de una condición."""
    if not filename_or_id.endswith(".yaml"):
        # Buscar por ID (ej. HM6011)
        conditions = list_remote_conditions()
        match = next((c for c in conditions if filename_or_id.lower() in c.lower()), None)
        if not match:
            raise FileNotFoundError(f"No se encontró la condición con identificador: {filename_or_id}")
        filename = match
    else:
        filename = filename_or_id

    url = f"{DB_RAW_BASE}/condiciones/{filename}"
    raw = fetch_url_text(url)
    return yaml.safe_load(raw), filename


def fetch_reference_yaml(ref_id: str) -> dict:
    """Descarga los metadatos verificados de una referencia PMID."""
    clean_id = ref_id.replace("pmid:", "pmid-")
    if not clean_id.endswith(".yaml"):
        clean_id += ".yaml"
    url = f"{DB_RAW_BASE}/referencias/{clean_id}"
    try:
        raw = fetch_url_text(url)
        return yaml.safe_load(raw)
    except Exception as e:
        print(f"[!] Advertencia: No se pudo cargar referencia {ref_id}: {e}")
        return {}


_CONCEPT_LIST_CACHE = None
_CONCEPT_CACHE = {}


def list_remote_concepts():
    """Obtiene la lista de conceptos disponibles en medsemiotics-db. Cacheado
    en memoria porque --sync-all resuelve decenas de conceptos por corrida."""
    global _CONCEPT_LIST_CACHE
    if _CONCEPT_LIST_CACHE is not None:
        return _CONCEPT_LIST_CACHE
    url = f"{DB_API_CONTENTS}/conceptos"
    try:
        items = fetch_url_json(url)
        _CONCEPT_LIST_CACHE = sorted(item["name"] for item in items if item["name"].endswith(".yaml"))
    except Exception as e:
        print(f"[!] Error al listar conceptos remotos: {e}")
        _CONCEPT_LIST_CACHE = []
    return _CONCEPT_LIST_CACHE


def fetch_concept_yaml(concepto_id: str) -> dict:
    """Resuelve un ID de concepto (ej. 'HM:3039') a su registro real en
    conceptos/*.yaml. Sin esto, el post solo tiene el ID en bruto y ninguna
    forma de nombrar el hallazgo del que habla."""
    if not concepto_id:
        return {}
    if concepto_id in _CONCEPT_CACHE:
        return _CONCEPT_CACHE[concepto_id]
    clean_id = concepto_id.replace(":", "").replace(" ", "").lower()
    conceptos = list_remote_concepts()
    match = next((c for c in conceptos if c.lower().startswith(clean_id + "-")), None)
    data = {}
    if match:
        url = f"{DB_RAW_BASE}/conceptos/{match}"
        try:
            raw = fetch_url_text(url)
            data = yaml.safe_load(raw) or {}
        except Exception as e:
            print(f"[!] Advertencia: no se pudo cargar concepto {concepto_id}: {e}")
    else:
        print(f"[!] Advertencia: concepto {concepto_id} no encontrado en medsemiotics-db")
    _CONCEPT_CACHE[concepto_id] = data
    return data


def determine_specialty(term: str, signs: list) -> tuple:
    """Asigna la especialidad médica real según el término y signos."""
    text_to_check = (term + " " + " ".join([str(s) for s in signs])).lower()
    for key, (cat, label) in SPECIALTY_MAP.items():
        if key in text_to_check:
            return cat, label
    return "medicina_interna", "Medicina Interna"


def generate_slug(text: str) -> str:
    """Genera un slug limpio y descriptivo."""
    text = text.lower()
    text = re.sub(r"[áäàâ]", "a", text)
    text = re.sub(r"[éëèê]", "e", text)
    text = re.sub(r"[íïìî]", "i", text)
    text = re.sub(r"[óöòô]", "o", text)
    text = re.sub(r"[úüùû]", "u", text)
    text = re.sub(r"[ñ]", "n", text)
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[-\s]+", "-", text).strip("-")


def select_main_sign(signs: list):
    """Elige el signo más discriminativo entre los medidos con LR y ref
    resoluble. Nunca devuelve un signo sin LR real: la condición puede no
    tener ninguno todavía, y en ese caso no hay post que generar."""
    candidates = []
    for s in signs:
        if not isinstance(s, dict) or s.get("estado_lr") != "medido":
            continue
        lr_pos_block = s.get("lr_positivo") or {}
        lr_neg_block = s.get("lr_negativo") or {}
        lr_pos = lr_pos_block.get("valor")
        lr_neg = lr_neg_block.get("valor")
        ref = lr_pos_block.get("ref") or lr_neg_block.get("ref")
        if not ref or (lr_pos is None and lr_neg is None):
            continue
        strength = 0
        if isinstance(lr_pos, (int, float)):
            strength = max(strength, lr_pos)
        if isinstance(lr_neg, (int, float)) and lr_neg > 0:
            strength = max(strength, 1 / lr_neg)
        candidates.append((strength, s))
    if not candidates:
        return None
    candidates.sort(key=lambda x: x[0], reverse=True)
    return candidates[0][1]


def create_post_markdown(cond_data: dict, filename: str):
    """Genera el contenido Markdown completo con Frontmatter enriquecido.

    Devuelve (None, None, motivo) si la condición no tiene una base
    verificable para un post cuantitativo: eso no es un error a silenciar
    con valores de relleno, es información para quien decide qué publicar.
    """
    cond_id = cond_data.get("id", "HM:XXXX")
    term = cond_data.get("termino", "Condición Clínica")
    term_en = cond_data.get("termino_en", "")
    signs = cond_data.get("signos", []) or []

    main_sign = select_main_sign(signs)
    if main_sign is None:
        return None, None, (
            "sin signos con estado_lr: medido y referencia resoluble — "
            "no hay cociente verificado sobre el que construir el post"
        )

    lr_pos_block = main_sign.get("lr_positivo") or {}
    lr_neg_block = main_sign.get("lr_negativo") or {}
    lr_pos = lr_pos_block.get("valor")
    lr_neg = lr_neg_block.get("valor")
    ref_key = lr_pos_block.get("ref") or lr_neg_block.get("ref")

    ref_data = fetch_reference_yaml(ref_key)
    pmid = (ref_data.get("identificadores") or {}).get("pmid") or ref_data.get("pmid")
    if not ref_data or not pmid:
        return None, None, f"la referencia {ref_key} no resolvió contra medsemiotics-db"

    concept_data = fetch_concept_yaml(main_sign.get("concepto"))
    concept_termino = concept_data.get("termino") or main_sign.get("concepto") or "hallazgo no identificado"
    concept_termino_en = concept_data.get("termino_en") or ""

    # Sensibilidad/especificidad: solo si la condición las publica. Un
    # número de relleno aquí es indistinguible de uno verificado para
    # quien lee, así que se omite en vez de inventarse.
    sens = main_sign.get("sensibilidad")
    spec = main_sign.get("especificidad")

    poblacion = main_sign.get("poblacion")
    if not poblacion:
        base = cond_data.get("probabilidad_base")
        if isinstance(base, dict):
            poblacion = base.get("poblacion")
    poblacion = poblacion or "no especificada en la fuente citada"

    doi = (ref_data.get("identificadores") or {}).get("doi") or ref_data.get("doi") or ""
    authors = ref_data.get("autores") or ["Investigadores Clínicos"]
    author_str = ", ".join(authors[:3]) + (" et al." if len(authors) > 3 else "")
    journal = ref_data.get("publicacion", "")
    year = ref_data.get("anio", "")
    title_ref = ref_data.get("titulo", "")
    citation = f"{author_str}. {title_ref}. {journal}. {year}."

    category, category_label = determine_specialty(term, signs)
    slug = f"{generate_slug(term)}-precision-semiotica"
    post_id = cond_id.replace(":", "") + "-01"

    # Interpretación de magnitud (McGee 2002), no del estudio: se etiqueta
    # como tal en el propio texto para no mezclarla con el dato verificado.
    interp_pos = interpret_lr_positive(lr_pos)
    interp_neg = interpret_lr_negative(lr_neg)

    decision_bits = []
    if main_sign.get("decision"):
        decision_bits.append(main_sign["decision"].strip())
    else:
        if interp_pos:
            decision_bits.append(f"si está presente, {interp_pos} (LR+ {lr_pos})")
        if interp_neg:
            decision_bits.append(f"si está ausente, {interp_neg} (LR- {lr_neg})")
    # La advertencia es una salvedad sobre el USO del cociente (precisión,
    # límites), no una explicación fisiopatológica: va pegada a la decisión
    # clínica, nunca al panel de "significado" (ver más abajo).
    if main_sign.get("advertencia"):
        decision_bits.append("Advertencia: " + main_sign["advertencia"].strip())
    decision_text = f"{concept_termino} — " + "; ".join(decision_bits) if decision_bits else concept_termino

    # El "significado" es la interpretación fisiopatológica del hallazgo, y
    # los conceptos del índice todavía no la traen (campo `significado` en
    # blanco, pendiente de migrar desde biosemiotics). Ninguna otra prosa del
    # índice sustituye eso sin mentir sobre lo que dice: `advertencia` es una
    # salvedad estadística, no una explicación de mecanismo, así que aquí
    # siempre queda la nota honesta en vez de un campo mal etiquetado.
    significado = (
        "La fuente no describe el mecanismo fisiopatológico de este hallazgo; "
        "su valor aquí es estadístico (cociente de verosimilitud), no explicativo."
    )

    significante = f"{concept_termino}"
    if concept_termino_en:
        significante += f" ({concept_termino_en})"
    significante += f", evaluado en: {poblacion}."

    lr_pos_str = f"{lr_pos}" if lr_pos is not None else "no medido"
    lr_neg_str = f"{lr_neg}" if lr_neg is not None else "no medido"

    sens_line = f'\n  sensibilidad: {sens}' if sens is not None else ""
    spec_line = f'\n  especificidad: {spec}' if spec is not None else ""

    # Cuerpo: bullets de rendimiento solo con lo que la fuente publica.
    sens_bullet = f"- **Sensibilidad estimada:** {int(sens * 100)}%\n" if isinstance(sens, (int, float)) else ""
    spec_bullet = f"- **Especificidad estimada:** {int(spec * 100)}%\n" if isinstance(spec, (int, float)) else ""
    lr_pos_bullet = f"- **Cociente de Verosimilitud Positivo (LR+):** {lr_pos_str}" + (f" — {interp_pos}" if interp_pos else "") + "\n" if lr_pos is not None else ""
    lr_neg_bullet = f"- **Cociente de Verosimilitud Negativo (LR-):** {lr_neg_str}" + (f" — {interp_neg}" if interp_neg else "") + "\n" if lr_neg is not None else ""

    # Pregunta 1 del quiz: opción sobre especificidad solo si hay una cifra real.
    if isinstance(spec, (int, float)):
        q1_wrong_feedback = f"Incorrecto. Presenta una especificidad documentada de {int(spec * 100)}%."
    else:
        q1_wrong_feedback = "Incorrecto. El hallazgo sí tiene valor discriminativo, documentado mediante su cociente de verosimilitud verificado."

    lr_pos_for_q1 = f"{lr_pos}" if lr_pos is not None else lr_neg_str

    content = f"""---
id: "{post_id}"
slug: "{slug}"
title: "{term}: Precisión diagnóstica y rendimiento de los hallazgos semiológicos"
subtitle: "Análisis bayesiano de {concept_termino.lower()} y su impacto en la toma de decisiones clínicas."
date: "2026-08-21"
author: "Dr. Alcy Torres"
category: "{category}"
category_label: "{category_label}"
tags: ["{category}", "{generate_slug(term)}", "semiologia", "evidencia"]
reading_time: "6 min"
difficulty: "Intermedio"
grounding:
  condicion_id: "{cond_id}"
  condicion_nombre: "{term}"
  concepto_id: "{main_sign.get('concepto', 'HM:0000')}"
  concepto_nombre: "{concept_termino}"{sens_line}{spec_line}
  lr_positivo: {lr_pos if lr_pos is not None else 'null'}
  lr_negativo: {lr_neg if lr_neg is not None else 'null'}
  poblacion: "{poblacion}"
  referencia_id: "pmid:{pmid}"
  referencia_cita: "{citation}"
  doi: "{doi}"
  pmid: "{pmid}"

triada:
  significante: "{significante}"
  significado: "{significado}"
  decision: "{decision_text}"

autoevaluacion:
  - id: "q1"
    pregunta: "¿Cuál es el valor diagnóstico de {concept_termino.lower()} en {term} según la literatura verificada (PMID: {pmid})?"
    opciones:
      - texto: "Aumenta o reduce la probabilidad clínica con un cociente de verosimilitud de {lr_pos_for_q1}, verificado contra la fuente citada."
        correcta: true
        feedback: "¡Correcto! El cociente proviene de la fuente citada, no de una estimación genérica."
      - texto: "Descarta en un 100% la patología independientemente de otros signos."
        correcta: false
        feedback: "Incorrecto. En razonamiento bayesiano clínico, ningún signo aislado produce certeza absoluta sin análisis contextual."
      - texto: "Carece de valor discriminativo en la exploración."
        correcta: false
        feedback: "{q1_wrong_feedback}"

  - id: "q2"
    pregunta: "En la toma de decisiones clínicas ante {term}, ¿cuál es el paso de confirmación o cribado más adecuado?"
    opciones:
      - texto: "Integrar el rendimiento de la exploración física con la estimación pre-test y solicitar pruebas dirigidas según estratificación de riesgo."
        correcta: true
        feedback: "¡Exacto! La medicina basada en evidencia exige combinar la semiología con escalas diagnósticas y estudios complementarios pertinentes."
      - texto: "Indicar tratamiento invasivo inmediato sin evaluar diagnósticos diferenciales."
        correcta: false
        feedback: "Incorrecto. Se deben descartar patologías concomitantes o secundarias."
---

## Introducción y Relevancia Clínica

El abordaje diagnóstico de **{term}** ({term_en}) requiere un examen clínico estructurado capaz de discriminar rápidamente la probabilidad de la enfermedad frente a otros síndromes clínicos frecuentes.

> **¿Qué es un cociente de verosimilitud (LR)?** Indica cuánto cambia la probabilidad de una enfermedad cuando un hallazgo está presente (LR+) o ausente (LR-). Como regla práctica (McGee S. *Simplifying likelihood ratios*. J Gen Intern Med. 2002), un LR+ ≥ 10 o un LR- ≤ 0.1 suele bastar por sí solo para confirmar o descartar; valores entre 0.5 y 2 apenas cambian la sospecha clínica.

---

## Semiología y Rendimiento Diagnóstico

El hallazgo con mejor rendimiento documentado para **{term}** es **{concept_termino}**. La literatura médica basada en evidencia cuantitativa describe los siguientes parámetros:

{sens_bullet}{spec_bullet}{lr_pos_bullet}{lr_neg_bullet}
---

## Evidencia Cuantitativa y Fuentes

- **Hallazgo evaluado:** {concept_termino}
{sens_bullet}{spec_bullet}{lr_pos_bullet}{lr_neg_bullet}- **Población evaluada:** {poblacion}.
- **Cita principal:** {citation} [PMID: {pmid}]

---

## Conclusión Semiótica

{decision_text}
"""
    return content, slug, None


def run_build_pipeline():
    """Ejecuta el script de construcción del blog."""
    print("\n--- Ejecutando motor de build:blog ---")
    cmd = ["node", str(ROOT_DIR / "tools" / "build-blog.mjs")]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(res.stdout)
    if res.returncode != 0:
        print("[!] Error en build:blog:")
        print(res.stderr)


def main():
    parser = argparse.ArgumentParser(description="Motor de Generación de Temas Clínicos para MedSemiotics")
    parser.add_argument("--list", action="store_true", help="Listar condiciones disponibles en medsemiotics-db")
    parser.add_argument("--condition", type=str, help="ID o nombre de condición a generar (ej. HM6011)")
    parser.add_argument("--sync-all", action="store_true", help="Generar todos los temas faltantes de medsemiotics-db")
    args = parser.parse_args()

    if not POSTS_DIR.exists():
        POSTS_DIR.mkdir(parents=True, exist_ok=True)

    if args.list:
        print("\n=== Condiciones Registradas en medsemiotics-db ===")
        conds = list_remote_conditions()
        for i, c in enumerate(conds, 1):
            print(f" {i:02d}. {c}")
        print(f"\nTotal: {len(conds)} condiciones.")
        return

    if args.condition:
        print(f"\n[+] Descargando y procesando: {args.condition}...")
        cond_data, filename = fetch_condition_yaml(args.condition)
        content, slug, motivo = create_post_markdown(cond_data, filename)

        if content is None:
            print(f"[!] No se generó post para {args.condition}: {motivo}")
            return

        out_path = POSTS_DIR / f"{filename.replace('.yaml', '')}.md"
        out_path.write_text(content, encoding="utf-8")
        print(f"✓ Post generado exitosamente en: posts/{out_path.name}")
        run_build_pipeline()
        return

    if args.sync_all:
        print("\n[+] Sincronizando todas las condiciones de medsemiotics-db...")
        conds = list_remote_conditions()
        existing_files = [p.name for p in POSTS_DIR.glob("*.md")]

        count = 0
        skipped = []
        for c in conds:
            base_name = c.replace(".yaml", "")
            prefix = base_name.split("-")[0]  # ej. HM6001
            already_covered = any(f.startswith(prefix) for f in existing_files)
            if already_covered:
                print(f"  - Ya cubierto: {base_name}")
                continue
            print(f"  + Generando: {base_name}...")
            try:
                cond_data, filename = fetch_condition_yaml(c)
                content, slug, motivo = create_post_markdown(cond_data, filename)
                if content is None:
                    print(f"    [!] Omitido: {motivo}")
                    skipped.append((base_name, motivo))
                    continue
                out_path = POSTS_DIR / f"{base_name}.md"
                out_path.write_text(content, encoding="utf-8")
                count += 1
            except Exception as e:
                print(f"    [!] Error al generar {c}: {e}")

        print(f"\n[OK] Sincronización completada. Se generaron {count} nuevos temas.")
        if skipped:
            print(f"[i] {len(skipped)} condición(es) omitida(s) por falta de LR verificado:")
            for name, motivo in skipped:
                print(f"    - {name}: {motivo}")
        run_build_pipeline()
        return

    parser.print_help()


if __name__ == "__main__":
    main()
