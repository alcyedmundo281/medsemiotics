---
id: HM6005-01
slug: derrame-pleural-exudado-criterios-light-colesterol
title: 'Derrame pleural exudativo: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-08-21'
author: Dr. Alcy Torres
category: neumologia
category_label: Neumología y Medicina Interna
tags:
- derrame-pleural-exudativo
- neumologia
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: a6b2afeb208457aaf6ce2d86ff78304f45071d5b
  condicion: condiciones/HM6005-derrame-pleural-exudativo.yaml
  archivos:
    conceptos/HM3007-derrame-pleural.yaml: a0ff591f0ccbe7b4ce56d06f14b904174cc9be542c879da32ea43688912c76c3
    conceptos/HM3008-colesterol-pleural-elevado.yaml: 54f1e2a139a84af23e9dac062e42c6a2b79a150d87d9657452f6860ecb5d13e6
    conceptos/HM3009-ldh-pleural-elevada.yaml: b2afdd29ba8d0e1489ef7ec4578124f9479c4586db527cf66e5f8fc8df6287d2
    conceptos/HM3010-cociente-colesterol-pleural-suero.yaml: 43eab803b2a803b5ab218164c56656161a0ceb952695913661ee48c75f443180
    conceptos/HM3011-criterios-de-light.yaml: 7eabb4a95b5af5e3287e70f2a81c8813560748ce04688c042675e12bd1dfa94f
    condiciones/HM6005-derrame-pleural-exudativo.yaml: be323c90b632013bda6e773b21184abc9afb8f77d920168ca036ee2b17c18d44
    referencias/pmid-24938565.yaml: e486bbf283c8e3791fee065bb75aa0dad8434e5930583c00d3ca456c255614dc
grounding:
  condicion_id: HM:6005
  condicion_nombre: Derrame pleural exudativo
  concepto_id: HM:3009
  concepto_nombre: LDH elevada en líquido pleural
  estado_lr: medido
  lr_positivo: 18
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:24938565
  referencia_cita: Wilcox ME, Chong CA, Stanbrook MB, Tricco AC, Wong C, Straus SE Does this patient have an exudative pleural effusion? The Rational Clinical Examination systematic review JAMA 2014
  pmid: '24938565'
  doi: 10.1001/jama.2014.5552
triada:
  significante: LDH elevada en líquido pleural
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: confirma exudado con un intervalo estrecho y reproducible
evidencia:
- concepto: HM:3008
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo:
    rango:
    - 7.1
    - 250
    umbral: colesterol pleural > 55 mg/dL
    ref: pmid:24938565
    nota: rango entre estudios, muy amplio. El extremo superior refleja series pequeñas; conviene leerlo como «desplaza mucho», no como un valor.
  decision: el indicador aislado más potente para clasificar el derrame
- concepto: HM:3009
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo:
    valor: 18
    ic95:
    - 6.8
    - 46
    umbral: LDH pleural > 200 U/L
    ref: pmid:24938565
  decision: confirma exudado con un intervalo estrecho y reproducible
- concepto: HM:3010
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo:
    valor: 14
    ic95:
    - 5.5
    - 38
    umbral: cociente > 0.3
    ref: pmid:24938565
  decision: alternativa al colesterol absoluto cuando se dispone del sérico
- concepto: HM:3011
  rol: prueba_sensible
  estado_lr: medido
  lr_negativo:
    valor: 0.04
    ic95:
    - 0.02
    - 0.11
    umbral: ausencia de los tres criterios
    ref: pmid:24938565
  decision: 'su valor está en el negativo: si no se cumple ninguno de los tres, el exudado queda prácticamente descartado'
- concepto: HM:3007
  rol: manifestacion
  estado_lr: no_medible
  motivo: 'es la condición previa, no una prueba: sin derrame no hay nada que clasificar como exudado o trasudado'
autoevaluacion:
- id: q1
  pregunta: ¿Qué cociente registra la fuente para LDH elevada en líquido pleural en Derrame pleural exudativo?
  concepto_id: HM:3009
  referencia_id: pmid:24938565
  pmid: '24938565'
  doi: 10.1001/jama.2014.5552
  opciones:
  - texto: 'LR positivo: 18.'
    correcta: true
    feedback: 'Registro HM:6005: LR positivo: 18.'
  - texto: La fuente no registra ningún cociente medido para este hallazgo.
    correcta: false
    feedback: 'El registro documenta: LR positivo: 18.'
- id: q2
  pregunta: ¿Cómo está documentado el LR de Colesterol elevado en líquido pleural en Derrame pleural exudativo?
  concepto_id: HM:3008
  referencia_id: pmid:24938565
  pmid: '24938565'
  doi: 10.1001/jama.2014.5552
  opciones:
  - texto: Hay una estimación numérica única disponible para calcular la probabilidad posterior.
    correcta: false
    feedback: 'El registro documenta: La fuente registra un rango, no una estimación numérica única.'
  - texto: La fuente registra un rango, no una estimación numérica única.
    correcta: true
    feedback: 'Registro HM:6005: La fuente registra un rango, no una estimación numérica única.'
---

# Derrame pleural exudativo

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Exudative pleural effusion

## Sinónimos

exudado pleural

derrame pleural tipo exudado

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Hallazgos clínicos

### Colesterol elevado en líquido pleural (HM:3008)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Rango documentado: 7.1 / 250; Umbral: colesterol pleural > 55 mg/dL; Referencia: pmid:24938565; Nota: rango entre estudios, muy amplio. El extremo superior refleja series pequeñas; conviene leerlo como «desplaza mucho», no como un valor.

**Decisión:** el indicador aislado más potente para clasificar el derrame

### LDH elevada en líquido pleural (HM:3009)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 18; IC del 95 %: 6.8 / 46; Umbral: LDH pleural > 200 U/L; Referencia: pmid:24938565

**Decisión:** confirma exudado con un intervalo estrecho y reproducible

### Cociente colesterol pleural/sérico elevado (HM:3010)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 14; IC del 95 %: 5.5 / 38; Umbral: cociente > 0.3; Referencia: pmid:24938565

**Decisión:** alternativa al colesterol absoluto cuando se dispone del sérico

### Criterios de Light (HM:3011)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**LR negativo:** Valor: 0.04; IC del 95 %: 0.02 / 0.11; Umbral: ausencia de los tres criterios; Referencia: pmid:24938565

**Decisión:** su valor está en el negativo: si no se cumple ninguno de los tres, el exudado queda prácticamente descartado

### Derrame pleural (HM:3007)

**Rol:** Manifestación

**Estado del LR:** LR no medible

**Motivo:** es la condición previa, no una prueba: sin derrame no hay nada que clasificar como exudado o trasudado

## Referencias y procedencia

**pmid:24938565:** Does this patient have an exudative pleural effusion? The Rational Clinical Examination systematic review. JAMA, 2014. DOI: 10.1001/jama.2014.5552.

Fuente clínica: medsemiotics-db, condición HM:6005.
