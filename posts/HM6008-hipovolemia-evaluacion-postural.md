---
id: HM6008-01
slug: hipovolemia-aguda-signos-vitales-posturales
title: 'Hipovolemia: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-08-21'
author: Dr. Alcy Torres
category: urgencias
category_label: Medicina de Urgencias y Críticos
tags:
- hipovolemia
- semiologia
- urgencias
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: 9c9015322734168fe0328362950237f8ad296a55
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6008-hipovolemia.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0100-signo-vital-alterado.yaml: 3e0914bff0c0dc8f1a07185d49c70c4ee7dcf11cfa7ebc3281d611f5abb4f504
    conceptos/HM0104-taquicardia.yaml: a71b0c60cea7fec615df5f089557df4c7275da3ab54bb060c0651c5ff79f15d6
    conceptos/HM0109-hipotension-arterial.yaml: 934b7dadbc768a08d34a84a322bb11c8008218f7b111b1bba2b766e67f4db7cc
    conceptos/HM0500-sintoma-neurologico.yaml: bfed2fddf9ee375171804badb4977b28916322ec3dc288af10da4918cd035044
    conceptos/HM0600-signo-de-exploracion.yaml: 86a2ac9babe66028eecc797ddbf4d9ea382a6fd685e9cb8df91bb959029d62bf
    conceptos/HM3019-mareo-postural-intenso.yaml: 7e119a6b7791169797291abac826a63b6117a0e7ff5c33ec27b0f18ac811938a
    conceptos/HM3020-incremento-postural-del-pulso.yaml: 9ae6d79e5bc0201bf89204bc06c2824a565d8a1ff2b2433c64e5326f11d4db40
    conceptos/HM3021-axila-seca.yaml: a0e492588458e16f639ca2acc73bb0f7f66135ca013584ebb650670365cca0be
    conceptos/HM3022-mucosas-humedas.yaml: d5284e5e61c586e8e65c53a078acd5730e412a47c516ad344ea96b956035533c
    conceptos/HM3023-lengua-sin-surcos.yaml: decc68cdb2fe02a5054c683e556a871ebd6dac53df6296564ca02187212733fe
    conceptos/HM3024-relleno-capilar-prolongado.yaml: 647c5f4a82265f763418f74807a155f0e30670423b924cca188582dd017568ce
    conceptos/HM3025-turgencia-cutanea-disminuida.yaml: cacb1862872bbc6670f0e6576b796837289f8c1b42740224ed31d21bab9ab1d4
    condiciones/HM6008-hipovolemia.yaml: 46d0a8360a8a324654ea420239ab9f2348ab5223c33df7c90ad6deeaa9302fba
    referencias/pmid-10086438.yaml: b63336db28ca997d4e2c31dc9518c172e2261fd09055c3902a5ff7236d038cd0
grounding:
  condicion_id: HM:6008
  condicion_nombre: Hipovolemia
  concepto_id: HM:3021
  concepto_nombre: Axila seca
  estado_lr: medido
  lr_positivo: 2.8
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: pacientes con vómitos, diarrea o descenso de la ingesta
  referencia_id: pmid:10086438
  referencia_cita: McGee S, Abernethy WB 3rd, Simel DL The rational clinical examination. Is this patient hypovolemic? JAMA 1999
  pmid: '10086438'
  doi: 10.1001/jama.281.11.1022
triada:
  significante: Axila seca
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: apoya el diagnóstico, con fuerza modesta
evidencia:
- concepto: HM:3019
  rol: prueba_especifica
  estado_lr: no_medido
  poblacion: adultos con sospecha de pérdida sanguínea
  especificidad: 0.98
  ic95_especificidad:
  - 0.97
  - 0.99
  sensibilidad_por_gravedad:
  - perdida: moderada
    sensibilidad: 0.22
    ic95:
    - 0.06
    - 0.48
    ref: pmid:10086438
  - perdida: grande
    sensibilidad: 0.97
    ic95:
    - 0.91
    - 1.0
    ref: pmid:10086438
  motivo: 'la fuente publica sensibilidad y especificidad pero no el cociente. Es derivable por aritmética, pero no se anota como medido porque el autor no lo calculó: la forma de agrupar entre estudios cambia el resultado.'
  nota: 'la fuente lo evalúa junto con el incremento postural del pulso como un solo hallazgo compuesto: basta con que esté presente uno de los dos.'
  decision: su presencia apoya con fuerza la pérdida grande; su ausencia no descarta una pérdida moderada
- concepto: HM:3020
  rol: prueba_especifica
  estado_lr: no_medido
  poblacion: adultos con sospecha de pérdida sanguínea
  especificidad: 0.98
  ic95_especificidad:
  - 0.97
  - 0.99
  motivo: componente del hallazgo compuesto con el mareo postural intenso; la fuente no publica cociente aislado
  ref: pmid:10086438
- concepto: HM:0109
  rol: apoyo
  estado_lr: no_medido
  poblacion: adultos con sospecha de pérdida sanguínea
  sensibilidad: 0.33
  ic95_sensibilidad:
  - 0.21
  - 0.47
  ref: pmid:10086438
  motivo: la fuente publica sensibilidad sin especificidad
  advertencia: la hipotensión en decúbito y la taquicardia FALTAN con frecuencia incluso tras perder 1150 mL. Su ausencia no tranquiliza.
- concepto: HM:3021
  rol: prueba_especifica
  estado_lr: medido
  poblacion: pacientes con vómitos, diarrea o descenso de la ingesta
  lr_positivo: &id001
    valor: 2.8
    ic95:
    - 1.4
    - 5.4
    ref: pmid:10086438
  decision: apoya el diagnóstico, con fuerza modesta
- concepto: HM:3022
  rol: prueba_sensible
  estado_lr: medido
  poblacion: pacientes con vómitos, diarrea o descenso de la ingesta
  lr_negativo:
    valor: 0.3
    ic95:
    - 0.1
    - 0.6
    ref: pmid:10086438
  decision: 'su PRESENCIA argumenta en contra de la hipovolemia. Es el hallazgo invertido: lo que ayuda es encontrarlo, no echarlo en falta.'
- concepto: HM:3023
  rol: prueba_sensible
  estado_lr: medido
  poblacion: pacientes con vómitos, diarrea o descenso de la ingesta
  lr_negativo:
    valor: 0.3
    ic95:
    - 0.1
    - 0.6
    ref: pmid:10086438
  decision: igual que las mucosas húmedas, su presencia argumenta en contra
- concepto: HM:3024
  rol: apoyo
  estado_lr: sin_efecto
  poblacion: adultos
  motivo: la fuente concluye que no tiene valor diagnóstico demostrado en adultos
  ref: pmid:10086438
- concepto: HM:3025
  rol: apoyo
  estado_lr: sin_efecto
  poblacion: adultos
  motivo: la fuente concluye que no tiene valor diagnóstico demostrado en adultos
  ref: pmid:10086438
autoevaluacion:
- id: q1
  pregunta: 'En Hipovolemia, ¿cuál es el resultado documentado del LR positivo para «Axila seca»? Población: pacientes con vómitos, diarrea o descenso de la ingesta.'
  concepto_id: HM:3021
  referencia_id: pmid:10086438
  pmid: '10086438'
  doi: 10.1001/jama.281.11.1022
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6008
    concepto_id: HM:3021
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: pacientes con vómitos, diarrea o descenso de la ingesta
    motivo: null
    decision: apoya el diagnóstico, con fuerza modesta
    advertencia: null
  opciones:
  - texto: 'LR positivo: 2.8.'
    correcta: true
    feedback: 'LR positivo: 2.8. IC del 95 %: 1.4 a 5.4. Población: pacientes con vómitos, diarrea o descenso de la ingesta. Interpretación registrada: apoya el diagnóstico, con fuerza modesta.'
  - texto: El valor 2.8 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 2.8. IC del 95 %: 1.4 a 5.4. Población: pacientes con vómitos, diarrea o descenso de la ingesta. Interpretación registrada: apoya el diagnóstico, con fuerza modesta.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 2.8. LR positivo: 2.8. IC del 95 %: 1.4 a 5.4. Población: pacientes con vómitos, diarrea o descenso de la ingesta. Interpretación registrada: apoya el diagnóstico, con fuerza modesta.'
- id: q2
  pregunta: En Hipovolemia, ¿qué estado de la evidencia corresponde a «Mareo postural intenso» según la fuente?
  concepto_id: HM:3019
  referencia_id: null
  pmid: null
  doi: null
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6008
    concepto_id: HM:3019
    estado_lr: no_medido
    campo: null
    dato: null
    poblacion: adultos con sospecha de pérdida sanguínea
    motivo: 'la fuente publica sensibilidad y especificidad pero no el cociente. Es derivable por aritmética, pero no se anota como medido porque el autor no lo calculó: la forma de agrupar entre estudios cambia el resultado.'
    decision: su presencia apoya con fuerza la pérdida grande; su ausencia no descarta una pérdida moderada
    advertencia: null
  opciones:
  - texto: LR no medible
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medido». LR no medido Población: adultos con sospecha de pérdida sanguínea. Motivo: la fuente publica sensibilidad y especificidad pero no el cociente. Es derivable por aritmética, pero no se anota como medido porque el autor no lo calculó: la forma de agrupar entre estudios cambia el resultado. Interpretación registrada: su presencia apoya con fuerza la pérdida grande; su ausencia no descarta una pérdida moderada.'
  - texto: Sin efecto discriminativo
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medido». LR no medido Población: adultos con sospecha de pérdida sanguínea. Motivo: la fuente publica sensibilidad y especificidad pero no el cociente. Es derivable por aritmética, pero no se anota como medido porque el autor no lo calculó: la forma de agrupar entre estudios cambia el resultado. Interpretación registrada: su presencia apoya con fuerza la pérdida grande; su ausencia no descarta una pérdida moderada.'
  - texto: LR no medido
    correcta: true
    feedback: 'LR no medido Población: adultos con sospecha de pérdida sanguínea. Motivo: la fuente publica sensibilidad y especificidad pero no el cociente. Es derivable por aritmética, pero no se anota como medido porque el autor no lo calculó: la forma de agrupar entre estudios cambia el resultado. Interpretación registrada: su presencia apoya con fuerza la pérdida grande; su ausencia no descarta una pérdida moderada.'
---

# Hipovolemia

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Hypovolemia

## Sinónimos

depleción de volumen

hipovolemia aguda

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Hallazgos clínicos

### Mareo postural intenso (HM:3019)

**Rol:** Prueba específica

**Estado del LR:** LR no medido

**Población:** adultos con sospecha de pérdida sanguínea

**Especificidad:** 0.98

**Ic95 especificidad:** 0.97 / 0.99

**Sensibilidad por gravedad:** Perdida: moderada; Sensibilidad: 0.22; IC del 95 %: 0.06 / 0.48; Referencia: pmid:10086438 / Perdida: grande; Sensibilidad: 0.97; IC del 95 %: 0.91 / 1.0; Referencia: pmid:10086438

**Motivo:** la fuente publica sensibilidad y especificidad pero no el cociente. Es derivable por aritmética, pero no se anota como medido porque el autor no lo calculó: la forma de agrupar entre estudios cambia el resultado.

**Nota:** la fuente lo evalúa junto con el incremento postural del pulso como un solo hallazgo compuesto: basta con que esté presente uno de los dos.

**Decisión:** su presencia apoya con fuerza la pérdida grande; su ausencia no descarta una pérdida moderada

### Incremento postural del pulso (HM:3020)

**Rol:** Prueba específica

**Estado del LR:** LR no medido

**Población:** adultos con sospecha de pérdida sanguínea

**Especificidad:** 0.98

**Ic95 especificidad:** 0.97 / 0.99

**Motivo:** componente del hallazgo compuesto con el mareo postural intenso; la fuente no publica cociente aislado

**Referencia:** pmid:10086438

### Hipotensión arterial (HM:0109)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR no medido

**Población:** adultos con sospecha de pérdida sanguínea

**Sensibilidad:** 0.33

**Ic95 sensibilidad:** 0.21 / 0.47

**Referencia:** pmid:10086438

**Motivo:** la fuente publica sensibilidad sin especificidad

**Advertencia:** la hipotensión en decúbito y la taquicardia FALTAN con frecuencia incluso tras perder 1150 mL. Su ausencia no tranquiliza.

### Axila seca (HM:3021)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Población:** pacientes con vómitos, diarrea o descenso de la ingesta

**LR positivo:** Valor: 2.8; IC del 95 %: 1.4 / 5.4; Referencia: pmid:10086438

**Decisión:** apoya el diagnóstico, con fuerza modesta

### Mucosas húmedas (HM:3022)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**Población:** pacientes con vómitos, diarrea o descenso de la ingesta

**LR negativo:** Valor: 0.3; IC del 95 %: 0.1 / 0.6; Referencia: pmid:10086438

**Decisión:** su PRESENCIA argumenta en contra de la hipovolemia. Es el hallazgo invertido: lo que ayuda es encontrarlo, no echarlo en falta.

### Lengua sin surcos longitudinales (HM:3023)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**Población:** pacientes con vómitos, diarrea o descenso de la ingesta

**LR negativo:** Valor: 0.3; IC del 95 %: 0.1 / 0.6; Referencia: pmid:10086438

**Decisión:** igual que las mucosas húmedas, su presencia argumenta en contra

### Relleno capilar prolongado (HM:3024)

**Rol:** Apoyo diagnóstico

**Estado del LR:** Sin efecto discriminativo

**Población:** adultos

**Motivo:** la fuente concluye que no tiene valor diagnóstico demostrado en adultos

**Referencia:** pmid:10086438

### Turgencia cutánea disminuida (HM:3025)

**Rol:** Apoyo diagnóstico

**Estado del LR:** Sin efecto discriminativo

**Población:** adultos

**Motivo:** la fuente concluye que no tiene valor diagnóstico demostrado en adultos

**Referencia:** pmid:10086438

## Conclusión de la fuente

Para diagnosticar hipovolemia por pérdida sanguínea hace falta un incremento postural del pulso de 30 latidos por minuto o más, o un mareo postural intenso, aunque ambos faltan a menudo tras pérdidas moderadas. En pacientes con vómitos, diarrea o descenso de la ingesta pocos hallazgos han demostrado utilidad, y conviene medir electrolitos, urea y creatinina cuando se necesita certeza diagnóstica.

## Referencias y procedencia

**pmid:10086438:** The rational clinical examination. Is this patient hypovolemic?. JAMA, 1999. DOI: 10.1001/jama.281.11.1022.

Fuente clínica: medsemiotics-db, condición HM:6008.
