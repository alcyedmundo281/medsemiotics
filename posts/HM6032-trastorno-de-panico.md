---
id: HM6032-01
slug: trastorno-de-panico-precision-semiotica
title: 'Trastorno de pánico: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-09-18'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- medicina_interna
- semiologia
- trastorno-de-panico
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: 97f51ff1d54adf8360b0e89cf56b36eb7e633e4f
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6032-trastorno-de-panico.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM3138-cuestionario-phq-panico-positivo.yaml: 2d87a17ec761d174db4b44a201334e6bfbfcd079d1ae7bb71cc28c88ac5567e3
    condiciones/HM6032-trastorno-de-panico.yaml: 9ff078266bae69107d2b13997d0c6b966f95f1c5779cc7707d131318aa86c012
    referencias/pmid-25058220.yaml: c0b00c67a6434792c8113c2fd0dcbf58e8d984f338e492cf5a56ef51f78801e3
grounding:
  condicion_id: HM:6032
  condicion_nombre: Trastorno de pánico
  concepto_id: HM:3138
  concepto_nombre: Cuestionario PHQ de pánico positivo
  estado_lr: medido
  lr_positivo: 78.0
  lr_negativo: 0.2
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:25058220
  referencia_cita: 'Herr NR, Williams JW Jr, Benjamin S, McDuffie J Does this patient have generalized anxiety or panic disorder?: The Rational Clinical Examination systematic review JAMA 2014'
  pmid: '25058220'
  doi: 10.1001/jama.2014.5950
triada:
  significante: Cuestionario PHQ de pánico positivo
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: el módulo de pánico del PHQ tiene un cociente positivo masivo (LR+ 78) y permite descartar eficazmente cuando es negativo (LR- 0.20)
evidencia:
- concepto: HM:3138
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id001
    valor: 78.0
    ic95:
    - 29.0
    - 210.0
    ref: pmid:25058220
  lr_negativo:
    valor: 0.2
    ic95:
    - 0.11
    - 0.37
    ref: pmid:25058220
  decision: el módulo de pánico del PHQ tiene un cociente positivo masivo (LR+ 78) y permite descartar eficazmente cuando es negativo (LR- 0.20)
autoevaluacion:
- id: q1
  pregunta: En Trastorno de pánico, ¿cuál es el resultado documentado del LR positivo para «Cuestionario PHQ de pánico positivo»?
  concepto_id: HM:3138
  referencia_id: pmid:25058220
  pmid: '25058220'
  doi: 10.1001/jama.2014.5950
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6032
    concepto_id: HM:3138
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: el módulo de pánico del PHQ tiene un cociente positivo masivo (LR+ 78) y permite descartar eficazmente cuando es negativo (LR- 0.20)
    advertencia: null
  opciones:
  - texto: 'LR positivo: 78.0.'
    correcta: true
    feedback: 'LR positivo: 78.0. IC del 95 %: 29.0 a 210.0. Interpretación registrada: el módulo de pánico del PHQ tiene un cociente positivo masivo (LR+ 78) y permite descartar eficazmente cuando es negativo (LR- 0.20).'
  - texto: El valor 78.0 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 78.0. IC del 95 %: 29.0 a 210.0. Interpretación registrada: el módulo de pánico del PHQ tiene un cociente positivo masivo (LR+ 78) y permite descartar eficazmente cuando es negativo (LR- 0.20).'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 78.0. LR positivo: 78.0. IC del 95 %: 29.0 a 210.0. Interpretación registrada: el módulo de pánico del PHQ tiene un cociente positivo masivo (LR+ 78) y permite descartar eficazmente cuando es negativo (LR- 0.20).'
---

# Trastorno de pánico

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Panic disorder

## Sinónimos

crisis de angustia

ataques de pánico

ansiedad paroxística episódica

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Probabilidad basal

Valor: 0.085; Población: pacientes adultos atendidos en consultas de atención primaria; Referencia: pmid:25058220

## Hallazgos clínicos

### Cuestionario PHQ de pánico positivo (HM:3138)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 78.0; IC del 95 %: 29.0 / 210.0; Referencia: pmid:25058220

**LR negativo:** Valor: 0.2; IC del 95 %: 0.11 / 0.37; Referencia: pmid:25058220

**Decisión:** el módulo de pánico del PHQ tiene un cociente positivo masivo (LR+ 78) y permite descartar eficazmente cuando es negativo (LR- 0.20)

## Conclusión de la fuente

El módulo de pánico del Patient Health Questionnaire (PHQ) es el instrumento de autoinforme más potente para detectar el trastorno de pánico en atención primaria (LR+ 78, LR- 0.20).

## Referencias y procedencia

**pmid:25058220:** Does this patient have generalized anxiety or panic disorder?: The Rational Clinical Examination systematic review. JAMA, 2014. DOI: 10.1001/jama.2014.5950.

Fuente clínica: medsemiotics-db, condición HM:6032.
