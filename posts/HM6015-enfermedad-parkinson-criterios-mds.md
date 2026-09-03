---
id: HM6015-01
slug: enfermedad-parkinson-criterios-clinicos-mds
title: 'Enfermedad de Parkinson: hallazgos y evidencia clínica'
subtitle: Hallazgos y criterios clínicos sin cocientes de verosimilitud medidos.
date: '2026-08-21'
author: Dr. Alcy Torres
category: neurologia
category_label: Neurología
tags:
- criterios
- enfermedad-de-parkinson
- neurologia
- semiologia
reading_time: 8 min
difficulty: Avanzado
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: a6b2afeb208457aaf6ce2d86ff78304f45071d5b
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6015-enfermedad-de-parkinson.yaml
  archivos:
    CITATION.cff: e2840db4d37cfb43ebe9835e23c1acfef6352e730051918fa0cbd9fe6fad77d7
    conceptos/HM3061-bradicinesia.yaml: 623f4a414f90755471fd23933757b9118848638e618f5a63fa01a4ab626182a0
    conceptos/HM3062-temblor-de-reposo.yaml: b181c4353fd0a2b46cc1bb9b46e240e468ab0e4de27f1aeedf8d081851671027
    conceptos/HM3063-rigidez-parkinsoniana.yaml: 97ec764a6867749d77971a91cde2028ec1cb43e13d7504e12308094528a43de5
    condiciones/HM6002-sindrome-intestino-irritable.yaml: de99a8c5755f450792d575897902bde932154119c4318ee30d916dbec0bd11f5
    condiciones/HM6015-enfermedad-de-parkinson.yaml: da6f3cf1eb93f27411eda8f603aac72d4a94af776a79c05e94afffd30ee5768c
    referencias/pmid-26474316.yaml: 409c161aa7d66ee82f74cac52519280375172cc5fe2c388633ab2b80dbbf38dc
grounding:
  condicion_id: HM:6015
  condicion_nombre: Enfermedad de Parkinson
  concepto_id: HM:3061
  concepto_nombre: Bradicinesia
  estado_lr: no_medible
  lr_positivo: null
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:26474316
  referencia_cita: Postuma RB, Berg D, Stern M, Poewe W, Olanow CW, Oertel W, Obeso J, Marek K, Litvan I, Lang AE, Halliday G, Goetz CG, Gasser T, Dubois B, Chan P, Bloem BR, Adler CH, Deuschl G MDS clinical diagnostic criteria for Parkinson's disease Mov Disord 2015
  pmid: '26474316'
  doi: 10.1002/mds.26424
triada:
  significante: Bradicinesia
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: La fuente no documenta una decisión específica para este hallazgo.
evidencia:
- concepto: HM:3061
  rol: manifestacion
  efecto: apoya
  estado_lr: no_medible
  motivo: 'forma parte de la definición de parkinsonismo motor, que es el patrón de referencia del propio criterio: sesgo de incorporación'
- concepto: HM:3062
  rol: manifestacion
  efecto: apoya
  estado_lr: no_medible
  motivo: componente del núcleo; sesgo de incorporación
- concepto: HM:3063
  rol: manifestacion
  efecto: apoya
  estado_lr: no_medible
  motivo: componente del núcleo; sesgo de incorporación
autoevaluacion:
- id: q1
  pregunta: En Enfermedad de Parkinson, ¿qué estado de la evidencia corresponde a «Bradicinesia» según la fuente?
  concepto_id: HM:3061
  referencia_id: null
  pmid: null
  doi: null
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6015
    concepto_id: HM:3061
    estado_lr: no_medible
    campo: null
    dato: null
    poblacion: null
    motivo: 'forma parte de la definición de parkinsonismo motor, que es el patrón de referencia del propio criterio: sesgo de incorporación'
    decision: null
    advertencia: null
  opciones:
  - texto: LR no medido
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medible». LR no medible Motivo: forma parte de la definición de parkinsonismo motor, que es el patrón de referencia del propio criterio: sesgo de incorporación.'
  - texto: Sin efecto discriminativo
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medible». LR no medible Motivo: forma parte de la definición de parkinsonismo motor, que es el patrón de referencia del propio criterio: sesgo de incorporación.'
  - texto: LR no medible
    correcta: true
    feedback: 'LR no medible Motivo: forma parte de la definición de parkinsonismo motor, que es el patrón de referencia del propio criterio: sesgo de incorporación.'
- id: q2
  pregunta: En Enfermedad de Parkinson, ¿qué estado de la evidencia corresponde a «Temblor de reposo» según la fuente?
  concepto_id: HM:3062
  referencia_id: null
  pmid: null
  doi: null
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6015
    concepto_id: HM:3062
    estado_lr: no_medible
    campo: null
    dato: null
    poblacion: null
    motivo: componente del núcleo; sesgo de incorporación
    decision: null
    advertencia: null
  opciones:
  - texto: Sin efecto discriminativo
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medible». LR no medible Motivo: componente del núcleo; sesgo de incorporación.'
  - texto: LR no medible
    correcta: true
    feedback: 'LR no medible Motivo: componente del núcleo; sesgo de incorporación.'
  - texto: LR no medido
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medible». LR no medible Motivo: componente del núcleo; sesgo de incorporación.'
---

# Enfermedad de Parkinson

Hallazgos y criterios clínicos sin cocientes de verosimilitud medidos.

## Nombre en inglés

Parkinson's disease

## Sinónimos

parkinson

EP

enfermedad de Parkinson idiopática

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Núcleo diagnóstico

Requiere: Bradicinesia (HM:3061); Y al menos uno de: Temblor de reposo (HM:3062) / Rigidez parkinsoniana (HM:3063); Referencia: pmid:26474316

## Balance de criterios

Referencia: pmid:26474316; Establecida: Apoyos minimos: 2; Banderas maximas: 0; Probable: Contrapeso: 1; Banderas maximas: 2

## Hallazgos clínicos

### Bradicinesia (HM:3061)

**Rol:** Manifestación

**Efecto:** Apoya

**Estado del LR:** LR no medible

**Motivo:** forma parte de la definición de parkinsonismo motor, que es el patrón de referencia del propio criterio: sesgo de incorporación

### Temblor de reposo (HM:3062)

**Rol:** Manifestación

**Efecto:** Apoya

**Estado del LR:** LR no medible

**Motivo:** componente del núcleo; sesgo de incorporación

### Rigidez parkinsoniana (HM:3063)

**Rol:** Manifestación

**Efecto:** Apoya

**Estado del LR:** LR no medible

**Motivo:** componente del núcleo; sesgo de incorporación

## Aspectos pendientes de documentación

Los criterios de apoyo y las banderas rojas de MDS no se pueblan en este ciclo. Cuando se hagan, les corresponde `consenso_con_afirmacion` y no `consenso_de_lista`: MDS las declara COMO CRITERIO, con su panel detrás y con una mecánica de contrapeso explícita, que es justo lo que una reseña que enumera síntomas de alarma no hace. Esa distinción es la que dejó fuera a la fiebre en HM:6002 y hay que justificarla por escrito, no darla por obvia.

## Referencias y procedencia

**pmid:26474316:** MDS clinical diagnostic criteria for Parkinson's disease. Mov Disord, 2015. DOI: 10.1002/mds.26424.

Fuente clínica: medsemiotics-db, condición HM:6015.
