---
id: HM6025-01
slug: hipertension-arterial-secundaria-pediatrica-precision-semiotica
title: 'Hipertensión arterial secundaria pediátrica: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-09-18'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- hipertension-arterial-secundaria-pediatrica
- medicina_interna
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: fbd5cbf59e75e77b70a630f881ac1c1754e1e063
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6025-hipertension-secundaria-pediatrica.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0600-signo-de-exploracion.yaml: 86a2ac9babe66028eecc797ddbf4d9ea382a6fd685e9cb8df91bb959029d62bf
    conceptos/HM3109-antecedente-familiar-de-hipertension-secundaria.yaml: b94cc9924892778effe26baca73560d92da494a843cad864167b711670d07a18
    conceptos/HM3110-peso-bajo-percentil-10-en-nino-hipertenso.yaml: 331ece63b61eef99b3fead086aafa9c52869ff7ca2563068176947c8fe0fd43f
    conceptos/HM3111-antecedente-de-prematuridad.yaml: 585196ce7386ffb350f6f6092ea3da79ad004e57e634b0d57c3d1d583d96ca77
    conceptos/HM3112-edad-menor-o-igual-a-6-anos-con-hipertension.yaml: 0f3d824c733b4a1f19b89b595e799b5837c813ddb0daa9fe2e06717dcee17215
    conceptos/HM3113-microalbuminuria.yaml: da4ff7b2c46ac107270d48c583bb8ed001cf4dca4ca6860ae86fe8fa3f335bd1
    conceptos/HM3114-acido-urico-serico-menor-de-5-5.yaml: 2bd70c99638f2fc515bf59cade2aef38889e6c12d0e2c6d15ac963ac3e285a46
    conceptos/HM3115-carga-tensional-aumentada-en-mapa.yaml: 7a12feca239e20ac76edb71d80c2454affc58492fd27a7408d6c5f9a8b4fcc15
    condiciones/HM6025-hipertension-secundaria-pediatrica.yaml: a980cce70076b3cb074c03a31a088d57713a24bb82d5f51d62b1f71169671c61
    referencias/pmid-36976276.yaml: f142f3f34ddca77f06c307508a4b4891dfe85a82dbe3e1eb07ac907d42160105
grounding:
  condicion_id: HM:6025
  condicion_nombre: Hipertensión arterial secundaria pediátrica
  concepto_id: HM:3113
  concepto_nombre: Microalbuminuria
  estado_lr: medido
  lr_positivo: 13.0
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:36976276
  referencia_cita: 'Nugent JT, Jiang K, Funaro MC, Saran I, Young C, Ghazi L, Bakhoum CY, Wilson FP, Greenberg JH Does This Child With High Blood Pressure Have Secondary Hypertension?: The Rational Clinical Examination Systematic Review JAMA 2023'
  pmid: '36976276'
  doi: 10.1001/jama.2023.3184
triada:
  significante: Microalbuminuria
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: el marcador de daño orgánico o nefropatía subyacente con mayor LR positivo en niños hipertensos
evidencia:
- concepto: HM:3113
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id001
    valor: 13.0
    ic95:
    - 3.2
    - 53.0
    ref: pmid:36976276
  decision: el marcador de daño orgánico o nefropatía subyacente con mayor LR positivo en niños hipertensos
- concepto: HM:3115
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id002
    valor: 4.8
    ic95:
    - 1.8
    - 13.0
    ref: pmid:36976276
  decision: alteración en la monitorización ambulatoria que orienta fuertemente hacia etiología secundaria
- concepto: HM:3109
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 4.7
    ic95:
    - 1.5
    - 15.0
    ref: pmid:36976276
  decision: historia familiar de nefropatía o trastornos vasculares orienta al diagnóstico etiológico
- concepto: HM:3110
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 4.5
    ic95:
    - 1.8
    - 11.0
    ref: pmid:36976276
  decision: la delgadez o bajo peso contrasta con la HTA primaria pediátrica típica asociada a obesidad
- concepto: HM:3114
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 3.6
    ic95:
    - 1.5
    - 8.6
    ref: pmid:36976276
  decision: niveles de ácido úrico no elevados aumentan la sospecha de causa secundaria frente a primaria
- concepto: HM:3111
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 3.0
    ic95:
    - 1.2
    - 7.5
    ref: pmid:36976276
  decision: antecedente perinatal asociado a oligonefronía o trombosis de arteria renal por catéter
- concepto: HM:3112
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 2.8
    ic95:
    - 1.3
    - 6.0
    ref: pmid:36976276
  decision: a menor edad de presentación, mucho mayor probabilidad de hipertensión secundaria
autoevaluacion:
- id: q1
  pregunta: En Hipertensión arterial secundaria pediátrica, ¿cuál es el resultado documentado del LR positivo para «Microalbuminuria»?
  concepto_id: HM:3113
  referencia_id: pmid:36976276
  pmid: '36976276'
  doi: 10.1001/jama.2023.3184
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6025
    concepto_id: HM:3113
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: el marcador de daño orgánico o nefropatía subyacente con mayor LR positivo en niños hipertensos
    advertencia: null
  opciones:
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 13.0. LR positivo: 13.0. IC del 95 %: 3.2 a 53.0. Interpretación registrada: el marcador de daño orgánico o nefropatía subyacente con mayor LR positivo en niños hipertensos.'
  - texto: 'LR positivo: 13.0.'
    correcta: true
    feedback: 'LR positivo: 13.0. IC del 95 %: 3.2 a 53.0. Interpretación registrada: el marcador de daño orgánico o nefropatía subyacente con mayor LR positivo en niños hipertensos.'
  - texto: El valor 13.0 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 13.0. IC del 95 %: 3.2 a 53.0. Interpretación registrada: el marcador de daño orgánico o nefropatía subyacente con mayor LR positivo en niños hipertensos.'
- id: q2
  pregunta: En Hipertensión arterial secundaria pediátrica, ¿cuál es el resultado documentado del LR positivo para «Carga tensional aumentada en monitorización ambulatoria (MAPA)»?
  concepto_id: HM:3115
  referencia_id: pmid:36976276
  pmid: '36976276'
  doi: 10.1001/jama.2023.3184
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6025
    concepto_id: HM:3115
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: null
    motivo: null
    decision: alteración en la monitorización ambulatoria que orienta fuertemente hacia etiología secundaria
    advertencia: null
  opciones:
  - texto: 'LR positivo: 4.8.'
    correcta: true
    feedback: 'LR positivo: 4.8. IC del 95 %: 1.8 a 13.0. Interpretación registrada: alteración en la monitorización ambulatoria que orienta fuertemente hacia etiología secundaria.'
  - texto: El valor 4.8 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 4.8. IC del 95 %: 1.8 a 13.0. Interpretación registrada: alteración en la monitorización ambulatoria que orienta fuertemente hacia etiología secundaria.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 4.8. LR positivo: 4.8. IC del 95 %: 1.8 a 13.0. Interpretación registrada: alteración en la monitorización ambulatoria que orienta fuertemente hacia etiología secundaria.'
---

# Hipertensión arterial secundaria pediátrica

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Pediatric secondary hypertension

## Sinónimos

HTA secundaria en niños

hipertensión renovascular o renal pediátrica

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Probabilidad basal

Valor: 0.15; IC del 95 %: 0.1 / 0.25; Población: niños y adolescentes con confirmación de hipertensión arterial; Referencia: pmid:36976276

## Hallazgos clínicos

### Microalbuminuria (HM:3113)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 13.0; IC del 95 %: 3.2 / 53.0; Referencia: pmid:36976276

**Decisión:** el marcador de daño orgánico o nefropatía subyacente con mayor LR positivo en niños hipertensos

### Carga tensional aumentada en monitorización ambulatoria (MAPA) (HM:3115)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 4.8; IC del 95 %: 1.8 / 13.0; Referencia: pmid:36976276

**Decisión:** alteración en la monitorización ambulatoria que orienta fuertemente hacia etiología secundaria

### Antecedente familiar de hipertensión secundaria (HM:3109)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 4.7; IC del 95 %: 1.5 / 15.0; Referencia: pmid:36976276

**Decisión:** historia familiar de nefropatía o trastornos vasculares orienta al diagnóstico etiológico

### Peso menor o igual al percentil 10 en niño con hipertensión (HM:3110)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 4.5; IC del 95 %: 1.8 / 11.0; Referencia: pmid:36976276

**Decisión:** la delgadez o bajo peso contrasta con la HTA primaria pediátrica típica asociada a obesidad

### Ácido úrico sérico menor de 5.5 mg/dL (HM:3114)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 3.6; IC del 95 %: 1.5 / 8.6; Referencia: pmid:36976276

**Decisión:** niveles de ácido úrico no elevados aumentan la sospecha de causa secundaria frente a primaria

### Antecedente de prematuridad (HM:3111)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 3.0; IC del 95 %: 1.2 / 7.5; Referencia: pmid:36976276

**Decisión:** antecedente perinatal asociado a oligonefronía o trombosis de arteria renal por catéter

### Edad menor o igual a 6 años con hipertensión arterial (HM:3112)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 2.8; IC del 95 %: 1.3 / 6.0; Referencia: pmid:36976276

**Decisión:** a menor edad de presentación, mucho mayor probabilidad de hipertensión secundaria

## Conclusión de la fuente

En niños hipertensos, la microalbuminuria (LR+ 13.0), una elevada carga tensional en el MAPA (LR+ 4.8), el bajo peso para la edad (LR+ 4.5) y el debut en menores de 6 años (LR+ 2.8) son las principales claves clínicas para sospechar hipertensión secundaria.

## Referencias y procedencia

**pmid:36976276:** Does This Child With High Blood Pressure Have Secondary Hypertension?: The Rational Clinical Examination Systematic Review. JAMA, 2023. DOI: 10.1001/jama.2023.3184.

Fuente clínica: medsemiotics-db, condición HM:6025.
