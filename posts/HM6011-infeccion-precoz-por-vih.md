---
id: HM6011-01
slug: infeccion-precoz-por-vih-precision-semiotica
title: 'Infección precoz por VIH: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-08-21'
author: Dr. Alcy Torres
category: infectologia
category_label: Infectología y Medicina Interna
tags:
- criterios
- infeccion-precoz-por-vih
- infectologia
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: 1d33074a25224a006e43e010c4be6ad39a771e7e
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6011-infeccion-precoz-por-vih.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0100-signo-vital-alterado.yaml: 3e0914bff0c0dc8f1a07185d49c70c4ee7dcf11cfa7ebc3281d611f5abb4f504
    conceptos/HM0101-fiebre.yaml: d8367b5824cbb321094893d8dde57e082205ace1ba21a89144af01209279e45e
    conceptos/HM0300-sintoma-digestivo.yaml: 2c9dfe41462c5927070d1020039bd0dac823bcf998d53ac0a7d8e04ccab240aa
    conceptos/HM0302-vomitos.yaml: c2a3e83028a5dbb8b5d22771c6f413648cbe087e1f3dffa381f416e6bc5a12c9
    conceptos/HM0600-signo-de-exploracion.yaml: 86a2ac9babe66028eecc797ddbf4d9ea382a6fd685e9cb8df91bb959029d62bf
    conceptos/HM0607-adenopatias.yaml: 849fe51a52fd503725ed3d2da2115ed0f2dab016bd0150088c7a5c079a718a10
    conceptos/HM0800-sintoma-general.yaml: 39761069b5de091733e7864bb0c96f68755b6d3fa5e59003f5f8c7949b0c4827
    conceptos/HM0803-perdida-de-peso.yaml: 78cd9514f8137e60f123c191cb3939fa57bc11c77dcda85c914e82e8eac1d22e
    conceptos/HM3039-ulceras-genitales.yaml: 8d597fccd98b8a83f14956f25483e0c0d5b2e10c73bb1dc3c849e10160f1245a
    conceptos/HM3040-adenopatias-referidas.yaml: ac43dcc86eab8dbe3ebbe9334eedf4bf57ba830257d2b3f5cfa6f008634e7643
    condiciones/HM6003-mononucleosis-infecciosa.yaml: fdd67306d3d26ce5724613adc81b59ab01bd965186ce7c3d82ca67bf267ce2e9
    condiciones/HM6011-infeccion-precoz-por-vih.yaml: da3f12b7d2d61192612c0bc2de23c0f8bb38cf47d7f94c19d50712de89160d80
    referencias/pmid-25027143.yaml: 9b6cbb935f7a83c37d6ec407afb0d65294b8b4cc753e02096259ca180ee189f0
    referencias/pmid-27929264.yaml: e81a2145a034e9bc8da32cec5e2648fd1bc2ebd2f180fe99434e3da94d8a8810
grounding:
  condicion_id: HM:6011
  condicion_nombre: Infección precoz por VIH
  concepto_id: HM:3039
  concepto_nombre: Úlceras genitales
  estado_lr: medido
  lr_positivo: 5.4
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:25027143
  referencia_cita: 'Wood E, Kerr T, Rowell G, Montaner JS, Phillips P, Korthuis PT, Simel DL Does this adult patient have early HIV infection?: The Rational Clinical Examination systematic review JAMA 2014'
  pmid: '25027143'
  doi: 10.1001/jama.2014.5954
triada:
  significante: Úlceras genitales
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: el síntoma que más aumenta la probabilidad
evidencia:
- concepto: HM:3039
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id001
    valor: 5.4
    ic95:
    - 2.5
    - 12
    ref: pmid:25027143
  decision: el síntoma que más aumenta la probabilidad
- concepto: HM:0803
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id002
    valor: 4.7
    ic95:
    - 2.1
    - 7.2
    ref: pmid:25027143
- concepto: HM:0302
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo:
    valor: 4.6
    ic95:
    - 2.5
    - 8.0
    ref: pmid:25027143
- concepto: HM:3040
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo:
    valor: 4.6
    ic95:
    - 1.3
    - 8.0
    ref: pmid:25027143
  decision: nótese que el síntoma referido pesa MÁS que el signo hallado en la exploración, que tiene LR 3.1
- concepto: HM:0101
  rol: prueba_sensible
  estado_lr: medido
  lr_negativo:
    valor: 0.74
    ic95:
    - 0.64
    - 0.84
    ref: pmid:25027143
  decision: su ausencia reduce la probabilidad muy poco; no sirve para descartar
- concepto: HM:0607
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo:
    valor: 3.1
    ic95:
    - 1.0
    - 5.2
    ref: pmid:25027143
  lr_negativo:
    valor: 0.7
    ic95:
    - 0.49
    - 0.92
    ref: pmid:25027143
  decision: el signo exploratorio más útil, y aun así modesto. El extremo inferior de su intervalo toca 1.0, es decir, es compatible con no aportar nada.
autoevaluacion:
- id: q1
  pregunta: En Infección precoz por VIH, ¿cuál es el resultado documentado del LR positivo para «Úlceras genitales»?
  concepto_id: HM:3039
  referencia_id: pmid:25027143
  pmid: '25027143'
  doi: 10.1001/jama.2014.5954
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6011
    concepto_id: HM:3039
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: el síntoma que más aumenta la probabilidad
    advertencia: null
  opciones:
  - texto: 'LR positivo: 5.4.'
    correcta: true
    feedback: 'LR positivo: 5.4. IC del 95 %: 2.5 a 12. Interpretación registrada: el síntoma que más aumenta la probabilidad.'
  - texto: El valor 5.4 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 5.4. IC del 95 %: 2.5 a 12. Interpretación registrada: el síntoma que más aumenta la probabilidad.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 5.4. LR positivo: 5.4. IC del 95 %: 2.5 a 12. Interpretación registrada: el síntoma que más aumenta la probabilidad.'
- id: q2
  pregunta: En Infección precoz por VIH, ¿cuál es el resultado documentado del LR positivo para «Pérdida de peso»?
  concepto_id: HM:0803
  referencia_id: pmid:25027143
  pmid: '25027143'
  doi: 10.1001/jama.2014.5954
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6011
    concepto_id: HM:0803
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: null
    motivo: null
    decision: null
    advertencia: null
  opciones:
  - texto: El valor 4.7 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 4.7. IC del 95 %: 2.1 a 7.2.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 4.7. LR positivo: 4.7. IC del 95 %: 2.1 a 7.2.'
  - texto: 'LR positivo: 4.7.'
    correcta: true
    feedback: 'LR positivo: 4.7. IC del 95 %: 2.1 a 7.2.'
---

# Infección precoz por VIH

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Early HIV infection

## Sinónimos

primoinfección por VIH

infección aguda por VIH

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Hallazgos clínicos

### Úlceras genitales (HM:3039)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 5.4; IC del 95 %: 2.5 / 12; Referencia: pmid:25027143

**Decisión:** el síntoma que más aumenta la probabilidad

### Pérdida de peso (HM:0803)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 4.7; IC del 95 %: 2.1 / 7.2; Referencia: pmid:25027143

### Vómitos (HM:0302)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 4.6; IC del 95 %: 2.5 / 8.0; Referencia: pmid:25027143

### Adenopatías referidas por el paciente (HM:3040)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 4.6; IC del 95 %: 1.3 / 8.0; Referencia: pmid:25027143

**Decisión:** nótese que el síntoma referido pesa MÁS que el signo hallado en la exploración, que tiene LR 3.1

### Fiebre (HM:0101)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**LR negativo:** Valor: 0.74; IC del 95 %: 0.64 / 0.84; Referencia: pmid:25027143

**Decisión:** su ausencia reduce la probabilidad muy poco; no sirve para descartar

### Adenopatías (HM:0607)

**Significante:** Ganglios linfáticos palpables de tamaño o consistencia anormales. Se describen por región, tamaño, consistencia, sensibilidad y movilidad; se clasifican como localizadas o generalizadas, cuando afectan dos o más regiones (pmid:27929264).

**Significado:** Respuesta de los ganglios a infección, inflamación o infiltración neoplásica. Las localizadas orientan a la región que drenan; las generalizadas suelen indicar una enfermedad sistémica (pmid:27929264).

**Falsos positivos:** Ganglios pequeños, blandos y móviles de tamaño normal, frecuentes en cuello e ingle / Masas no ganglionares como lipomas, quistes o glándulas salivales

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 3.1; IC del 95 %: 1.0 / 5.2; Referencia: pmid:25027143

**LR negativo:** Valor: 0.7; IC del 95 %: 0.49 / 0.92; Referencia: pmid:25027143

**Decisión:** el signo exploratorio más útil, y aun así modesto. El extremo inferior de su intervalo toca 1.0, es decir, es compatible con no aportar nada.

## Reglas clínicas

Nombre: Ausencia de todo hallazgo; Componentes: Úlceras genitales / Pérdida de peso / Vómitos / Adenopatías referidas por el paciente / Fiebre / Adenopatías; Criterio: ninguno de los hallazgos considerados presente; LR negativo: 0.47; IC del 95 %: 0.38 / 0.58; Referencia: pmid:25027143; Decisión: ni siquiera no encontrar NADA descarta la infección: la probabilidad baja a menos de la mitad, no a cero; Nota: calculado sobre estudios que consideraban combinaciones de 4 a 17 hallazgos posibles

## Conclusión de la fuente

La utilidad limitada de la exploración clínica para detectar o descartar la infección precoz por VIH subraya la importancia del cribado sistemático en adultos.

## Referencias y procedencia

**pmid:25027143:** Does this adult patient have early HIV infection?: The Rational Clinical Examination systematic review. JAMA, 2014. DOI: 10.1001/jama.2014.5954.

**pmid:27929264:** Unexplained Lymphadenopathy: Evaluation and Differential Diagnosis. Am Fam Physician, 2016. DOI: no documentado.

Fuente clínica: medsemiotics-db, condición HM:6011.
