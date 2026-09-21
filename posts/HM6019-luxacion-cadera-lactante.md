---
id: HM6019-01
slug: luxacion-cadera-lactante-barlow-ortolani
title: 'Luxación de cadera en el lactante: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-08-22'
author: Dr. Alcy Torres
category: pediatria
category_label: Pediatría y Ortopedia
tags:
- luxacion-de-cadera-en-el-lactante
- pediatria
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: e654998bddbb8c2b1d22e4da2f3375f9db6bc432
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6019-luxacion-cadera-lactante.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM3075-maniobras-de-barlow-y-ortolani.yaml: 43c819ea911471811bf4a17ff48eea18f4e84b64b57238a996fc999ddc4bca43
    conceptos/HM3076-limitacion-abduccion-cadera-lactante.yaml: 9573e001bae058b99488d56515e007eb920038be62889c2e83e4a37b2caca157
    conceptos/HM3077-chasquido-articular-cadera-lactante.yaml: ca91e3bf119a83bd0546f000c7203a50cd7595f1e4921202d0cc03b9d63bfa33
    condiciones/HM6019-luxacion-cadera-lactante.yaml: a59d5752344e43911133e92639cd19bb048fed52922287102d7a392dd360b47f
    referencias/pmid-38619828.yaml: 4d7ba894e0678354a11cec41782b767ceebd056d308c1ff8edde131894a71268
grounding:
  condicion_id: HM:6019
  condicion_nombre: Luxación de cadera en el lactante
  concepto_id: HM:3075
  concepto_nombre: Maniobras de Barlow y Ortolani positivas
  estado_lr: medido
  lr_positivo: 52
  lr_negativo: 0.55
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: lactantes de 3 meses o menores (n = 44 827 caderas en 8 estudios)
  referencia_id: pmid:38619828
  referencia_cita: 'Singh A, Wade RG, Metcalfe D, Perry DC Does This Infant Have a Dislocated Hip?: The Rational Clinical Examination Systematic Review JAMA 2024'
  pmid: '38619828'
  doi: 10.1001/jama.2024.2404
  sensibilidad: 0.46
  especificidad: 0.991
triada:
  significante: Maniobras de Barlow y Ortolani positivas
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: 'Maniobras de Barlow y Ortolani positivas: el signo que confirma la luxación inestable. Cuando es positiva eleva la probabilidad pretest de 0.94% a más del 33% (LR+ 52); su negatividad no descarta la displasia (LR- 0.55).'
evidencia:
- concepto: HM:3075
  rol: prueba_especifica
  estado_lr: medido
  sensibilidad: 0.46
  especificidad: 0.991
  poblacion: lactantes de 3 meses o menores (n = 44 827 caderas en 8 estudios)
  lr_positivo: &id001
    valor: 52
    ic95:
    - 21
    - 127
    ref: pmid:38619828
  lr_negativo:
    valor: 0.55
    ic95:
    - 0.37
    - 0.82
    ref: pmid:38619828
  decision: 'Maniobras de Barlow y Ortolani positivas: el signo que confirma la luxación inestable. Cuando es positiva eleva la probabilidad pretest de 0.94% a más del 33% (LR+ 52); su negatividad no descarta la displasia (LR- 0.55).'
- concepto: HM:3076
  rol: apoyo
  estado_lr: medido
  sensibilidad: 0.13
  especificidad: 0.97
  poblacion: lactantes de 3 meses o menores (n = 22 472 caderas en 3 estudios)
  lr_positivo: &id002
    valor: 3.6
    ic95:
    - 0.72
    - 18
    ref: pmid:38619828
  lr_negativo:
    valor: 0.91
    ic95:
    - 0.76
    - 1.1
    ref: pmid:38619828
  decision: 'Limitación de la abducción: no concluyente por sí sola en menores de 3 meses; el intervalo de confianza abarca el 1.0 y la sensibilidad es de apenas 13%.'
- concepto: HM:3077
  rol: apoyo
  estado_lr: medido
  sensibilidad: 0.13
  especificidad: 0.92
  poblacion: lactantes de 3 meses o menores (n = 13 096 caderas en 1 estudio)
  lr_positivo:
    valor: 1.6
    ic95:
    - 0.91
    - 2.8
    ref: pmid:38619828
  lr_negativo:
    valor: 0.95
    ic95:
    - 0.88
    - 1.0
    ref: pmid:38619828
  decision: 'Chasquido o click articular aislado: hallazgo inespecífico sin valor discriminativo para luxación o displasia (el intervalo cruza el neutro).'
autoevaluacion:
- id: q1
  pregunta: 'En Luxación de cadera en el lactante, ¿cuál es el resultado documentado del LR positivo para «Maniobras de Barlow y Ortolani positivas»? Población: lactantes de 3 meses o menores (n = 44 827 caderas en 8 estudios).'
  concepto_id: HM:3075
  referencia_id: pmid:38619828
  pmid: '38619828'
  doi: 10.1001/jama.2024.2404
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6019
    concepto_id: HM:3075
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: lactantes de 3 meses o menores (n = 44 827 caderas en 8 estudios)
    motivo: null
    decision: 'Maniobras de Barlow y Ortolani positivas: el signo que confirma la luxación inestable. Cuando es positiva eleva la probabilidad pretest de 0.94% a más del 33% (LR+ 52); su negatividad no descarta la displasia (LR- 0.55).'
    advertencia: null
  opciones:
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 52. LR positivo: 52. IC del 95 %: 21 a 127. Población: lactantes de 3 meses o menores (n = 44 827 caderas en 8 estudios). Interpretación registrada: Maniobras de Barlow y Ortolani positivas: el signo que confirma la luxación inestable. Cuando es positiva eleva la probabilidad pretest de 0.94% a más del 33% (LR+ 52); su negatividad no descarta la displasia (LR- 0.55).'
  - texto: 'LR positivo: 52.'
    correcta: true
    feedback: 'LR positivo: 52. IC del 95 %: 21 a 127. Población: lactantes de 3 meses o menores (n = 44 827 caderas en 8 estudios). Interpretación registrada: Maniobras de Barlow y Ortolani positivas: el signo que confirma la luxación inestable. Cuando es positiva eleva la probabilidad pretest de 0.94% a más del 33% (LR+ 52); su negatividad no descarta la displasia (LR- 0.55).'
  - texto: El valor 52 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 52. IC del 95 %: 21 a 127. Población: lactantes de 3 meses o menores (n = 44 827 caderas en 8 estudios). Interpretación registrada: Maniobras de Barlow y Ortolani positivas: el signo que confirma la luxación inestable. Cuando es positiva eleva la probabilidad pretest de 0.94% a más del 33% (LR+ 52); su negatividad no descarta la displasia (LR- 0.55).'
- id: q2
  pregunta: 'En Luxación de cadera en el lactante, ¿cuál es el resultado documentado del LR positivo para «Limitación de la abducción de la cadera en el lactante»? Población: lactantes de 3 meses o menores (n = 22 472 caderas en 3 estudios).'
  concepto_id: HM:3076
  referencia_id: pmid:38619828
  pmid: '38619828'
  doi: 10.1001/jama.2024.2404
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6019
    concepto_id: HM:3076
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: lactantes de 3 meses o menores (n = 22 472 caderas en 3 estudios)
    motivo: null
    decision: 'Limitación de la abducción: no concluyente por sí sola en menores de 3 meses; el intervalo de confianza abarca el 1.0 y la sensibilidad es de apenas 13%.'
    advertencia: null
  opciones:
  - texto: 'LR positivo: 3.6.'
    correcta: true
    feedback: 'LR positivo: 3.6. IC del 95 %: 0.72 a 18. Población: lactantes de 3 meses o menores (n = 22 472 caderas en 3 estudios). Interpretación registrada: Limitación de la abducción: no concluyente por sí sola en menores de 3 meses; el intervalo de confianza abarca el 1.0 y la sensibilidad es de apenas 13%.'
  - texto: El valor 3.6 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 3.6. IC del 95 %: 0.72 a 18. Población: lactantes de 3 meses o menores (n = 22 472 caderas en 3 estudios). Interpretación registrada: Limitación de la abducción: no concluyente por sí sola en menores de 3 meses; el intervalo de confianza abarca el 1.0 y la sensibilidad es de apenas 13%.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 3.6. LR positivo: 3.6. IC del 95 %: 0.72 a 18. Población: lactantes de 3 meses o menores (n = 22 472 caderas en 3 estudios). Interpretación registrada: Limitación de la abducción: no concluyente por sí sola en menores de 3 meses; el intervalo de confianza abarca el 1.0 y la sensibilidad es de apenas 13%.'
---

# Luxación de cadera en el lactante

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Dislocated hip in infants

## Sinónimos

displasia del desarrollo de la cadera

luxación congénita de cadera

displasia de cadera del lactante

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Probabilidad basal

Valor: 0.0094; Población: lactantes de 3 meses o menores cribados con examen clínico y ecografía (n = 37 859 caderas); Referencia: pmid:38619828

## Factores de riesgo

Factor: Presentación podálica al nacer

Factor: Sexo femenino

Factor: Antecedente familiar de displasia de cadera

## Hallazgos clínicos

### Maniobras de Barlow y Ortolani positivas (HM:3075)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Sensibilidad:** 0.46

**Especificidad:** 0.991

**Población:** lactantes de 3 meses o menores (n = 44 827 caderas en 8 estudios)

**LR positivo:** Valor: 52; IC del 95 %: 21 / 127; Referencia: pmid:38619828

**LR negativo:** Valor: 0.55; IC del 95 %: 0.37 / 0.82; Referencia: pmid:38619828

**Decisión:** Maniobras de Barlow y Ortolani positivas: el signo que confirma la luxación inestable. Cuando es positiva eleva la probabilidad pretest de 0.94% a más del 33% (LR+ 52); su negatividad no descarta la displasia (LR- 0.55).

### Limitación de la abducción de la cadera en el lactante (HM:3076)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**Sensibilidad:** 0.13

**Especificidad:** 0.97

**Población:** lactantes de 3 meses o menores (n = 22 472 caderas en 3 estudios)

**LR positivo:** Valor: 3.6; IC del 95 %: 0.72 / 18; Referencia: pmid:38619828

**LR negativo:** Valor: 0.91; IC del 95 %: 0.76 / 1.1; Referencia: pmid:38619828

**Decisión:** Limitación de la abducción: no concluyente por sí sola en menores de 3 meses; el intervalo de confianza abarca el 1.0 y la sensibilidad es de apenas 13%.

### Chasquido o click articular de cadera en el lactante (HM:3077)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**Sensibilidad:** 0.13

**Especificidad:** 0.92

**Población:** lactantes de 3 meses o menores (n = 13 096 caderas en 1 estudio)

**LR positivo:** Valor: 1.6; IC del 95 %: 0.91 / 2.8; Referencia: pmid:38619828

**LR negativo:** Valor: 0.95; IC del 95 %: 0.88 / 1.0; Referencia: pmid:38619828

**Decisión:** Chasquido o click articular aislado: hallazgo inespecífico sin valor discriminativo para luxación o displasia (el intervalo cruza el neutro).

## Conclusión de la fuente

En lactantes evaluados para displasia del desarrollo de la cadera, la prevalencia de luxación es de 0.94%. Las maniobras de Barlow y Ortolani positivas son el hallazgo más fuertemente asociado (LR+ 52). La abducción limitada o el chasquido aislado carecen de utilidad diagnóstica clara.

## Referencias y procedencia

**pmid:38619828:** Does This Infant Have a Dislocated Hip?: The Rational Clinical Examination Systematic Review. JAMA, 2024. DOI: 10.1001/jama.2024.2404.

Fuente clínica: medsemiotics-db, condición HM:6019.
