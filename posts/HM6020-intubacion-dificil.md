---
id: HM6020-01
slug: intubacion-dificil-mallampati-mordida-labio
title: 'Intubación difícil: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-08-22'
author: Dr. Alcy Torres
category: anestesiologia
category_label: Anestesiología y Cuidados Críticos
tags:
- anestesiologia
- intubacion-dificil
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: fbd5cbf59e75e77b70a630f881ac1c1754e1e063
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6020-intubacion-dificil.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0600-signo-de-exploracion.yaml: 86a2ac9babe66028eecc797ddbf4d9ea382a6fd685e9cb8df91bb959029d62bf
    conceptos/HM3078-test-mordida-labio-superior-clase-3.yaml: bf284c373f4ef74131492f0264af906aec28dcc1891e19f7776d424495a11f1b
    conceptos/HM3079-distancia-hiodomentoniana-corta.yaml: 6afcfa37fd303843404cf8c9c6853885f52b3ec85a76b5c63f471ac54511f141
    conceptos/HM3080-retrognatia.yaml: e0426d5c59bdb9bb724ba58534dde9467384985e631ab5ec912f8ec2a7a8c54b
    conceptos/HM3081-mallampati-clase-3-o-4.yaml: 366c0d1c97f6fa6e8742157e005d8058c19a3df9b131b41cdef47fd1360ae170
    conceptos/HM3082-score-de-wilson.yaml: a6c034805fc5b741f39efffe0d2d933c1737147705c7fb53b518bd8b3e34ffa0
    condiciones/HM6020-intubacion-dificil.yaml: ff9a4c558137006cb089f056c8f5bf3a48d9ec9bd951225ca5502a571b871704
    referencias/pmid-30721300.yaml: ad82c0d43425b8e7808e9c35f6c5c8e3a626e0af90641b3673f7469cb13fc9ea
grounding:
  condicion_id: HM:6020
  condicion_nombre: Intubación difícil
  concepto_id: HM:3078
  concepto_nombre: Test de mordida del labio superior clase 3
  estado_lr: medido
  lr_positivo: 14
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: pacientes quirúrgicos adultos (n = 33 559)
  referencia_id: pmid:30721300
  referencia_cita: 'Detsky ME, Jivraj N, Adhikari NK, Friedrich JO, Pinto R, Simel DL, Wijeysundera DN, Scales DC Will This Patient Be Difficult to Intubate?: The Rational Clinical Examination Systematic Review JAMA 2019'
  pmid: '30721300'
  doi: 10.1001/jama.2018.21413
  especificidad: 0.96
triada:
  significante: Test de mordida del labio superior clase 3
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: 'Test de mordida del labio superior clase 3: el predictor físico individual más potente. Con LR+ 14 y especificidad del 96%, eleva la probabilidad postest de 10% a más de 60%.'
evidencia:
- concepto: HM:3078
  rol: prueba_especifica
  estado_lr: medido
  especificidad: 0.96
  poblacion: pacientes quirúrgicos adultos (n = 33 559)
  lr_positivo: &id001
    valor: 14
    ic95:
    - 8.9
    - 22
    ref: pmid:30721300
  decision: 'Test de mordida del labio superior clase 3: el predictor físico individual más potente. Con LR+ 14 y especificidad del 96%, eleva la probabilidad postest de 10% a más de 60%.'
- concepto: HM:3079
  rol: prueba_especifica
  estado_lr: medido
  especificidad: 0.97
  poblacion: pacientes quirúrgicos adultos
  lr_positivo: &id002
    valor: 6.4
    ic95:
    - 4.1
    - 10
    ref: pmid:30721300
  decision: 'Distancia hiodomentoniana o tiromentoniana corta (<3 a 5.5 cm): alta especificidad (97%) con LR+ 6.4.'
- concepto: HM:3080
  rol: prueba_especifica
  estado_lr: medido
  especificidad: 0.98
  poblacion: pacientes quirúrgicos adultos
  lr_positivo:
    valor: 6.0
    ic95:
    - 3.1
    - 11
    ref: pmid:30721300
  decision: 'Retrognatia (mandíbula <9 cm): especificidad del 98% con LR+ 6.0.'
- concepto: HM:3082
  rol: prueba_especifica
  estado_lr: medido
  especificidad: 0.95
  poblacion: pacientes quirúrgicos adultos
  lr_positivo:
    valor: 9.1
    ic95:
    - 5.1
    - 16
    ref: pmid:30721300
  decision: 'Score de Wilson de riesgo aumentado: combinación de 5 factores anatómicos con LR+ 9.1 y especificidad del 95%.'
- concepto: HM:3081
  rol: prueba_especifica
  estado_lr: medido
  especificidad: 0.87
  poblacion: pacientes quirúrgicos adultos
  lr_positivo:
    valor: 4.1
    ic95:
    - 3.0
    - 5.6
    ref: pmid:30721300
  decision: 'Escala de Mallampati modificada (clase 3 o 4): el test más difundido; aporta un LR+ de 4.1 pero con especificidad moderada (87%).'
autoevaluacion:
- id: q1
  pregunta: 'En Intubación difícil, ¿cuál es el resultado documentado del LR positivo para «Test de mordida del labio superior clase 3»? Población: pacientes quirúrgicos adultos (n = 33 559).'
  concepto_id: HM:3078
  referencia_id: pmid:30721300
  pmid: '30721300'
  doi: 10.1001/jama.2018.21413
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6020
    concepto_id: HM:3078
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: pacientes quirúrgicos adultos (n = 33 559)
    motivo: null
    decision: 'Test de mordida del labio superior clase 3: el predictor físico individual más potente. Con LR+ 14 y especificidad del 96%, eleva la probabilidad postest de 10% a más de 60%.'
    advertencia: null
  opciones:
  - texto: 'LR positivo: 14.'
    correcta: true
    feedback: 'LR positivo: 14. IC del 95 %: 8.9 a 22. Población: pacientes quirúrgicos adultos (n = 33 559). Interpretación registrada: Test de mordida del labio superior clase 3: el predictor físico individual más potente. Con LR+ 14 y especificidad del 96%, eleva la probabilidad postest de 10% a más de 60%.'
  - texto: El valor 14 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 14. IC del 95 %: 8.9 a 22. Población: pacientes quirúrgicos adultos (n = 33 559). Interpretación registrada: Test de mordida del labio superior clase 3: el predictor físico individual más potente. Con LR+ 14 y especificidad del 96%, eleva la probabilidad postest de 10% a más de 60%.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 14. LR positivo: 14. IC del 95 %: 8.9 a 22. Población: pacientes quirúrgicos adultos (n = 33 559). Interpretación registrada: Test de mordida del labio superior clase 3: el predictor físico individual más potente. Con LR+ 14 y especificidad del 96%, eleva la probabilidad postest de 10% a más de 60%.'
- id: q2
  pregunta: 'En Intubación difícil, ¿cuál es el resultado documentado del LR positivo para «Distancia hiodomentoniana o tiromentoniana corta»? Población: pacientes quirúrgicos adultos.'
  concepto_id: HM:3079
  referencia_id: pmid:30721300
  pmid: '30721300'
  doi: 10.1001/jama.2018.21413
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6020
    concepto_id: HM:3079
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: pacientes quirúrgicos adultos
    motivo: null
    decision: 'Distancia hiodomentoniana o tiromentoniana corta (<3 a 5.5 cm): alta especificidad (97%) con LR+ 6.4.'
    advertencia: null
  opciones:
  - texto: El valor 6.4 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 6.4. IC del 95 %: 4.1 a 10. Población: pacientes quirúrgicos adultos. Interpretación registrada: Distancia hiodomentoniana o tiromentoniana corta (<3 a 5.5 cm): alta especificidad (97%) con LR+ 6.4.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 6.4. LR positivo: 6.4. IC del 95 %: 4.1 a 10. Población: pacientes quirúrgicos adultos. Interpretación registrada: Distancia hiodomentoniana o tiromentoniana corta (<3 a 5.5 cm): alta especificidad (97%) con LR+ 6.4.'
  - texto: 'LR positivo: 6.4.'
    correcta: true
    feedback: 'LR positivo: 6.4. IC del 95 %: 4.1 a 10. Población: pacientes quirúrgicos adultos. Interpretación registrada: Distancia hiodomentoniana o tiromentoniana corta (<3 a 5.5 cm): alta especificidad (97%) con LR+ 6.4.'
---

# Intubación difícil

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Difficult endotracheal intubation

## Sinónimos

vía aérea difícil

intubación orotraqueal dificultosa

laringoscopia difícil

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Probabilidad basal

Valor: 0.1; Población: pacientes adultos quirúrgicos generales candidatos a intubación (n = 33 559 en 62 estudios); Referencia: pmid:30721300

## Factores de riesgo

Factor: Obesidad con IMC elevado

Factor: Movilidad cervical limitada o artropatía cervical

Factor: Antecedente personal de intubación difícil

## Hallazgos clínicos

### Test de mordida del labio superior clase 3 (HM:3078)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Especificidad:** 0.96

**Población:** pacientes quirúrgicos adultos (n = 33 559)

**LR positivo:** Valor: 14; IC del 95 %: 8.9 / 22; Referencia: pmid:30721300

**Decisión:** Test de mordida del labio superior clase 3: el predictor físico individual más potente. Con LR+ 14 y especificidad del 96%, eleva la probabilidad postest de 10% a más de 60%.

### Distancia hiodomentoniana o tiromentoniana corta (HM:3079)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Especificidad:** 0.97

**Población:** pacientes quirúrgicos adultos

**LR positivo:** Valor: 6.4; IC del 95 %: 4.1 / 10; Referencia: pmid:30721300

**Decisión:** Distancia hiodomentoniana o tiromentoniana corta (<3 a 5.5 cm): alta especificidad (97%) con LR+ 6.4.

### Retrognatia o longitud mandibular reducida (HM:3080)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Especificidad:** 0.98

**Población:** pacientes quirúrgicos adultos

**LR positivo:** Valor: 6.0; IC del 95 %: 3.1 / 11; Referencia: pmid:30721300

**Decisión:** Retrognatia (mandíbula <9 cm): especificidad del 98% con LR+ 6.0.

### Score de Wilson de riesgo aumentado (HM:3082)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Especificidad:** 0.95

**Población:** pacientes quirúrgicos adultos

**LR positivo:** Valor: 9.1; IC del 95 %: 5.1 / 16; Referencia: pmid:30721300

**Decisión:** Score de Wilson de riesgo aumentado: combinación de 5 factores anatómicos con LR+ 9.1 y especificidad del 95%.

### Escala de Mallampati modificada clase 3 o 4 (HM:3081)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Especificidad:** 0.87

**Población:** pacientes quirúrgicos adultos

**LR positivo:** Valor: 4.1; IC del 95 %: 3.0 / 5.6; Referencia: pmid:30721300

**Decisión:** Escala de Mallampati modificada (clase 3 o 4): el test más difundido; aporta un LR+ de 4.1 pero con especificidad moderada (87%).

## Conclusión de la fuente

Varios hallazgos de exploración física simple permiten identificar a pacientes con alta probabilidad de intubación difícil (especialmente el test de mordida del labio superior, LR+ 14), pero ningún hallazgo clínico permite excluir de forma fiable una vía aérea difícil.

## Referencias y procedencia

**pmid:30721300:** Will This Patient Be Difficult to Intubate?: The Rational Clinical Examination Systematic Review. JAMA, 2019. DOI: 10.1001/jama.2018.21413.

Fuente clínica: medsemiotics-db, condición HM:6020.
