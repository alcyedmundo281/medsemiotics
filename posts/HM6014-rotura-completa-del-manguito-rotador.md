---
id: HM6014-01
slug: rotura-completa-del-manguito-rotador-precision-semiotica
title: 'Rotura completa del manguito rotador: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-08-21'
author: Dr. Alcy Torres
category: traumatologia
category_label: Traumatología y Medicina Deportiva
tags:
- rotura-completa-del-manguito-rotador
- semiologia
- traumatologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: f2e95a0834f2c2789e6cc56b5610d9612bdec93b
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6014-rotura-completa-del-manguito-rotador.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM3056-lag-rotacion-externa.yaml: 89f1056f9840213b12973fd986960c9acce2cd4e1659313609b9f348683f8464
    conceptos/HM3057-lag-rotacion-interna.yaml: af8fb988476f76fe41cf62414d3d78eb79c6c92ae5e378f150ac4ec2cf6b5bed
    condiciones/HM6014-rotura-completa-del-manguito-rotador.yaml: 948a520a9c00092a5e3a1fd4b58e9745c3cd733f976167157f29f89c4437c6d0
    referencias/pmid-23982370.yaml: a069ef6d93f543653e62805872e4ffaf929021cd19668bcb2eb3b5413613c18b
grounding:
  condicion_id: HM:6014
  condicion_nombre: Rotura completa del manguito rotador
  concepto_id: HM:3057
  concepto_nombre: Signo de lag de rotación interna
  estado_lr: medido
  lr_positivo: 5.6
  lr_negativo: 0.04
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:23982370
  referencia_cita: 'Hermans J, Luime JJ, Meuffels DE, Reijman M, Simel DL, Bierma-Zeinstra SM Does this patient with shoulder pain have rotator cuff disease?: The Rational Clinical Examination systematic review JAMA 2013'
  pmid: '23982370'
  doi: 10.1001/jama.2013.276187
triada:
  significante: Signo de lag de rotación interna
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: 'sirve en ambos sentidos y su normalidad es lo más preciso para descartar la rotura completa. Ojo con el extremo inferior del intervalo: llega a 0, lo que refleja series pequeñas, no certeza absoluta.'
evidencia:
- concepto: HM:3056
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id002
    valor: 7.2
    ic95:
    - 1.7
    - 31
    ref: pmid:23982370
  decision: el cociente más alto para la rotura completa, con intervalo muy ancho
- concepto: HM:3057
  rol: prueba_sensible
  estado_lr: medido
  lr_positivo: &id001
    valor: 5.6
    ic95:
    - 2.6
    - 12
    ref: pmid:23982370
  lr_negativo:
    valor: 0.04
    ic95:
    - 0.0
    - 0.58
    ref: pmid:23982370
  decision: 'sirve en ambos sentidos y su normalidad es lo más preciso para descartar la rotura completa. Ojo con el extremo inferior del intervalo: llega a 0, lo que refleja series pequeñas, no certeza absoluta.'
autoevaluacion:
- id: q1
  pregunta: En Rotura completa del manguito rotador, ¿cuál es el resultado documentado del LR positivo para «Signo de lag de rotación interna»?
  concepto_id: HM:3057
  referencia_id: pmid:23982370
  pmid: '23982370'
  doi: 10.1001/jama.2013.276187
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6014
    concepto_id: HM:3057
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: 'sirve en ambos sentidos y su normalidad es lo más preciso para descartar la rotura completa. Ojo con el extremo inferior del intervalo: llega a 0, lo que refleja series pequeñas, no certeza absoluta.'
    advertencia: null
  opciones:
  - texto: 'LR positivo: 5.6.'
    correcta: true
    feedback: 'LR positivo: 5.6. IC del 95 %: 2.6 a 12. Interpretación registrada: sirve en ambos sentidos y su normalidad es lo más preciso para descartar la rotura completa. Ojo con el extremo inferior del intervalo: llega a 0, lo que refleja series pequeñas, no certeza absoluta.'
  - texto: El valor 5.6 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 5.6. IC del 95 %: 2.6 a 12. Interpretación registrada: sirve en ambos sentidos y su normalidad es lo más preciso para descartar la rotura completa. Ojo con el extremo inferior del intervalo: llega a 0, lo que refleja series pequeñas, no certeza absoluta.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 5.6. LR positivo: 5.6. IC del 95 %: 2.6 a 12. Interpretación registrada: sirve en ambos sentidos y su normalidad es lo más preciso para descartar la rotura completa. Ojo con el extremo inferior del intervalo: llega a 0, lo que refleja series pequeñas, no certeza absoluta.'
- id: q2
  pregunta: En Rotura completa del manguito rotador, ¿cuál es el resultado documentado del LR positivo para «Signo de lag de rotación externa»?
  concepto_id: HM:3056
  referencia_id: pmid:23982370
  pmid: '23982370'
  doi: 10.1001/jama.2013.276187
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6014
    concepto_id: HM:3056
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: null
    motivo: null
    decision: el cociente más alto para la rotura completa, con intervalo muy ancho
    advertencia: null
  opciones:
  - texto: El valor 7.2 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 7.2. IC del 95 %: 1.7 a 31. Interpretación registrada: el cociente más alto para la rotura completa, con intervalo muy ancho.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 7.2. LR positivo: 7.2. IC del 95 %: 1.7 a 31. Interpretación registrada: el cociente más alto para la rotura completa, con intervalo muy ancho.'
  - texto: 'LR positivo: 7.2.'
    correcta: true
    feedback: 'LR positivo: 7.2. IC del 95 %: 1.7 a 31. Interpretación registrada: el cociente más alto para la rotura completa, con intervalo muy ancho.'
---

# Rotura completa del manguito rotador

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Full-thickness rotator cuff tear

## Sinónimos

rotura de espesor completo del manguito

desgarro transmural del manguito

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Hallazgos clínicos

### Signo de lag de rotación externa (HM:3056)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 7.2; IC del 95 %: 1.7 / 31; Referencia: pmid:23982370

**Decisión:** el cociente más alto para la rotura completa, con intervalo muy ancho

### Signo de lag de rotación interna (HM:3057)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**LR positivo:** Valor: 5.6; IC del 95 %: 2.6 / 12; Referencia: pmid:23982370

**LR negativo:** Valor: 0.04; IC del 95 %: 0.0 / 0.58; Referencia: pmid:23982370

**Decisión:** sirve en ambos sentidos y su normalidad es lo más preciso para descartar la rotura completa. Ojo con el extremo inferior del intervalo: llega a 0, lo que refleja series pequeñas, no certeza absoluta.

## Conclusión de la fuente

La presencia de un signo de lag positivo, de rotación externa o interna, fue lo más preciso para diagnosticar la rotura de espesor completo del manguito rotador.

## Referencias y procedencia

**pmid:23982370:** Does this patient with shoulder pain have rotator cuff disease?: The Rational Clinical Examination systematic review. JAMA, 2013. DOI: 10.1001/jama.2013.276187.

Fuente clínica: medsemiotics-db, condición HM:6014.
