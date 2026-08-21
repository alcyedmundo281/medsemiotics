---
id: "HM6004-01"
slug: "meningitis-aguda-sacudida-cefalica"
title: "Meningitis aguda en adultos: ¿Qué valor real tiene la acentuación de la cefalea con la sacudida cefálica?"
subtitle: "Análisis semiótico y discriminación bayesiana del jolt accentuation sign en el paciente con fiebre y cefalea."
date: "2026-08-20"
author: "Dr. Alcy Torres"
category: "neurologia"
category_label: "Neurología"
tags: ["meningitis", "cefalea", "semiótica", "urgencias"]
reading_time: "5 min"
difficulty: "Intermedio"
grounding:
  condicion_id: "HM:6004"
  condicion_nombre: "Meningitis aguda"
  concepto_id: "HM:3006"
  concepto_nombre: "Acentuación de la cefalea con la sacudida cefálica (Jolt accentuation)"
  sensibilidad: 1.00
  especificidad: 0.54
  lr_positivo: 2.2
  lr_negativo: 0.0
  poblacion: "Pacientes adultos que ya presentan fiebre y cefalea aguda"
  referencia_id: "pmid:10411200"
  referencia_cita: "Attia J, Hatala R, Cook DJ, Wong JG. The rational clinical examination. Does this adult patient have acute meningitis? JAMA. 1999;282(2):175-81."
  doi: "10.1001/jama.282.2.175"
  pmid: "10411200"

triada:
  significante: "Empeoramiento agudo de la cefalea al rotar la cabeza rápidamente en plano horizontal (2-3 giros por segundo)."
  significado: "Irritación meníngea con tracción y estrés mecánico sobre las estructuras vasculares y meníngeas inflamadas."
  decision: "Maniobra adjunta de alta sensibilidad: su ausencia (LR- 0.0 en serie de derivación) reduce sustancialmente la sospecha en fiebre + cefalea, pero su positividad (LR+ 2.2) solo ofrece modesta confirmación y requiere estudio de LCR si persisten banderas rojas."

autoevaluacion:
  - id: "q1"
    pregunta: "En un paciente adulto con fiebre y cefalea aguda, la maniobra de sacudida cefálica ('jolt accentuation') resulta NEGATIVA. ¿Cuál es el significado bayesiano de este hallazgo según la evidencia verificada (PMID: 10411200)?"
    opciones:
      - texto: "Aumenta la probabilidad de meningitis con un LR+ de 2.2."
        correcta: false
        feedback: "Incorrecto. Un resultado negativo se evalúa con el Likelihood Ratio Negativo (LR-), no con el positivo."
      - texto: "Presenta una sensibilidad del 100% (LR- 0.0 en la serie analizada), lo que reduce marcadamente la probabilidad post-test de meningitis bacteriana en este subgrupo."
        correcta: true
        feedback: "¡Correcto! En la serie de Attia et al. (JAMA 1999), la sensibilidad fue del 100% (LR- 0.0), convirtiéndola en una excelente prueba de exclusión en pacientes con fiebre y cefalea."
      - texto: "Confirma definitivamente meningitis tuberculosa."
        correcta: false
        feedback: "Incorrecto. No permite confirmar etiologías específicas y un resultado negativo no confirma patología."
      - texto: "Indica que se debe realizar punción lumbar de inmediato sin más anamnesis."
        correcta: false
        feedback: "Incorrecto. La ausencia del signo aleja la sospecha meníngea primaria si no coexisten otros signos de focalidad o rigidez nucal marcada."

  - id: "q2"
    pregunta: "¿Por qué un Likelihood Ratio positivo (LR+) de 2.2 se considera solo de impacto diagnóstico 'moderado a bajo' para confirmar meningitis aguda?"
    opciones:
      - texto: "Porque un LR+ de 2.2 solo genera un incremento discreto en la probabilidad post-test (~15%), insuficiente por sí solo para confirmar sin análisis citoquímico de LCR."
        correcta: true
        feedback: "¡Exacto! Según la regla bayesiana, un LR+ entre 2 y 5 produce cambios pequeños a moderados. En una enfermedad de alta gravedad como la meningitis, un LR+ de 2.2 exige pruebas confirmatorias (punción lumbar)."
      - texto: "Porque la especificidad del signo es del 100%."
        correcta: false
        feedback: "Incorrecto. La especificidad reportada es del 54% (0.54), lo que explica que existan falsos positivos en cefaleas febriles no meníngeas."
      - texto: "Porque el LR positivo solo aplica en pacientes pediátricos menores de 2 años."
        correcta: false
        feedback: "Incorrecto. La serie de Attia et al. evaluó exclusivamente cohortes de pacientes adultos."
---

## El dilema en el servicio de urgencias

El paciente con fiebre y cefalea aguda representa uno de los desafíos más comunes y de mayor compromiso pronóstico en la medicina de urgencias. La clásica tríada de fiebre, rigidez de nuca y alteración del estado mental tiene una sensibilidad clínica global subóptima.

Ante este escenario, la maniobra descrita por Uchihara y Tsukagoshi (popularizada por la serie *The Rational Clinical Examination* de JAMA) evalúa la **acentuación de la cefalea mediante la sacudida cefálica horizontal** (*jolt accentuation of headache*).

---

## Técnica del Signo Semiótico

1. Se solicita al paciente que gire la cabeza en el plano horizontal de lado a lado a una frecuencia de **2 a 3 rotaciones por segundo**.
2. **Signo Positivo:** El paciente refiere un empeoramiento o agudización franca de su cefalea basal.
3. **Signo Negativo:** La intensidad de la cefalea permanece inalterada durante y tras la maniobra.

```
       [ Paciente con Fiebre + Cefalea ]
                      │
           ┌──────────┴──────────┐
           ▼                     ▼
     Jolt Positivo         Jolt Negativo
      (LR+ = 2.2)           (LR- = 0.0*)
           │                     │
  Aumento modesto de      Sospecha meníngea
  probabilidad clínica.   sustancialmente menor.
  Evaluar LCR si hay      Reevaluar diagnósticos
  otros signos de alarma. diferenciales febriles.
```
*\*Nota metodológica: El LR- de 0.0 procede de una sensibilidad del 100% en la serie estudiada (PMID: 10411200); es un hallazgo muestral de alta potencia de cribado, no una imposibilidad absoluta.*

---

## Evidencia Cuantitativa y Fuentes

Parámetros diagnósticos validados en la literatura médica (serie *The Rational Clinical Examination*, JAMA):

- **Sensibilidad:** 1.00 (100%)
- **Especificidad:** 0.54 (54%)
- **Cociente de Verosimilitud Positivo (LR+):** 2.20 [Attia et al., JAMA 1999]
- **Cociente de Verosimilitud Negativo (LR-):** 0.00 [Attia et al., JAMA 1999]
- **Población evaluada:** Pacientes adultos en urgencias con presencia confirmada de fiebre y cefalea aguda.

---

## Conclusión Semiótica

La sacudida cefálica es una herramienta de **descarte (alta sensibilidad)** más que de confirmación definitiva. Su mayor utilidad clínica reside en su valor predictivo negativo cuando se aplica rigurosamente en la población adecuada.
