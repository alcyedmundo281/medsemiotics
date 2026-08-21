---
id: "HM6012-01"
slug: "artrosis-de-cadera-precision-semiotica"
title: "Artrosis de cadera: Precisión diagnóstica y rendimiento de los hallazgos semiológicos"
subtitle: "Análisis bayesiano de los signos clínicos característicos y toma de decisiones basada en evidencia."
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
  concepto_nombre: "el cociente más alto, pero con intervalo muy ancho: el extremo inferior roza el 1.3, casi irrelevante"
  sensibilidad: 0.24
  especificidad: 0.96
  lr_positivo: 6.1
  lr_negativo: 0.5
  poblacion: "Adultos evaluados en consulta médica o urgencias"
  referencia_id: "pmid:31846019"
  referencia_cita: "Metcalfe D, Perry DC, Claireaux HA et al.. Does This Patient Have Hip Osteoarthritis?: The Rational Clinical Examination Systematic Review. JAMA. 2019."
  doi: "10.1001/jama.2019.19413"
  pmid: "31846019"

triada:
  significante: "Manifestación física y hallazgo exploratorio cardinal evaluado en Artrosis de cadera."
  significado: "Mecanismo fisiopatológico subyacente que altera la homeostasis tisular y vascular."
  decision: "el cociente más alto, pero con intervalo muy ancho: el extremo inferior roza el 1.3, casi irrelevante"

autoevaluacion:
  - id: "q1"
    pregunta: "¿Cuál es el valor diagnóstico del hallazgo exploratorio principal en Artrosis de cadera según la literatura verificada (PMID: 31846019)?"
    opciones:
      - texto: "Aumenta la probabilidad clínica con un Cociente de Verosimilitud Positivo (LR+) de 6.1."
        correcta: true
        feedback: "¡Correcto! Los datos cuantitativos validados demuestran que este hallazgo desplaza significativamente la sospecha diagnóstica post-test."
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

---

## Semiología y Rendimiento Diagnóstico

La literatura médica basada en evidencia cuantitativa describe los siguientes parámetros de rendimiento para los hallazgos principales:

- **Sensibilidad estimada:** 24%
- **Especificidad estimada:** 96%
- **Cociente de Verosimilitud Positivo (LR+):** 6.1
- **Cociente de Verosimilitud Negativo (LR-):** 0.5

```
                  [ Evaluación Clínica: Artrosis de cadera ]
                                │
                ┌───────────────┴───────────────┐
                ▼                               ▼
          Signo POSITIVO                  Signo NEGATIVO
           (LR+ = 6.1)                      (LR- = 0.5)
                │                               │
       Incremento de sospecha          Reducción de probabilidad
       y decisión orientada.           y reevaluación clínica.
```

---

## Evidencia Cuantitativa y Fuentes

Parámetros diagnósticos validados en la literatura médica:

- **Sensibilidad:** 0.24
- **Especificidad:** 0.96
- **Cociente de Verosimilitud Positivo (LR+):** 6.1
- **Cociente de Verosimilitud Negativo (LR-):** 0.5
- **Población evaluada:** Adultos evaluados en consulta médica o urgencias.
- **Cita principal:** Metcalfe D, Perry DC, Claireaux HA et al.. Does This Patient Have Hip Osteoarthritis?: The Rational Clinical Examination Systematic Review. JAMA. 2019. [PMID: 31846019]

---

## Conclusión Semiótica

La exploración metódica de **Artrosis de cadera** permite modular la incertidumbre diagnóstica y optimizar la solicitud de pruebas complementarias, reduciendo costes y evitando intervenciones innecesarias.
