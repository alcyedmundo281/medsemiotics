---
id: "HM6013-01"
slug: "enfermedad-del-manguito-rotador-precision-semiotica"
title: "Enfermedad del manguito rotador: Precisión diagnóstica y rendimiento de los hallazgos semiológicos"
subtitle: "Análisis bayesiano de los signos clínicos característicos y toma de decisiones basada en evidencia."
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
  concepto_nombre: "la única prueba de provocación de dolor con cociente positivo por encima de 2, y la que mejor descarta cuando es normal"
  sensibilidad: 0.7
  especificidad: 0.85
  lr_positivo: 3.7
  lr_negativo: 0.36
  poblacion: "Adultos evaluados en consulta médica o urgencias"
  referencia_id: "pmid:23982370"
  referencia_cita: "Hermans J, Luime JJ, Meuffels DE et al.. Does this patient with shoulder pain have rotator cuff disease?: The Rational Clinical Examination systematic review. JAMA. 2013."
  doi: "10.1001/jama.2013.276187"
  pmid: "23982370"

triada:
  significante: "Manifestación física y hallazgo exploratorio cardinal evaluado en Enfermedad del manguito rotador."
  significado: "Mecanismo fisiopatológico subyacente que altera la homeostasis tisular y vascular."
  decision: "la única prueba de provocación de dolor con cociente positivo por encima de 2, y la que mejor descarta cuando es normal"

autoevaluacion:
  - id: "q1"
    pregunta: "¿Cuál es el valor diagnóstico del hallazgo exploratorio principal en Enfermedad del manguito rotador según la literatura verificada (PMID: 23982370)?"
    opciones:
      - texto: "Aumenta la probabilidad clínica con un Cociente de Verosimilitud Positivo (LR+) de 3.7."
        correcta: true
        feedback: "¡Correcto! Los datos cuantitativos validados demuestran que este hallazgo desplaza significativamente la sospecha diagnóstica post-test."
      - texto: "Descarta en un 100% la patología independientemente de otros signos."
        correcta: false
        feedback: "Incorrecto. En razonamiento bayesiano clínico, ningún signo aislado produce certeza absoluta sin análisis contextual."
      - texto: "Carece de valor discriminativo en la exploración."
        correcta: false
        feedback: "Incorrecto. Presenta una especificidad documentada de 85%."

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

---

## Semiología y Rendimiento Diagnóstico

La literatura médica basada en evidencia cuantitativa describe los siguientes parámetros de rendimiento para los hallazgos principales:

- **Sensibilidad estimada:** 70%
- **Especificidad estimada:** 85%
- **Cociente de Verosimilitud Positivo (LR+):** 3.7
- **Cociente de Verosimilitud Negativo (LR-):** 0.36

```
                  [ Evaluación Clínica: Enfermedad del manguito rotador ]
                                │
                ┌───────────────┴───────────────┐
                ▼                               ▼
          Signo POSITIVO                  Signo NEGATIVO
           (LR+ = 3.7)                      (LR- = 0.36)
                │                               │
       Incremento de sospecha          Reducción de probabilidad
       y decisión orientada.           y reevaluación clínica.
```

---

## Evidencia Cuantitativa y Fuentes

Parámetros diagnósticos validados en la literatura médica:

- **Sensibilidad:** 0.7
- **Especificidad:** 0.85
- **Cociente de Verosimilitud Positivo (LR+):** 3.7
- **Cociente de Verosimilitud Negativo (LR-):** 0.36
- **Población evaluada:** Adultos evaluados en consulta médica o urgencias.
- **Cita principal:** Hermans J, Luime JJ, Meuffels DE et al.. Does this patient with shoulder pain have rotator cuff disease?: The Rational Clinical Examination systematic review. JAMA. 2013. [PMID: 23982370]

---

## Conclusión Semiótica

La exploración metódica de **Enfermedad del manguito rotador** permite modular la incertidumbre diagnóstica y optimizar la solicitud de pruebas complementarias, reduciendo costes y evitando intervenciones innecesarias.
