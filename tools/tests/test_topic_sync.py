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


if __name__ == "__main__":
    unittest.main()
