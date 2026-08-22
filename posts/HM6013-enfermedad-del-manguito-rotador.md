---
id: "HM6013-01"
slug: "enfermedad-del-manguito-rotador-precision-semiotica"
title: "Enfermedad del manguito rotador: Precisión diagnóstica y rendimiento de los hallazgos semiológicos"
subtitle: "Análisis bayesiano de arco doloroso y su impacto en la toma de decisiones clínicas."
date: "2026-08-21"
author: "Dr. Alcy Torres"
category: "traumatologia"
category_label: "Traumatología y Medicina Deportiva"
tags: ["traumatologia", "enfermedad-del-manguito-rotador", "semiologia", "evidencia"]
reading_time: "6 min"
difficulty: "Intermedio"
grounding:
  condicion_id: "HM:6013"
  condicion_nombre: "Enfermedad del manguito rotador"
  concepto_id: "HM:3055"
  concepto_nombre: "Arco doloroso"
  lr_positivo: 3.7
  lr_negativo: 0.36
  poblacion: "pacientes derivados a especialista por dolor de hombro, en los estudios de calidad nivel 1-2"
  referencia_id: "pmid:23982370"
  referencia_cita: "Hermans J, Luime JJ, Meuffels DE et al.. Does this patient with shoulder pain have rotator cuff disease?: The Rational Clinical Examination systematic review. JAMA. 2013."
  doi: "10.1001/jama.2013.276187"
  pmid: "23982370"

triada:
  significante: "Arco doloroso, evaluado en: pacientes derivados a especialista por dolor de hombro, en los estudios de calidad nivel 1-2."
  significado: "La fuente no describe el mecanismo fisiopatológico de este hallazgo; su valor aquí es estadístico (cociente de verosimilitud), no explicativo."
  decision: "Arco doloroso — la única prueba de provocación de dolor con cociente positivo por encima de 2, y la que mejor descarta cuando es normal"

autoevaluacion:
  - id: "q1"
    pregunta: "¿Cuál es el valor diagnóstico de arco doloroso en Enfermedad del manguito rotador según la literatura verificada (PMID: 23982370)?"
    opciones:
      - texto: "Aumenta o reduce la probabilidad clínica con un cociente de verosimilitud de 3.7, verificado contra la fuente citada."
        correcta: true
        feedback: "¡Correcto! El cociente proviene de la fuente citada, no de una estimación genérica."
      - texto: "Descarta en un 100% la patología independientemente de otros signos."
        correcta: false
        feedback: "Incorrecto. En razonamiento bayesiano clínico, ningún signo aislado produce certeza absoluta sin análisis contextual."
      - texto: "Carece de valor discriminativo en la exploración."
        correcta: false
        feedback: "Incorrecto. El hallazgo sí tiene valor discriminativo, documentado mediante su cociente de verosimilitud verificado."

  - id: "q2"
    pregunta: "En la toma de decisiones clínicas ante Enfermedad del manguito rotador, ¿cuál es el paso de confirmación o cribado más adecuado?"
    opciones:
      - texto: "Integrar el rendimiento de la exploración física con la estimación pre-test y solicitar pruebas dirigidas según estratificación de riesgo."
        correcta: true
        feedback: "¡Exacto! La medicina basada en evidencia exige combinar la semiología con escalas diagnósticas y estudios complementarios pertinentes."
      - texto: "Indicar tratamiento invasivo inmediato sin evaluar diagnósticos diferenciales."
        correcta: false
        feedback: "Incorrecto. Se deben descartar patologías concomitantes o secundarias."
---

## Introducción y Relevancia Clínica

El abordaje diagnóstico de **Enfermedad del manguito rotador** (Rotator cuff disease) requiere un examen clínico estructurado capaz de discriminar rápidamente la probabilidad de la enfermedad frente a otros síndromes clínicos frecuentes.

> **¿Qué es un cociente de verosimilitud (LR)?** Indica cuánto cambia la probabilidad de una enfermedad cuando un hallazgo está presente (LR+) o ausente (LR-). Como regla práctica (McGee S. *Simplifying likelihood ratios*. J Gen Intern Med. 2002), un LR+ ≥ 10 o un LR- ≤ 0.1 suele bastar por sí solo para confirmar o descartar; valores entre 0.5 y 2 apenas cambian la sospecha clínica.

---

## Semiología y Rendimiento Diagnóstico

El hallazgo con mejor rendimiento documentado para **Enfermedad del manguito rotador** es **Arco doloroso**. La literatura médica basada en evidencia cuantitativa describe los siguientes parámetros:

- **Cociente de Verosimilitud Positivo (LR+):** 3.7 — cambia poco la probabilidad: evidencia débil
- **Cociente de Verosimilitud Negativo (LR-):** 0.36 — cambia poco la probabilidad

---

## Evidencia Cuantitativa y Fuentes

- **Hallazgo evaluado:** Arco doloroso
- **Cociente de Verosimilitud Positivo (LR+):** 3.7 — cambia poco la probabilidad: evidencia débil
- **Cociente de Verosimilitud Negativo (LR-):** 0.36 — cambia poco la probabilidad
- **Población evaluada:** pacientes derivados a especialista por dolor de hombro, en los estudios de calidad nivel 1-2.
- **Cita principal:** Hermans J, Luime JJ, Meuffels DE et al.. Does this patient with shoulder pain have rotator cuff disease?: The Rational Clinical Examination systematic review. JAMA. 2013. [PMID: 23982370]

---

## Conclusión Semiótica

Arco doloroso — la única prueba de provocación de dolor con cociente positivo por encima de 2, y la que mejor descarta cuando es normal
