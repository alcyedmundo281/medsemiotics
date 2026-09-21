---
id: HM6027-01
slug: rotura-del-ligamento-cruzado-anterior-precision-semiotica
title: 'Rotura del ligamento cruzado anterior: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-09-18'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- medicina_interna
- rotura-del-ligamento-cruzado-anterior
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: e654998bddbb8c2b1d22e4da2f3375f9db6bc432
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6027-rotura-del-ligamento-cruzado-anterior.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0600-signo-de-exploracion.yaml: 86a2ac9babe66028eecc797ddbf4d9ea382a6fd685e9cb8df91bb959029d62bf
    conceptos/HM3119-prueba-de-lachman-positiva.yaml: f1262827c44da29b5f39f4f226b7715dcfc6390d26b4e2958e54e8ff18283ecd
    conceptos/HM3120-prueba-del-cajon-anterior-de-rodilla-positiva.yaml: 5d0abbc5761601b3d36e1dd38a114eea754462744b5c3ed540a913ecc4b98d95
    conceptos/HM3123-examen-compuesto-de-rodilla-positivo-para-lca.yaml: 0105b1d42c0dfce2f482b36f14d810eb57dc7c4eb859603fab51324dd9c788aa
    condiciones/HM6027-rotura-del-ligamento-cruzado-anterior.yaml: 7f6d84e236c818d0332ad1dbced4061a1edde342fe80ac367c0fa5fb74061a94
    referencias/pmid-11585485.yaml: e1de8ca5ef9d38cc51bb3337dd446e13d07426b80c8cd769c37c582f962fac61
grounding:
  condicion_id: HM:6027
  condicion_nombre: Rotura del ligamento cruzado anterior
  concepto_id: HM:3119
  concepto_nombre: Prueba de Lachman positiva
  estado_lr: medido
  lr_positivo: 25.0
  lr_negativo: 0.1
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:11585485
  referencia_cita: Solomon DH, Simel DL, Bates DW, Katz JN, Schaffer JL The rational clinical examination. Does this patient have a torn meniscus or ligament of the knee? Value of the physical examination JAMA 2001
  pmid: '11585485'
  doi: 10.1001/jama.286.13.1610
triada:
  significante: Prueba de Lachman positiva
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: la prueba clínica individual de referencia; altamente sensible y específica para confirmar o descartar rotura del LCA
evidencia:
- concepto: HM:3119
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id001
    valor: 25.0
    ic95:
    - 2.7
    - 250.0
    ref: pmid:11585485
  lr_negativo:
    valor: 0.1
    ic95:
    - 0.04
    - 0.2
    ref: pmid:11585485
  decision: la prueba clínica individual de referencia; altamente sensible y específica para confirmar o descartar rotura del LCA
- concepto: HM:3123
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id002
    valor: 25.0
    ic95:
    - 2.7
    - 250.0
    ref: pmid:11585485
  lr_negativo:
    valor: 0.04
    ic95:
    - 0.01
    - 0.4
    ref: pmid:11585485
  decision: la combinación de maniobras clínicas por un examinador entrenado descarta con fiabilidad casi absoluta (LR- 0.04)
- concepto: HM:3120
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 3.8
    ic95:
    - 0.7
    - 22.0
    ref: pmid:11585485
  decision: maniobra clásica pero con menor sensibilidad que la prueba de Lachman debido al bloqueo de isquiotibiales
autoevaluacion:
- id: q1
  pregunta: En Rotura del ligamento cruzado anterior, ¿cuál es el resultado documentado del LR positivo para «Prueba de Lachman positiva»?
  concepto_id: HM:3119
  referencia_id: pmid:11585485
  pmid: '11585485'
  doi: 10.1001/jama.286.13.1610
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6027
    concepto_id: HM:3119
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: la prueba clínica individual de referencia; altamente sensible y específica para confirmar o descartar rotura del LCA
    advertencia: null
  opciones:
  - texto: El valor 25.0 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 25.0. IC del 95 %: 2.7 a 250.0. Interpretación registrada: la prueba clínica individual de referencia; altamente sensible y específica para confirmar o descartar rotura del LCA.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 25.0. LR positivo: 25.0. IC del 95 %: 2.7 a 250.0. Interpretación registrada: la prueba clínica individual de referencia; altamente sensible y específica para confirmar o descartar rotura del LCA.'
  - texto: 'LR positivo: 25.0.'
    correcta: true
    feedback: 'LR positivo: 25.0. IC del 95 %: 2.7 a 250.0. Interpretación registrada: la prueba clínica individual de referencia; altamente sensible y específica para confirmar o descartar rotura del LCA.'
- id: q2
  pregunta: En Rotura del ligamento cruzado anterior, ¿cuál es el resultado documentado del LR positivo para «Examen compuesto de rodilla positivo para ligamento cruzado anterior»?
  concepto_id: HM:3123
  referencia_id: pmid:11585485
  pmid: '11585485'
  doi: 10.1001/jama.286.13.1610
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6027
    concepto_id: HM:3123
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: null
    motivo: null
    decision: la combinación de maniobras clínicas por un examinador entrenado descarta con fiabilidad casi absoluta (LR- 0.04)
    advertencia: null
  opciones:
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 25.0. LR positivo: 25.0. IC del 95 %: 2.7 a 250.0. Interpretación registrada: la combinación de maniobras clínicas por un examinador entrenado descarta con fiabilidad casi absoluta (LR- 0.04).'
  - texto: 'LR positivo: 25.0.'
    correcta: true
    feedback: 'LR positivo: 25.0. IC del 95 %: 2.7 a 250.0. Interpretación registrada: la combinación de maniobras clínicas por un examinador entrenado descarta con fiabilidad casi absoluta (LR- 0.04).'
  - texto: El valor 25.0 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 25.0. IC del 95 %: 2.7 a 250.0. Interpretación registrada: la combinación de maniobras clínicas por un examinador entrenado descarta con fiabilidad casi absoluta (LR- 0.04).'
---

# Rotura del ligamento cruzado anterior

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Anterior cruciate ligament tear

## Sinónimos

desgarro del LCA

rotura del ligamento cruzado de la rodilla

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Hallazgos clínicos

### Prueba de Lachman positiva (HM:3119)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 25.0; IC del 95 %: 2.7 / 250.0; Referencia: pmid:11585485

**LR negativo:** Valor: 0.1; IC del 95 %: 0.04 / 0.2; Referencia: pmid:11585485

**Decisión:** la prueba clínica individual de referencia; altamente sensible y específica para confirmar o descartar rotura del LCA

### Examen compuesto de rodilla positivo para ligamento cruzado anterior (HM:3123)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 25.0; IC del 95 %: 2.7 / 250.0; Referencia: pmid:11585485

**LR negativo:** Valor: 0.04; IC del 95 %: 0.01 / 0.4; Referencia: pmid:11585485

**Decisión:** la combinación de maniobras clínicas por un examinador entrenado descarta con fiabilidad casi absoluta (LR- 0.04)

### Prueba del cajón anterior de rodilla positiva (HM:3120)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 3.8; IC del 95 %: 0.7 / 22.0; Referencia: pmid:11585485

**Decisión:** maniobra clásica pero con menor sensibilidad que la prueba de Lachman debido al bloqueo de isquiotibiales

## Conclusión de la fuente

La prueba de Lachman es la maniobra con mayor exactitud diagnóstica para confirmar (LR+ 25) o descartar (LR- 0.1) la rotura del ligamento cruzado anterior, superando al cajón anterior.

## Referencias y procedencia

**pmid:11585485:** The rational clinical examination. Does this patient have a torn meniscus or ligament of the knee? Value of the physical examination. JAMA, 2001. DOI: 10.1001/jama.286.13.1610.

Fuente clínica: medsemiotics-db, condición HM:6027.
