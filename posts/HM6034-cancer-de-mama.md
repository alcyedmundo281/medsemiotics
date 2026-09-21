---
id: HM6034-01
slug: cancer-de-mama-precision-semiotica
title: 'Cáncer de mama: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-09-18'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- cancer-de-mama
- medicina_interna
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: 97f51ff1d54adf8360b0e89cf56b36eb7e633e4f
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6034-cancer-de-mama.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM3142-masa-mamaria-palpable-sospechosa.yaml: f11f27c1edc99011448c3818fbae8799dad25cbd5df600b47f5f6136f60218c9
    conceptos/HM3143-examen-clinico-mamario-reglado-normal.yaml: 5a107bc0bf6672b131ceac761664ae19eca3bbb043d0291ba6fb0a72992dd450
    condiciones/HM6034-cancer-de-mama.yaml: eab87d90399daf8948d669883195f2284c932252bf03bab648bc5c922eaead2f
    referencias/pmid-10517431.yaml: 8ebe10c6f72dd592a497d527f6bc8a3d8cbdc4cd8b626cf974280489fe49e662
grounding:
  condicion_id: HM:6034
  condicion_nombre: Cáncer de mama
  concepto_id: HM:3142
  concepto_nombre: Masa mamaria palpable o hallazgo sospechoso en la exploración
  estado_lr: medido
  lr_positivo: 10.6
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:10517431
  referencia_cita: 'Barton MB, Harris R, Fletcher SW The rational clinical examination. Does this patient have breast cancer? The screening clinical breast examination: should it be done? How? JAMA 1999'
  pmid: '10517431'
  doi: 10.1001/jama.282.13.1270
  sensibilidad: 0.54
  especificidad: 0.94
triada:
  significante: Masa mamaria palpable o hallazgo sospechoso en la exploración
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: el hallazgo de una masa dominante o nódulo sospechoso en el examen clínico eleva marcadamente la probabilidad (LR+ 10.6)
evidencia:
- concepto: HM:3142
  rol: prueba_especifica
  estado_lr: medido
  sensibilidad: 0.54
  especificidad: 0.94
  lr_positivo: &id001
    valor: 10.6
    ic95:
    - 5.8
    - 19.2
    ref: pmid:10517431
  decision: el hallazgo de una masa dominante o nódulo sospechoso en el examen clínico eleva marcadamente la probabilidad (LR+ 10.6)
- concepto: HM:3143
  rol: prueba_sensible
  estado_lr: medido
  lr_negativo: &id002
    valor: 0.47
    ic95:
    - 0.4
    - 0.56
    ref: pmid:10517431
  decision: una palpación normal reduce la probabilidad de forma modesta (LR- 0.47) pero no excluye la necesidad de mamografía de cribado
autoevaluacion:
- id: q1
  pregunta: En Cáncer de mama, ¿cuál es el resultado documentado del LR positivo para «Masa mamaria palpable o hallazgo sospechoso en la exploración»?
  concepto_id: HM:3142
  referencia_id: pmid:10517431
  pmid: '10517431'
  doi: 10.1001/jama.282.13.1270
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6034
    concepto_id: HM:3142
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: el hallazgo de una masa dominante o nódulo sospechoso en el examen clínico eleva marcadamente la probabilidad (LR+ 10.6)
    advertencia: null
  opciones:
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 10.6. LR positivo: 10.6. IC del 95 %: 5.8 a 19.2. Interpretación registrada: el hallazgo de una masa dominante o nódulo sospechoso en el examen clínico eleva marcadamente la probabilidad (LR+ 10.6).'
  - texto: 'LR positivo: 10.6.'
    correcta: true
    feedback: 'LR positivo: 10.6. IC del 95 %: 5.8 a 19.2. Interpretación registrada: el hallazgo de una masa dominante o nódulo sospechoso en el examen clínico eleva marcadamente la probabilidad (LR+ 10.6).'
  - texto: El valor 10.6 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 10.6. IC del 95 %: 5.8 a 19.2. Interpretación registrada: el hallazgo de una masa dominante o nódulo sospechoso en el examen clínico eleva marcadamente la probabilidad (LR+ 10.6).'
- id: q2
  pregunta: En Cáncer de mama, ¿cuál es el resultado documentado del LR negativo para «Examen clínico de mama reglado normal»?
  concepto_id: HM:3143
  referencia_id: pmid:10517431
  pmid: '10517431'
  doi: 10.1001/jama.282.13.1270
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6034
    concepto_id: HM:3143
    estado_lr: medido
    campo: lr_negativo
    dato: *id002
    poblacion: null
    motivo: null
    decision: una palpación normal reduce la probabilidad de forma modesta (LR- 0.47) pero no excluye la necesidad de mamografía de cribado
    advertencia: null
  opciones:
  - texto: 'LR negativo: 0.47.'
    correcta: true
    feedback: 'LR negativo: 0.47. IC del 95 %: 0.4 a 0.56. Interpretación registrada: una palpación normal reduce la probabilidad de forma modesta (LR- 0.47) pero no excluye la necesidad de mamografía de cribado.'
  - texto: El valor 0.47 corresponde al LR positivo y no al LR negativo.
    correcta: false
    feedback: 'Ese número corresponde al LR negativo, no al LR positivo. LR negativo: 0.47. IC del 95 %: 0.4 a 0.56. Interpretación registrada: una palpación normal reduce la probabilidad de forma modesta (LR- 0.47) pero no excluye la necesidad de mamografía de cribado.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR negativo: 0.47. LR negativo: 0.47. IC del 95 %: 0.4 a 0.56. Interpretación registrada: una palpación normal reduce la probabilidad de forma modesta (LR- 0.47) pero no excluye la necesidad de mamografía de cribado.'
---

# Cáncer de mama

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Breast cancer

## Sinónimos

carcinoma mamario

neoplasia maligna de mama

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Hallazgos clínicos

### Masa mamaria palpable o hallazgo sospechoso en la exploración (HM:3142)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Sensibilidad:** 0.54

**Especificidad:** 0.94

**LR positivo:** Valor: 10.6; IC del 95 %: 5.8 / 19.2; Referencia: pmid:10517431

**Decisión:** el hallazgo de una masa dominante o nódulo sospechoso en el examen clínico eleva marcadamente la probabilidad (LR+ 10.6)

### Examen clínico de mama reglado normal (HM:3143)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**LR negativo:** Valor: 0.47; IC del 95 %: 0.4 / 0.56; Referencia: pmid:10517431

**Decisión:** una palpación normal reduce la probabilidad de forma modesta (LR- 0.47) pero no excluye la necesidad de mamografía de cribado

## Conclusión de la fuente

La exploración clínica mamaria (CBE) reglada y minuciosa de al menos 3 minutos por mama es una herramienta diagnóstica complementaria relevante: un resultado positivo tiene un cociente de 10.6 (especificidad 94%), aunque un examen normal no descarta la enfermedad (LR- 0.47).

## Referencias y procedencia

**pmid:10517431:** The rational clinical examination. Does this patient have breast cancer? The screening clinical breast examination: should it be done? How?. JAMA, 1999. DOI: 10.1001/jama.282.13.1270.

Fuente clínica: medsemiotics-db, condición HM:6034.
