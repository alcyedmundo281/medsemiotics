---
id: HM6033-01
slug: melanoma-cutaneo-precision-semiotica
title: 'Melanoma cutáneo: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-09-18'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- medicina_interna
- melanoma-cutaneo
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: 97f51ff1d54adf8360b0e89cf56b36eb7e633e4f
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6033-melanoma-cutaneo.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM3139-criterios-abcd-de-melanoma-positivos.yaml: 404beb1eb965a5c407754b3121d72c2245a3e1cdf9c00ca37b6425a0ec3bc256
    conceptos/HM3140-asimetria-y-bordes-irregulares-en-lesion-cutanea.yaml: 7677966496a1f369c013c20a30bf359b3577565514cf0d0fa006bf000cd5473e
    conceptos/HM3141-color-heterogeneo-y-diametro-mayor-de-6mm.yaml: 772a8f13150061fc073ec2631a3697326757a562a9dfc54d034297cb69b299b1
    condiciones/HM6033-melanoma-cutaneo.yaml: a285af88e38dca74cb4b12599312ae463176c0f72ff0839a2f4820356100b29a
    referencias/pmid-9496989.yaml: 991643f724b46ed9d4747e3fd9a92422e90ca8ea1503d55419ebcefe6bd294a5
grounding:
  condicion_id: HM:6033
  condicion_nombre: Melanoma cutáneo
  concepto_id: HM:3139
  concepto_nombre: Criterios ABCD de lesión pigmentada positivos
  estado_lr: medido
  lr_positivo: 46.0
  lr_negativo: 0.08
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:9496989
  referencia_cita: Whited JD, Grichnik JM The rational clinical examination. Does this patient have a mole or a melanoma? JAMA 1998
  pmid: '9496989'
  doi: 10.1001/jama.279.9.696
  sensibilidad: 0.92
  especificidad: 0.98
triada:
  significante: Criterios ABCD de lesión pigmentada positivos
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: la regla clínica ABCD (Asimetría, Bordes, Color, Diámetro >6mm) es altamente sensible y específica
evidencia:
- concepto: HM:3139
  rol: prueba_especifica
  estado_lr: medido
  sensibilidad: 0.92
  especificidad: 0.98
  lr_positivo: &id001
    valor: 46.0
    ic95:
    - 18.4
    - 96.0
    ref: pmid:9496989
  lr_negativo:
    valor: 0.08
    ic95:
    - 0.04
    - 0.18
    ref: pmid:9496989
  decision: la regla clínica ABCD (Asimetría, Bordes, Color, Diámetro >6mm) es altamente sensible y específica
- concepto: HM:3140
  rol: apoyo
  estado_lr: no_medido
  motivo: componente de los criterios semiológicos combinados de dermatología clínica
- concepto: HM:3141
  rol: apoyo
  estado_lr: no_medido
  motivo: componente de los criterios semiológicos combinados de dermatología clínica
autoevaluacion:
- id: q1
  pregunta: En Melanoma cutáneo, ¿cuál es el resultado documentado del LR positivo para «Criterios ABCD de lesión pigmentada positivos»?
  concepto_id: HM:3139
  referencia_id: pmid:9496989
  pmid: '9496989'
  doi: 10.1001/jama.279.9.696
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6033
    concepto_id: HM:3139
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: la regla clínica ABCD (Asimetría, Bordes, Color, Diámetro >6mm) es altamente sensible y específica
    advertencia: null
  opciones:
  - texto: El valor 46.0 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 46.0. IC del 95 %: 18.4 a 96.0. Interpretación registrada: la regla clínica ABCD (Asimetría, Bordes, Color, Diámetro >6mm) es altamente sensible y específica.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 46.0. LR positivo: 46.0. IC del 95 %: 18.4 a 96.0. Interpretación registrada: la regla clínica ABCD (Asimetría, Bordes, Color, Diámetro >6mm) es altamente sensible y específica.'
  - texto: 'LR positivo: 46.0.'
    correcta: true
    feedback: 'LR positivo: 46.0. IC del 95 %: 18.4 a 96.0. Interpretación registrada: la regla clínica ABCD (Asimetría, Bordes, Color, Diámetro >6mm) es altamente sensible y específica.'
- id: q2
  pregunta: En Melanoma cutáneo, ¿qué estado de la evidencia corresponde a «Asimetría y bordes irregulares en lesión cutánea» según la fuente?
  concepto_id: HM:3140
  referencia_id: null
  pmid: null
  doi: null
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6033
    concepto_id: HM:3140
    estado_lr: no_medido
    campo: null
    dato: null
    poblacion: null
    motivo: componente de los criterios semiológicos combinados de dermatología clínica
    decision: null
    advertencia: null
  opciones:
  - texto: Sin efecto discriminativo
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medido». LR no medido Motivo: componente de los criterios semiológicos combinados de dermatología clínica.'
  - texto: LR no medido
    correcta: true
    feedback: 'LR no medido Motivo: componente de los criterios semiológicos combinados de dermatología clínica.'
  - texto: LR no medible
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medido». LR no medido Motivo: componente de los criterios semiológicos combinados de dermatología clínica.'
---

# Melanoma cutáneo

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Cutaneous melanoma

## Sinónimos

melanoma maligno

cáncer de piel tipo melanoma

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Hallazgos clínicos

### Criterios ABCD de lesión pigmentada positivos (HM:3139)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Sensibilidad:** 0.92

**Especificidad:** 0.98

**LR positivo:** Valor: 46.0; IC del 95 %: 18.4 / 96.0; Referencia: pmid:9496989

**LR negativo:** Valor: 0.08; IC del 95 %: 0.04 / 0.18; Referencia: pmid:9496989

**Decisión:** la regla clínica ABCD (Asimetría, Bordes, Color, Diámetro >6mm) es altamente sensible y específica

### Asimetría y bordes irregulares en lesión cutánea (HM:3140)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR no medido

**Motivo:** componente de los criterios semiológicos combinados de dermatología clínica

### Color heterogéneo y diámetro mayor de 6 mm en lesión cutánea (HM:3141)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR no medido

**Motivo:** componente de los criterios semiológicos combinados de dermatología clínica

## Conclusión de la fuente

La detección precoz del melanoma mediante la regla semiológica ABCD (Asimetría, Bordes irregulares, Color heterogéneo y Diámetro >6 mm) presenta una sensibilidad del 92-100% y una especificidad del 98%, siendo la principal herramienta clínica de triaje y derivación para biopsia.

## Referencias y procedencia

**pmid:9496989:** The rational clinical examination. Does this patient have a mole or a melanoma?. JAMA, 1998. DOI: 10.1001/jama.279.9.696.

Fuente clínica: medsemiotics-db, condición HM:6033.
