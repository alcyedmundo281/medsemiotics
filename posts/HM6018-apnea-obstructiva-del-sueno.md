---
id: HM6018-01
slug: apnea-obstructiva-del-sueno-precision-semiotica
title: 'Apnea obstructiva del sueño: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-08-21'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- apnea-obstructiva-del-sueno
- medicina_interna
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: a6b2afeb208457aaf6ce2d86ff78304f45071d5b
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6018-apnea-obstructiva-del-sueno.yaml
  archivos:
    CITATION.cff: e2840db4d37cfb43ebe9835e23c1acfef6352e730051918fa0cbd9fe6fad77d7
    conceptos/HM3072-ahogo-o-jadeo-nocturno.yaml: bb978561f85d04ea3c3d96596aed38b1fccd27c88a0c6855cef56cdc1d111d92
    conceptos/HM3073-ronquido.yaml: 7b20f9582eab041322e5a8b9209a4bd214bb831c3476d25c74ffa78bec5d4f5b
    conceptos/HM3074-indice-de-masa-corporal-bajo.yaml: 55a3f9877aee395d377f92bd9235307ef18d9a02c85c6345d8529b2256949caa
    condiciones/HM6018-apnea-obstructiva-del-sueno.yaml: 1cf4cd6512f8168487b509b4c743cb9f7dcec67eec9581cbd642e8213c950d82
    referencias/pmid-23989984.yaml: adade58f82c42307bf63354293d2c8ce4a392f3f9cc3e4e5291fec62b652fad0
grounding:
  condicion_id: HM:6018
  condicion_nombre: Apnea obstructiva del sueño
  concepto_id: HM:3072
  concepto_nombre: Ahogo o jadeo nocturno
  estado_lr: medido
  lr_positivo: 3.3
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:23989984
  referencia_cita: 'Myers KA, Mrkobrada M, Simel DL Does this patient have obstructive sleep apnea?: The Rational Clinical Examination systematic review JAMA 2013'
  pmid: '23989984'
  doi: 10.1001/jama.2013.276185
triada:
  significante: Ahogo o jadeo nocturno
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: la observación aislada más útil de la revisión para identificar apnea obstructiva del sueño
evidencia:
- concepto: HM:3072
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id001
    valor: 3.3
    ic95:
    - 2.1
    - 4.6
    umbral_condicion: IAH ≥10/h
    ref: pmid:23989984
  decision: la observación aislada más útil de la revisión para identificar apnea obstructiva del sueño
- concepto: HM:3073
  rol: apoyo
  estado_lr: medido
  lr_positivo: &id002
    valor: 1.1
    ic95:
    - 1.0
    - 1.1
    ref: pmid:23989984
  decision: frecuente en la enfermedad, pero el cociente pegado a 1.0 significa que no sirve para establecer el diagnóstico por sí solo
  advertencia: un hallazgo casi universal en la sospecha clínica que, precisamente por serlo, no discrimina nada
autoevaluacion:
- id: q1
  pregunta: En Apnea obstructiva del sueño, ¿cuál es el resultado documentado del LR positivo para «Ahogo o jadeo nocturno»?
  concepto_id: HM:3072
  referencia_id: pmid:23989984
  pmid: '23989984'
  doi: 10.1001/jama.2013.276185
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6018
    concepto_id: HM:3072
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: la observación aislada más útil de la revisión para identificar apnea obstructiva del sueño
    advertencia: null
  opciones:
  - texto: El valor 3.3 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 3.3. IC del 95 %: 2.1 a 4.6. Interpretación registrada: la observación aislada más útil de la revisión para identificar apnea obstructiva del sueño.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 3.3. LR positivo: 3.3. IC del 95 %: 2.1 a 4.6. Interpretación registrada: la observación aislada más útil de la revisión para identificar apnea obstructiva del sueño.'
  - texto: 'LR positivo: 3.3.'
    correcta: true
    feedback: 'LR positivo: 3.3. IC del 95 %: 2.1 a 4.6. Interpretación registrada: la observación aislada más útil de la revisión para identificar apnea obstructiva del sueño.'
- id: q2
  pregunta: En Apnea obstructiva del sueño, ¿cuál es el resultado documentado del LR positivo para «Ronquido»?
  concepto_id: HM:3073
  referencia_id: pmid:23989984
  pmid: '23989984'
  doi: 10.1001/jama.2013.276185
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6018
    concepto_id: HM:3073
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: null
    motivo: null
    decision: frecuente en la enfermedad, pero el cociente pegado a 1.0 significa que no sirve para establecer el diagnóstico por sí solo
    advertencia: un hallazgo casi universal en la sospecha clínica que, precisamente por serlo, no discrimina nada
  opciones:
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 1.1. LR positivo: 1.1. IC del 95 %: 1.0 a 1.1. Interpretación registrada: frecuente en la enfermedad, pero el cociente pegado a 1.0 significa que no sirve para establecer el diagnóstico por sí solo. Advertencia: un hallazgo casi universal en la sospecha clínica que, precisamente por serlo, no discrimina nada.'
  - texto: 'LR positivo: 1.1.'
    correcta: true
    feedback: 'LR positivo: 1.1. IC del 95 %: 1.0 a 1.1. Interpretación registrada: frecuente en la enfermedad, pero el cociente pegado a 1.0 significa que no sirve para establecer el diagnóstico por sí solo. Advertencia: un hallazgo casi universal en la sospecha clínica que, precisamente por serlo, no discrimina nada.'
  - texto: El valor 1.1 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 1.1. IC del 95 %: 1.0 a 1.1. Interpretación registrada: frecuente en la enfermedad, pero el cociente pegado a 1.0 significa que no sirve para establecer el diagnóstico por sí solo. Advertencia: un hallazgo casi universal en la sospecha clínica que, precisamente por serlo, no discrimina nada.'
---

# Apnea obstructiva del sueño

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Obstructive sleep apnea

## Sinónimos

SAOS

apnea del sueño

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Probabilidad basal

Rango documentado: 0.02 / 0.9; Población: 2%-14% en cribado comunitario, 21%-90% en pacientes derivados a evaluación del sueño; varía además con el umbral de IAH usado (≥5/h: 14%; ≥15/h: 6%; ≥5/h con síntomas: 2%-4%); Referencia: pmid:23989984; Nota: tres variables mueven este número a la vez —tipo de población, umbral de IAH, y si exige síntomas—, así que no hay una previa única que citar sin fijar las tres

## Hallazgos clínicos

### Ahogo o jadeo nocturno (HM:3072)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 3.3; IC del 95 %: 2.1 / 4.6; Umbral condicion: IAH ≥10/h; Referencia: pmid:23989984

**Decisión:** la observación aislada más útil de la revisión para identificar apnea obstructiva del sueño

### Ronquido (HM:3073)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 1.1; IC del 95 %: 1.0 / 1.1; Referencia: pmid:23989984

**Decisión:** frecuente en la enfermedad, pero el cociente pegado a 1.0 significa que no sirve para establecer el diagnóstico por sí solo

**Advertencia:** un hallazgo casi universal en la sospecha clínica que, precisamente por serlo, no discrimina nada

## Aspectos pendientes de documentación

La fuente publica un cociente combinado real que este índice no estructura todavía: «ronquido leve y IMC menor de 26» tiene LR− 0.07 (IC95% 0.03-0.19) para descartar apnea moderada o grave (IAH ≥15/h). No es una arista de un solo concepto —combina HM:3073 con un umbral de HM:3074— y `reglas` está pensado para criterios con nombre propio pendientes de activar, no para una combinación con cociente ya publicado. Se declara aquí en vez de forzarla en un campo que no la describe bien; entrará estructurada cuando el esquema tenga un lugar para cocientes combinados de dos hallazgos.

## Conclusión de la fuente

El ahogo o jadeo nocturno es el indicador clínico aislado más fiable de apnea obstructiva del sueño; el ronquido, en cambio, es poco específico. La exploración clínica es útil para seleccionar a quién derivar a pruebas diagnósticas definitivas.

## Referencias y procedencia

**pmid:23989984:** Does this patient have obstructive sleep apnea?: The Rational Clinical Examination systematic review. JAMA, 2013. DOI: 10.1001/jama.2013.276185.

Fuente clínica: medsemiotics-db, condición HM:6018.
