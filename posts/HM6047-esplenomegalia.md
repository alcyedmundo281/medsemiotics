---
id: HM6047-01
slug: esplenomegalia-precision-semiotica
title: 'Esplenomegalia: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-09-21'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- esplenomegalia
- medicina_interna
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: e654998bddbb8c2b1d22e4da2f3375f9db6bc432
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6047-esplenomegalia.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0603-esplenomegalia.yaml: d694a903ae98ee750e432f8b2f95e52b856440a67ebef8ea14396108447626a6
    conceptos/HM3184-matidez-en-espacio-de-traube.yaml: aaedd1334225d41771e89034e12046e6c91d1e07452e9ecaeedfc544cba88af9
    conceptos/HM3185-signo-de-percusion-de-castell.yaml: 493c920a3f6cb1c793b2844448d16198914b6532a8faaf387d34e0cc7421154f
    condiciones/HM6047-esplenomegalia.yaml: c29d0e9bdff4998849728513181ffe00fdb6e93d10ed797a7b969add69d0df0d
    referencias/pmid-8411607.yaml: cacb8c8bd67b1f8fe3b0d2d8c35cd177811366fa77deeb28650fe548c42e8efa
grounding:
  condicion_id: HM:6047
  condicion_nombre: Esplenomegalia
  concepto_id: HM:0603
  concepto_nombre: Esplenomegalia
  estado_lr: medido
  lr_positivo: 8.2
  lr_negativo: 0.41
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: adultos evaluados mediante palpación abdominal supina o bimanual frente a ecografía o gammagrafía esplénica como estándar de referencia (pmid:8411607)
  referencia_id: pmid:8411607
  referencia_cita: Grover SA, Barkun AN, Sackett DL The rational clinical examination. Does this patient have splenomegaly? JAMA 1993
  pmid: '8411607'
  doi: null
  sensibilidad: 0.58
  especificidad: 0.93
triada:
  significante: Polo inferior del bazo palpable por debajo del reborde costal izquierdo en decúbito supino o decúbito lateral derecho (maniobra bimanual o de Middleton), o percusión mate anormal en el área esplénica (HM:3184, HM:3185).
  significado: Aumento patológico del volumen o masa esplénica más allá de sus límites fisiológicos normales.
  decision: un polo esplénico palpable por debajo del reborde costal en adultos sin deformidad torácica previa confirma esplenomegalia con alta probabilidad (LR+ 8.2)
evidencia:
- concepto: HM:0603
  rol: prueba_especifica
  estado_lr: medido
  poblacion: adultos evaluados mediante palpación abdominal supina o bimanual frente a ecografía o gammagrafía esplénica como estándar de referencia (pmid:8411607)
  ref: pmid:8411607
  sensibilidad: 0.58
  especificidad: 0.93
  lr_positivo: &id001
    valor: 8.2
    ref: pmid:8411607
  lr_negativo:
    valor: 0.41
    ref: pmid:8411607
  decision: un polo esplénico palpable por debajo del reborde costal en adultos sin deformidad torácica previa confirma esplenomegalia con alta probabilidad (LR+ 8.2)
  advertencia: la ausencia de palpación no descarta agrandamiento esplénico (Se 58%, LR- 0.41); el bazo requiere un aumento de volumen del 40-50% antes de ser palpable
- concepto: HM:3184
  rol: apoyo
  estado_lr: medido
  poblacion: adultos evaluados mediante percusión del espacio semilunar de Traube frente a estándar de referencia por imagen (pmid:8411607)
  ref: pmid:8411607
  sensibilidad: 0.62
  especificidad: 0.73
  lr_positivo: &id002
    valor: 2.3
    ref: pmid:8411607
  lr_negativo:
    valor: 0.48
    ref: pmid:8411607
  decision: la matidez en el espacio de Traube eleva la sospecha de bazo agrandado e indica proceder a palpación orientada o ecografía
  advertencia: falso positivo común en pacientes sin ayuno previo (estómago ocupado por alimentos sólidos o líquidos)
- concepto: HM:3185
  rol: prueba_sensible
  estado_lr: medido
  poblacion: adultos evaluados mediante percusión en el espacio intercostal más inferior en la línea axilar anterior durante inspiración profunda frente a estándar de imagen
  ref: pmid:8411607
  lr_positivo:
    rango:
    - 2.0
    - 2.7
    ref: pmid:8411607
  lr_negativo:
    rango:
    - 0.4
    - 0.6
    ref: pmid:8411607
  decision: el viraje de timpanismo espiratorio a matidez inspiratoria en la línea axilar anterior es la maniobra percutoria más sensible para detectar esplenomegalia incipiente
  advertencia: requiere percusión suave y adecuada coordinación respiratoria con el paciente
autoevaluacion:
- id: q1
  pregunta: 'En Esplenomegalia, ¿cuál es el resultado documentado del LR positivo para «Esplenomegalia»? Población: adultos evaluados mediante palpación abdominal supina o bimanual frente a ecografía o gammagrafía esplénica como estándar de referencia (pmid:8411607).'
  concepto_id: HM:0603
  referencia_id: pmid:8411607
  pmid: '8411607'
  doi: null
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6047
    concepto_id: HM:0603
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: adultos evaluados mediante palpación abdominal supina o bimanual frente a ecografía o gammagrafía esplénica como estándar de referencia (pmid:8411607)
    motivo: null
    decision: un polo esplénico palpable por debajo del reborde costal en adultos sin deformidad torácica previa confirma esplenomegalia con alta probabilidad (LR+ 8.2)
    advertencia: la ausencia de palpación no descarta agrandamiento esplénico (Se 58%, LR- 0.41); el bazo requiere un aumento de volumen del 40-50% antes de ser palpable
  opciones:
  - texto: 'LR positivo: 8.2.'
    correcta: true
    feedback: 'LR positivo: 8.2. Población: adultos evaluados mediante palpación abdominal supina o bimanual frente a ecografía o gammagrafía esplénica como estándar de referencia (pmid:8411607). Interpretación registrada: un polo esplénico palpable por debajo del reborde costal en adultos sin deformidad torácica previa confirma esplenomegalia con alta probabilidad (LR+ 8.2). Advertencia: la ausencia de palpación no descarta agrandamiento esplénico (Se 58%, LR- 0.41); el bazo requiere un aumento de volumen del 40-50% antes de ser palpable.'
  - texto: El valor 8.2 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 8.2. Población: adultos evaluados mediante palpación abdominal supina o bimanual frente a ecografía o gammagrafía esplénica como estándar de referencia (pmid:8411607). Interpretación registrada: un polo esplénico palpable por debajo del reborde costal en adultos sin deformidad torácica previa confirma esplenomegalia con alta probabilidad (LR+ 8.2). Advertencia: la ausencia de palpación no descarta agrandamiento esplénico (Se 58%, LR- 0.41); el bazo requiere un aumento de volumen del 40-50% antes de ser palpable.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 8.2. LR positivo: 8.2. Población: adultos evaluados mediante palpación abdominal supina o bimanual frente a ecografía o gammagrafía esplénica como estándar de referencia (pmid:8411607). Interpretación registrada: un polo esplénico palpable por debajo del reborde costal en adultos sin deformidad torácica previa confirma esplenomegalia con alta probabilidad (LR+ 8.2). Advertencia: la ausencia de palpación no descarta agrandamiento esplénico (Se 58%, LR- 0.41); el bazo requiere un aumento de volumen del 40-50% antes de ser palpable.'
- id: q2
  pregunta: 'En Esplenomegalia, ¿cuál es el resultado documentado del LR positivo para «Matidez en el espacio de Traube»? Población: adultos evaluados mediante percusión del espacio semilunar de Traube frente a estándar de referencia por imagen (pmid:8411607).'
  concepto_id: HM:3184
  referencia_id: pmid:8411607
  pmid: '8411607'
  doi: null
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6047
    concepto_id: HM:3184
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: adultos evaluados mediante percusión del espacio semilunar de Traube frente a estándar de referencia por imagen (pmid:8411607)
    motivo: null
    decision: la matidez en el espacio de Traube eleva la sospecha de bazo agrandado e indica proceder a palpación orientada o ecografía
    advertencia: falso positivo común en pacientes sin ayuno previo (estómago ocupado por alimentos sólidos o líquidos)
  opciones:
  - texto: El valor 2.3 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 2.3. Población: adultos evaluados mediante percusión del espacio semilunar de Traube frente a estándar de referencia por imagen (pmid:8411607). Interpretación registrada: la matidez en el espacio de Traube eleva la sospecha de bazo agrandado e indica proceder a palpación orientada o ecografía. Advertencia: falso positivo común en pacientes sin ayuno previo (estómago ocupado por alimentos sólidos o líquidos).'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 2.3. LR positivo: 2.3. Población: adultos evaluados mediante percusión del espacio semilunar de Traube frente a estándar de referencia por imagen (pmid:8411607). Interpretación registrada: la matidez en el espacio de Traube eleva la sospecha de bazo agrandado e indica proceder a palpación orientada o ecografía. Advertencia: falso positivo común en pacientes sin ayuno previo (estómago ocupado por alimentos sólidos o líquidos).'
  - texto: 'LR positivo: 2.3.'
    correcta: true
    feedback: 'LR positivo: 2.3. Población: adultos evaluados mediante percusión del espacio semilunar de Traube frente a estándar de referencia por imagen (pmid:8411607). Interpretación registrada: la matidez en el espacio de Traube eleva la sospecha de bazo agrandado e indica proceder a palpación orientada o ecografía. Advertencia: falso positivo común en pacientes sin ayuno previo (estómago ocupado por alimentos sólidos o líquidos).'
---

# Esplenomegalia

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Splenomegaly

## Sinónimos

bazo aumentado de tamaño

hipertrofia esplénica

bazo palpable

## Códigos

Snomed: 16294009; Cie10: R16.1

## Factores de riesgo

hipertensión portal o cirrosis hepática

síndrome linfoproliferativo, leucemia o linfoma

infección sistémica aguda o subaguda (mononucleosis infecciosa, endocarditis bacteriana, leishmaniasis, paludismo)

anemia hemolítica o hemoglobinopatía crónica

## Hallazgos clínicos

### Esplenomegalia (HM:0603)

**Significante:** Polo inferior del bazo palpable por debajo del reborde costal izquierdo en decúbito supino o decúbito lateral derecho (maniobra bimanual o de Middleton), o percusión mate anormal en el área esplénica (HM:3184, HM:3185).

**Significado:** Aumento patológico del volumen o masa esplénica más allá de sus límites fisiológicos normales.

**Falsos positivos:** Ptosis esplénica (bazo móvil o desplazado caudalmente sin incremento de masa) / Masa en polo inferior de riñón izquierdo o hidronefrosis / Tumor retroperitoneal o masa dependiente del ángulo esplénico del colon

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Población:** adultos evaluados mediante palpación abdominal supina o bimanual frente a ecografía o gammagrafía esplénica como estándar de referencia (pmid:8411607)

**Referencia:** pmid:8411607

**Sensibilidad:** 0.58

**Especificidad:** 0.93

**LR positivo:** Valor: 8.2; Referencia: pmid:8411607

**LR negativo:** Valor: 0.41; Referencia: pmid:8411607

**Decisión:** un polo esplénico palpable por debajo del reborde costal en adultos sin deformidad torácica previa confirma esplenomegalia con alta probabilidad (LR+ 8.2)

**Advertencia:** la ausencia de palpación no descarta agrandamiento esplénico (Se 58%, LR- 0.41); el bazo requiere un aumento de volumen del 40-50% antes de ser palpable

### Matidez en el espacio de Traube (HM:3184)

**Significante:** Pérdida del timpanismo gástrico normal y presencia de sonido mate a la percusión en el espacio semilunar de Traube (delimitado por el 6º cartílago costal superiormente, la línea axilar media lateralmente y el reborde costal inferiormente).

**Significado:** Ocupación del receso subdiafragmático izquierdo anterolateral por un bazo aumentado de tamaño que reemplaza la cámara de aire gástrica.

**Falsos positivos:** Ingesta alimentaria reciente o estómago lleno de contenido sólido/líquido / Derrame pleural izquierdo o consolidación pulmonar basal izquierda / Cardiomegalia grave o lóbulo hepático izquierdo agrandado

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**Población:** adultos evaluados mediante percusión del espacio semilunar de Traube frente a estándar de referencia por imagen (pmid:8411607)

**Referencia:** pmid:8411607

**Sensibilidad:** 0.62

**Especificidad:** 0.73

**LR positivo:** Valor: 2.3; Referencia: pmid:8411607

**LR negativo:** Valor: 0.48; Referencia: pmid:8411607

**Decisión:** la matidez en el espacio de Traube eleva la sospecha de bazo agrandado e indica proceder a palpación orientada o ecografía

**Advertencia:** falso positivo común en pacientes sin ayuno previo (estómago ocupado por alimentos sólidos o líquidos)

### Signo de percusión de Castell (HM:3185)

**Significante:** Con el paciente en decúbito supino, se percute en el espacio intercostal más inferior en la línea axilar anterior izquierda (habitualmente 8º o 9º espacio) durante la espiración (debe ser timpánico) y luego durante una inspiración profunda mantenida: el sonido vira de timpánico a mate.

**Significado:** Descenso diafragmático inspiratorio del polo inferior de un bazo agrandado (esplenomegalia) que interfiere y reemplaza la resonancia aérea circundante.

**Falsos positivos:** Abundante contenido fecal o alimentario en el ángulo esplénico del colon o estómago / Pequeño derrame pleural izquierdo basal

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**Población:** adultos evaluados mediante percusión en el espacio intercostal más inferior en la línea axilar anterior durante inspiración profunda frente a estándar de imagen

**Referencia:** pmid:8411607

**LR positivo:** Rango documentado: 2.0 / 2.7; Referencia: pmid:8411607

**LR negativo:** Rango documentado: 0.4 / 0.6; Referencia: pmid:8411607

**Decisión:** el viraje de timpanismo espiratorio a matidez inspiratoria en la línea axilar anterior es la maniobra percutoria más sensible para detectar esplenomegalia incipiente

**Advertencia:** requiere percusión suave y adecuada coordinación respiratoria con el paciente

## Referencias y procedencia

**pmid:8411607:** The rational clinical examination. Does this patient have splenomegaly?. JAMA, 1993. DOI: no documentado.

Fuente clínica: medsemiotics-db, condición HM:6047.
