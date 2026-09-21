---
id: HM6003-01
slug: mononucleosis-infecciosa-adenopatias-linfocitos-atipicos
title: 'Mononucleosis infecciosa: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-08-21'
author: Dr. Alcy Torres
category: infectologia
category_label: Infectología y Medicina Interna
tags:
- infectologia
- mononucleosis-infecciosa
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: e654998bddbb8c2b1d22e4da2f3375f9db6bc432
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6003-mononucleosis-infecciosa.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0211-odinofagia.yaml: cdb3be1c4118ddfbdbf416bfee31243ab624779e988a089984d8f863ad51551f
    conceptos/HM0603-esplenomegalia.yaml: d694a903ae98ee750e432f8b2f95e52b856440a67ebef8ea14396108447626a6
    conceptos/HM0607-adenopatias.yaml: f06993f52d4da10988e367f6b1f9de12b802d261ce4cf6c6c9879a4761f0e561
    conceptos/HM0801-astenia.yaml: 95bc981acd8d63bc1c693bd3ba572e4e714a900777e0d933281d82d22bcaa097
    conceptos/HM3001-adenopatia-cervical-posterior.yaml: 771bd6d4c7525ad532de18c2977bb2420d1abba7ed1f0f5d2c57444eb6f7467f
    conceptos/HM3002-adenopatia-inguinal-o-axilar.yaml: ed55476401fe6508e8147f39abd6c52d6ef52ed15a2eb21037d33892a19b7283
    conceptos/HM3003-petequias-en-paladar.yaml: 64eecce570f47b537bf1f3a38f89bfefe8f6ec6d2babe3acbccb65e82935e5ad
    conceptos/HM3004-linfocitosis-atipica.yaml: 1e115e6db2ec1f26c0a14a915b5490531f21ae8de6938767a68809d9cc32b1ea
    condiciones/HM6003-mononucleosis-infecciosa.yaml: ad06be6c03439dcfab6bad9012bfdc3553e229daae0870deec069eeb40f46c09
    referencias/pmid-27115266.yaml: 668a562cc651aa3a28a6b5f3e3519ad1b80287b8bf35f31c7f32225a9013f17b
grounding:
  condicion_id: HM:6003
  condicion_nombre: Mononucleosis infecciosa
  concepto_id: HM:3001
  concepto_nombre: Adenopatía cervical posterior
  estado_lr: medido
  lr_positivo: 3.1
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:27115266
  referencia_cita: 'Ebell MH, Call M, Shinholser J, Gardner J Does This Patient Have Infectious Mononucleosis?: The Rational Clinical Examination Systematic Review JAMA 2016'
  pmid: '27115266'
  doi: 10.1001/jama.2016.2111
  especificidad: 0.87
triada:
  significante: Adenopatía cervical posterior
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: aumenta la probabilidad; por sí sola no confirma
evidencia:
- concepto: HM:3001
  rol: prueba_especifica
  estado_lr: medido
  especificidad: 0.87
  lr_positivo: &id001
    valor: 3.1
    ic95:
    - 1.6
    - 5.9
    ref: pmid:27115266
  decision: aumenta la probabilidad; por sí sola no confirma
- concepto: HM:3002
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id002
    rango:
    - 3.0
    - 3.1
    ref: pmid:27115266
    nota: rango entre estudios; la fuente no da estimación resumida
  decision: aumenta la probabilidad de forma similar a la cervical posterior
- concepto: HM:3003
  rol: prueba_especifica
  estado_lr: medido
  especificidad: 0.95
  lr_positivo:
    valor: 5.3
    ic95:
    - 2.1
    - 13
    ref: pmid:27115266
  decision: el hallazgo exploratorio que más aumenta la probabilidad
- concepto: HM:0603
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo:
    rango:
    - 1.9
    - 6.6
    ref: pmid:27115266
    nota: rango entre estudios, con especificidad de 0.71 a 0.99. La amplitud refleja lo mucho que depende del explorador.
  decision: apoya el diagnóstico y condiciona el consejo de evitar deporte de contacto
- concepto: HM:0607
  rol: prueba_sensible
  estado_lr: medido
  sensibilidad: 0.91
  lr_negativo:
    rango:
    - 0.23
    - 0.44
    ref: pmid:27115266
    nota: la fuente lo expresa como el LR positivo de la AUSENCIA de adenopatías, que es el cociente negativo del hallazgo.
  decision: su ausencia reduce la probabilidad; es el hallazgo que más descarta
- concepto: HM:0211
  rol: manifestacion
  estado_lr: sin_efecto
  sensibilidad: 0.81
  motivo: '«symptoms are of limited value»: sensible (0.81-0.83) pero inespecífico. La fuente no publica cociente porque no discrimina.'
- concepto: HM:0801
  rol: manifestacion
  estado_lr: sin_efecto
  motivo: sensible (0.81-0.83) pero inespecífico; la fuente no publica cociente
- concepto: HM:3004
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo:
    valor: 11.4
    ic95:
    - 2.7
    - 35
    umbral: linfocitos atípicos ≥ 10%
    ref: pmid:27115266
  decision: a partir del 10% ya desplaza la probabilidad con fuerza
  graduacion:
    parametro: Linfocitos atípicos
    unidad: '%'
    lectura: acumulativo
  tramos:
  - umbral: linfocitos atípicos ≥ 10%
    desde: 10
    lr_positivo: 11.4
    ic95:
    - 2.7
    - 35
    ref: pmid:27115266
  - umbral: linfocitos atípicos ≥ 20%
    desde: 20
    lr_positivo: 26
    ic95:
    - 9.6
    - 68
    ref: pmid:27115266
  - umbral: linfocitos atípicos ≥ 40%
    desde: 40
    lr_positivo: 50
    ic95:
    - 38
    - 64
    ref: pmid:27115266
  - umbral: linfocitos > 50% y atípicos > 10%
    lr_positivo: 54
    ic95:
    - 8.4
    - 189
    especificidad: 0.99
    ref: pmid:27115266
autoevaluacion:
- id: q1
  pregunta: En Mononucleosis infecciosa, ¿cuál es el resultado documentado del LR positivo para «Adenopatía cervical posterior»?
  concepto_id: HM:3001
  referencia_id: pmid:27115266
  pmid: '27115266'
  doi: 10.1001/jama.2016.2111
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6003
    concepto_id: HM:3001
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: aumenta la probabilidad; por sí sola no confirma
    advertencia: null
  opciones:
  - texto: El valor 3.1 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 3.1. IC del 95 %: 1.6 a 5.9. Interpretación registrada: aumenta la probabilidad; por sí sola no confirma.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 3.1. LR positivo: 3.1. IC del 95 %: 1.6 a 5.9. Interpretación registrada: aumenta la probabilidad; por sí sola no confirma.'
  - texto: 'LR positivo: 3.1.'
    correcta: true
    feedback: 'LR positivo: 3.1. IC del 95 %: 1.6 a 5.9. Interpretación registrada: aumenta la probabilidad; por sí sola no confirma.'
- id: q2
  pregunta: Al evaluar «Adenopatía inguinal o axilar» en Mononucleosis infecciosa, ¿cómo debe comunicarse el LR positivo según la fuente?
  concepto_id: HM:3002
  referencia_id: pmid:27115266
  pmid: '27115266'
  doi: 10.1001/jama.2016.2111
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6003
    concepto_id: HM:3002
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: null
    motivo: null
    decision: aumenta la probabilidad de forma similar a la cervical posterior
    advertencia: null
  opciones:
  - texto: 'LR positivo: 3.1, como estimación puntual única.'
    correcta: false
    feedback: '3.1 es el límite superior del rango documentado, no una estimación puntual. LR positivo: rango de 3.0 a 3.1; no se registra una estimación puntual única. Nota: rango entre estudios; la fuente no da estimación resumida. Interpretación registrada: aumenta la probabilidad de forma similar a la cervical posterior.'
  - texto: 'LR positivo: rango de 3.0 a 3.1; no se registra una estimación puntual única.'
    correcta: true
    feedback: 'LR positivo: rango de 3.0 a 3.1; no se registra una estimación puntual única. Nota: rango entre estudios; la fuente no da estimación resumida. Interpretación registrada: aumenta la probabilidad de forma similar a la cervical posterior.'
  - texto: 'LR positivo: 3.0, como estimación puntual única.'
    correcta: false
    feedback: '3.0 es el límite inferior del rango documentado, no una estimación puntual. LR positivo: rango de 3.0 a 3.1; no se registra una estimación puntual única. Nota: rango entre estudios; la fuente no da estimación resumida. Interpretación registrada: aumenta la probabilidad de forma similar a la cervical posterior.'
---

# Mononucleosis infecciosa

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Infectious mononucleosis

## Sinónimos

mononucleosis

enfermedad del beso

infección aguda por virus de Epstein-Barr

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Probabilidad basal

Valor: 0.077; Población: pacientes de 16 a 20 años que consultan por odinofagia; Referencia: pmid:27115266

## Factores de riesgo

Factor: Edad entre 5 y 25 años; Referencia: pmid:27115266; Nota: máxima frecuencia entre los 16 y 20 años

## Hallazgos clínicos

### Adenopatía cervical posterior (HM:3001)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Especificidad:** 0.87

**LR positivo:** Valor: 3.1; IC del 95 %: 1.6 / 5.9; Referencia: pmid:27115266

**Decisión:** aumenta la probabilidad; por sí sola no confirma

### Adenopatía inguinal o axilar (HM:3002)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Rango documentado: 3.0 / 3.1; Referencia: pmid:27115266; Nota: rango entre estudios; la fuente no da estimación resumida

**Decisión:** aumenta la probabilidad de forma similar a la cervical posterior

### Petequias en paladar (HM:3003)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Especificidad:** 0.95

**LR positivo:** Valor: 5.3; IC del 95 %: 2.1 / 13; Referencia: pmid:27115266

**Decisión:** el hallazgo exploratorio que más aumenta la probabilidad

### Esplenomegalia (HM:0603)

**Significante:** Polo inferior del bazo palpable por debajo del reborde costal izquierdo en decúbito supino o decúbito lateral derecho (maniobra bimanual o de Middleton), o percusión mate anormal en el área esplénica (HM:3184, HM:3185).

**Significado:** Aumento patológico del volumen o masa esplénica más allá de sus límites fisiológicos normales.

**Falsos positivos:** Ptosis esplénica (bazo móvil o desplazado caudalmente sin incremento de masa) / Masa en polo inferior de riñón izquierdo o hidronefrosis / Tumor retroperitoneal o masa dependiente del ángulo esplénico del colon

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Rango documentado: 1.9 / 6.6; Referencia: pmid:27115266; Nota: rango entre estudios, con especificidad de 0.71 a 0.99. La amplitud refleja lo mucho que depende del explorador.

**Decisión:** apoya el diagnóstico y condiciona el consejo de evitar deporte de contacto

### Adenopatías (HM:0607)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**Sensibilidad:** 0.91

**LR negativo:** Rango documentado: 0.23 / 0.44; Referencia: pmid:27115266; Nota: la fuente lo expresa como el LR positivo de la AUSENCIA de adenopatías, que es el cociente negativo del hallazgo.

**Decisión:** su ausencia reduce la probabilidad; es el hallazgo que más descarta

### Odinofagia (HM:0211)

**Rol:** Manifestación

**Estado del LR:** Sin efecto discriminativo

**Sensibilidad:** 0.81

**Motivo:** «symptoms are of limited value»: sensible (0.81-0.83) pero inespecífico. La fuente no publica cociente porque no discrimina.

### Astenia (HM:0801)

**Rol:** Manifestación

**Estado del LR:** Sin efecto discriminativo

**Motivo:** sensible (0.81-0.83) pero inespecífico; la fuente no publica cociente

### Linfocitosis atípica (HM:3004)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 11.4; IC del 95 %: 2.7 / 35; Umbral: linfocitos atípicos ≥ 10%; Referencia: pmid:27115266

**Decisión:** a partir del 10% ya desplaza la probabilidad con fuerza

**Graduación:** Parámetro: Linfocitos atípicos; Unidad: %; Lectura: acumulativo

**Tramos:** Umbral: linfocitos atípicos ≥ 10%; Desde: 10; LR positivo: 11.4; IC del 95 %: 2.7 / 35; Referencia: pmid:27115266 / Umbral: linfocitos atípicos ≥ 20%; Desde: 20; LR positivo: 26; IC del 95 %: 9.6 / 68; Referencia: pmid:27115266 / Umbral: linfocitos atípicos ≥ 40%; Desde: 40; LR positivo: 50; IC del 95 %: 38 / 64; Referencia: pmid:27115266 / Umbral: linfocitos > 50% y atípicos > 10%; LR positivo: 54; IC del 95 %: 8.4 / 189; Especificidad: 0.99; Referencia: pmid:27115266

## Referencias y procedencia

**pmid:27115266:** Does This Patient Have Infectious Mononucleosis?: The Rational Clinical Examination Systematic Review. JAMA, 2016. DOI: 10.1001/jama.2016.2111.

Fuente clínica: medsemiotics-db, condición HM:6003.
