#!/usr/bin/env python3
"""Sincroniza todas las condiciones de medsemiotics-db con el blog.

Los registros YAML son la única fuente clínica. Los Markdown y JSON son
derivados; se preservan los slugs publicados, no afirmaciones independientes.
Sin LR medidos se publica un tema cualitativo, nunca cifras de sustitución.
"""

import argparse
from datetime import date
import hashlib
import json
import os
import re
import subprocess
import sys
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REPO = "alcyedmundo281/medsemiotics-db"
SITE = "https://powersemiotics.com/medsemiotics/"
POSTS = ROOT / "posts"
STATES = {
    "medido": "LR medido",
    "no_medido": "LR no medido",
    "no_medible": "LR no medible",
    "sin_efecto": "Sin efecto discriminativo",
}
TERMS = {**STATES, "manifestacion": "Manifestación", "prueba_sensible": "Prueba sensible",
         "prueba_especifica": "Prueba específica", "apoyo": "Apoyo diagnóstico",
         "imagen": "Imagen", "apoya": "Apoya", "bandera_roja": "Signo de alarma",
         "consenso_con_afirmacion": "Afirmación respaldada por consenso",
         "consenso_de_lista": "Listado de consenso", "discriminacion_medida": "Discriminación medida"}
CATEGORIES = {
    "hepatitis": ("gastroenterologia", "Gastroenterología"),
    "intestino": ("gastroenterologia", "Gastroenterología"),
    "meningitis": ("neurologia", "Neurología"),
    "parkinson": ("neurologia", "Neurología"),
    "alcohol": ("psiquiatria", "Psiquiatría"),
}
LABELS = {
    "termino_en": "Nombre en inglés", "sinonimos": "Sinónimos",
    "codigos": "Códigos", "probabilidad_base": "Probabilidad basal",
    "factores_riesgo": "Factores de riesgo", "signos": "Hallazgos clínicos",
    "signos_de_alarma": "Signos de alarma", "nucleo": "Núcleo diagnóstico",
    "balance": "Balance de criterios", "reglas": "Reglas clínicas",
    "modificadores": "Modificadores", "escalas": "Escalas",
    "notas_de_uso": "Notas de uso", "conclusion_de_la_fuente": "Conclusión de la fuente",
    "pendiente": "Aspectos pendientes de documentación", "discrepancias": "Discrepancias entre fuentes",
    "no_emitidos": "Relaciones no incorporadas y sus motivos",
    "lr_positivo": "LR positivo", "lr_negativo": "LR negativo",
    "ic95": "IC del 95 %", "ref": "Referencia", "rango": "Rango documentado",
    "valor": "Valor", "estado_lr": "Estado del LR", "concepto": "Hallazgo",
    "poblacion": "Población", "umbral": "Umbral", "decision": "Decisión",
    "advertencia": "Advertencia", "motivo": "Motivo", "nota": "Nota",
    "sensibilidad": "Sensibilidad", "especificidad": "Especificidad",
}


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Medsemiotics-Sync/2"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def git(directory, *args):
    return subprocess.check_output(
        ["git", "-C", str(directory), *args], text=True, encoding="utf-8"
    ).strip()


class Source:
    def __init__(self, directory=None, ref="main"):
        self.directory = Path(directory).resolve() if directory else None
        self.cache = {}
        if self.directory:
            self.revision = git(self.directory, "rev-parse", "HEAD")
            self.paths = [
                p.relative_to(self.directory).as_posix()
                for folder in ("condiciones", "conceptos", "referencias")
                for p in (self.directory / folder).glob("*.yaml")
            ]
        else:
            commit = json.loads(fetch(f"https://api.github.com/repos/{REPO}/commits/{ref}"))
            self.revision = commit["sha"]
            tree = json.loads(fetch(
                f"https://api.github.com/repos/{REPO}/git/trees/{self.revision}?recursive=1"
            ))
            if tree.get("truncated"):
                raise ValueError("El inventario remoto está truncado.")
            self.paths = [p["path"] for p in tree["tree"] if p["path"].endswith(".yaml")]
        self.paths.sort()

    def read(self, path):
        if path not in self.cache:
            raw = ((self.directory / path).read_text(encoding="utf-8") if self.directory else
                   fetch(f"https://raw.githubusercontent.com/{REPO}/{self.revision}/{path}"))
            raw = raw.replace("\r\n", "\n")
            self.cache[path] = (yaml.safe_load(raw), hashlib.sha256(raw.encode()).hexdigest())
        return self.cache[path][0]

    def resolve(self, identifier):
        if identifier.startswith("HM:"):
            prefixes = tuple(folder + "/" + identifier.replace(":", "") + "-"
                             for folder in ("conceptos", "condiciones"))
            matches = [p for p in self.paths if p.startswith(prefixes)]
        elif identifier.startswith("pmid:"):
            matches = [p for p in self.paths if p == "referencias/" +
                       identifier.replace(":", "-") + ".yaml"]
        else:
            raise ValueError(f"Identificador no soportado: {identifier}")
        if len(matches) != 1:
            raise ValueError(f"Referencia no resoluble o ambigua: {identifier}")
        data = self.read(matches[0])
        if data.get("id") != identifier:
            raise ValueError(f"ID diferente al archivo: {identifier}")
        return matches[0], data


def identifiers(value):
    """Incluye conceptos de reglas y referencias de rangos, no solo del signo principal."""
    if isinstance(value, dict):
        for item in value.values():
            yield from identifiers(item)
    elif isinstance(value, list):
        for item in value:
            yield from identifiers(item)
    elif isinstance(value, str):
        yield from re.findall(r"\b(?:HM:\d+|pmid:\d+)\b", value)


def scalar(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value >= 0


def slugify(value):
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def url_slug(url):
    parsed = urllib.parse.urlparse(url or "")
    if parsed.scheme != "https" or parsed.netloc != "powersemiotics.com":
        return None
    if parsed.path != "/medsemiotics/post.html":
        return None
    slug = urllib.parse.parse_qs(parsed.query).get("slug", [None])[0]
    return slug if slug and re.fullmatch(r"[a-z0-9-]+", slug) else None


def read_posts(root=POSTS):
    result = {}
    for path in sorted(root.glob("*.md")):
        parts = re.split(r"^---\s*$", path.read_text(encoding="utf-8"), maxsplit=2, flags=re.M)
        if len(parts) != 3:
            raise ValueError(f"Frontmatter ausente: {path}")
        data = yaml.safe_load(parts[1])
        cid = data.get("grounding", {}).get("condicion_id")
        if not cid or cid in result:
            raise ValueError(f"Condición ausente o duplicada: {path}")
        result[cid] = (path, data)
    slugs = [d["slug"] for _, d in result.values()]
    if len(slugs) != len(set(slugs)):
        raise ValueError("Hay slugs duplicados.")
    return result


def render_value(value, concepts):
    """Prosa de presentación sobre datos literales; no calcula LR ni completa vacíos."""
    if value is None:
        return "No documentado."
    if isinstance(value, dict):
        return "; ".join(f"{LABELS.get(k, k.replace('_', ' ').capitalize())}: "
                         f"{render_value(v, concepts)}" for k, v in value.items())
    if isinstance(value, list):
        return " / ".join(render_value(v, concepts) for v in value) if value else "No documentado."
    if isinstance(value, bool):
        return "Sí" if value else "No"
    text = str(value).strip()
    if text in concepts:
        return f"{concepts[text]['termino']} ({text})"
    return TERMS.get(text, text)


def make_post(source, condition_path, previous=None):
    c = source.read(condition_path)
    if not re.fullmatch(r"HM:\d+", c.get("id", "")):
        raise ValueError(f"ID de condición inválido: {condition_path}")
    cid = c["id"]
    files = {condition_path}
    concepts, references = {}, {}
    # Resolve clinical IDs anywhere, including criteria, warnings and pending material.
    for identifier in sorted(set(identifiers(c)) - {cid}):
        path, data = source.resolve(identifier)
        files.add(path)
        (concepts if identifier.startswith("HM:") else references)[identifier] = data
    # References embedded in concept definitions must also be tracked.
    for concept in concepts.values():
        if concept.get("tipo") != "concepto":
            continue
        for identifier in set(identifiers(concept)):
            if identifier.startswith("pmid:"):
                path, ref = source.resolve(identifier)
                files.add(path)
                references[identifier] = ref
    for rid, ref in references.items():
        verification = ref.get("verificacion", {})
        if not verification.get("pubmed") or verification.get("retractado"):
            raise ValueError(f"Referencia sin verificación o retractada: {rid}")

    signs = c.get("signos", [])
    for sign in signs:
        for key in ("lr_positivo", "lr_negativo"):
            block = sign.get(key)
            if block and (sign.get("estado_lr") != "medido" or block.get("ref") not in references):
                raise ValueError(f"{cid}: {key} sin estado medido y referencia resoluble.")
    measured = [s for s in signs if s.get("estado_lr") == "medido"]
    numeric = [s for s in measured if any(
        scalar((s.get(k) or {}).get("valor")) for k in ("lr_positivo", "lr_negativo"))]
    # Keep a published clinical focus only when the source still supports its LR.
    old = previous or {}
    main = next((s for s in numeric if s["concepto"] ==
                 old.get("grounding", {}).get("concepto_id")), None)
    main = main or next(iter(numeric or measured or signs), {})
    concept = concepts.get(main.get("concepto"), {})
    pos, neg = main.get("lr_positivo") or {}, main.get("lr_negativo") or {}
    main_ref = pos.get("ref") or neg.get("ref") or next(iter(references), None)
    ref = references.get(main_ref, {})
    ref_ids = ref.get("identificadores") or {}
    citation = " ".join(str(v) for v in [
        ", ".join(ref.get("autores", [])), ref.get("titulo"), ref.get("publicacion"), ref.get("anio")
    ] if v)
    slug = old.get("slug") or url_slug(c.get("url")) or slugify(c["termino"]) + "-precision-semiotica"
    if not re.fullmatch(r"[a-z0-9-]+", slug):
        raise ValueError(f"Slug inválido: {slug}")
    category, label = next((v for k, v in CATEGORIES.items() if k in c["termino"].lower()),
                           ("medicina_interna", "Medicina Interna"))
    category, label = old.get("category", category), old.get("category_label", label)
    g = {
        "condicion_id": cid, "condicion_nombre": c["termino"],
        "concepto_id": main.get("concepto"), "concepto_nombre": concept.get("termino"),
        "estado_lr": main.get("estado_lr"), "lr_positivo": pos.get("valor"),
        "lr_negativo": neg.get("valor"), "lr_positivo_rango": pos.get("rango"),
        "lr_negativo_rango": neg.get("rango"), "poblacion": main.get("poblacion"),
        "referencia_id": main_ref, "referencia_cita": citation or None,
        "pmid": str(ref_ids["pmid"]) if ref_ids.get("pmid") else None,
        "doi": ref_ids.get("doi"),
    }
    for field in ("sensibilidad", "especificidad"):
        if field in main:
            g[field] = main[field]
    t = {
        "significante": concept.get("significante") or concept.get("termino") or c["termino"],
        "significado": concept.get("significado") or
                      "El mecanismo fisiopatológico no está documentado en esta fuente.",
        "decision": main.get("decision") or
                    c.get("conclusion_de_la_fuente") or
                    "La fuente no documenta una decisión específica para este hallazgo.",
    }
    quiz = []
    chosen = ([main] + [s for s in signs if s is not main])[:2] if main else []
    for number, sign in enumerate(chosen, 1):
        sign_concept = concepts[sign["concepto"]]
        blocks = [("LR positivo", sign.get("lr_positivo") or {}),
                  ("LR negativo", sign.get("lr_negativo") or {})]
        field, block = next(((k, b) for k, b in blocks if scalar(b.get("valor"))), (None, {}))
        if field:
            answer = f"{field}: {block['valor']}."
            question = f"¿Qué cociente registra la fuente para {sign_concept['termino']} en {c['termino']}?"
            wrong = "La fuente no registra ningún cociente medido para este hallazgo."
        else:
            answer = render_value(sign.get("estado_lr"), concepts)
            question = f"¿Cómo está documentado el LR de {sign_concept['termino']} en {c['termino']}?"
            wrong = "Hay una estimación numérica única disponible para calcular la probabilidad posterior."
            if sign.get("estado_lr") == "medido":
                answer = "La fuente registra un rango, no una estimación numérica única."
                block = next((b for _, b in blocks if b.get("rango")), {})
        rid = block.get("ref")
        qref = references.get(rid, {})
        qids = qref.get("identificadores", {})
        options = [
            {"texto": answer, "correcta": True, "feedback": f"Registro {cid}: {answer}"},
            {"texto": wrong, "correcta": False, "feedback": f"El registro documenta: {answer}"},
        ]
        if number % 2 == 0:
            options.reverse()
        quiz.append({"id": f"q{number}", "pregunta": question, "concepto_id": sign["concepto"],
                     "referencia_id": rid, "pmid": str(qids["pmid"]) if qids.get("pmid") else None,
                     "doi": qids.get("doi"), "opciones": options})
    source_data = {
        "repositorio": REPO, "revision": source.revision,
        "condicion": condition_path,
        "archivos": {path: source.cache[path][1] for path in sorted(files)},
    }
    meta = {
        "id": old.get("id", cid.replace(":", "") + "-01"), "slug": slug,
        "title": f"{c['termino']}: hallazgos y evidencia clínica",
        "subtitle": ("Hallazgos, cocientes documentados y límites de la evidencia." if measured else
                     "Hallazgos y criterios clínicos sin cocientes de verosimilitud medidos."),
        "date": str(old.get("date") or date.today().isoformat()),
        "author": old.get("author", "Dr. Alcy Torres"),
        "category": old.get("category", category),
        "category_label": old.get("category_label", label),
        "tags": sorted(set([category, slugify(c["termino"]), "semiologia"] +
                          (["criterios"] if c.get("reglas") or c.get("nucleo") or c.get("escalas") else []))),
        "reading_time": "8 min", "difficulty": old.get("difficulty", "Intermedio"),
        "fuente": source_data, "grounding": g, "triada": t,
        "evidencia": signs, "autoevaluacion": quiz,
    }
    body = [f"# {c['termino']}", meta["subtitle"]]
    # Each source field remains visible, including limitations and unresolved discrepancies.
    excluded = {"id", "tipo", "clase", "termino", "url", "procedencia", "medios"}
    for key, value in c.items():
        if key in excluded or value in (None, [], {}):
            continue
        body.append("## " + LABELS.get(key, key.replace("_", " ").capitalize()))
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict) and item.get("concepto"):
                    body.append("### " + render_value(item["concepto"], concepts))
                    definition = concepts[item["concepto"]]
                    for field in ("significante", "significado", "umbrales", "falsos_positivos"):
                        if definition.get(field):
                            body.append("**" + field.replace("_", " ").capitalize() + ":** " +
                                        render_value(definition[field], concepts))
                    body.extend("**" + LABELS.get(k, k.replace("_", " ").capitalize()) + ":** " +
                                render_value(v, concepts) for k, v in item.items() if k != "concepto")
                else:
                    body.append(render_value(item, concepts))
        else:
            body.append(render_value(value, concepts))
    body.append("## Referencias y procedencia")
    for rid, reference in references.items():
        ids = reference.get("identificadores", {})
        body.append(f"**{rid}:** {reference['titulo']}. "
                    f"{reference.get('publicacion', '')}, {reference.get('anio', '')}. "
                    f"DOI: {ids.get('doi', 'no documentado')}.")
    body.append(f"Fuente clínica: medsemiotics-db, condición {cid}.")
    text = "---\n" + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, width=1000) + \
           "---\n\n" + "\n\n".join(body) + "\n"
    return text, meta


def sync(source, check=False, condition=None, write_backlinks=False):
    previous = read_posts()
    paths = [p for p in source.paths if p.startswith("condiciones/")]
    if condition:
        key = condition.replace(":", "")
        paths = [p for p in paths if Path(p).name == condition or Path(p).name.split("-")[0] == key]
        if len(paths) != 1:
            raise ValueError(f"Condición no encontrada o ambigua: {condition}")
    planned = []
    for path in paths:
        cid = source.read(path)["id"]
        oldpath, old = previous.get(cid, (POSTS / (Path(path).stem + ".md"), None))
        text, meta = make_post(source, path, old)
        planned.append((oldpath, text, meta))
    if not condition:
        orphaned = set(previous) - {m["grounding"]["condicion_id"] for _, _, m in planned}
        if orphaned:
            raise ValueError(f"Artículos sin condición en la fuente: {sorted(orphaned)}")
    slugs = [m["slug"] for _, _, m in planned]
    if len(slugs) != len(set(slugs)):
        raise ValueError("La fuente propone URLs duplicadas.")
    changed = [p for p, text, _ in planned if not p.exists() or p.read_text(encoding="utf-8") != text]
    links = [{"condicion_id": m["grounding"]["condicion_id"],
              "archivo": m["fuente"]["condicion"], "slug": m["slug"],
              "url": SITE + "post.html?slug=" + m["slug"]} for _, _, m in planned]
    different_urls = [link for link in links if source.read(link["archivo"]).get("url") != link["url"]]
    if check:
        for p in changed:
            print("DESACTUALIZADO:", p.relative_to(ROOT))
        for link in different_urls:
            print("URL PENDIENTE:", link["condicion_id"], link["url"])
        if changed or different_urls:
            raise ValueError("La sincronización no está al día.")
        subprocess.run(["node", str(ROOT / "tools/build-blog.mjs"), "--check"], cwd=ROOT, check=True)
    else:
        POSTS.mkdir(exist_ok=True)
        for p, text, _ in planned:
            if p in changed:
                p.write_text(text, encoding="utf-8", newline="\n")
        subprocess.run(["node", str(ROOT / "tools/build-blog.mjs")], cwd=ROOT, check=True)
    if write_backlinks:
        if not source.directory:
            raise ValueError("--write-backlinks requiere --db-dir.")
        # A successful HTTP response for post.html is insufficient: verify the actual JSON.
        for link in links:
            published = json.loads(fetch(SITE + "assets/data/posts/" + link["slug"] + ".json"))
            if (published.get("slug") != link["slug"] or
                    published.get("grounding", {}).get("condicion_id") != link["condicion_id"]):
                raise ValueError(f"Artículo aún no publicado: {link['url']}")
        for link in different_urls:
            p = source.directory / link["archivo"]
            raw = p.read_bytes().decode("utf-8")
            newline = "\r\n" if "\r\n" in raw else "\n"
            replacement = 'url: "' + link["url"] + '"'
            if re.search(r"^url:", raw, re.M):
                raw = re.sub(r"^url:[^\r\n]*", lambda _: replacement, raw, flags=re.M)
            else:
                raw = raw.rstrip("\r\n") + newline + replacement + newline
            p.write_bytes(raw.encode("utf-8"))
        print(f"Publicación verificada: {len(links)} artículos; URLs actualizadas: {len(different_urls)}.")
        if different_urls:
            sync(Source(source.directory), condition=condition)
    print(f"Condiciones: {len(paths)}. Artículos: {len(planned)}. Cambios: {len(changed)}.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db-dir", default=os.environ.get("MEDSEMIOTICS_DB_DIR"),
                        help="Checkout local de medsemiotics-db; se lee sin modificar.")
    parser.add_argument("--ref", default="main", help="Ref remota que se fija a un commit al iniciar.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--list", action="store_true")
    group.add_argument("--condition")
    group.add_argument("--sync-all", action="store_true")
    group.add_argument("--check", action="store_true")
    parser.add_argument("--write-backlinks", action="store_true",
                        help="Verifica la publicación y actualiza únicamente url en el checkout fuente.")
    args = parser.parse_args()
    if args.write_backlinks and (not args.db_dir or args.check or args.list):
        parser.error("--write-backlinks requiere --db-dir y --sync-all o --condition.")
    source = Source(args.db_dir, args.ref)
    if args.list:
        print("\n".join(p for p in source.paths if p.startswith("condiciones/")))
        return
    sync(source, args.check, args.condition, args.write_backlinks)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
