---
id: HM6031-01
slug: trastorno-de-ansiedad-generalizada-precision-semiotica
title: 'Trastorno de ansiedad generalizada: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-09-18'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- medicina_interna
- semiologia
- trastorno-de-ansiedad-generalizada
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: fbd5cbf59e75e77b70a630f881ac1c1754e1e063
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6031-trastorno-de-ansiedad-generalizada.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0001-hallazgo-clinico.yaml: 5cf5cbb0a6ce5c773fd60ad80c8b467259ad4d480cd2cd60aa1335d5c8b65329
    conceptos/HM3137-cuestionario-gad7-positivo.yaml: 135b9bc5ba635c2a20eabe0de9721b6702c2c7d8830c5f56cd9f9a2d221ff94e
    condiciones/HM6031-trastorno-de-ansiedad-generalizada.yaml: 7401b2b5e3b058e58f1417121ede0e2a0c351ffd1945b66fa797f177cde27402
    referencias/pmid-25058220.yaml: c0b00c67a6434792c8113c2fd0dcbf58e8d984f338e492cf5a56ef51f78801e3
grounding:
  condicion_id: HM:6031
  condicion_nombre: Trastorno de ansiedad generalizada
  concepto_id: HM:3137
  concepto_nombre: Cuestionario GAD-7 positivo
  estado_lr: medido
  lr_positivo: 5.1
  lr_negativo: 0.13
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:25058220
  referencia_cita: 'Herr NR, Williams JW Jr, Benjamin S, McDuffie J Does this patient have generalized anxiety or panic disorder?: The Rational Clinical Examination systematic review JAMA 2014'
  pmid: '25058220'
  doi: 10.1001/jama.2014.5950
triada:
  significante: Cuestionario GAD-7 positivo
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: la escala GAD-7 es el mejor instrumento de cribado en atención primaria, con alta capacidad tanto confirmatoria como de exclusión (LR- 0.13)
evidencia:
- concepto: HM:3137
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id001
    valor: 5.1
    ic95:
    - 4.3
    - 6.0
    ref: pmid:25058220
  lr_negativo:
    valor: 0.13
    ic95:
    - 0.07
    - 0.25
    ref: pmid:25058220
  decision: la escala GAD-7 es el mejor instrumento de cribado en atención primaria, con alta capacidad tanto confirmatoria como de exclusión (LR- 0.13)
autoevaluacion:
- id: q1
  pregunta: En Trastorno de ansiedad generalizada, ¿cuál es el resultado documentado del LR positivo para «Cuestionario GAD-7 positivo»?
  concepto_id: HM:3137
  referencia_id: pmid:25058220
  pmid: '25058220'
  doi: 10.1001/jama.2014.5950
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6031
    concepto_id: HM:3137
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: la escala GAD-7 es el mejor instrumento de cribado en atención primaria, con alta capacidad tanto confirmatoria como de exclusión (LR- 0.13)
    advertencia: null
  opciones:
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 5.1. LR positivo: 5.1. IC del 95 %: 4.3 a 6.0. Interpretación registrada: la escala GAD-7 es el mejor instrumento de cribado en atención primaria, con alta capacidad tanto confirmatoria como de exclusión (LR- 0.13).'
  - texto: 'LR positivo: 5.1.'
    correcta: true
    feedback: 'LR positivo: 5.1. IC del 95 %: 4.3 a 6.0. Interpretación registrada: la escala GAD-7 es el mejor instrumento de cribado en atención primaria, con alta capacidad tanto confirmatoria como de exclusión (LR- 0.13).'
  - texto: El valor 5.1 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 5.1. IC del 95 %: 4.3 a 6.0. Interpretación registrada: la escala GAD-7 es el mejor instrumento de cribado en atención primaria, con alta capacidad tanto confirmatoria como de exclusión (LR- 0.13).'
---

# Trastorno de ansiedad generalizada

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Generalized anxiety disorder

## Sinónimos

TAG

GAD

ansiedad crónica

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Probabilidad basal

Valor: 0.092; Población: pacientes adultos en centros de atención primaria; Referencia: pmid:25058220

## Hallazgos clínicos

### Cuestionario GAD-7 positivo (HM:3137)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 5.1; IC del 95 %: 4.3 / 6.0; Referencia: pmid:25058220

**LR negativo:** Valor: 0.13; IC del 95 %: 0.07 / 0.25; Referencia: pmid:25058220

**Decisión:** la escala GAD-7 es el mejor instrumento de cribado en atención primaria, con alta capacidad tanto confirmatoria como de exclusión (LR- 0.13)

## Conclusión de la fuente

El cuestionario GAD-7 presenta excelentes características de rendimiento diagnóstico para detectar el trastorno de ansiedad generalizada en atención primaria (LR+ 5.1, LR- 0.13) y es factible de implementar en la práctica clínica diaria.

## Referencias y procedencia

**pmid:25058220:** Does this patient have generalized anxiety or panic disorder?: The Rational Clinical Examination systematic review. JAMA, 2014. DOI: 10.1001/jama.2014.5950.

Fuente clínica: medsemiotics-db, condición HM:6031.
