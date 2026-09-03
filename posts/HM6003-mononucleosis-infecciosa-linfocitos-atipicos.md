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
  revision: a6b2afeb208457aaf6ce2d86ff78304f45071d5b
  condicion: condiciones/HM6003-mononucleosis-infecciosa.yaml
  archivos:
    conceptos/HM0211-odinofagia.yaml: cdb3be1c4118ddfbdbf416bfee31243ab624779e988a089984d8f863ad51551f
    conceptos/HM0603-esplenomegalia.yaml: 91ae572020e5fae4f29d8937cd19223374e4f2feffab036fdbf5b99085fdd0a5
    conceptos/HM0607-adenopatias.yaml: f06993f52d4da10988e367f6b1f9de12b802d261ce4cf6c6c9879a4761f0e561
    conceptos/HM0801-astenia.yaml: 95bc981acd8d63bc1c693bd3ba572e4e714a900777e0d933281d82d22bcaa097
    conceptos/HM3001-adenopatia-cervical-posterior.yaml: 771bd6d4c7525ad532de18c2977bb2420d1abba7ed1f0f5d2c57444eb6f7467f
    conceptos/HM3002-adenopatia-inguinal-o-axilar.yaml: ed55476401fe6508e8147f39abd6c52d6ef52ed15a2eb21037d33892a19b7283
    conceptos/HM3003-petequias-en-paladar.yaml: 64eecce570f47b537bf1f3a38f89bfefe8f6ec6d2babe3acbccb65e82935e5ad
    conceptos/HM3004-linfocitosis-atipica.yaml: 1e115e6db2ec1f26c0a14a915b5490531f21ae8de6938767a68809d9cc32b1ea
    condiciones/HM6003-mononucleosis-infecciosa.yaml: a09354b3a9d4e54f2ae83ceddb09caf69b8f76f4f155ef031223ada310a90371
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
  lr_positivo:
    valor: 3.1
    ic95:
    - 1.6
    - 5.9
    ref: pmid:27115266
  decision: aumenta la probabilidad; por sí sola no confirma
- concepto: HM:3002
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo:
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
  tramos:
  - umbral: linfocitos atípicos ≥ 10%
    lr_positivo: 11.4
    ic95:
    - 2.7
    - 35
    ref: pmid:27115266
  - umbral: linfocitos atípicos ≥ 20%
    lr_positivo: 26
    ic95:
    - 9.6
    - 68
    ref: pmid:27115266
  - umbral: linfocitos atípicos ≥ 40%
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
  pregunta: ¿Qué cociente registra la fuente para Adenopatía cervical posterior en Mononucleosis infecciosa?
  concepto_id: HM:3001
  referencia_id: pmid:27115266
  pmid: '27115266'
  doi: 10.1001/jama.2016.2111
  opciones:
  - texto: 'LR positivo: 3.1.'
    correcta: true
    feedback: 'Registro HM:6003: LR positivo: 3.1.'
  - texto: La fuente no registra ningún cociente medido para este hallazgo.
    correcta: false
    feedback: 'El registro documenta: LR positivo: 3.1.'
- id: q2
  pregunta: ¿Cómo está documentado el LR de Adenopatía inguinal o axilar en Mononucleosis infecciosa?
  concepto_id: HM:3002
  referencia_id: pmid:27115266
  pmid: '27115266'
  doi: 10.1001/jama.2016.2111
  opciones:
  - texto: Hay una estimación numérica única disponible para calcular la probabilidad posterior.
    correcta: false
    feedback: 'El registro documenta: La fuente registra un rango, no una estimación numérica única.'
  - texto: La fuente registra un rango, no una estimación numérica única.
    correcta: true
    feedback: 'Registro HM:6003: La fuente registra un rango, no una estimación numérica única.'
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

**Tramos:** Umbral: linfocitos atípicos ≥ 10%; LR positivo: 11.4; IC del 95 %: 2.7 / 35; Referencia: pmid:27115266 / Umbral: linfocitos atípicos ≥ 20%; LR positivo: 26; IC del 95 %: 9.6 / 68; Referencia: pmid:27115266 / Umbral: linfocitos atípicos ≥ 40%; LR positivo: 50; IC del 95 %: 38 / 64; Referencia: pmid:27115266 / Umbral: linfocitos > 50% y atípicos > 10%; LR positivo: 54; IC del 95 %: 8.4 / 189; Especificidad: 0.99; Referencia: pmid:27115266

## Referencias y procedencia

**pmid:27115266:** Does This Patient Have Infectious Mononucleosis?: The Rational Clinical Examination Systematic Review. JAMA, 2016. DOI: 10.1001/jama.2016.2111.

Fuente clínica: medsemiotics-db, condición HM:6003.
