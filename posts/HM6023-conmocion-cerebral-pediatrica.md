---
id: HM6023-01
slug: conmocion-cerebral-pediatrica-precision-semiotica
title: 'Conmoción cerebral pediátrica: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-09-18'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- conmocion-cerebral-pediatrica
- medicina_interna
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: e654998bddbb8c2b1d22e4da2f3375f9db6bc432
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6023-conmocion-cerebral-pediatrica.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0105-bradicardia.yaml: 088974edd57d3a795e8df4a594180e440f0821a08fc12ef6e4a22f7af9d66607
    conceptos/HM0201-dolor-abdominal.yaml: 564819078999f876e7aa0107eaa37bedc03a6e883b9722492cede175c5cb7bda
    conceptos/HM3094-niebla-mental.yaml: edba2bd487bfd1c0b34a33f4762a78d33e6911ef7373b14badff7a1f96c3f03f
    conceptos/HM3095-fonofobia-o-sensibilidad-al-ruido.yaml: ebcd511d4f323df138cd1d4a8dcced8d5673d99c1b49af975e5cf15ee120445e
    conceptos/HM3096-fotofobia-o-sensibilidad-a-la-luz.yaml: bf007f38615273e68025c7f51a03ad2aa99bc7d92c8fa306dd8f016fc022a4fc
    conceptos/HM3097-punto-proximo-de-convergencia-anormal.yaml: e652c6a21318fffa323862abb88f3570d077900498ce2d079519c99bc55530fd
    conceptos/HM3098-movimientos-de-persecucion-suave-anormales.yaml: 48ebc6227ba3c681a5d3e0bd6378be7aeac41aea9ea2d3d4ff15c290fbfae32c
    conceptos/HM3099-sacadas-oculares-anormales.yaml: 96dba68766d1678acadb7b30e890122f25fdf325f812b05371553369e90db62b
    condiciones/HM6023-conmocion-cerebral-pediatrica.yaml: d63ec5841dbc0749f78ad4ecc2b45254ed5262b4756783b72eb83551b7c57a8c
    referencias/pmid-41941197.yaml: 18cbdb879da36a79aef7d6c8911332329c408e68df1052682cb850affb3dd528
grounding:
  condicion_id: HM:6023
  condicion_nombre: Conmoción cerebral pediátrica
  concepto_id: HM:3094
  concepto_nombre: Niebla mental
  estado_lr: medido
  lr_positivo: 11.9
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:41941197
  referencia_cita: 'Shah SN, Chizuk HM, Fong HF, Hannon M, Mannix RC Does This Child Have a Concussion?: The Rational Clinical Examination Systematic Review JAMA 2026'
  pmid: '41941197'
  doi: 10.1001/jama.2026.1233
triada:
  significante: Niebla mental
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: el síntoma cognitivo autoinformado con mayor LR positivo en la evaluación postraumática
evidencia:
- concepto: HM:3094
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id001
    valor: 11.9
    ic95:
    - 5.2
    - 27.0
    ref: pmid:41941197
  decision: el síntoma cognitivo autoinformado con mayor LR positivo en la evaluación postraumática
- concepto: HM:3097
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id002
    valor: 7.0
    ic95:
    - 3.1
    - 16.0
    ref: pmid:41941197
  decision: el signo físico oculomotor más potente del examen vestibular/ocular motor (VOMS)
- concepto: HM:3095
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 6.9
    ic95:
    - 3.4
    - 14.0
    ref: pmid:41941197
  decision: hipersensibilidad sensorial fuertemente indicativa de disfunción corticosensorial aguda
- concepto: HM:0105
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 6.7
    ic95:
    - 3.5
    - 13.0
    ref: pmid:41941197
  decision: síntoma neurovegetativo precoz muy prevalente tras conmoción cerebral
- concepto: HM:3096
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 5.6
    ic95:
    - 2.9
    - 11.0
    ref: pmid:41941197
  decision: síntoma sensorial complementario de alta especificidad
- concepto: HM:3098
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 4.5
    ic95:
    - 2.0
    - 10.0
    ref: pmid:41941197
  decision: signo exploratorio de afectación cerebelosa o de vías de seguimiento visual
- concepto: HM:3099
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 4.4
    ic95:
    - 2.0
    - 9.7
    ref: pmid:41941197
  decision: dismetría sacádica indicativa de alteración en la coordinación ocular rápida
- concepto: HM:0201
  rol: prueba_sensible
  estado_lr: medido
  lr_positivo:
    valor: 0.2
    ic95:
    - 0.1
    - 0.4
    ref: pmid:41941197
  dispara_si: ausente
  efecto: excluye
  sostiene: discriminacion_medida
  ref: pmid:41941197
  decision: la ausencia completa de cefalea reduce sustancialmente la probabilidad de conmoción cerebral (LR 0.20)
autoevaluacion:
- id: q1
  pregunta: En Conmoción cerebral pediátrica, ¿cuál es el resultado documentado del LR positivo para «Niebla mental»?
  concepto_id: HM:3094
  referencia_id: pmid:41941197
  pmid: '41941197'
  doi: 10.1001/jama.2026.1233
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6023
    concepto_id: HM:3094
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: el síntoma cognitivo autoinformado con mayor LR positivo en la evaluación postraumática
    advertencia: null
  opciones:
  - texto: 'LR positivo: 11.9.'
    correcta: true
    feedback: 'LR positivo: 11.9. IC del 95 %: 5.2 a 27.0. Interpretación registrada: el síntoma cognitivo autoinformado con mayor LR positivo en la evaluación postraumática.'
  - texto: El valor 11.9 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 11.9. IC del 95 %: 5.2 a 27.0. Interpretación registrada: el síntoma cognitivo autoinformado con mayor LR positivo en la evaluación postraumática.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 11.9. LR positivo: 11.9. IC del 95 %: 5.2 a 27.0. Interpretación registrada: el síntoma cognitivo autoinformado con mayor LR positivo en la evaluación postraumática.'
- id: q2
  pregunta: En Conmoción cerebral pediátrica, ¿cuál es el resultado documentado del LR positivo para «Punto próximo de convergencia anormal»?
  concepto_id: HM:3097
  referencia_id: pmid:41941197
  pmid: '41941197'
  doi: 10.1001/jama.2026.1233
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6023
    concepto_id: HM:3097
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: null
    motivo: null
    decision: el signo físico oculomotor más potente del examen vestibular/ocular motor (VOMS)
    advertencia: null
  opciones:
  - texto: El valor 7.0 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 7.0. IC del 95 %: 3.1 a 16.0. Interpretación registrada: el signo físico oculomotor más potente del examen vestibular/ocular motor (VOMS).'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 7.0. LR positivo: 7.0. IC del 95 %: 3.1 a 16.0. Interpretación registrada: el signo físico oculomotor más potente del examen vestibular/ocular motor (VOMS).'
  - texto: 'LR positivo: 7.0.'
    correcta: true
    feedback: 'LR positivo: 7.0. IC del 95 %: 3.1 a 16.0. Interpretación registrada: el signo físico oculomotor más potente del examen vestibular/ocular motor (VOMS).'
---

# Conmoción cerebral pediátrica

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Pediatric concussion

## Sinónimos

traumatismo craneoencefálico leve pediátrico

concusión cerebral en niños

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Hallazgos clínicos

### Niebla mental (HM:3094)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 11.9; IC del 95 %: 5.2 / 27.0; Referencia: pmid:41941197

**Decisión:** el síntoma cognitivo autoinformado con mayor LR positivo en la evaluación postraumática

### Punto próximo de convergencia anormal (HM:3097)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 7.0; IC del 95 %: 3.1 / 16.0; Referencia: pmid:41941197

**Decisión:** el signo físico oculomotor más potente del examen vestibular/ocular motor (VOMS)

### Fonofobia o sensibilidad al ruido (HM:3095)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 6.9; IC del 95 %: 3.4 / 14.0; Referencia: pmid:41941197

**Decisión:** hipersensibilidad sensorial fuertemente indicativa de disfunción corticosensorial aguda

### Bradicardia (HM:0105)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 6.7; IC del 95 %: 3.5 / 13.0; Referencia: pmid:41941197

**Decisión:** síntoma neurovegetativo precoz muy prevalente tras conmoción cerebral

### Fotofobia o sensibilidad a la luz (HM:3096)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 5.6; IC del 95 %: 2.9 / 11.0; Referencia: pmid:41941197

**Decisión:** síntoma sensorial complementario de alta especificidad

### Movimientos de persecución suave anormales (HM:3098)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 4.5; IC del 95 %: 2.0 / 10.0; Referencia: pmid:41941197

**Decisión:** signo exploratorio de afectación cerebelosa o de vías de seguimiento visual

### Sacadas oculares anormales (HM:3099)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 4.4; IC del 95 %: 2.0 / 9.7; Referencia: pmid:41941197

**Decisión:** dismetría sacádica indicativa de alteración en la coordinación ocular rápida

### Dolor abdominal (HM:0201)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**LR positivo:** Valor: 0.2; IC del 95 %: 0.1 / 0.4; Referencia: pmid:41941197

**Dispara si:** ausente

**Efecto:** excluye

**Sostiene:** Discriminación medida

**Referencia:** pmid:41941197

**Decisión:** la ausencia completa de cefalea reduce sustancialmente la probabilidad de conmoción cerebral (LR 0.20)

## Conclusión de la fuente

Los síntomas referidos como sentirse 'en una niebla' (LR+ 11.9) y los hallazgos del examen de motilidad ocular/convergencia (LR+ 7.0) son los mejores predictores de conmoción cerebral pediátrica. La ausencia de cefalea prácticamente descarta el cuadro (LR 0.20).

## Referencias y procedencia

**pmid:41941197:** Does This Child Have a Concussion?: The Rational Clinical Examination Systematic Review. JAMA, 2026. DOI: 10.1001/jama.2026.1233.

Fuente clínica: medsemiotics-db, condición HM:6023.
