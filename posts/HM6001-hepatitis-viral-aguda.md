---
id: HM6001-01
slug: hepatitis-viral-aguda-precision-semiotica
title: 'Hepatitis viral aguda: hallazgos y evidencia clínica'
subtitle: Hallazgos y criterios clínicos sin cocientes de verosimilitud medidos.
date: '2026-09-02'
author: Dr. Alcy Torres
category: gastroenterologia
category_label: Gastroenterología
tags:
- gastroenterologia
- hepatitis-viral-aguda
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: a6b2afeb208457aaf6ce2d86ff78304f45071d5b
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6001-hepatitis-viral-aguda.yaml
  archivos:
    CITATION.cff: e2840db4d37cfb43ebe9835e23c1acfef6352e730051918fa0cbd9fe6fad77d7
    conceptos/HM0101-fiebre.yaml: fb16183d00cc93f60aff82d7904798fe984a3cef751a56e41e3d4f82bd58cc93
    conceptos/HM0203-dolor-en-hipocondrio-derecho.yaml: c247a6de7fe880329b9949ead27eb93991f9d824dc7c06a2924e8f3d93e1361f
    conceptos/HM0305-ictericia.yaml: 87323a0b278fc5c8d70ae931a46478eccb092cec8330f28434d136003b6ad270
    conceptos/HM0306-coluria.yaml: 103fe65f0cbe26bc6e06f186234246227b04cde241b8ec4625ff30ddfe01ef2e
    conceptos/HM0307-acolia.yaml: d753e6cbaa96116d92baa7836ec987a3eec9284280c8199b688051df744e6aef
    conceptos/HM0602-hepatomegalia.yaml: 51c18ec466026b08b337817e2c5b004960c0f3862e814e6d629ec27d375618aa
    conceptos/HM0733-elevacion-de-transaminasas.yaml: 57ca69d57c386aea3a46015b76181a5ff05fdae4adfe53f0b16c52abb4e3762e
    conceptos/HM0745-hiperbilirrubinemia.yaml: ea9070ab1927760a0d4257c84bd763673fe29378372f3ac7bdf3028761480e92
    conceptos/HM0801-astenia.yaml: 95bc981acd8d63bc1c693bd3ba572e4e714a900777e0d933281d82d22bcaa097
    conceptos/HM0802-anorexia.yaml: 41f5d159539277ac7fb97cdefeefb66395ea5f70741a4d577bb22efed5940bba
    condiciones/HM6001-hepatitis-viral-aguda.yaml: 5289dc6268987469b2bfd8fa5ebae8fa70066f1bfc491f518e4106cbe979b225
grounding:
  condicion_id: HM:6001
  condicion_nombre: Hepatitis viral aguda
  concepto_id: HM:0305
  concepto_nombre: Ictericia
  estado_lr: no_medible
  lr_positivo: null
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: null
  referencia_cita: null
  pmid: null
  doi: null
triada:
  significante: Ictericia
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: La fuente no documenta una decisión específica para este hallazgo.
evidencia:
- concepto: HM:0305
  rol: manifestacion
  estado_lr: no_medible
  motivo: forma parte de la definición de caso; sesgo de incorporación
- concepto: HM:0306
  rol: manifestacion
  estado_lr: no_medido
- concepto: HM:0307
  rol: manifestacion
  estado_lr: no_medido
- concepto: HM:0733
  rol: prueba_sensible
  estado_lr: no_medible
  motivo: forma parte de la definición de caso; sesgo de incorporación
- concepto: HM:0745
  rol: apoyo
  estado_lr: no_medible
  motivo: forma parte de la definición de caso; sesgo de incorporación
- concepto: HM:0203
  rol: apoyo
  estado_lr: no_medido
- concepto: HM:0602
  rol: apoyo
  estado_lr: no_medido
- concepto: HM:0101
  rol: apoyo
  estado_lr: no_medido
- concepto: HM:0801
  rol: apoyo
  estado_lr: no_medido
- concepto: HM:0802
  rol: apoyo
  estado_lr: no_medido
autoevaluacion:
- id: q1
  pregunta: ¿Cómo está documentado el LR de Ictericia en Hepatitis viral aguda?
  concepto_id: HM:0305
  referencia_id: null
  pmid: null
  doi: null
  opciones:
  - texto: LR no medible
    correcta: true
    feedback: 'Registro HM:6001: LR no medible'
  - texto: Hay una estimación numérica única disponible para calcular la probabilidad posterior.
    correcta: false
    feedback: 'El registro documenta: LR no medible'
- id: q2
  pregunta: ¿Cómo está documentado el LR de Coluria en Hepatitis viral aguda?
  concepto_id: HM:0306
  referencia_id: null
  pmid: null
  doi: null
  opciones:
  - texto: Hay una estimación numérica única disponible para calcular la probabilidad posterior.
    correcta: false
    feedback: 'El registro documenta: LR no medido'
  - texto: LR no medido
    correcta: true
    feedback: 'Registro HM:6001: LR no medido'
---

# Hepatitis viral aguda

Hallazgos y criterios clínicos sin cocientes de verosimilitud medidos.

## Nombre en inglés

Acute viral hepatitis

## Sinónimos

hepatitis aguda

hepatitis A

hepatitis vírica aguda

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Hallazgos clínicos

### Ictericia (HM:0305)

**Rol:** Manifestación

**Estado del LR:** LR no medible

**Motivo:** forma parte de la definición de caso; sesgo de incorporación

### Coluria (HM:0306)

**Rol:** Manifestación

**Estado del LR:** LR no medido

### Acolia (HM:0307)

**Rol:** Manifestación

**Estado del LR:** LR no medido

### Elevación de transaminasas (HM:0733)

**Rol:** Prueba sensible

**Estado del LR:** LR no medible

**Motivo:** forma parte de la definición de caso; sesgo de incorporación

### Hiperbilirrubinemia (HM:0745)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR no medible

**Motivo:** forma parte de la definición de caso; sesgo de incorporación

### Dolor en hipocondrio derecho (HM:0203)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR no medido

### Hepatomegalia (HM:0602)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR no medido

### Fiebre (HM:0101)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR no medido

### Astenia (HM:0801)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR no medido

### Anorexia (HM:0802)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR no medido

## Referencias y procedencia

Fuente clínica: medsemiotics-db, condición HM:6001.
