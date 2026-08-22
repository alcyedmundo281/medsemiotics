---
id: "HM6012-01"
slug: "artrosis-de-cadera-precision-semiotica"
title: "Artrosis de cadera: Precisión diagnóstica y rendimiento de los hallazgos semiológicos"
subtitle: "Análisis bayesiano de dolor posterior de cadera al ponerse en cuclillas y su impacto en la toma de decisiones clínicas."
date: "2026-08-21"
author: "Dr. Alcy Torres"
category: "reumatologia"
category_label: "Reumatología y Traumatología"
tags: ["reumatologia", "artrosis-de-cadera", "semiologia", "evidencia"]
reading_time: "6 min"
difficulty: "Intermedio"
grounding:
  condicion_id: "HM:6012"
  condicion_nombre: "Artrosis de cadera"
  concepto_id: "HM:3041"
  concepto_nombre: "Dolor posterior de cadera al ponerse en cuclillas"
  sensibilidad: 0.24
  especificidad: 0.96
  lr_positivo: 6.1
  lr_negativo: null
  poblacion: "pacientes que consultan en atención primaria por dolor de cadera o inguinal"
  referencia_id: "pmid:31846019"
  referencia_cita: "Metcalfe D, Perry DC, Claireaux HA et al.. Does This Patient Have Hip Osteoarthritis?: The Rational Clinical Examination Systematic Review. JAMA. 2019."
  doi: "10.1001/jama.2019.19413"
  pmid: "31846019"

triada:
  significante: "Dolor posterior de cadera al ponerse en cuclillas, evaluado en: pacientes que consultan en atención primaria por dolor de cadera o inguinal."
  significado: "La fuente no describe el mecanismo fisiopatológico de este hallazgo; su valor aquí es estadístico (cociente de verosimilitud), no explicativo."
  decision: "Dolor posterior de cadera al ponerse en cuclillas — el cociente más alto, pero con intervalo muy ancho: el extremo inferior roza el 1.3, casi irrelevante"

autoevaluacion:
  - id: "q1"
    pregunta: "¿Cuál es el valor diagnóstico de dolor posterior de cadera al ponerse en cuclillas en Artrosis de cadera según la literatura verificada (PMID: 31846019)?"
    opciones:
      - texto: "Aumenta o reduce la probabilidad clínica con un cociente de verosimilitud de 6.1, verificado contra la fuente citada."
        correcta: true
        feedback: "¡Correcto! El cociente proviene de la fuente citada, no de una estimación genérica."
      - texto: "Descarta en un 100% la patología independientemente de otros signos."
        correcta: false
        feedback: "Incorrecto. En razonamiento bayesiano clínico, ningún signo aislado produce certeza absoluta sin análisis contextual."
      - texto: "Carece de valor discriminativo en la exploración."
        correcta: false
        feedback: "Incorrecto. Presenta una especificidad documentada de 96%."

  - id: "q2"
    pregunta: "En la toma de decisiones clínicas ante Artrosis de cadera, ¿cuál es el paso de confirmación o cribado más adecuado?"
    opciones:
      - texto: "Integrar el rendimiento de la exploración física con la estimación pre-test y solicitar pruebas dirigidas según estratificación de riesgo."
        correcta: true
        feedback: "¡Exacto! La medicina basada en evidencia exige combinar la semiología con escalas diagnósticas y estudios complementarios pertinentes."
      - texto: "Indicar tratamiento invasivo inmediato sin evaluar diagnósticos diferenciales."
        correcta: false
        feedback: "Incorrecto. Se deben descartar patologías concomitantes o secundarias."
---

## Introducción y Relevancia Clínica

El abordaje diagnóstico de **Artrosis de cadera** (Hip osteoarthritis) requiere un examen clínico estructurado capaz de discriminar rápidamente la probabilidad de la enfermedad frente a otros síndromes clínicos frecuentes.

> **¿Qué es un cociente de verosimilitud (LR)?** Indica cuánto cambia la probabilidad de una enfermedad cuando un hallazgo está presente (LR+) o ausente (LR-). Como regla práctica (McGee S. *Simplifying likelihood ratios*. J Gen Intern Med. 2002), un LR+ ≥ 10 o un LR- ≤ 0.1 suele bastar por sí solo para confirmar o descartar; valores entre 0.5 y 2 apenas cambian la sospecha clínica.

---

## Semiología y Rendimiento Diagnóstico

El hallazgo con mejor rendimiento documentado para **Artrosis de cadera** es **Dolor posterior de cadera al ponerse en cuclillas**. La literatura médica basada en evidencia cuantitativa describe los siguientes parámetros:

- **Sensibilidad estimada:** 24%
- **Especificidad estimada:** 96%
- **Cociente de Verosimilitud Positivo (LR+):** 6.1 — cambia moderadamente la probabilidad: evidencia útil

---

## Evidencia Cuantitativa y Fuentes

- **Hallazgo evaluado:** Dolor posterior de cadera al ponerse en cuclillas
- **Sensibilidad estimada:** 24%
- **Especificidad estimada:** 96%
- **Cociente de Verosimilitud Positivo (LR+):** 6.1 — cambia moderadamente la probabilidad: evidencia útil
- **Población evaluada:** pacientes que consultan en atención primaria por dolor de cadera o inguinal.
- **Cita principal:** Metcalfe D, Perry DC, Claireaux HA et al.. Does This Patient Have Hip Osteoarthritis?: The Rational Clinical Examination Systematic Review. JAMA. 2019. [PMID: 31846019]

---

## Conclusión Semiótica

Dolor posterior de cadera al ponerse en cuclillas — el cociente más alto, pero con intervalo muy ancho: el extremo inferior roza el 1.3, casi irrelevante
