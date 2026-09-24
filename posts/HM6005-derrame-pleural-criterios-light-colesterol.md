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
  revision: 1d33074a25224a006e43e010c4be6ad39a771e7e
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6005-derrame-pleural-exudativo.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0400-sintoma-respiratorio.yaml: 437414db42a3586a5896d3f91e90ee8ed51c7baef7b67741067b3ee04ca7a53b
    conceptos/HM0700-alteracion-analitica.yaml: 855280729989c53c674d74df1d9d1459df52ecfe46d1bb650f6bf3b590383f5b
    conceptos/HM0730-alteracion-enzimatica.yaml: eaace3c0ef5fc70eda08396c77e4b145c690302347b2c6dca54ffe7c2ceb5298
    conceptos/HM3007-derrame-pleural.yaml: c9c8eaf748230a1ecee3b74a98548dba77dc6f6c2690be1aa36daa58cd362bc5
    conceptos/HM3008-colesterol-pleural-elevado.yaml: 54f1e2a139a84af23e9dac062e42c6a2b79a150d87d9657452f6860ecb5d13e6
    conceptos/HM3009-ldh-pleural-elevada.yaml: b2afdd29ba8d0e1489ef7ec4578124f9479c4586db527cf66e5f8fc8df6287d2
    conceptos/HM3010-cociente-colesterol-pleural-suero.yaml: 43eab803b2a803b5ab218164c56656161a0ceb952695913661ee48c75f443180
    conceptos/HM3011-criterios-de-light.yaml: 7eabb4a95b5af5e3287e70f2a81c8813560748ce04688c042675e12bd1dfa94f
    conceptos/HM3148-lineas-b-pulmonares-bilaterales.yaml: bf438bf8faf27db643fbcfa947ad803782ce7e30b057ddcd3e21790d952d516e
    condiciones/HM6005-derrame-pleural-exudativo.yaml: 0e8b529637113d3e77650e09fafa6166ab43e58e3d62a252ee05990cda61e9dc
    referencias/pmid-22392031.yaml: 167a3ea8e8037ca94a29ecff6c379200f402babf474159c1a9b6a94336ee5e7b
    referencias/pmid-24360987.yaml: 8378261ca47f282fed9721d99f26ed84b33e42267908a065babf6ab0095501b2
    referencias/pmid-24938565.yaml: e486bbf283c8e3791fee065bb75aa0dad8434e5930583c00d3ca456c255614dc
    referencias/pmid-26218493.yaml: 6d5857478ed53b16e1e807535dfd875a1268ced08bfca4be21a703991508150f
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
  lr_positivo: &id002
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
  lr_positivo: &id001
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
  pregunta: 'En Derrame pleural exudativo, ¿cuál es el resultado documentado del LR positivo para «LDH elevada en líquido pleural»? Umbral: LDH pleural > 200 U/L.'
  concepto_id: HM:3009
  referencia_id: pmid:24938565
  pmid: '24938565'
  doi: 10.1001/jama.2014.5552
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6005
    concepto_id: HM:3009
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: confirma exudado con un intervalo estrecho y reproducible
    advertencia: null
  opciones:
  - texto: 'LR positivo: 18.'
    correcta: true
    feedback: 'LR positivo: 18. IC del 95 %: 6.8 a 46. Umbral: LDH pleural > 200 U/L. Interpretación registrada: confirma exudado con un intervalo estrecho y reproducible.'
  - texto: El valor 18 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 18. IC del 95 %: 6.8 a 46. Umbral: LDH pleural > 200 U/L. Interpretación registrada: confirma exudado con un intervalo estrecho y reproducible.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 18. LR positivo: 18. IC del 95 %: 6.8 a 46. Umbral: LDH pleural > 200 U/L. Interpretación registrada: confirma exudado con un intervalo estrecho y reproducible.'
- id: q2
  pregunta: 'Al evaluar «Colesterol elevado en líquido pleural» en Derrame pleural exudativo, ¿cómo debe comunicarse el LR positivo según la fuente? Umbral: colesterol pleural > 55 mg/dL.'
  concepto_id: HM:3008
  referencia_id: pmid:24938565
  pmid: '24938565'
  doi: 10.1001/jama.2014.5552
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6005
    concepto_id: HM:3008
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: null
    motivo: null
    decision: el indicador aislado más potente para clasificar el derrame
    advertencia: null
  opciones:
  - texto: 'LR positivo: 7.1, como estimación puntual única.'
    correcta: false
    feedback: '7.1 es el límite inferior del rango documentado, no una estimación puntual. LR positivo: rango de 7.1 a 250; no se registra una estimación puntual única. Umbral: colesterol pleural > 55 mg/dL. Nota: rango entre estudios, muy amplio. El extremo superior refleja series pequeñas; conviene leerlo como «desplaza mucho», no como un valor. Interpretación registrada: el indicador aislado más potente para clasificar el derrame.'
  - texto: 'LR positivo: 250, como estimación puntual única.'
    correcta: false
    feedback: '250 es el límite superior del rango documentado, no una estimación puntual. LR positivo: rango de 7.1 a 250; no se registra una estimación puntual única. Umbral: colesterol pleural > 55 mg/dL. Nota: rango entre estudios, muy amplio. El extremo superior refleja series pequeñas; conviene leerlo como «desplaza mucho», no como un valor. Interpretación registrada: el indicador aislado más potente para clasificar el derrame.'
  - texto: 'LR positivo: rango de 7.1 a 250; no se registra una estimación puntual única.'
    correcta: true
    feedback: 'LR positivo: rango de 7.1 a 250; no se registra una estimación puntual única. Umbral: colesterol pleural > 55 mg/dL. Nota: rango entre estudios, muy amplio. El extremo superior refleja series pequeñas; conviene leerlo como «desplaza mucho», no como un valor. Interpretación registrada: el indicador aislado más potente para clasificar el derrame.'
---

# Derrame pleural exudativo

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Exudative pleural effusion

## Sinónimos

exudado pleural

derrame pleural tipo exudado

## Códigos

Snomed: 13841000119107; Cie10: J90

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

**Significante:** Espacio anecoico entre la pared torácica y el pulmón, sobre el diafragma.

**Significado:** Líquido en el espacio pleural.

**Falsos positivos:** Ascitis subdiafragmática / Consolidación pulmonar / Órgano sólido / Engrosamiento o masa pleural / Derrame pericárdico / Ventana mala

**Rol:** Manifestación

**Estado del LR:** LR no medible

**Motivo:** es la condición previa, no una prueba: sin derrame no hay nada que clasificar como exudado o trasudado

## Aspectos pendientes de documentación

Sin probabilidad_base. Búsqueda en PubMed del 2026-09-23 de series de toracocentesis consecutivas: Porcel 2014 (pmid:24360987; 3077 pacientes) da las causas del derrame pero no la proporción de exudados en su resumen, y Wilcox 2014 (pmid:24938565) tampoco. Sumar las causas que suelen dar exudado sería inferir la cifra, no transcribirla. Falta leer el texto completo de Porcel 2014.

## Referencias y procedencia

**pmid:24360987:** Etiology of pleural effusions: analysis of more than 3,000 consecutive thoracenteses. Arch Bronconeumol, 2014. DOI: 10.1016/j.arbres.2013.11.007.

**pmid:24938565:** Does this patient have an exudative pleural effusion? The Rational Clinical Examination systematic review. JAMA, 2014. DOI: 10.1001/jama.2014.5552.

**pmid:22392031:** International evidence-based recommendations for point-of-care lung ultrasound. Intensive Care Med, 2012. DOI: 10.1007/s00134-012-2513-4.

**pmid:26218493:** Ultrasound in the diagnosis and management of pleural effusions. J Hosp Med, 2015. DOI: 10.1002/jhm.2434.

Fuente clínica: medsemiotics-db, condición HM:6005.
