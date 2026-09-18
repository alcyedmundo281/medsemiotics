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
  revision: f2e95a0834f2c2789e6cc56b5610d9612bdec93b
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6009-faringitis-estreptococica.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0211-odinofagia.yaml: cdb3be1c4118ddfbdbf416bfee31243ab624779e988a089984d8f863ad51551f
    conceptos/HM3026-exudado-amigdalino.yaml: 2035d19d7697ad00e8860ba5bf2e4be6d4c17b557a6f8ab8b8c966ae088e8b43
    conceptos/HM3027-exudado-faringeo.yaml: 06a0f094562bd1a1b9c9ec09d5dc2c2ca5b963c627c82897dd1f93ac6dca0c50
    conceptos/HM3028-exposicion-estreptococo.yaml: 26edc47823c8d5fa6dc3268a3bdcc36f8470f2fe973db587f023d6ac3ccaff21
    conceptos/HM3029-adenopatia-cervical-anterior-dolorosa.yaml: c126e8e1eee16e645ed035c25ba116ac1aa29d60638b8b8dae0a98875240574a
    conceptos/HM3030-hipertrofia-amigdalina.yaml: c5638d1545cdfaeeec3fa4b95fd6b0b104c48be33b947131f4e3b8e8dc4198eb
    condiciones/HM6009-faringitis-estreptococica.yaml: 3d245901b5953adc1bc2bb4fabfb95e3855fa4b1d5009751cfbe62f421bc4ef7
    referencias/pmid-11147989.yaml: f6aca870e75ab118eba2a41950cb38d56cabbcb69b65ba4e5eadc1f671edafc8
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

strep throat

## Códigos

Snomed: No documentado.; Cie10: No documentado.

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

**Rol:** Manifestación

**Estado del LR:** LR no medible

**Motivo:** es el motivo de consulta que define la población estudiada, no una prueba dentro de ella

## Reglas clínicas

Nombre: Ausencia de exudado; Componentes: Exudado amigdalino (HM:3026) / Exudado faríngeo (HM:3027); Criterio: ausencia de exudado amigdalino o faríngeo; LR negativo: 0.74; Referencia: pmid:11147989; Decisión: su ausencia apenas modifica la probabilidad; no sirve para descartar

## Conclusión de la fuente

Ningún elemento aislado de la anamnesis o de la exploración física es lo bastante preciso para excluir ni para diagnosticar la faringitis estreptocócica. Una regla de predicción clínica bien validada sí resulta útil y ayuda al médico a usar de forma más informada las pruebas rápidas de antígeno y el cultivo faríngeo.

## Aspectos pendientes de documentación

La fuente describe tres reglas de predicción clínica validadas, para población adulta y pediátrica, pero el abstract no las nombra ni las cuantifica. Registrarlas exige el texto completo.

## Referencias y procedencia

**pmid:11147989:** The rational clinical examination. Does this patient have strep throat?. JAMA, 2000. DOI: 10.1001/jama.284.22.2912.

Fuente clínica: medsemiotics-db, condición HM:6009.
