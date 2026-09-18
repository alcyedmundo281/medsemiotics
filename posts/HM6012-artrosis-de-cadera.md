---
id: HM6012-01
slug: artrosis-de-cadera-precision-semiotica
title: 'Artrosis de cadera: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-08-21'
author: Dr. Alcy Torres
category: reumatologia
category_label: Reumatología y Traumatología
tags:
- artrosis-de-cadera
- reumatologia
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: f2e95a0834f2c2789e6cc56b5610d9612bdec93b
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6012-artrosis-de-cadera.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM3041-dolor-posterior-en-cuclillas.yaml: 96fcce3b26f280f51628c1f17a08a4de45b992674fe7e6746399e714583693b4
    conceptos/HM3042-dolor-inguinal-abduccion-aduccion.yaml: b7d701d16997b0d6ed38d9ee16dc7d0ef4d7ea5423ad7e64119f985fc7b7ec6a
    conceptos/HM3043-debilidad-de-abductores.yaml: 5cc8943c630898ae3f35af6571edeed0a3ebbca0b288bf67987360aa999d3e4b
    conceptos/HM3044-aduccion-pasiva-disminuida.yaml: f265a1f9aae2ef994c1ce9b55cb39240024556da7e32dec99556ae1a8aa85ac3
    conceptos/HM3045-rotacion-interna-disminuida.yaml: 0d919631287eedd020362b01e0e2c3b0296c53fba4d9dc4ccb971336298e34f6
    conceptos/HM3046-dolor-al-subir-escaleras.yaml: c9c8d30f103eb8269ba4ec296e05d48cb4cc76b3d7c8a9543fb5c401b30dd93c
    conceptos/HM3047-antecedente-familiar-artrosis.yaml: a5e15a81a91308ef0b8f243c45cbafc5e6562c79e3330ae1c08156f3179027e9
    conceptos/HM3048-antecedente-artrosis-de-rodilla.yaml: 7abf91d1caa9856fe7c58d7235b8616dca566f8f5dbc7fbe57a96722daed4b61
    condiciones/HM6012-artrosis-de-cadera.yaml: 031ae0b9a25da2de810bca47feea7a8eb76b360d03bd06b25df92b4f11010ea8
    referencias/pmid-31846019.yaml: b01d3c39fe0f1808b637635828f325109795ca8975031303f200957a7c2e53f7
grounding:
  condicion_id: HM:6012
  condicion_nombre: Artrosis de cadera
  concepto_id: HM:3041
  concepto_nombre: Dolor posterior de cadera al ponerse en cuclillas
  estado_lr: medido
  lr_positivo: 6.1
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:31846019
  referencia_cita: 'Metcalfe D, Perry DC, Claireaux HA, Simel DL, Zogg CK, Costa ML Does This Patient Have Hip Osteoarthritis?: The Rational Clinical Examination Systematic Review JAMA 2019'
  pmid: '31846019'
  doi: 10.1001/jama.2019.19413
  sensibilidad: 0.24
  especificidad: 0.96
triada:
  significante: Dolor posterior de cadera al ponerse en cuclillas
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: 'el cociente más alto, pero con intervalo muy ancho: el extremo inferior roza el 1.3, casi irrelevante'
evidencia:
- concepto: HM:3041
  rol: prueba_especifica
  estado_lr: medido
  sensibilidad: 0.24
  especificidad: 0.96
  lr_positivo: &id001
    valor: 6.1
    ic95:
    - 1.3
    - 29
    ref: pmid:31846019
  decision: 'el cociente más alto, pero con intervalo muy ancho: el extremo inferior roza el 1.3, casi irrelevante'
- concepto: HM:3042
  rol: prueba_especifica
  estado_lr: medido
  sensibilidad: 0.33
  especificidad: 0.94
  lr_positivo: &id002
    valor: 5.7
    ic95:
    - 1.6
    - 20
    ref: pmid:31846019
- concepto: HM:3043
  rol: prueba_especifica
  estado_lr: medido
  sensibilidad: 0.44
  especificidad: 0.9
  lr_positivo:
    valor: 4.5
    ic95:
    - 2.4
    - 8.4
    ref: pmid:31846019
  decision: intervalo más estrecho que los anteriores; en la práctica, más fiable pese a un cociente algo menor
- concepto: HM:3044
  rol: prueba_sensible
  estado_lr: medido
  sensibilidad: 0.8
  especificidad: 0.81
  lr_positivo:
    valor: 4.2
    ic95:
    - 3.0
    - 6.0
    ref: pmid:31846019
  lr_negativo:
    valor: 0.25
    ic95:
    - 0.11
    - 0.54
    ref: pmid:31846019
    nota: la fuente lo expresa como el valor de encontrar una aducción pasiva NORMAL, que es el cociente negativo de este hallazgo
  decision: 'el hallazgo más equilibrado y el único que sirve en los dos sentidos: su presencia apoya y su normalidad es lo que mejor descarta'
- concepto: HM:3045
  rol: prueba_sensible
  estado_lr: medido
  sensibilidad: 0.66
  especificidad: 0.79
  lr_positivo:
    valor: 3.2
    ic95:
    - 1.7
    - 6.0
    ref: pmid:31846019
- concepto: HM:3046
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 2.1
    ic95:
    - 1.1
    - 3.8
    ref: pmid:31846019
    nota: la fuente agrupa tres datos de anamnesis con idéntico cociente de 2.1; el intervalo citado es el más ancho de los tres
- concepto: HM:3047
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 2.1
    ic95:
    - 1.1
    - 3.8
    ref: pmid:31846019
    nota: mismo cociente agrupado que el dolor al subir escaleras
- concepto: HM:3048
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 2.1
    ic95:
    - 1.1
    - 3.8
    ref: pmid:31846019
    nota: mismo cociente agrupado que el dolor al subir escaleras
autoevaluacion:
- id: q1
  pregunta: En Artrosis de cadera, ¿cuál es el resultado documentado del LR positivo para «Dolor posterior de cadera al ponerse en cuclillas»?
  concepto_id: HM:3041
  referencia_id: pmid:31846019
  pmid: '31846019'
  doi: 10.1001/jama.2019.19413
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6012
    concepto_id: HM:3041
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: 'el cociente más alto, pero con intervalo muy ancho: el extremo inferior roza el 1.3, casi irrelevante'
    advertencia: null
  opciones:
  - texto: El valor 6.1 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 6.1. IC del 95 %: 1.3 a 29. Interpretación registrada: el cociente más alto, pero con intervalo muy ancho: el extremo inferior roza el 1.3, casi irrelevante.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 6.1. LR positivo: 6.1. IC del 95 %: 1.3 a 29. Interpretación registrada: el cociente más alto, pero con intervalo muy ancho: el extremo inferior roza el 1.3, casi irrelevante.'
  - texto: 'LR positivo: 6.1.'
    correcta: true
    feedback: 'LR positivo: 6.1. IC del 95 %: 1.3 a 29. Interpretación registrada: el cociente más alto, pero con intervalo muy ancho: el extremo inferior roza el 1.3, casi irrelevante.'
- id: q2
  pregunta: En Artrosis de cadera, ¿cuál es el resultado documentado del LR positivo para «Dolor inguinal a la abducción o aducción pasiva»?
  concepto_id: HM:3042
  referencia_id: pmid:31846019
  pmid: '31846019'
  doi: 10.1001/jama.2019.19413
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6012
    concepto_id: HM:3042
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: null
    motivo: null
    decision: null
    advertencia: null
  opciones:
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 5.7. LR positivo: 5.7. IC del 95 %: 1.6 a 20.'
  - texto: 'LR positivo: 5.7.'
    correcta: true
    feedback: 'LR positivo: 5.7. IC del 95 %: 1.6 a 20.'
  - texto: El valor 5.7 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 5.7. IC del 95 %: 1.6 a 20.'
---

# Artrosis de cadera

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Hip osteoarthritis

## Sinónimos

coxartrosis

osteoartritis de cadera

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Probabilidad basal

Valor: 0.34; Población: pacientes que consultan en atención primaria por dolor de cadera o inguinal; Referencia: pmid:31846019

## Hallazgos clínicos

### Dolor posterior de cadera al ponerse en cuclillas (HM:3041)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Sensibilidad:** 0.24

**Especificidad:** 0.96

**LR positivo:** Valor: 6.1; IC del 95 %: 1.3 / 29; Referencia: pmid:31846019

**Decisión:** el cociente más alto, pero con intervalo muy ancho: el extremo inferior roza el 1.3, casi irrelevante

### Dolor inguinal a la abducción o aducción pasiva (HM:3042)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Sensibilidad:** 0.33

**Especificidad:** 0.94

**LR positivo:** Valor: 5.7; IC del 95 %: 1.6 / 20; Referencia: pmid:31846019

### Debilidad de los abductores de cadera (HM:3043)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Sensibilidad:** 0.44

**Especificidad:** 0.9

**LR positivo:** Valor: 4.5; IC del 95 %: 2.4 / 8.4; Referencia: pmid:31846019

**Decisión:** intervalo más estrecho que los anteriores; en la práctica, más fiable pese a un cociente algo menor

### Aducción pasiva de cadera disminuida (HM:3044)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**Sensibilidad:** 0.8

**Especificidad:** 0.81

**LR positivo:** Valor: 4.2; IC del 95 %: 3.0 / 6.0; Referencia: pmid:31846019

**LR negativo:** Valor: 0.25; IC del 95 %: 0.11 / 0.54; Referencia: pmid:31846019; Nota: la fuente lo expresa como el valor de encontrar una aducción pasiva NORMAL, que es el cociente negativo de este hallazgo

**Decisión:** el hallazgo más equilibrado y el único que sirve en los dos sentidos: su presencia apoya y su normalidad es lo que mejor descarta

### Rotación interna de cadera disminuida (HM:3045)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**Sensibilidad:** 0.66

**Especificidad:** 0.79

**LR positivo:** Valor: 3.2; IC del 95 %: 1.7 / 6.0; Referencia: pmid:31846019

### Dolor al subir escaleras o cuestas (HM:3046)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 2.1; IC del 95 %: 1.1 / 3.8; Referencia: pmid:31846019; Nota: la fuente agrupa tres datos de anamnesis con idéntico cociente de 2.1; el intervalo citado es el más ancho de los tres

### Antecedente familiar de artrosis (HM:3047)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 2.1; IC del 95 %: 1.1 / 3.8; Referencia: pmid:31846019; Nota: mismo cociente agrupado que el dolor al subir escaleras

### Antecedente personal de artrosis de rodilla (HM:3048)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 2.1; IC del 95 %: 1.1 / 3.8; Referencia: pmid:31846019; Nota: mismo cociente agrupado que el dolor al subir escaleras

## Conclusión de la fuente

Pruebas sencillas de movilidad de la cadera, observando si aparece dolor durante el movimiento, distinguen a los pacientes con más probabilidad de tener artrosis en la radiografía. Una combinación de hallazgos detecta con eficiencia a quienes tienen artrosis grave.

## Referencias y procedencia

**pmid:31846019:** Does This Patient Have Hip Osteoarthritis?: The Rational Clinical Examination Systematic Review. JAMA, 2019. DOI: 10.1001/jama.2019.19413.

Fuente clínica: medsemiotics-db, condición HM:6012.
