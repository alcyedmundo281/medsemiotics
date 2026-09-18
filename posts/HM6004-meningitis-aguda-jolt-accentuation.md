---
id: HM6004-01
slug: meningitis-aguda-sacudida-cefalica
title: 'Meningitis aguda: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-08-20'
author: Dr. Alcy Torres
category: neurologia
category_label: Neurología
tags:
- criterios
- meningitis-aguda
- neurologia
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: 1db38dcd49a911196aa7c2f30bd8ad0e6cb17c54
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6004-meningitis-aguda.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0101-fiebre.yaml: d8367b5824cbb321094893d8dde57e082205ace1ba21a89144af01209279e45e
    conceptos/HM0207-cefalea.yaml: 3a7957f3f8cda87461090f0aff7e5cccde0cbea0a59b1bd8716a6fb509bb4b8c
    conceptos/HM0301-nauseas.yaml: e678ffbd65c8ecbae1afe311de0693dc240bff7d676879838347df44fa30556a
    conceptos/HM0302-vomitos.yaml: c2a3e83028a5dbb8b5d22771c6f413648cbe087e1f3dffa381f416e6bc5a12c9
    conceptos/HM0501-alteracion-del-nivel-de-conciencia.yaml: c3d0515c056d2458152b77498e02ec985a7f67d31c63bec961722da48ac6d980
    conceptos/HM3005-rigidez-de-nuca.yaml: acf2a79e35697ca46f2a084ef549f5345ad4d40e9014474088cb2f897f43e9c7
    conceptos/HM3006-acentuacion-cefalea-sacudida.yaml: b7e237eb2e3f5ead09a07aff8832f8b79afc05a258a7649cc778aba725441a12
    condiciones/HM6004-meningitis-aguda.yaml: 094b0b47f35478cc7db439647a545a988f3804088f1bfbc0df379019c3efb45a
    referencias/pmid-10411200.yaml: 8b029e69cf573d005a0416d103199e091dfd7156895fad9de3768aebf43a5eab
grounding:
  condicion_id: HM:6004
  condicion_nombre: Meningitis aguda
  concepto_id: HM:3006
  concepto_nombre: Acentuación de la cefalea con la sacudida cefálica
  estado_lr: medido
  lr_positivo: 2.2
  lr_negativo: 0.0
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:10411200
  referencia_cita: Attia J, Hatala R, Cook DJ, Wong JG The rational clinical examination. Does this adult patient have acute meningitis? JAMA 1999
  pmid: '10411200'
  doi: 10.1001/jama.282.2.175
  sensibilidad: 1.0
  especificidad: 0.54
triada:
  significante: Acentuación de la cefalea con la sacudida cefálica
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: maniobra adjunta útil en quien ya tiene fiebre y cefalea; su negatividad es lo que más ayuda
evidencia:
- concepto: HM:3006
  rol: prueba_sensible
  estado_lr: medido
  sensibilidad: 1.0
  especificidad: 0.54
  lr_positivo: &id001
    valor: 2.2
    ref: pmid:10411200
    poblacion: pacientes que ya presentan fiebre y cefalea
  lr_negativo:
    valor: 0.0
    ref: pmid:10411200
    poblacion: pacientes que ya presentan fiebre y cefalea
    nota: 'un LR− de 0 procede de una sensibilidad del 100% en la serie estudiada. Tratarlo como certeza absoluta sería un error de lectura: es el resultado de una muestra, no una imposibilidad.'
  decision: maniobra adjunta útil en quien ya tiene fiebre y cefalea; su negatividad es lo que más ayuda
- concepto: HM:0207
  rol: manifestacion
  estado_lr: no_medido
  sensibilidad: 0.5
  ic95_sensibilidad:
  - 0.32
  - 0.68
  motivo: la fuente publica sensibilidad agrupada pero no especificidad, así que el cociente no es calculable desde el abstract
- concepto: HM:0301
  rol: manifestacion
  estado_lr: no_medido
  sensibilidad: 0.3
  ic95_sensibilidad:
  - 0.22
  - 0.38
  motivo: sensibilidad agrupada sin especificidad; LR no calculable
- concepto: HM:0302
  rol: manifestacion
  estado_lr: no_medido
  sensibilidad: 0.3
  ic95_sensibilidad:
  - 0.22
  - 0.38
  motivo: la fuente agrupa náuseas y vómitos en una sola estimación
- concepto: HM:0101
  rol: prueba_sensible
  estado_lr: no_medido
  motivo: forma parte de la tríada fiebre + rigidez de nuca + alteración del estado mental, cuya presencia de al menos uno tiene sensibilidad del 99-100%. La fuente no desglosa el cociente de cada componente por separado.
- concepto: HM:3005
  rol: prueba_sensible
  estado_lr: no_medido
  motivo: componente de la tríada; la fuente no publica su cociente aislado
- concepto: HM:0501
  rol: prueba_sensible
  estado_lr: no_medido
  motivo: componente de la tríada; la fuente no publica su cociente aislado
autoevaluacion:
- id: q1
  pregunta: En Meningitis aguda, ¿cuál es el resultado documentado del LR positivo para «Acentuación de la cefalea con la sacudida cefálica»?
  concepto_id: HM:3006
  referencia_id: pmid:10411200
  pmid: '10411200'
  doi: 10.1001/jama.282.2.175
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6004
    concepto_id: HM:3006
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: maniobra adjunta útil en quien ya tiene fiebre y cefalea; su negatividad es lo que más ayuda
    advertencia: null
  opciones:
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 2.2. LR positivo: 2.2. Interpretación registrada: maniobra adjunta útil en quien ya tiene fiebre y cefalea; su negatividad es lo que más ayuda.'
  - texto: 'LR positivo: 2.2.'
    correcta: true
    feedback: 'LR positivo: 2.2. Interpretación registrada: maniobra adjunta útil en quien ya tiene fiebre y cefalea; su negatividad es lo que más ayuda.'
  - texto: El valor 2.2 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 2.2. Interpretación registrada: maniobra adjunta útil en quien ya tiene fiebre y cefalea; su negatividad es lo que más ayuda.'
- id: q2
  pregunta: En Meningitis aguda, ¿qué estado de la evidencia corresponde a «Cefalea» según la fuente?
  concepto_id: HM:0207
  referencia_id: null
  pmid: null
  doi: null
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6004
    concepto_id: HM:0207
    estado_lr: no_medido
    campo: null
    dato: null
    poblacion: null
    motivo: la fuente publica sensibilidad agrupada pero no especificidad, así que el cociente no es calculable desde el abstract
    decision: null
    advertencia: null
  opciones:
  - texto: LR no medido
    correcta: true
    feedback: 'LR no medido Motivo: la fuente publica sensibilidad agrupada pero no especificidad, así que el cociente no es calculable desde el abstract.'
  - texto: LR no medible
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medido». LR no medido Motivo: la fuente publica sensibilidad agrupada pero no especificidad, así que el cociente no es calculable desde el abstract.'
  - texto: Sin efecto discriminativo
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medido». LR no medido Motivo: la fuente publica sensibilidad agrupada pero no especificidad, así que el cociente no es calculable desde el abstract.'
---

# Meningitis aguda

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Acute meningitis

## Sinónimos

meningitis bacteriana aguda

meningitis vírica aguda

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Hallazgos clínicos

### Acentuación de la cefalea con la sacudida cefálica (HM:3006)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**Sensibilidad:** 1.0

**Especificidad:** 0.54

**LR positivo:** Valor: 2.2; Referencia: pmid:10411200; Población: pacientes que ya presentan fiebre y cefalea

**LR negativo:** Valor: 0.0; Referencia: pmid:10411200; Población: pacientes que ya presentan fiebre y cefalea; Nota: un LR− de 0 procede de una sensibilidad del 100% en la serie estudiada. Tratarlo como certeza absoluta sería un error de lectura: es el resultado de una muestra, no una imposibilidad.

**Decisión:** maniobra adjunta útil en quien ya tiene fiebre y cefalea; su negatividad es lo que más ayuda

### Cefalea (HM:0207)

**Rol:** Manifestación

**Estado del LR:** LR no medido

**Sensibilidad:** 0.5

**Ic95 sensibilidad:** 0.32 / 0.68

**Motivo:** la fuente publica sensibilidad agrupada pero no especificidad, así que el cociente no es calculable desde el abstract

### Náuseas (HM:0301)

**Rol:** Manifestación

**Estado del LR:** LR no medido

**Sensibilidad:** 0.3

**Ic95 sensibilidad:** 0.22 / 0.38

**Motivo:** sensibilidad agrupada sin especificidad; LR no calculable

### Vómitos (HM:0302)

**Rol:** Manifestación

**Estado del LR:** LR no medido

**Sensibilidad:** 0.3

**Ic95 sensibilidad:** 0.22 / 0.38

**Motivo:** la fuente agrupa náuseas y vómitos en una sola estimación

### Fiebre (HM:0101)

**Rol:** Prueba sensible

**Estado del LR:** LR no medido

**Motivo:** forma parte de la tríada fiebre + rigidez de nuca + alteración del estado mental, cuya presencia de al menos uno tiene sensibilidad del 99-100%. La fuente no desglosa el cociente de cada componente por separado.

### Rigidez de nuca (HM:3005)

**Rol:** Prueba sensible

**Estado del LR:** LR no medido

**Motivo:** componente de la tríada; la fuente no publica su cociente aislado

### Alteración del nivel de conciencia (HM:0501)

**Rol:** Prueba sensible

**Estado del LR:** LR no medido

**Motivo:** componente de la tríada; la fuente no publica su cociente aislado

## Reglas clínicas

Nombre: Ausencia de la tríada clásica; Componentes: Fiebre (HM:0101) / Rigidez de nuca (HM:3005) / Alteración del nivel de conciencia (HM:0501); Criterio: ninguno de los tres presente; Sensibilidad de la presencia: 0.99 / 1.0; Referencia: pmid:10411200; Decisión: la ausencia simultánea de fiebre, rigidez de nuca y alteración del estado mental descarta la meningitis en la práctica; Advertencia: la fuente matiza que ante alto riesgo clínico hay que ir directamente a la punción lumbar, sin apoyarse en la exploración

## Referencias y procedencia

**pmid:10411200:** The rational clinical examination. Does this adult patient have acute meningitis?. JAMA, 1999. DOI: 10.1001/jama.282.2.175.

Fuente clínica: medsemiotics-db, condición HM:6004.
