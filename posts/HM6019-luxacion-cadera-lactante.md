---
id: "HM6019-01"
slug: "luxacion-cadera-lactante-barlow-ortolani"
title: "Luxación y displasia de cadera en el lactante: Precisión de las maniobras de Barlow y Ortolani"
subtitle: "Análisis bayesiano de la exploración física neonatal frente al estándar ecográfico de Graf según la evidencia de JAMA."
date: "2026-08-22"
author: "Dr. Alcy Torres"
category: "pediatria"
category_label: "Pediatría y Ortopedia"
tags: ["pediatria", "ortopedia", "displasia-cadera", "recien-nacido", "semiologia", "evidencia"]
reading_time: "6 min"
difficulty: "Intermedio"
grounding_badge: "HM:6019 · PMID:38619828"
featured_image: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Ultrasound_measuring_the_developmental_dysplasia_of_right_hip.jpg/960px-Ultrasound_measuring_the_developmental_dysplasia_of_right_hip.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail"
image_source: "https://commons.wikimedia.org/wiki/File:Ultrasound_measuring_the_developmental_dysplasia_of_right_hip.jpg"
image_license: "CC BY-SA 4.0"
image_title: "Ultrasound measuring the developmental dysplasia of right hip.jpg"

grounding:
  condicion_id: "HM:6019"
  condicion_nombre: "Luxación de cadera en el lactante"
  concepto_id: "HM:3075"
  concepto_nombre: "Maniobras de Barlow y Ortolani positivas"
  sensibilidad: 0.46
  especificidad: 0.991
  lr_positivo: 52
  lr_negativo: 0.55
  poblacion: "lactantes de 3 meses o menores evaluados con examen físico y ecografía (n = 44 827 caderas)"
  referencia_id: "pmid:38619828"
  referencia_cita: "Tidwell JE, et al. Does This Infant Have a Dislocated Hip?: The Rational Clinical Examination Systematic Review. JAMA. 2024;331(18):1576-1585."
  doi: "10.1001/jama.2024.2404"
  pmid: "38619828"

triada:
  significante: "Maniobras de Barlow y Ortolani positivas (provocación y reducción palpable de luxación coxofemoral)."
  significado: "Inestabilidad articular por displasia acetabular o laxitud ligamentosa neonatal."
  decision: "Confirma luxación inestable con alta especificidad (LR+ 52); un examen negativo (LR- 0.55) no descarta la patología."

autoevaluacion:
  - id: "q1"
    pregunta: "¿Cuál es el valor diagnóstico de las maniobras de Barlow y Ortolani en el lactante menor de 3 meses según JAMA (PMID: 38619828)?"
    opciones:
      - texto: "Alta especificidad (99.1%) y LR+ de 52 para confirmar, pero sensibilidad limitada (46%), por lo que no descarta si es negativa."
        correcta: true
        feedback: "¡Correcto! El signo confirma con gran fuerza diagnóstica pero no excluye la displasia silente."
      - texto: "Descarta en 100% la displasia si el examen es normal."
        correcta: false
        feedback: "Incorrecto. Sensibilidad de 46% (LR- 0.55)."
---

# Introducción y Fundamentos Clínicos

La displasia del desarrollo de la cadera (DDC) abarca un espectro continuo que va desde la laxitud capsular leve hasta la luxación franca de la cabeza femoral fuera del acetábulo. La detección precoz en los primeros meses de vida previene cirugías invasivas, artrosis prematura y discapacidad funcional.

La revisión sistemática de la serie *Rational Clinical Examination* de JAMA (Tidwell et al., 2024; PMID: 38619828) evaluó con rigor metodológico el rendimiento diagnóstico de las maniobras de exploración física neonatal frente al estándar de referencia ecográfico (método de Graf).

## Análisis Semiótico y Razonamiento Bayesiano

En la población general de lactantes de 3 meses o menores cribados, la prevalencia base de luxación de cadera es de **0.94%**.

### Rendimiento de los Hallazgos Semiológicos

1. **Maniobras de Barlow y Ortolani**:
   - **Sensibilidad:** 46% (IC 95%: 26%–67%)
   - **Especificidad:** 99.1% (IC 95%: 97.9%–99.6%)
   - **Cociente de Verosimilitud Positivo ($LR^+$):** **52** (IC 95%: 21–127)
   - **Cociente de Verosimilitud Negativo ($LR^-$):** **0.55** (IC 95%: 0.37–0.82)
   - **Impacto Clínico:** Cuando una maniobra es francamente positiva, la probabilidad postest salta del **0.94% a más del 33%**, justificando la colocación inmediata de un arnés de Pavlik y valoración ortopédica. Sin embargo, su negatividad apenas reduce la probabilidad a **0.52%**, demostrando que más de la mitad de las displasias no presentan inestabilidad palpable en el examen inicial.

2. **Limitación de la Abducción de Cadera**:
   - $LR^+ = 3.6$ (IC 95%: 0.72–18). En menores de 3 meses, la contractura fisiológica neonatal limita su utilidad; adquiere mayor relevancia después de los 3 a 6 meses.

3. **Chasquidos o Clicks Articulares**:
   - $LR^+ = 1.6$ (IC 95%: 0.91–2.8). Los chasquidos adventicios son predominantemente benignos y no deben interpretarse como signo de luxación.
