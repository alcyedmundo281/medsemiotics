---
id: HM6026-01
slug: insuficiencia-aortica-precision-semiotica
title: 'Insuficiencia aórtica: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-09-18'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- insuficiencia-aortica
- medicina_interna
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: e654998bddbb8c2b1d22e4da2f3375f9db6bc432
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6026-insuficiencia-aortica.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0109-hipotension-arterial.yaml: 934b7dadbc768a08d34a84a322bb11c8008218f7b111b1bba2b766e67f4db7cc
    conceptos/HM0600-signo-de-exploracion.yaml: 86a2ac9babe66028eecc797ddbf4d9ea382a6fd685e9cb8df91bb959029d62bf
    conceptos/HM0608-soplo-cardiaco.yaml: 47bf7c076b53036a2d48cedd74b74aaa26ba69f1cb243c07f96afcc8a0068475
    conceptos/HM3116-soplo-diastolico-precoz.yaml: 37b9bc68c6c7ee2c103f014c04aa4010b9ecf1d5cb019f825457e043e24a29d4
    conceptos/HM3117-presion-de-pulso-amplia.yaml: 778885d546492a734b8df1094da2e6b4ba9dc11ec4717fbf453e522dd6b5f396
    conceptos/HM3118-maniobra-de-oclusion-arterial-transitoria.yaml: b8dde95621d686f2bfd5b7640530fc8bd766200ed4b9ce2d5903dafbc1800482
    condiciones/HM6026-insuficiencia-aortica.yaml: 225ba4e8acc7794a1930bef4f5600cd5656ce3170baf1f6b27a7cbc49a9ea623
    referencias/pmid-10376577.yaml: feae2c2a3d4086c1a6dcc4485d2cb32bb3de83d22ce185ee1f213cce2b8f8d8a
grounding:
  condicion_id: HM:6026
  condicion_nombre: Insuficiencia aórtica
  concepto_id: HM:3116
  concepto_nombre: Soplo diastólico precoz
  estado_lr: medido
  lr_positivo: 8.8
  lr_negativo: 0.2
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:10376577
  referencia_cita: Choudhry NK, Etchells EE The rational clinical examination. Does this patient have aortic regurgitation? JAMA 1999
  pmid: '10376577'
  doi: 10.1001/jama.281.23.2231
triada:
  significante: Soplo diastólico precoz
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: el signo físico cardinal; su presencia confirma fuertemente (LR+ 8.8) y su ausencia reduce marcadamente la probabilidad (LR- 0.20)
evidencia:
- concepto: HM:3116
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id001
    valor: 8.8
    ic95:
    - 7.3
    - 11.0
    ref: pmid:10376577
  lr_negativo:
    valor: 0.2
    ic95:
    - 0.1
    - 0.3
    ref: pmid:10376577
  decision: el signo físico cardinal; su presencia confirma fuertemente (LR+ 8.8) y su ausencia reduce marcadamente la probabilidad (LR- 0.20)
- concepto: HM:3118
  rol: apoyo
  estado_lr: medido
  lr_positivo: &id002
    valor: 8.4
    ic95:
    - 3.9
    - 18.0
    ref: pmid:10376577
  lr_negativo:
    valor: 0.3
    ic95:
    - 0.1
    - 0.7
    ref: pmid:10376577
  decision: la maniobra de oclusión con manguito acentúa el soplo diastólico con excelente rendimiento diagnóstico
- concepto: HM:3117
  rol: apoyo
  estado_lr: no_medido
  motivo: signo hemodinámico clásico de regurgitación aórtica moderada o severa
autoevaluacion:
- id: q1
  pregunta: En Insuficiencia aórtica, ¿cuál es el resultado documentado del LR positivo para «Soplo diastólico precoz»?
  concepto_id: HM:3116
  referencia_id: pmid:10376577
  pmid: '10376577'
  doi: 10.1001/jama.281.23.2231
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6026
    concepto_id: HM:3116
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: el signo físico cardinal; su presencia confirma fuertemente (LR+ 8.8) y su ausencia reduce marcadamente la probabilidad (LR- 0.20)
    advertencia: null
  opciones:
  - texto: 'LR positivo: 8.8.'
    correcta: true
    feedback: 'LR positivo: 8.8. IC del 95 %: 7.3 a 11.0. Interpretación registrada: el signo físico cardinal; su presencia confirma fuertemente (LR+ 8.8) y su ausencia reduce marcadamente la probabilidad (LR- 0.20).'
  - texto: El valor 8.8 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 8.8. IC del 95 %: 7.3 a 11.0. Interpretación registrada: el signo físico cardinal; su presencia confirma fuertemente (LR+ 8.8) y su ausencia reduce marcadamente la probabilidad (LR- 0.20).'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 8.8. LR positivo: 8.8. IC del 95 %: 7.3 a 11.0. Interpretación registrada: el signo físico cardinal; su presencia confirma fuertemente (LR+ 8.8) y su ausencia reduce marcadamente la probabilidad (LR- 0.20).'
- id: q2
  pregunta: En Insuficiencia aórtica, ¿cuál es el resultado documentado del LR positivo para «Maniobra de oclusión arterial transitoria»?
  concepto_id: HM:3118
  referencia_id: pmid:10376577
  pmid: '10376577'
  doi: 10.1001/jama.281.23.2231
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6026
    concepto_id: HM:3118
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: null
    motivo: null
    decision: la maniobra de oclusión con manguito acentúa el soplo diastólico con excelente rendimiento diagnóstico
    advertencia: null
  opciones:
  - texto: El valor 8.4 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 8.4. IC del 95 %: 3.9 a 18.0. Interpretación registrada: la maniobra de oclusión con manguito acentúa el soplo diastólico con excelente rendimiento diagnóstico.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 8.4. LR positivo: 8.4. IC del 95 %: 3.9 a 18.0. Interpretación registrada: la maniobra de oclusión con manguito acentúa el soplo diastólico con excelente rendimiento diagnóstico.'
  - texto: 'LR positivo: 8.4.'
    correcta: true
    feedback: 'LR positivo: 8.4. IC del 95 %: 3.9 a 18.0. Interpretación registrada: la maniobra de oclusión con manguito acentúa el soplo diastólico con excelente rendimiento diagnóstico.'
---

# Insuficiencia aórtica

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Aortic regurgitation

## Sinónimos

regurgitación aórtica

valvulopatía aórtica incompetente

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Hallazgos clínicos

### Soplo diastólico precoz (HM:3116)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 8.8; IC del 95 %: 7.3 / 11.0; Referencia: pmid:10376577

**LR negativo:** Valor: 0.2; IC del 95 %: 0.1 / 0.3; Referencia: pmid:10376577

**Decisión:** el signo físico cardinal; su presencia confirma fuertemente (LR+ 8.8) y su ausencia reduce marcadamente la probabilidad (LR- 0.20)

### Maniobra de oclusión arterial transitoria (HM:3118)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 8.4; IC del 95 %: 3.9 / 18.0; Referencia: pmid:10376577

**LR negativo:** Valor: 0.3; IC del 95 %: 0.1 / 0.7; Referencia: pmid:10376577

**Decisión:** la maniobra de oclusión con manguito acentúa el soplo diastólico con excelente rendimiento diagnóstico

### Presión de pulso amplia (HM:3117)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR no medido

**Motivo:** signo hemodinámico clásico de regurgitación aórtica moderada o severa

## Conclusión de la fuente

La auscultación de un soplo diastólico precoz es el signo más potente para diagnosticar o descartar la insuficiencia aórtica (LR+ 8.8, LR- 0.20). Maniobras como la oclusión arterial transitoria aumentan la sensibilidad de la auscultación en casos dudosos.

## Referencias y procedencia

**pmid:10376577:** The rational clinical examination. Does this patient have aortic regurgitation?. JAMA, 1999. DOI: 10.1001/jama.281.23.2231.

Fuente clínica: medsemiotics-db, condición HM:6026.
