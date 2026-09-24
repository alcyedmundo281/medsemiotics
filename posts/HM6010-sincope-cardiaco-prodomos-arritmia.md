---
id: HM6010-01
slug: sincope-cardiaco-vs-vasovagal-anamnesis
title: 'Síncope cardíaco: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-08-21'
author: Dr. Alcy Torres
category: cardiologia
category_label: Cardiología y Urgencias
tags:
- cardiologia
- criterios
- semiologia
- sincope-cardiaco
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: fbd5cbf59e75e77b70a630f881ac1c1754e1e063
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6010-sincope-cardiaco.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0200-dolor.yaml: 583f1c01f2eeeed369469010e4b7d24d73d883bc3ef40266f80eaa0db0089463
    conceptos/HM0207-cefalea.yaml: 3a7957f3f8cda87461090f0aff7e5cccde0cbea0a59b1bd8716a6fb509bb4b8c
    conceptos/HM0500-sintoma-neurologico.yaml: bfed2fddf9ee375171804badb4977b28916322ec3dc288af10da4918cd035044
    conceptos/HM0505-sincope.yaml: c17b05914b15e6b6a14b4c974424a0c3b36d222dba00c39a9dc405e45ec54b5c
    conceptos/HM0606-cianosis.yaml: ed93e7260a197f59efd82fdacb9cbf6369a52b0176c881b46cf6faf6ffc9f53e
    conceptos/HM1000-trastorno.yaml: 9862513dc10aa15c0adccc15214151612f5c4e54e079cad422d03adf8d795c0b
    conceptos/HM3031-primer-sincope-desde-los-35.yaml: 3e37b7c7209b24ceae6068e78f9b25ea0556115acee35c9c927e82c2de1962fa
    conceptos/HM3032-fibrilacion-o-flutter-auricular.yaml: 2877f7e08d60a0632a58fd5f30ad58846ee9222b099d0582f37588246c12f0c6
    conceptos/HM3033-cardiopatia-estructural-grave.yaml: 03e8e3289317f111216fc2e7f84145729dace21f7ada8a9d719e50f834e10edb
    conceptos/HM3034-cianosis-durante-el-episodio.yaml: 4c4ed4f0596f03a7636d29c887532df450900a4a513ebc87e454787bc7129d65
    conceptos/HM3035-cambio-de-humor-prodromico.yaml: d9854dc1996b0424d1811e769778e35dc2937b364f521d11f33862d666c5d928
    conceptos/HM3036-sensacion-de-frio.yaml: dba095414da8b845a5b9633a999b5abc1d0a300ca84372afa7e71767b2e3a672
    conceptos/HM3037-cambio-de-humor-tras-sincope.yaml: b9b67d523e646f9ac5cdb1485cfc695850606465d39f8757457b1c781a565716
    conceptos/HM3038-amnesia-de-la-conducta-previa.yaml: 14e2e16f8fe44a282a932e1cd7320655aefa24fac8713585af88f90926dab65f
    condiciones/HM6010-sincope-cardiaco.yaml: 6d3870a293876020049dbc882c5f78be0302bd81ed4b67f69b2f590450154cba
    referencias/pmid-12239256.yaml: 08708b832ccadcd95c4ea8ece4c4cb3f3756239d7632e43b9dc2968fcbfa3f35
    referencias/pmid-29136314.yaml: a3a8604202d152c89bf95ca449f96d9af9b0cae638e51da1f7bfaacc5f1c46a8
    referencias/pmid-31237649.yaml: b8a3d22701b7aceb50254216ad315c9c7235424e0bba5bd261e1621a976c75bb
    referencias/pmid-33382159.yaml: c062ec9a3ced78cf64262a9465f988cb92e10dc1809d45d63086b637431520d5
grounding:
  condicion_id: HM:6010
  condicion_nombre: Síncope cardíaco
  concepto_id: HM:3032
  concepto_nombre: Fibrilación o flutter auricular
  estado_lr: medido
  lr_positivo: 7.3
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:31237649
  referencia_cita: 'Albassam OT, Redelmeier RJ, Shadowitz S, Husain AM, Simel D, Etchells EE Did This Patient Have Cardiac Syncope?: The Rational Clinical Examination Systematic Review JAMA 2019'
  pmid: '31237649'
  doi: 10.1001/jama.2019.8001
  sensibilidad: 0.13
  especificidad: 0.98
triada:
  significante: Fibrilación o flutter auricular
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: el antecedente que más desplaza hacia el origen cardíaco
evidencia:
- concepto: HM:3032
  rol: prueba_especifica
  estado_lr: medido
  sensibilidad: 0.13
  ic95_sensibilidad:
  - 0.06
  - 0.2
  especificidad: 0.98
  ic95_especificidad:
  - 0.96
  - 1.0
  lr_positivo: &id001
    valor: 7.3
    ic95:
    - 2.4
    - 22
    ref: pmid:31237649
  decision: el antecedente que más desplaza hacia el origen cardíaco
- concepto: HM:3034
  rol: prueba_especifica
  estado_lr: medido
  sensibilidad: 0.08
  ic95_sensibilidad:
  - 0.02
  - 0.14
  especificidad: 0.99
  ic95_especificidad:
  - 0.98
  - 1.0
  lr_positivo: &id002
    valor: 6.2
    ic95:
    - 1.6
    - 24
    ref: pmid:31237649
  decision: 'rarísima pero casi definitiva cuando la hay: especificidad del 99%. Depende de que alguien presenciara el episodio.'
- concepto: HM:3033
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo:
    rango:
    - 3.3
    - 4.8
    ref: pmid:31237649
    nota: rango entre 2 estudios; sensibilidad 0.35-0.51, especificidad 0.84-0.93
  decision: antecedente que apoya con fuerza moderada
- concepto: HM:3031
  rol: prueba_sensible
  estado_lr: medido
  sensibilidad: 0.91
  ic95_sensibilidad:
  - 0.85
  - 0.97
  especificidad: 0.72
  ic95_especificidad:
  - 0.66
  - 0.78
  lr_positivo:
    valor: 3.3
    ic95:
    - 2.6
    - 4.1
    ref: pmid:31237649
  lr_negativo:
    valor: 0.13
    ic95:
    - 0.06
    - 0.25
    ref: pmid:31237649
    nota: la fuente lo expresa como el cociente de la edad menor de 35 años, que es el negativo de este hallazgo
  decision: 'el dato más útil para DESCARTAR: un primer síncope antes de los 35 prácticamente excluye el origen cardíaco'
- concepto: HM:3035
  rol: apoyo
  estado_lr: medido
  sensibilidad: 0.02
  especificidad: 0.76
  lr_positivo:
    valor: 0.09
    ic95:
    - 0.02
    - 0.38
    ref: pmid:31237649
  decision: su presencia aleja del origen cardíaco y orienta a vasovagal
- concepto: HM:3036
  rol: apoyo
  estado_lr: medido
  sensibilidad: 0.02
  especificidad: 0.89
  lr_positivo:
    valor: 0.16
    ic95:
    - 0.06
    - 0.64
    ref: pmid:31237649
  decision: pródromo vegetativo; su presencia aleja del origen cardíaco
- concepto: HM:0207
  rol: apoyo
  estado_lr: medido
  sensibilidad: 0.03
  especificidad: 0.8
  lr_positivo:
    valor: 0.17
    ic95:
    - 0.06
    - 0.55
    ref: pmid:31237649
  decision: su presencia aleja del origen cardíaco
- concepto: HM:3037
  rol: apoyo
  estado_lr: medido
  sensibilidad: 0.03
  especificidad: 0.83
  lr_positivo:
    valor: 0.21
    ic95:
    - 0.06
    - 0.65
    ref: pmid:31237649
  decision: su presencia aleja del origen cardíaco
- concepto: HM:3038
  rol: apoyo
  estado_lr: medido
  sensibilidad: 0.05
  especificidad: 0.82
  lr_positivo:
    valor: 0.25
    ic95:
    - 0.09
    - 0.69
    ref: pmid:31237649
  decision: su presencia aleja del origen cardíaco
- concepto: HM:0505
  rol: manifestacion
  estado_lr: no_medible
  motivo: es el motivo de consulta que define la población estudiada; la pregunta no es si hubo síncope sino si fue cardíaco
autoevaluacion:
- id: q1
  pregunta: En Síncope cardíaco, ¿cuál es el resultado documentado del LR positivo para «Fibrilación o flutter auricular»?
  concepto_id: HM:3032
  referencia_id: pmid:31237649
  pmid: '31237649'
  doi: 10.1001/jama.2019.8001
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6010
    concepto_id: HM:3032
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: el antecedente que más desplaza hacia el origen cardíaco
    advertencia: null
  opciones:
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 7.3. LR positivo: 7.3. IC del 95 %: 2.4 a 22. Interpretación registrada: el antecedente que más desplaza hacia el origen cardíaco.'
  - texto: 'LR positivo: 7.3.'
    correcta: true
    feedback: 'LR positivo: 7.3. IC del 95 %: 2.4 a 22. Interpretación registrada: el antecedente que más desplaza hacia el origen cardíaco.'
  - texto: El valor 7.3 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 7.3. IC del 95 %: 2.4 a 22. Interpretación registrada: el antecedente que más desplaza hacia el origen cardíaco.'
- id: q2
  pregunta: En Síncope cardíaco, ¿cuál es el resultado documentado del LR positivo para «Cianosis presenciada durante el episodio»?
  concepto_id: HM:3034
  referencia_id: pmid:31237649
  pmid: '31237649'
  doi: 10.1001/jama.2019.8001
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6010
    concepto_id: HM:3034
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: null
    motivo: null
    decision: 'rarísima pero casi definitiva cuando la hay: especificidad del 99%. Depende de que alguien presenciara el episodio.'
    advertencia: null
  opciones:
  - texto: 'LR positivo: 6.2.'
    correcta: true
    feedback: 'LR positivo: 6.2. IC del 95 %: 1.6 a 24. Interpretación registrada: rarísima pero casi definitiva cuando la hay: especificidad del 99%. Depende de que alguien presenciara el episodio.'
  - texto: El valor 6.2 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 6.2. IC del 95 %: 1.6 a 24. Interpretación registrada: rarísima pero casi definitiva cuando la hay: especificidad del 99%. Depende de que alguien presenciara el episodio.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 6.2. LR positivo: 6.2. IC del 95 %: 1.6 a 24. Interpretación registrada: rarísima pero casi definitiva cuando la hay: especificidad del 99%. Depende de que alguien presenciara el episodio.'
---

# Síncope cardíaco

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Cardiac syncope

## Sinónimos

síncope de origen cardíaco

síncope arrítmico

## Códigos

Snomed: 788877005; Cie10: R55

## Probabilidad basal

Valor: 0.095; Población: 822 participantes del Framingham Heart Study que refirieron síncope durante un seguimiento medio de 17 años (población general, 1971-1998); Nota: proporción de síncopes atribuidos a causa cardíaca en la comunidad; el 36.6% quedó sin causa identificada. No es la población de urgencias ni de consulta especializada en la que se midieron los cocientes; ver pendiente; Referencia: pmid:12239256

## Hallazgos clínicos

### Fibrilación o flutter auricular (HM:3032)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Sensibilidad:** 0.13

**Ic95 sensibilidad:** 0.06 / 0.2

**Especificidad:** 0.98

**Ic95 especificidad:** 0.96 / 1.0

**LR positivo:** Valor: 7.3; IC del 95 %: 2.4 / 22; Referencia: pmid:31237649

**Decisión:** el antecedente que más desplaza hacia el origen cardíaco

### Cianosis presenciada durante el episodio (HM:3034)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Sensibilidad:** 0.08

**Ic95 sensibilidad:** 0.02 / 0.14

**Especificidad:** 0.99

**Ic95 especificidad:** 0.98 / 1.0

**LR positivo:** Valor: 6.2; IC del 95 %: 1.6 / 24; Referencia: pmid:31237649

**Decisión:** rarísima pero casi definitiva cuando la hay: especificidad del 99%. Depende de que alguien presenciara el episodio.

### Cardiopatía estructural grave conocida (HM:3033)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Rango documentado: 3.3 / 4.8; Referencia: pmid:31237649; Nota: rango entre 2 estudios; sensibilidad 0.35-0.51, especificidad 0.84-0.93

**Decisión:** antecedente que apoya con fuerza moderada

### Primer síncope a los 35 años o más (HM:3031)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**Sensibilidad:** 0.91

**Ic95 sensibilidad:** 0.85 / 0.97

**Especificidad:** 0.72

**Ic95 especificidad:** 0.66 / 0.78

**LR positivo:** Valor: 3.3; IC del 95 %: 2.6 / 4.1; Referencia: pmid:31237649

**LR negativo:** Valor: 0.13; IC del 95 %: 0.06 / 0.25; Referencia: pmid:31237649; Nota: la fuente lo expresa como el cociente de la edad menor de 35 años, que es el negativo de este hallazgo

**Decisión:** el dato más útil para DESCARTAR: un primer síncope antes de los 35 prácticamente excluye el origen cardíaco

### Cambio de humor o preocupación prodrómica por los detalles (HM:3035)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**Sensibilidad:** 0.02

**Especificidad:** 0.76

**LR positivo:** Valor: 0.09; IC del 95 %: 0.02 / 0.38; Referencia: pmid:31237649

**Decisión:** su presencia aleja del origen cardíaco y orienta a vasovagal

### Sensación de frío previa al síncope (HM:3036)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**Sensibilidad:** 0.02

**Especificidad:** 0.89

**LR positivo:** Valor: 0.16; IC del 95 %: 0.06 / 0.64; Referencia: pmid:31237649

**Decisión:** pródromo vegetativo; su presencia aleja del origen cardíaco

### Cefalea (HM:0207)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**Sensibilidad:** 0.03

**Especificidad:** 0.8

**LR positivo:** Valor: 0.17; IC del 95 %: 0.06 / 0.55; Referencia: pmid:31237649

**Decisión:** su presencia aleja del origen cardíaco

### Cambio de humor tras el síncope (HM:3037)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**Sensibilidad:** 0.03

**Especificidad:** 0.83

**LR positivo:** Valor: 0.21; IC del 95 %: 0.06 / 0.65; Referencia: pmid:31237649

**Decisión:** su presencia aleja del origen cardíaco

### Incapacidad para recordar la conducta previa al síncope (HM:3038)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**Sensibilidad:** 0.05

**Especificidad:** 0.82

**LR positivo:** Valor: 0.25; IC del 95 %: 0.09 / 0.69; Referencia: pmid:31237649

**Decisión:** su presencia aleja del origen cardíaco

### Síncope (HM:0505)

**Rol:** Manifestación

**Estado del LR:** LR no medible

**Motivo:** es el motivo de consulta que define la población estudiada; la pregunta no es si hubo síncope sino si fue cardíaco

## Escalas

Nombre: EGSYS; Componentes declarados: seis variables clínicas, electrocardiograma incluido; Graduación: Parámetro: Puntuación EGSYS; Unidad: puntos; Lectura: disjunto; Tramos: Rango documentado: menor de 3; Hasta: 3; Lr negativo rango: 0.12 / 0.17; Referencia: pmid:31237649; Nota: rango entre 2 estudios que la validaron de forma prospectiva; sensibilidad 0.89-0.91, especificidad 0.69-0.73; Decisión: una puntuación menor de 3 es lo que mejor descarta el origen cardíaco

## Aspectos pendientes de documentación

Los biomarcadores cardíacos muestran exactitud prometedora según la fuente, pero sus umbrales diagnósticos aún requieren validación. No se registran.

Probabilidad base en urgencias. Toarta 2018 (pmid:29136314; 5010 adultos en seis servicios de urgencias) da un 5.4% de síncopes de presunta causa cardíaca, pero es la impresión del médico al final de la visita, no un diagnóstico contra un patrón de referencia. No se transcribe como probabilidad base.

Búsqueda en PubMed del 2026-09-24. Consulta «syncope AND (history OR clinical features OR clinical examination) AND (cardiac OR arrhythmic) AND (diagnostic accuracy OR likelihood ratio)», filtrada a revisiones sistemáticas y metaanálisis desde 2019-06: 16 resultados, cribados por título y resumen. Ninguno actualiza la exactitud de la anamnesis para el síncope cardíaco. Sweanor 2021 (pmid:33382159) evalúa escalas multivariables, pero contra eventos adversos a 30 días, no contra el origen cardíaco.

Factores de riesgo. Búsqueda en PubMed del 2026-09-24. Consulta «cardiac syncope[Title/Abstract] AND (risk factor OR predictors)»: 97 resultados, cribados por título los 20 primeros. No aparece ninguna fuente con grupo control que dé OR o RR de síncope cardíaco. Lo que Albassam 2019 cuantifica como cociente (edad, fibrilación auricular, cardiopatía estructural) ya está en las aristas.

## Conclusión de la fuente

La exploración clínica, con el electrocardiograma dentro de puntuaciones multivariable, puede identificar con precisión a los pacientes con y sin síncope cardíaco.

## Referencias y procedencia

**pmid:12239256:** Incidence and prognosis of syncope. N Engl J Med, 2002. DOI: 10.1056/NEJMoa012407.

**pmid:29136314:** Syncope Prognosis Based on Emergency Department Diagnosis: A Prospective Cohort Study. Acad Emerg Med, 2018. DOI: 10.1111/acem.13346.

**pmid:31237649:** Did This Patient Have Cardiac Syncope?: The Rational Clinical Examination Systematic Review. JAMA, 2019. DOI: 10.1001/jama.2019.8001.

**pmid:33382159:** Multivariable risk scores for predicting short-term outcomes for emergency department patients with unexplained syncope: A systematic review. Acad Emerg Med, 2021. DOI: 10.1111/acem.14203.

Fuente clínica: medsemiotics-db, condición HM:6010.
