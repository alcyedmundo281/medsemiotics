import hashlib
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("topic_sync", Path(__file__).parents[1] / "generate_topic.py")
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class Source:
    revision = "abc123"

    def __init__(self, state="no_medido", block=None):
        self.c = {"id": "HM:9999", "tipo": "condicion", "termino": "Tema de prueba",
                  "url": sync.SITE + "post.html?slug=tema-publicado",
                  "signos": [{"concepto": "HM:0001", "estado_lr": state}]}
        if block:
            self.c["signos"][0]["lr_positivo"] = block
        self.records = {
            "CITATION.cff": {"title": "Fuente de prueba", "doi": "10.test/dataset"},
            "condiciones/HM9999-tema.yaml": self.c,
            "conceptos/HM0001-signo.yaml": {"id": "HM:0001", "tipo": "concepto", "termino": "Signo"},
            "referencias/pmid-123.yaml": {"id": "pmid:123", "titulo": "Fuente",
                "identificadores": {"pmid": 123, "doi": "10.test/fuente"},
                "verificacion": {"pubmed": True, "retractado": False}},
        }
        self.cache = {}

    def read(self, path):
        record = self.records[path]
        self.cache[path] = (record, hashlib.sha256(repr(record).encode()).hexdigest())
        return record

    def resolve(self, identifier):
        for path, data in self.records.items():
            if data.get("id") == identifier:
                return path, self.read(path)
        for path, data in self.records.items():
            if path.startswith("referencias/"):
                verif = data.get("verificacion") or {}
                if verif.get("errata_pmid") == identifier:
                    errata_data = {
                        "id": identifier, "tipo": "errata",
                        "titulo": verif.get("errata_corrige") or f"Erratum a {data.get('titulo')}",
                        "publicacion": data.get("publicacion", ""),
                        "anio": data.get("anio", ""),
                        "identificadores": {"pmid": identifier.split(":")[1]},
                        "verificacion": {"pubmed": True, "retractado": False},
                        "errata_de": data.get("id"),
                    }
                    return path, errata_data
        raise ValueError("No resoluble: " + identifier)


class SynchronizationTests(unittest.TestCase):
    def make(self, source, previous=None):
        return sync.make_post(source, "condiciones/HM9999-tema.yaml", previous)

    def test_qualitative_conditions_are_published_without_lr_or_fake_reference(self):
        for state in ("no_medido", "no_medible", "sin_efecto"):
            text, post = self.make(Source(state))
            self.assertEqual(post["slug"], "tema-publicado")
            self.assertIsNone(post["grounding"]["lr_positivo"])
            self.assertIsNone(post["grounding"]["lr_negativo"])
            self.assertIsNone(post["grounding"]["pmid"])
            self.assertTrue(post["autoevaluacion"])
            self.assertIn(sync.STATES[state], text)

    def test_range_is_preserved_not_converted_to_an_estimate(self):
        source = Source("medido", {"rango": [7.1, 250], "ref": "pmid:123"})
        text, post = self.make(source)
        self.assertIsNone(post["grounding"]["lr_positivo"])
        self.assertEqual(post["grounding"]["lr_positivo_rango"], [7.1, 250])
        self.assertIn("Rango documentado: 7.1 / 250", text)

    def test_source_updates_existing_post_preserving_its_url(self):
        source = Source("medido", {"valor": 6.5, "ref": "pmid:123"})
        _, post = self.make(source)
        post["slug"] = "url-ya-publicada"
        source.c["signos"][0]["lr_positivo"]["valor"] = 8
        text, updated = self.make(source, post)
        self.assertEqual(updated["slug"], "url-ya-publicada")
        self.assertEqual(updated["grounding"]["lr_positivo"], 8)
        self.assertIn("LR positivo: 8.", text)
        self.assertNotIn("LR positivo: 6.5.", text)
        self.assertEqual(self.make(source, updated)[0], text)

    def test_reference_failure_stops_generation(self):
        source = Source("medido", {"valor": 6.5, "ref": "pmid:999"})
        with self.assertRaises(ValueError):
            self.make(source)

    def test_dataset_doi_and_study_doi_remain_separate(self):
        _, post = self.make(Source("medido", {"valor": 6.5, "ref": "pmid:123"}))
        self.assertEqual(post["fuente"]["doi"], "10.test/dataset")
        self.assertEqual(post["grounding"]["doi"], "10.test/fuente")

    def test_unmeasured_sign_cannot_carry_numeric_lr(self):
        with self.assertRaises(ValueError):
            self.make(Source("no_medible", {"valor": 7.5, "ref": "pmid:123"}))

    def test_questions_preserve_interval_population_and_reference(self):
        source = Source("medido", {"valor": 6.5, "ic95": [3.9, 11],
                                   "umbral": "Prueba >= 8", "ref": "pmid:123"})
        source.c["signos"][0]["poblacion"] = "Población de la fuente"
        source.c["signos"][0]["decision"] = "Decisión descrita por la fuente."
        _, post = self.make(source)
        q = post["autoevaluacion"][0]
        self.assertEqual(len(q["opciones"]), 3)
        self.assertEqual(sum(o["correcta"] for o in q["opciones"]), 1)
        answer = next(o for o in q["opciones"] if o["correcta"])
        self.assertIn("3.9 a 11", answer["feedback"])
        self.assertIn("Población de la fuente", q["pregunta"])
        self.assertIn("Decisión descrita por la fuente.", answer["feedback"])
        self.assertEqual(q["evidencia"]["dato"], source.c["signos"][0]["lr_positivo"])
        self.assertEqual(q["doi"], "10.test/fuente")
        self.assertEqual(q["fuente_doi"], "10.test/dataset")

    def test_range_question_never_treats_an_endpoint_as_a_point_estimate(self):
        _, post = self.make(Source("medido", {"rango": [7.1, 250], "ref": "pmid:123"}))
        q = post["autoevaluacion"][0]
        answer = next(o for o in q["opciones"] if o["correcta"])
        self.assertIn("7.1 a 250", answer["texto"])
        self.assertEqual(q["evidencia"]["dato"]["rango"], [7.1, 250])
        self.assertTrue(all("límite" in o["feedback"] for o in q["opciones"] if not o["correcta"]))

    def test_negative_lr_question_remains_negative(self):
        source = Source("medido")
        source.c["signos"][0]["lr_negativo"] = {"valor": 0.3, "ref": "pmid:123"}
        _, post = self.make(source)
        q = post["autoevaluacion"][0]
        answer = next(o for o in q["opciones"] if o["correcta"])
        self.assertEqual(answer["texto"], "LR negativo: 0.3.")
        self.assertEqual(q["evidencia"]["campo"], "lr_negativo")

    def test_errata_reference_in_notes_resolves_and_generates_post(self):
        source = Source("medido", {"valor": 6.5, "ref": "pmid:123"})
        source.records["referencias/pmid-123.yaml"]["verificacion"]["errata_pmid"] = "pmid:456"
        source.records["referencias/pmid-123.yaml"]["verificacion"]["errata_corrige"] = "Corrección de prueba"
        source.c["notas_de_uso"] = ["Tiene errata cotejada (pmid:456)."]
        text, post = self.make(source)
        self.assertIn("pmid:456", text)
        self.assertIn("Corrección de prueba", text)

    def test_real_source_resolves_errata_from_parent_reference(self):
        source = sync.Source.__new__(sync.Source)
        source.paths = ["referencias/pmid-100.yaml"]
        source.cache = {
            "referencias/pmid-100.yaml": ({
                "id": "pmid:100",
                "titulo": "Estudio principal",
                "publicacion": "JAMA",
                "anio": 2024,
                "verificacion": {
                    "pubmed": True,
                    "errata": "JAMA 2025. doi: 10.1001/errata.",
                    "errata_pmid": "pmid:200",
                    "errata_corrige": "Corrección al estudio principal",
                    "errata_verificada": True,
                },
            }, "hash123")
        }
        path, errata = source.resolve("pmid:200")
        self.assertEqual(path, "referencias/pmid-100.yaml")
        self.assertEqual(errata["id"], "pmid:200")
        self.assertEqual(errata["tipo"], "errata")
        self.assertEqual(errata["titulo"], "Corrección al estudio principal")
        self.assertEqual(errata["identificadores"]["doi"], "10.1001/errata")
        self.assertTrue(errata["verificacion"]["pubmed"])
        self.assertFalse(errata["verificacion"]["retractado"])


class ProsaTests(unittest.TestCase):
    """Los IDs HM: incrustados en la prosa de la base se leen como nombres."""

    conceptos = {"HM:0745": {"termino": "Hiperbilirrubinemia"},
                 "HM:3184": {"termino": "Bazo palpable"},
                 "HM:3060": {"termino": "Hematoquecia"},
                 "HM:9001": {"termino": "Trauma Screening Questionnaire positivo"}}

    def prosa(self, texto):
        return sync.prosa(texto, self.conceptos)

    def test_parentesis_redundante_se_elimina(self):
        self.assertEqual(self.prosa("por hiperbilirrubinemia (HM:0745), no conjugada"),
                         "por hiperbilirrubinemia, no conjugada")

    def test_id_se_sustituye_por_el_nombre(self):
        self.assertEqual(self.prosa("o percusión mate (HM:3184)."), "o percusión mate (bazo palpable).")
        self.assertEqual(self.prosa("se acuñó HM:3060 «Hematoquecia», que"), "se acuñó «Hematoquecia», que")
        self.assertEqual(self.prosa("Con él, HM:9001 declara"),
                         "Con él, Trauma Screening Questionnaire positivo declara")

    def test_id_sin_registro_no_se_inventa(self):
        self.assertEqual(self.prosa("ver HM:4040"), "ver HM:4040")


if __name__ == "__main__":
    unittest.main()
