---
id: HM6009-01
slug: faringitis-estreptococica-exudado-criterios-centor
title: 'Faringitis estreptocócica: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-08-21'
author: Dr. Alcy Torres
category: infectologia
category_label: Infectología y Atención Primaria
tags:
- criterios
- faringitis-estreptococica
- infectologia
- semiologia
reading_time: 8 min
difficulty: Básico
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: 22c5b2fce06af1f9f795698b328c074355dc9b3f
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6009-faringitis-estreptococica.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0001-hallazgo-clinico.yaml: 5cf5cbb0a6ce5c773fd60ad80c8b467259ad4d480cd2cd60aa1335d5c8b65329
    conceptos/HM0200-dolor.yaml: 583f1c01f2eeeed369469010e4b7d24d73d883bc3ef40266f80eaa0db0089463
    conceptos/HM0211-odinofagia.yaml: 569ee7652e0d175874ec72a78844d970e5bd1f9275888b6e2cc708fe81a83caf
    conceptos/HM0600-signo-de-exploracion.yaml: 86a2ac9babe66028eecc797ddbf4d9ea382a6fd685e9cb8df91bb959029d62bf
    conceptos/HM0607-adenopatias.yaml: 849fe51a52fd503725ed3d2da2115ed0f2dab016bd0150088c7a5c079a718a10
    conceptos/HM3001-adenopatia-cervical-posterior.yaml: e4cea821c77f56e47f14272fa6fda7d778d855fc56206708a2c2c9a0054a8c6e
    conceptos/HM3026-exudado-amigdalino.yaml: 2035d19d7697ad00e8860ba5bf2e4be6d4c17b557a6f8ab8b8c966ae088e8b43
    conceptos/HM3027-exudado-faringeo.yaml: 06a0f094562bd1a1b9c9ec09d5dc2c2ca5b963c627c82897dd1f93ac6dca0c50
    conceptos/HM3028-exposicion-estreptococo.yaml: 26edc47823c8d5fa6dc3268a3bdcc36f8470f2fe973db587f023d6ac3ccaff21
    conceptos/HM3029-adenopatia-cervical-anterior-dolorosa.yaml: c126e8e1eee16e645ed035c25ba116ac1aa29d60638b8b8dae0a98875240574a
    conceptos/HM3030-hipertrofia-amigdalina.yaml: 51d8082f89cd126da2b5bbab75f43b3b012b4ba611edc0553074a895b4b87a48
    condiciones/HM6003-mononucleosis-infecciosa.yaml: fdd67306d3d26ce5724613adc81b59ab01bd965186ce7c3d82ca67bf267ce2e9
    condiciones/HM6009-faringitis-estreptococica.yaml: 577adfd44018dc25fe603a6246de493f07d935ac5eb9c239191d8053ef591dda
    referencias/pmid-11147989.yaml: f6aca870e75ab118eba2a41950cb38d56cabbcb69b65ba4e5eadc1f671edafc8
    referencias/pmid-20696723.yaml: 52e42702cf5a15dbc1a860b863d464c03e47499f391b72a24f003b7636ce700d
    referencias/pmid-21631919.yaml: 86c170183405f9a73aa2aa6a394707098f5ab83a89a8c1f3609d296a9c0e7336
    referencias/pmid-25774295.yaml: a22df30cf7f245df0ade141487ffe5a6ce5d9f7a45bf4833fbb030f249e7c7ab
    referencias/pmid-25822555.yaml: a0e7997279e60745f64a2474332b4637d7d316a9dae025a6008c2af7ac5d2718
    referencias/pmid-6763125.yaml: 764d2c78e1fd8f05c848d65e20a4927365168d36051cb96e00bd7b7576af1cd8
    referencias/pmid-9475915.yaml: 2b19c59f77bc92ff3d8a770384ecdf63a7e28433eda7d8030995781991597827
grounding:
  condicion_id: HM:6009
  condicion_nombre: Faringitis estreptocócica
  concepto_id: HM:3026
  concepto_nombre: Exudado amigdalino
  estado_lr: medido
  lr_positivo: 3.4
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:11147989
  referencia_cita: Ebell MH, Smith MA, Barry HC, Ives K, Carey M The rational clinical examination. Does this patient have strep throat? JAMA 2000
  pmid: '11147989'
  doi: 10.1001/jama.284.22.2912
triada:
  significante: Exudado amigdalino
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: el hallazgo aislado más útil, y aun así insuficiente por sí solo
evidencia:
- concepto: HM:3026
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id001
    valor: 3.4
    ref: pmid:11147989
    nota: la fuente no publica intervalo de confianza en el abstract
  decision: el hallazgo aislado más útil, y aun así insuficiente por sí solo
- concepto: HM:3027
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id002
    valor: 2.1
    ref: pmid:11147989
    nota: la fuente no publica intervalo de confianza en el abstract
  decision: apoya menos que el exudado amigdalino, del que se distingue
- concepto: HM:3028
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 1.9
    ref: pmid:11147989
    nota: exposición en las dos semanas previas; sin intervalo en el abstract
  decision: dato de anamnesis con peso escaso
- concepto: HM:3029
  rol: prueba_sensible
  estado_lr: medido
  lr_negativo:
    valor: 0.6
    ref: pmid:11147989
    nota: la fuente no publica intervalo de confianza en el abstract
  decision: su ausencia es lo que más reduce la probabilidad, y aun así la deja en más de la mitad de la previa
- concepto: HM:3030
  rol: prueba_sensible
  estado_lr: medido
  lr_negativo:
    valor: 0.63
    ref: pmid:11147989
    nota: la fuente no publica intervalo de confianza en el abstract
  decision: su ausencia reduce poco la probabilidad
- concepto: HM:0211
  rol: manifestacion
  estado_lr: no_medible
  motivo: es el motivo de consulta que define la población estudiada, no una prueba dentro de ella
autoevaluacion:
- id: q1
  pregunta: En Faringitis estreptocócica, ¿cuál es el resultado documentado del LR positivo para «Exudado amigdalino»?
  concepto_id: HM:3026
  referencia_id: pmid:11147989
  pmid: '11147989'
  doi: 10.1001/jama.284.22.2912
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6009
    concepto_id: HM:3026
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: el hallazgo aislado más útil, y aun así insuficiente por sí solo
    advertencia: null
  opciones:
  - texto: El valor 3.4 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 3.4. Nota: la fuente no publica intervalo de confianza en el abstract. Interpretación registrada: el hallazgo aislado más útil, y aun así insuficiente por sí solo.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 3.4. LR positivo: 3.4. Nota: la fuente no publica intervalo de confianza en el abstract. Interpretación registrada: el hallazgo aislado más útil, y aun así insuficiente por sí solo.'
  - texto: 'LR positivo: 3.4.'
    correcta: true
    feedback: 'LR positivo: 3.4. Nota: la fuente no publica intervalo de confianza en el abstract. Interpretación registrada: el hallazgo aislado más útil, y aun así insuficiente por sí solo.'
- id: q2
  pregunta: En Faringitis estreptocócica, ¿cuál es el resultado documentado del LR positivo para «Exudado faríngeo»?
  concepto_id: HM:3027
  referencia_id: pmid:11147989
  pmid: '11147989'
  doi: 10.1001/jama.284.22.2912
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6009
    concepto_id: HM:3027
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: null
    motivo: null
    decision: apoya menos que el exudado amigdalino, del que se distingue
    advertencia: null
  opciones:
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 2.1. LR positivo: 2.1. Nota: la fuente no publica intervalo de confianza en el abstract. Interpretación registrada: apoya menos que el exudado amigdalino, del que se distingue.'
  - texto: 'LR positivo: 2.1.'
    correcta: true
    feedback: 'LR positivo: 2.1. Nota: la fuente no publica intervalo de confianza en el abstract. Interpretación registrada: apoya menos que el exudado amigdalino, del que se distingue.'
  - texto: El valor 2.1 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 2.1. Nota: la fuente no publica intervalo de confianza en el abstract. Interpretación registrada: apoya menos que el exudado amigdalino, del que se distingue.'
---

# Faringitis estreptocócica

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Streptococcal pharyngitis

## Sinónimos

faringoamigdalitis estreptocócica

faringitis por estreptococo del grupo A

## Códigos

Snomed: 43878008; Cie10: J02.0

## Probabilidad basal

Valor: 0.37; IC del 95 %: 0.32 / 0.43; Población: niños menores de 18 años que consultan por odinofagia; metaanálisis de 29 estudios; Nota: solo vale para niños: en los menores de 5 años baja al 24% (IC95% 21-26%). En adultos no hay estimación agrupada; ver pendiente; Referencia: pmid:20696723

## Hallazgos clínicos

### Exudado amigdalino (HM:3026)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 3.4; Referencia: pmid:11147989; Nota: la fuente no publica intervalo de confianza en el abstract

**Decisión:** el hallazgo aislado más útil, y aun así insuficiente por sí solo

### Exudado faríngeo (HM:3027)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 2.1; Referencia: pmid:11147989; Nota: la fuente no publica intervalo de confianza en el abstract

**Decisión:** apoya menos que el exudado amigdalino, del que se distingue

### Exposición reciente a faringitis estreptocócica (HM:3028)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 1.9; Referencia: pmid:11147989; Nota: exposición en las dos semanas previas; sin intervalo en el abstract

**Decisión:** dato de anamnesis con peso escaso

### Adenopatía cervical anterior dolorosa (HM:3029)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**LR negativo:** Valor: 0.6; Referencia: pmid:11147989; Nota: la fuente no publica intervalo de confianza en el abstract

**Decisión:** su ausencia es lo que más reduce la probabilidad, y aun así la deja en más de la mitad de la previa

### Hipertrofia amigdalina (HM:3030)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**LR negativo:** Valor: 0.63; Referencia: pmid:11147989; Nota: la fuente no publica intervalo de confianza en el abstract

**Decisión:** su ausencia reduce poco la probabilidad

### Odinofagia (HM:0211)

**Significante:** Dolor al tragar referido por el paciente, habitualmente localizado en la garganta; es el motivo de consulta más frecuente de la mononucleosis infecciosa y de las faringitis (pmid:25822555).

**Significado:** Inflamación o lesión de la mucosa orofaríngea o esofágica que se estimula con la deglución; en la mononucleosis refleja la replicación viral inicial en la orofaringe (pmid:25774295).

**Falsos positivos:** Disfagia sin dolor, que indica dificultad para tragar y no dolor / Dolor cervical musculoesquelético que el paciente refiere a la garganta

**Rol:** Manifestación

**Estado del LR:** LR no medible

**Motivo:** es el motivo de consulta que define la población estudiada, no una prueba dentro de ella

## Reglas clínicas

Nombre: Ausencia de exudado; Componentes: Exudado amigdalino / Exudado faríngeo; Criterio: ausencia de exudado amigdalino o faríngeo; LR negativo: 0.74; Referencia: pmid:11147989; Decisión: su ausencia apenas modifica la probabilidad; no sirve para descartar

## Escalas

Nombre: Criterios de Centor; Componentes declarados: cuatro variables clínicas (1 punto cada una): fiebre referida o medida > 38 °C, ausencia de tos, exudado amigdalino o faríngeo y adenopatía cervical anterior dolorosa; Graduación: Parámetro: Puntuación de Centor; Unidad: puntos; Lectura: disjunto; Tramos: Rango documentado: 4 puntos (probabilidad alta); Desde: 4; Hasta: 5; Prevalencia: 0.56; Referencia: pmid:6763125; Decisión: la probabilidad ronda el 56%; orienta a realizar prueba rápida o tratamiento según protocolo local / Rango documentado: 3 puntos (probabilidad intermedia-alta); Desde: 3; Hasta: 4; Prevalencia: 0.32; Referencia: pmid:6763125; Decisión: probabilidad de 32%; indicación habitual de prueba rápida de antígeno o cultivo / Rango documentado: 2 puntos (probabilidad intermedia); Desde: 2; Hasta: 3; Prevalencia: 0.15; Referencia: pmid:6763125; Decisión: probabilidad de 15%; orienta a prueba diagnóstica rápida antes de tratar / Rango documentado: 1 punto (probabilidad baja); Desde: 1; Hasta: 2; Prevalencia: 0.065; Referencia: pmid:6763125; Decisión: probabilidad muy baja (6.5%); generalmente no requiere prueba ni antibiótico / Rango documentado: 0 puntos (probabilidad mínima); Desde: 0; Hasta: 1; Prevalencia: 0.025; Referencia: pmid:6763125; Decisión: descarta prácticamente la etiología estreptocócica (2.5%); no tratar ni cultivar

Nombre: Escala de McIsaac (Centor modificada); Componentes declarados: criterios de Centor con ajuste por edad: fiebre > 38 °C (+1), ausencia de tos (+1), exudado o hipertrofia amigdalina (+1), adenopatía cervical anterior dolorosa (+1); edad 3 a 14 años (+1), edad 15 a 44 años (0), edad ≥ 45 años (-1); Graduación: Parámetro: Puntuación de McIsaac; Unidad: puntos; Lectura: disjunto; Tramos: Rango documentado: 4 a 5 puntos (riesgo alto); Desde: 4; Hasta: 6; Prevalencia rango: 0.51 / 0.53; Referencia: pmid:9475915; Decisión: riesgo alto (51-53%); indicación de prueba rápida o tratamiento empírico según guías locales / Rango documentado: 3 puntos (riesgo intermedio-alto); Desde: 3; Hasta: 4; Prevalencia rango: 0.28 / 0.35; Referencia: pmid:9475915; Decisión: riesgo del 28-35%; indicación de prueba diagnóstica rápida o cultivo / Rango documentado: 2 puntos (riesgo intermedio); Desde: 2; Hasta: 3; Prevalencia rango: 0.11 / 0.17; Referencia: pmid:9475915; Decisión: riesgo del 11-17%; indicación de prueba diagnóstica rápida o cultivo / Rango documentado: 1 punto (riesgo bajo); Desde: 1; Hasta: 2; Prevalencia rango: 0.05 / 0.1; Referencia: pmid:9475915; Decisión: riesgo del 5-10%; no requiere pruebas adicionales ni antibióticos / Rango documentado: 0 o menor (riesgo mínimo); Hasta: 1; Prevalencia rango: 0.01 / 0.025; Referencia: pmid:9475915; Decisión: riesgo mínimo (1-2.5%); manejo sintomático exclusivo sin antibióticos

## Conclusión de la fuente

Ningún elemento aislado de la anamnesis o de la exploración física es lo bastante preciso para excluir ni para diagnosticar la faringitis estreptocócica. Una regla de predicción clínica bien validada sí resulta útil y ayuda al médico a usar de forma más informada las pruebas rápidas de antígeno y el cultivo faríngeo.

## Aspectos pendientes de documentación

Se incorporaron las escalas canónicas de Centor (pmid:6763125) y McIsaac (pmid:9475915). Queda pendiente evaluar la incorporación de la regla de Breese para población pediátrica específica si se requiere mayor granularidad.

Probabilidad base en adultos. Aalbers 2011 (pmid:21631919; 21 estudios, mayores de 14 años) no da prevalencia agrupada: en sus series oscila entre el 4.7% y el 37.6%, y tres de ellas excluían a los pacientes con Centor menor de 2, lo que infla el extremo alto. No se transcribe como rango para no leerlo como estimación.

## Referencias y procedencia

**pmid:11147989:** The rational clinical examination. Does this patient have strep throat?. JAMA, 2000. DOI: 10.1001/jama.284.22.2912.

**pmid:20696723:** Prevalence of streptococcal pharyngitis and streptococcal carriage in children: a meta-analysis. Pediatrics, 2010. DOI: 10.1542/peds.2009-2648.

**pmid:21631919:** Predicting streptococcal pharyngitis in adults in primary care: a systematic review of the diagnostic accuracy of symptoms and signs and validation of the Centor score. BMC Med, 2011. DOI: 10.1186/1741-7015-9-67.

**pmid:6763125:** The diagnosis of strep throat in adults in the emergency room. Med Decis Making, 1981. DOI: 10.1177/0272989X8100100304.

**pmid:9475915:** A clinical score to reduce unnecessary antibiotic use in patients with sore throat. CMAJ, 1998. DOI: no documentado.

**pmid:25774295:** Infectious mononucleosis. Clin Transl Immunology, 2015. DOI: 10.1038/cti.2015.1.

**pmid:25822555:** Common questions about infectious mononucleosis. Am Fam Physician, 2015. DOI: no documentado.

Fuente clínica: medsemiotics-db, condición HM:6009.
