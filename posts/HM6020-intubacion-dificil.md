---
id: "HM6020-01"
slug: "intubacion-dificil-mallampati-mordida-labio"
title: "Vía aérea difícil: Rendimiento del test de mordida del labio superior y la escala de Mallampati"
subtitle: "Análisis bayesiano de los predictores físicos preoperatorios de intubación difícil según la evidencia de JAMA."
date: "2026-08-22"
author: "Dr. Alcy Torres"
category: "anestesiologia"
category_label: "Anestesiología y Cuidados Críticos"
tags: ["anestesiologia", "via-aerea", "intubacion", "urgencias", "semiologia", "evidencia"]
reading_time: "6 min"
difficulty: "Intermedio"
grounding_badge: "HM:6020 · PMID:30721300"
featured_image: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Mallampati.svg/960px-Mallampati.svg.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail"
image_source: "https://commons.wikimedia.org/wiki/File:Mallampati.svg"
image_license: "CC BY-SA 3.0"
image_title: "Mallampati.svg"

grounding:
  condicion_id: "HM:6020"
  condicion_nombre: "Intubación difícil"
  concepto_id: "HM:3078"
  concepto_nombre: "Test de mordida del labio superior clase 3"
  especificidad: 0.96
  lr_positivo: 14
  poblacion: "pacientes adultos quirúrgicos generales (n = 33 559 en 62 estudios)"
  referencia_id: "pmid:30721300"
  referencia_cita: "Detsky ME, et al. Will This Patient Be Difficult to Intubate?: The Rational Clinical Examination Systematic Review. JAMA. 2019;321(5):493-503."
  doi: "10.1001/jama.2018.21413"
  pmid: "30721300"

triada:
  significante: "Incapacidad de los incisivos inferiores para alcanzar el labio superior (Test de mordida clase 3), Mallampati 3/4 o distancia tiromentoniana corta."
  significado: "Restricción mecánica en la alineación de los ejes faríngeo, oral y laríngeo durante la laringoscopia directa."
  decision: "Confirma alta probabilidad de vía aérea difícil (LR+ 14 con test de mordida clase 3); ningún signo negativo la descarta por completo."

autoevaluacion:
  - id: "q1"
    pregunta: "¿Cuál es el hallazgo físico con mayor LR+ para predecir intubación difícil según JAMA (PMID: 30721300)?"
    opciones:
      - texto: "Test de mordida del labio superior clase 3 (LR+ 14, especificidad 96%)."
        correcta: true
        feedback: "¡Correcto! Es el signo físico individual más potente."
      - texto: "Cualquier examen físico normal descarta la vía aérea difícil."
        correcta: false
        feedback: "Incorrecto. Ningún signo permite excluirla de forma concluyente."
---

# Introducción y Fundamentos Clínicos

La identificación previa a la inducción anestésica de una vía aérea difícil es fundamental para prevenir eventos catastróficos de hipoxia y paro cardiorrespiratorio.

La revisión sistemática de la serie *Rational Clinical Examination* de JAMA (Detsky et al., 2019; PMID: 30721300) analizó 62 estudios metodológicamente rigurosos con 33 559 pacientes para definir la precisión de las pruebas físicas en la cabecera del paciente.

## Análisis Semiótico y Razonamiento Bayesiano

En la población general de adultos intervenidos quirúrgicamente, la incidencia basal de intubación difícil se sitúa en torno al **10%** (IC 95%: 8.2%–12%).

### Rendimiento de los Predictores Anatómicos

1. **Test de Mordida del Labio Superior (Upper Lip Bite Test - Clase 3)**:
   - **Definición:** Los incisivos inferiores no logran morder ni alcanzar la línea del bermellón del labio superior.
   - **Especificidad:** 96% (IC 95%: 93%–97%)
   - **Cociente de Verosimilitud Positivo ($LR^+$):** **14** (IC 95%: 8.9–22)
   - **Impacto Clínico:** Eleva la probabilidad postest del 10% a **más del 60%**, siendo el predictor individual más potente y sencillo de explorar.

2. **Score de Riesgo de Wilson Aumentado**:
   - $LR^+ = 9.1$ (IC 95%: 5.1–16), especificidad 95%.

3. **Distancia Tiromentoniana / Hiodomentoniana Corta (<3 a 5.5 cm)**:
   - $LR^+ = 6.4$ (IC 95%: 4.1–10), especificidad 97%.

4. **Retrognatia (Longitud mandibular <9 cm o subjetivamente retraída)**:
   - $LR^+ = 6.0$ (IC 95%: 3.1–11), especificidad 98%.

5. **Escala de Mallampati Modificada (Clase 3 o 4)**:
   - $LR^+ = 4.1$ (IC 95%: 3.0–5.6), especificidad 87%.

### La Regla de Oro: La Exploración Negativa No Descarta
A diferencia de otras áreas de la semiología diagnóstica, ningún predictor físico individual posee un cociente negativo lo suficientemente potente como para descartar una intubación difícil ($LR^-$ entre 0.40 y 0.70). Por ello, el clínico siempre debe disponer de equipo de rescate (videolaringoscopio, mascarillas laríngeas) incluso ante un examen aparentemente favorable.
