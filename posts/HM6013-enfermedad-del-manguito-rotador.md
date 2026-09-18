---
id: HM6013-01
slug: enfermedad-del-manguito-rotador-precision-semiotica
title: 'Enfermedad del manguito rotador: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-08-21'
author: Dr. Alcy Torres
category: traumatologia
category_label: Traumatología y Medicina Deportiva
tags:
- enfermedad-del-manguito-rotador
- semiologia
- traumatologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: f2e95a0834f2c2789e6cc56b5610d9612bdec93b
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6013-enfermedad-del-manguito-rotador.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM3055-arco-doloroso.yaml: 3548cc14bec9a5d961bcdddcdcc82ccad1ccf929916776673aa2aca3cc9f28b3
    conceptos/HM3058-drop-arm.yaml: 27f9b42dcac851d3c59294207f5ee6cf42d3205bdffb08da8c5e854c801ddb1c
    conceptos/HM3059-dolor-de-hombro.yaml: 99c4073545b37133cd7e218ead1bfbe7ea6d4d11b970fd95c2aa91bb8696fcff
    condiciones/HM6013-enfermedad-del-manguito-rotador.yaml: 20562fb16c0d1d17104d710f6b21f8da0bbd8782cb5e9ddf99af3f81f4ef9f52
    referencias/pmid-23982370.yaml: a069ef6d93f543653e62805872e4ffaf929021cd19668bcb2eb3b5413613c18b
grounding:
  condicion_id: HM:6013
  condicion_nombre: Enfermedad del manguito rotador
  concepto_id: HM:3055
  concepto_nombre: Arco doloroso
  estado_lr: medido
  lr_positivo: 3.7
  lr_negativo: 0.36
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:23982370
  referencia_cita: 'Hermans J, Luime JJ, Meuffels DE, Reijman M, Simel DL, Bierma-Zeinstra SM Does this patient with shoulder pain have rotator cuff disease?: The Rational Clinical Examination systematic review JAMA 2013'
  pmid: '23982370'
  doi: 10.1001/jama.2013.276187
triada:
  significante: Arco doloroso
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: la única prueba de provocación de dolor con cociente positivo por encima de 2, y la que mejor descarta cuando es normal
evidencia:
- concepto: HM:3055
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id001
    valor: 3.7
    ic95:
    - 1.9
    - 7.0
    ref: pmid:23982370
  lr_negativo:
    valor: 0.36
    ic95:
    - 0.23
    - 0.54
    ref: pmid:23982370
  decision: la única prueba de provocación de dolor con cociente positivo por encima de 2, y la que mejor descarta cuando es normal
- concepto: HM:3058
  rol: apoyo
  estado_lr: medido
  lr_positivo: &id002
    valor: 3.3
    ic95:
    - 1.0
    - 11
    ref: pmid:23982370
  decision: 'puede ayudar a identificar la enfermedad, pero su intervalo toca 1.0: es compatible con no aportar nada'
- concepto: HM:3059
  rol: manifestacion
  estado_lr: no_medible
  motivo: es el motivo de consulta que define la población estudiada, no una prueba dentro de ella
autoevaluacion:
- id: q1
  pregunta: En Enfermedad del manguito rotador, ¿cuál es el resultado documentado del LR positivo para «Arco doloroso»?
  concepto_id: HM:3055
  referencia_id: pmid:23982370
  pmid: '23982370'
  doi: 10.1001/jama.2013.276187
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6013
    concepto_id: HM:3055
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: la única prueba de provocación de dolor con cociente positivo por encima de 2, y la que mejor descarta cuando es normal
    advertencia: null
  opciones:
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 3.7. LR positivo: 3.7. IC del 95 %: 1.9 a 7.0. Interpretación registrada: la única prueba de provocación de dolor con cociente positivo por encima de 2, y la que mejor descarta cuando es normal.'
  - texto: 'LR positivo: 3.7.'
    correcta: true
    feedback: 'LR positivo: 3.7. IC del 95 %: 1.9 a 7.0. Interpretación registrada: la única prueba de provocación de dolor con cociente positivo por encima de 2, y la que mejor descarta cuando es normal.'
  - texto: El valor 3.7 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 3.7. IC del 95 %: 1.9 a 7.0. Interpretación registrada: la única prueba de provocación de dolor con cociente positivo por encima de 2, y la que mejor descarta cuando es normal.'
- id: q2
  pregunta: En Enfermedad del manguito rotador, ¿cuál es el resultado documentado del LR positivo para «Signo del brazo caído»?
  concepto_id: HM:3058
  referencia_id: pmid:23982370
  pmid: '23982370'
  doi: 10.1001/jama.2013.276187
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6013
    concepto_id: HM:3058
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: null
    motivo: null
    decision: 'puede ayudar a identificar la enfermedad, pero su intervalo toca 1.0: es compatible con no aportar nada'
    advertencia: null
  opciones:
  - texto: 'LR positivo: 3.3.'
    correcta: true
    feedback: 'LR positivo: 3.3. IC del 95 %: 1.0 a 11. Interpretación registrada: puede ayudar a identificar la enfermedad, pero su intervalo toca 1.0: es compatible con no aportar nada.'
  - texto: El valor 3.3 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 3.3. IC del 95 %: 1.0 a 11. Interpretación registrada: puede ayudar a identificar la enfermedad, pero su intervalo toca 1.0: es compatible con no aportar nada.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 3.3. LR positivo: 3.3. IC del 95 %: 1.0 a 11. Interpretación registrada: puede ayudar a identificar la enfermedad, pero su intervalo toca 1.0: es compatible con no aportar nada.'
---

# Enfermedad del manguito rotador

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Rotator cuff disease

## Sinónimos

patología del manguito rotador

tendinopatía del manguito

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Probabilidad basal

Rango documentado: 0.33 / 0.81; Población: pacientes derivados a especialista por dolor de hombro, en los estudios de calidad nivel 1-2; Referencia: pmid:23982370; Nota: rango tan amplio que la previa hay que tomarla del contexto propio, no de aquí

## Hallazgos clínicos

### Arco doloroso (HM:3055)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 3.7; IC del 95 %: 1.9 / 7.0; Referencia: pmid:23982370

**LR negativo:** Valor: 0.36; IC del 95 %: 0.23 / 0.54; Referencia: pmid:23982370

**Decisión:** la única prueba de provocación de dolor con cociente positivo por encima de 2, y la que mejor descarta cuando es normal

### Signo del brazo caído (HM:3058)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 3.3; IC del 95 %: 1.0 / 11; Referencia: pmid:23982370

**Decisión:** puede ayudar a identificar la enfermedad, pero su intervalo toca 1.0: es compatible con no aportar nada

### Dolor de hombro (HM:3059)

**Rol:** Manifestación

**Estado del LR:** LR no medible

**Motivo:** es el motivo de consulta que define la población estudiada, no una prueba dentro de ella

## Aspectos pendientes de documentación

La conclusión menciona la prueba de resistencia a la rotación externa entre las más precisas para la enfermedad, pero el abstract no publica su cociente. Requiere el texto completo.

## Conclusión de la fuente

El arco doloroso positivo y la prueba de resistencia a la rotación externa fueron los hallazgos más precisos para detectar la enfermedad del manguito. Como todas las maniobras las realizaron especialistas, se desconoce hasta qué punto los resultados se generalizan a población no derivada.

## Referencias y procedencia

**pmid:23982370:** Does this patient with shoulder pain have rotator cuff disease?: The Rational Clinical Examination systematic review. JAMA, 2013. DOI: 10.1001/jama.2013.276187.

Fuente clínica: medsemiotics-db, condición HM:6013.
