---
id: "HM6021-01"
slug: "trastorno-consumo-alcohol-audit-audit-c"
title: "Trastorno por consumo de alcohol: Precisión del cuestionario AUDIT según criterios DSM-5"
subtitle: "Evaluación bayesiana del cribado en atención primaria, diferencias por sexo y despistaje postparto según JAMA."
date: "2026-08-22"
author: "Dr. Alcy Torres"
category: "psiquiatria"
category_label: "Psiquiatría y Atención Primaria"
tags: ["psiquiatria", "adicciones", "alcoholismo", "atencion-primaria", "audit", "semiologia", "evidencia"]
reading_time: "6 min"
difficulty: "Intermedio"
grounding_badge: "HM:6021 · PMID:38592385"
featured_image: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/NIH_standard_drink_comparison-es.png/960px-NIH_standard_drink_comparison-es.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail"
image_source: "https://commons.wikimedia.org/wiki/File:NIH_standard_drink_comparison-es.png"
image_license: "CC BY-SA 4.0"
image_title: "NIH standard drink comparison-es.png"

grounding:
  condicion_id: "HM:6021"
  condicion_nombre: "Trastorno por consumo de alcohol"
  concepto_id: "HM:3083"
  concepto_nombre: "Cuestionario AUDIT con puntuación ≥ 8"
  lr_positivo: 6.5
  lr_negativo: 0.33
  poblacion: "adultos evaluados en cribado frente a criterios diagnósticos DSM-5 (n = 79 633 en 35 estudios)"
  referencia_id: "pmid:38592385"
  referencia_cita: "Keyes KM, et al. Does This Patient Have Alcohol Use Disorder?: The Rational Clinical Examination Systematic Review. JAMA. 2024;331(14):1218-1229."
  doi: "10.1001/jama.2024.3101"
  pmid: "38592385"

triada:
  significante: "Puntuación ≥ 8 en el cuestionario AUDIT o consumo de riesgo en AUDIT-C (hombres ≥4, mujeres ≥3)."
  significado: "Patrón disfuncional de consumo etílico con deterioro clínico o malestar bajo criterios DSM-5."
  decision: "AUDIT ≥ 8 confirma con LR+ de 6.5 (6.9 en mujeres, 3.8 en hombres); AUDIT < 8 reduce probabilidad (LR- 0.33)."

autoevaluacion:
  - id: "q1"
    pregunta: "¿Cuál es la precisión del test AUDIT (corte ≥ 8) para identificar trastorno por consumo de alcohol según el DSM-5 en JAMA (PMID: 38592385)?"
    opciones:
      - texto: "Aumenta la probabilidad con LR+ de 6.5 global (6.9 en mujeres y 3.8 en hombres); un puntaje < 8 la reduce (LR- 0.33)."
        correcta: true
        feedback: "¡Correcto! Rendimiento metaanalítico verificado."
      - texto: "El AUDIT carece de validez diagnóstica frente al DSM-5."
        correcta: false
        feedback: "Incorrecto. Es el estándar de oro en cribado clínico."
---

# Introducción y Fundamentos Clínicos

El trastorno por consumo de alcohol (TCA) constituye una de las principales causas prevenibles de morbimortalidad a nivel global. Con la transición al Manual Diagnóstico y Estadístico de los Trastornos Mentales (5ª edición, DSM-5), se unificaron las categorías previas de abuso y dependencia en un único espectro de gravedad clínica.

La revisión sistemática de la serie *Rational Clinical Examination* de JAMA (Keyes et al., 2024; PMID: 38592385) analizó 35 estudios con 79 633 pacientes para evaluar la precisión de las escalas breves de despistaje frente al estándar del DSM-5.

## Análisis Semiótico y Razonamiento Bayesiano

### Rendimiento del Cuestionario AUDIT (Corte $\ge 8$)

El *Alcohol Use Disorders Identification Test* (AUDIT) de 10 preguntas es el instrumento de cribado más validado:
- **Cociente de Verosimilitud Positivo ($LR^+$) Global:** **6.5** (IC 95%: 3.9–11)
- **Diferencias por Sexo:**
  - En **mujeres**: $LR^+ =$ **6.9** (IC 95%: 3.9–12)
  - En **hombres**: $LR^+ =$ **3.8** (IC 95%: 2.6–5.5) ($P = .003$)
- **Cociente de Verosimilitud Negativo ($LR^-$):** **0.33** (IC 95%: 0.20–0.52) tanto en hombres como en mujeres.

### Versiones Abreviadas y Poblaciones Especiales

1. **AUDIT-C (Consumo Abreviado de 3 ítems)**:
   - Con puntos de corte de $\ge 4$ para hombres ($LR^+ 1.8$) y $\ge 3$ para mujeres ($LR^+ 2.0$), es ideal para identificar consumo de riesgo rápido en triaje o revisiones generales.
2. **Población Puérpera y Gestante (Primeras 48 h postparto)**:
   - **AUDIT $\ge 4$**: $LR^+ =$ **6.4** (IC 95%: 5.1–8.0) para confirmar.
   - **TWEAK o T-ACE $< 2$**: $LR^- =$ **0.05** (IC 95%: 0.01–0.20), logrando una exclusión diagnóstica casi absoluta.
