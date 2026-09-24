---
id: HM6021-01
slug: trastorno-consumo-alcohol-audit-audit-c
title: 'Trastorno por consumo de alcohol: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-08-22'
author: Dr. Alcy Torres
category: psiquiatria
category_label: Psiquiatría y Atención Primaria
tags:
- psiquiatria
- semiologia
- trastorno-por-consumo-de-alcohol
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: fbd5cbf59e75e77b70a630f881ac1c1754e1e063
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6021-trastorno-consumo-alcohol.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0600-signo-de-exploracion.yaml: 86a2ac9babe66028eecc797ddbf4d9ea382a6fd685e9cb8df91bb959029d62bf
    conceptos/HM3083-cuestionario-audit-puntuacion-8-o-mas.yaml: 4ad5e1df5b1314d9c53d47f705bd4249a293d7356e44534c91b744c675e66d35
    conceptos/HM3084-cuestionario-audit-c-positivo.yaml: 60e3da4774c89b58acb80595b1f82a226028c10b8c738cf7a7e6af4e1261cb37
    conceptos/HM3085-cuestionario-audit-puntuacion-menor-8.yaml: 2be92861ce25aed9b93718a5047e7231b5269fc8f0d7ec0e99d530f31e33a406
    conceptos/HM3086-audit-postparto-puntuacion-4-o-mas.yaml: aaa992fc60e316a7203b23e37ff2d8e6f109ad56e0310cde66ad69fb875a0294
    conceptos/HM3087-tweak-t-ace-menor-2-postparto.yaml: 4b778da7722fe4d93254cea0e7d90d584d874ef12c531adbc35472dc7c1f0433
    condiciones/HM6021-trastorno-consumo-alcohol.yaml: 17f70ee11c9f4f3d631beafc361a17b2d0c9261f099cd9171852292a627f86fc
    referencias/pmid-38592385.yaml: 58bb53d39a0494342209a56cbc96e0c66000e96f4e960a6d0b9793ae0a7f7882
grounding:
  condicion_id: HM:6021
  condicion_nombre: Trastorno por consumo de alcohol
  concepto_id: HM:3083
  concepto_nombre: Cuestionario AUDIT con puntuación ≥ 8
  estado_lr: medido
  lr_positivo: 6.5
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: adultos evaluados con cuestionario AUDIT frente a criterios diagnósticos DSM-5 (n = 79 633)
  referencia_id: pmid:38592385
  referencia_cita: 'Wood E, Pan J, Cui Z, Bach P, Dennis B, Nolan S, Socias ME Does This Patient Have Alcohol Use Disorder?: The Rational Clinical Examination Systematic Review JAMA 2024'
  pmid: '38592385'
  doi: 10.1001/jama.2024.3101
triada:
  significante: Cuestionario AUDIT con puntuación ≥ 8
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: 'AUDIT ≥ 8: el instrumento estándar de cribado. Con LR+ de 6.5 global (6.9 en mujeres y 3.8 en hombres), confirma alta probabilidad de trastorno por consumo de alcohol según DSM-5 y exige intervención breve o derivación.'
evidencia:
- concepto: HM:3083
  rol: prueba_especifica
  estado_lr: medido
  poblacion: adultos evaluados con cuestionario AUDIT frente a criterios diagnósticos DSM-5 (n = 79 633)
  lr_positivo: &id001
    valor: 6.5
    ic95:
    - 3.9
    - 11
    ref: pmid:38592385
    nota: 'en mujeres el LR+ es 6.9 (IC 95%: 3.9-12); en hombres es 3.8 (IC 95%: 2.6-5.5)'
  decision: 'AUDIT ≥ 8: el instrumento estándar de cribado. Con LR+ de 6.5 global (6.9 en mujeres y 3.8 en hombres), confirma alta probabilidad de trastorno por consumo de alcohol según DSM-5 y exige intervención breve o derivación.'
- concepto: HM:3085
  rol: prueba_sensible
  estado_lr: medido
  poblacion: adultos evaluados con AUDIT
  lr_negativo: &id002
    valor: 0.33
    ic95:
    - 0.2
    - 0.52
    ref: pmid:38592385
  decision: 'AUDIT < 8: reduce la probabilidad de trastorno por consumo de alcohol (LR- 0.33) de forma consistente en mujeres y hombres.'
- concepto: HM:3084
  rol: apoyo
  estado_lr: medido
  poblacion: adultos en atención primaria
  lr_positivo:
    rango:
    - 1.8
    - 2.0
    ref: pmid:38592385
    nota: 'hombres LR+ 1.8 (IC 95%: 1.5-2.2); mujeres LR+ 2.0 (IC 95%: 1.8-2.3)'
  decision: 'AUDIT-C positivo (hombres ≥4, mujeres ≥3): útil para detectar consumo excesivo de riesgo rápido, pero modesto para confirmar trastorno por consumo formal (LR+ ~1.9).'
- concepto: HM:3086
  rol: prueba_especifica
  estado_lr: medido
  poblacion: mujeres puérperas evaluadas en las primeras 48 horas postparto
  lr_positivo:
    valor: 6.4
    ic95:
    - 5.1
    - 8.0
    ref: pmid:38592385
  decision: 'AUDIT ≥ 4 en postparto: identifica eficazmente a puérperas con alta probabilidad de trastorno por consumo de alcohol (LR+ 6.4).'
- concepto: HM:3087
  rol: prueba_sensible
  estado_lr: medido
  poblacion: mujeres puérperas evaluadas en las primeras 48 horas postparto
  lr_negativo:
    valor: 0.05
    ic95:
    - 0.01
    - 0.2
    ref: pmid:38592385
  decision: 'TWEAK o T-ACE < 2 en postparto: excelente poder de exclusión (LR- 0.05), descartando prácticamente el trastorno en esta población.'
autoevaluacion:
- id: q1
  pregunta: 'En Trastorno por consumo de alcohol, ¿cuál es el resultado documentado del LR positivo para «Cuestionario AUDIT con puntuación ≥ 8»? Población: adultos evaluados con cuestionario AUDIT frente a criterios diagnósticos DSM-5 (n = 79 633).'
  concepto_id: HM:3083
  referencia_id: pmid:38592385
  pmid: '38592385'
  doi: 10.1001/jama.2024.3101
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6021
    concepto_id: HM:3083
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: adultos evaluados con cuestionario AUDIT frente a criterios diagnósticos DSM-5 (n = 79 633)
    motivo: null
    decision: 'AUDIT ≥ 8: el instrumento estándar de cribado. Con LR+ de 6.5 global (6.9 en mujeres y 3.8 en hombres), confirma alta probabilidad de trastorno por consumo de alcohol según DSM-5 y exige intervención breve o derivación.'
    advertencia: null
  opciones:
  - texto: El valor 6.5 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 6.5. IC del 95 %: 3.9 a 11. Población: adultos evaluados con cuestionario AUDIT frente a criterios diagnósticos DSM-5 (n = 79 633). Nota: en mujeres el LR+ es 6.9 (IC 95%: 3.9-12); en hombres es 3.8 (IC 95%: 2.6-5.5). Interpretación registrada: AUDIT ≥ 8: el instrumento estándar de cribado. Con LR+ de 6.5 global (6.9 en mujeres y 3.8 en hombres), confirma alta probabilidad de trastorno por consumo de alcohol según DSM-5 y exige intervención breve o derivación.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 6.5. LR positivo: 6.5. IC del 95 %: 3.9 a 11. Población: adultos evaluados con cuestionario AUDIT frente a criterios diagnósticos DSM-5 (n = 79 633). Nota: en mujeres el LR+ es 6.9 (IC 95%: 3.9-12); en hombres es 3.8 (IC 95%: 2.6-5.5). Interpretación registrada: AUDIT ≥ 8: el instrumento estándar de cribado. Con LR+ de 6.5 global (6.9 en mujeres y 3.8 en hombres), confirma alta probabilidad de trastorno por consumo de alcohol según DSM-5 y exige intervención breve o derivación.'
  - texto: 'LR positivo: 6.5.'
    correcta: true
    feedback: 'LR positivo: 6.5. IC del 95 %: 3.9 a 11. Población: adultos evaluados con cuestionario AUDIT frente a criterios diagnósticos DSM-5 (n = 79 633). Nota: en mujeres el LR+ es 6.9 (IC 95%: 3.9-12); en hombres es 3.8 (IC 95%: 2.6-5.5). Interpretación registrada: AUDIT ≥ 8: el instrumento estándar de cribado. Con LR+ de 6.5 global (6.9 en mujeres y 3.8 en hombres), confirma alta probabilidad de trastorno por consumo de alcohol según DSM-5 y exige intervención breve o derivación.'
- id: q2
  pregunta: 'En Trastorno por consumo de alcohol, ¿cuál es el resultado documentado del LR negativo para «Cuestionario AUDIT con puntuación < 8»? Población: adultos evaluados con AUDIT.'
  concepto_id: HM:3085
  referencia_id: pmid:38592385
  pmid: '38592385'
  doi: 10.1001/jama.2024.3101
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6021
    concepto_id: HM:3085
    estado_lr: medido
    campo: lr_negativo
    dato: *id002
    poblacion: adultos evaluados con AUDIT
    motivo: null
    decision: 'AUDIT < 8: reduce la probabilidad de trastorno por consumo de alcohol (LR- 0.33) de forma consistente en mujeres y hombres.'
    advertencia: null
  opciones:
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR negativo: 0.33. LR negativo: 0.33. IC del 95 %: 0.2 a 0.52. Población: adultos evaluados con AUDIT. Interpretación registrada: AUDIT < 8: reduce la probabilidad de trastorno por consumo de alcohol (LR- 0.33) de forma consistente en mujeres y hombres.'
  - texto: 'LR negativo: 0.33.'
    correcta: true
    feedback: 'LR negativo: 0.33. IC del 95 %: 0.2 a 0.52. Población: adultos evaluados con AUDIT. Interpretación registrada: AUDIT < 8: reduce la probabilidad de trastorno por consumo de alcohol (LR- 0.33) de forma consistente en mujeres y hombres.'
  - texto: El valor 0.33 corresponde al LR positivo y no al LR negativo.
    correcta: false
    feedback: 'Ese número corresponde al LR negativo, no al LR positivo. LR negativo: 0.33. IC del 95 %: 0.2 a 0.52. Población: adultos evaluados con AUDIT. Interpretación registrada: AUDIT < 8: reduce la probabilidad de trastorno por consumo de alcohol (LR- 0.33) de forma consistente en mujeres y hombres.'
---

# Trastorno por consumo de alcohol

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Alcohol use disorder

## Sinónimos

alcoholismo

dependencia del alcohol

abuso de alcohol

consumo perjudicial de alcohol

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Factores de riesgo

Factor: Antecedente familiar de trastorno por consumo de sustancias

Factor: Inicio precoz del consumo de alcohol en la adolescencia

Factor: Trastornos psiquiátricos comórbidos (depresión, ansiedad)

## Hallazgos clínicos

### Cuestionario AUDIT con puntuación ≥ 8 (HM:3083)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Población:** adultos evaluados con cuestionario AUDIT frente a criterios diagnósticos DSM-5 (n = 79 633)

**LR positivo:** Valor: 6.5; IC del 95 %: 3.9 / 11; Referencia: pmid:38592385; Nota: en mujeres el LR+ es 6.9 (IC 95%: 3.9-12); en hombres es 3.8 (IC 95%: 2.6-5.5)

**Decisión:** AUDIT ≥ 8: el instrumento estándar de cribado. Con LR+ de 6.5 global (6.9 en mujeres y 3.8 en hombres), confirma alta probabilidad de trastorno por consumo de alcohol según DSM-5 y exige intervención breve o derivación.

### Cuestionario AUDIT con puntuación < 8 (HM:3085)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**Población:** adultos evaluados con AUDIT

**LR negativo:** Valor: 0.33; IC del 95 %: 0.2 / 0.52; Referencia: pmid:38592385

**Decisión:** AUDIT < 8: reduce la probabilidad de trastorno por consumo de alcohol (LR- 0.33) de forma consistente en mujeres y hombres.

### Cuestionario AUDIT-C positivo (hombres ≥ 4, mujeres ≥ 3) (HM:3084)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**Población:** adultos en atención primaria

**LR positivo:** Rango documentado: 1.8 / 2.0; Referencia: pmid:38592385; Nota: hombres LR+ 1.8 (IC 95%: 1.5-2.2); mujeres LR+ 2.0 (IC 95%: 1.8-2.3)

**Decisión:** AUDIT-C positivo (hombres ≥4, mujeres ≥3): útil para detectar consumo excesivo de riesgo rápido, pero modesto para confirmar trastorno por consumo formal (LR+ ~1.9).

### Cuestionario AUDIT con puntuación ≥ 4 en postparto (HM:3086)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Población:** mujeres puérperas evaluadas en las primeras 48 horas postparto

**LR positivo:** Valor: 6.4; IC del 95 %: 5.1 / 8.0; Referencia: pmid:38592385

**Decisión:** AUDIT ≥ 4 en postparto: identifica eficazmente a puérperas con alta probabilidad de trastorno por consumo de alcohol (LR+ 6.4).

### Cuestionario TWEAK o T-ACE con puntuación < 2 en postparto (HM:3087)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**Población:** mujeres puérperas evaluadas en las primeras 48 horas postparto

**LR negativo:** Valor: 0.05; IC del 95 %: 0.01 / 0.2; Referencia: pmid:38592385

**Decisión:** TWEAK o T-ACE < 2 en postparto: excelente poder de exclusión (LR- 0.05), descartando prácticamente el trastorno en esta población.

## Conclusión de la fuente

El cuestionario AUDIT (≥ 8) es la herramienta más útil para identificar trastorno por consumo de alcohol según el DSM-5 en adultos (LR+ 6.5; LR- 0.33). El AUDIT-C es adecuado para consumo de riesgo. En el postparto inmediato, el AUDIT ≥ 4 confirma (LR+ 6.4) y las herramientas TWEAK/T-ACE < 2 descartan con gran exactitud (LR- 0.05).

## Referencias y procedencia

**pmid:38592385:** Does This Patient Have Alcohol Use Disorder?: The Rational Clinical Examination Systematic Review. JAMA, 2024. DOI: 10.1001/jama.2024.3101.

Fuente clínica: medsemiotics-db, condición HM:6021.
