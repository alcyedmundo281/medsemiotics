---
id: HM6028-01
slug: alergia-a-penicilina-precision-semiotica
title: 'Alergia a penicilina: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-09-18'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- alergia-a-penicilina
- medicina_interna
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: 1db38dcd49a911196aa7c2f30bd8ad0e6cb17c54
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6028-alergia-a-penicilina.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM3125-antecedente-referido-de-alergia-a-penicilina.yaml: cde9b548831034bf68455dc22a3b5d1ccdc309998f3ab33be1a6220f3923619d
    conceptos/HM3126-prueba-cutanea-positiva-a-penicilina.yaml: 70e9fbd90708978f3c252aac45fbcb47cabfb1a9fb6986047e63924be88b00da
    condiciones/HM6028-alergia-a-penicilina.yaml: 7f2fb7617504f48dc51d288c54f0d8b19b4b37733e2572e6cd47c711e57d0a3e
    referencias/pmid-11368703.yaml: 37596dbc27a0ff3259412f5a0df332d992662f586e45fd89eee19f63d25124de
grounding:
  condicion_id: HM:6028
  condicion_nombre: Alergia a penicilina
  concepto_id: HM:3125
  concepto_nombre: Antecedente referido de alergia a penicilina
  estado_lr: medido
  lr_positivo: 1.9
  lr_negativo: 0.5
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:11368703
  referencia_cita: Salkind AR, Cuddy PG, Foxworth JW The rational clinical examination. Is this patient allergic to penicillin? An evidence-based analysis of the likelihood of penicillin allergy JAMA 2001
  pmid: '11368703'
  doi: 10.1001/jama.285.19.2498
triada:
  significante: Antecedente referido de alergia a penicilina
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: el autorreporte de alergia tiene muy baja exactitud discriminativa (LR+ 1.9); solo un 10-20% son verdaderos alérgicos
evidencia:
- concepto: HM:3126
  rol: prueba_especifica
  estado_lr: no_medible
  motivo: es el estándar de referencia (gold standard) contra el que se calculan los cocientes de la historia clínica
  decision: el patrón de referencia para hipersensibilidad mediada por IgE; la negatividad descarta anafilaxia con seguridad casi absoluta
- concepto: HM:3125
  rol: apoyo
  estado_lr: medido
  lr_positivo: &id001
    valor: 1.9
    ic95:
    - 1.5
    - 2.5
    ref: pmid:11368703
  lr_negativo:
    valor: 0.5
    ic95:
    - 0.4
    - 0.6
    ref: pmid:11368703
  decision: el autorreporte de alergia tiene muy baja exactitud discriminativa (LR+ 1.9); solo un 10-20% son verdaderos alérgicos
autoevaluacion:
- id: q1
  pregunta: En Alergia a penicilina, ¿cuál es el resultado documentado del LR positivo para «Antecedente referido de alergia a penicilina»?
  concepto_id: HM:3125
  referencia_id: pmid:11368703
  pmid: '11368703'
  doi: 10.1001/jama.285.19.2498
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6028
    concepto_id: HM:3125
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: el autorreporte de alergia tiene muy baja exactitud discriminativa (LR+ 1.9); solo un 10-20% son verdaderos alérgicos
    advertencia: null
  opciones:
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 1.9. LR positivo: 1.9. IC del 95 %: 1.5 a 2.5. Interpretación registrada: el autorreporte de alergia tiene muy baja exactitud discriminativa (LR+ 1.9); solo un 10-20% son verdaderos alérgicos.'
  - texto: 'LR positivo: 1.9.'
    correcta: true
    feedback: 'LR positivo: 1.9. IC del 95 %: 1.5 a 2.5. Interpretación registrada: el autorreporte de alergia tiene muy baja exactitud discriminativa (LR+ 1.9); solo un 10-20% son verdaderos alérgicos.'
  - texto: El valor 1.9 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 1.9. IC del 95 %: 1.5 a 2.5. Interpretación registrada: el autorreporte de alergia tiene muy baja exactitud discriminativa (LR+ 1.9); solo un 10-20% son verdaderos alérgicos.'
- id: q2
  pregunta: En Alergia a penicilina, ¿qué estado de la evidencia corresponde a «Prueba cutánea a determinantes de penicilina» según la fuente?
  concepto_id: HM:3126
  referencia_id: null
  pmid: null
  doi: null
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6028
    concepto_id: HM:3126
    estado_lr: no_medible
    campo: null
    dato: null
    poblacion: null
    motivo: es el estándar de referencia (gold standard) contra el que se calculan los cocientes de la historia clínica
    decision: el patrón de referencia para hipersensibilidad mediada por IgE; la negatividad descarta anafilaxia con seguridad casi absoluta
    advertencia: null
  opciones:
  - texto: LR no medible
    correcta: true
    feedback: 'LR no medible Motivo: es el estándar de referencia (gold standard) contra el que se calculan los cocientes de la historia clínica. Interpretación registrada: el patrón de referencia para hipersensibilidad mediada por IgE; la negatividad descarta anafilaxia con seguridad casi absoluta.'
  - texto: LR no medido
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medible». LR no medible Motivo: es el estándar de referencia (gold standard) contra el que se calculan los cocientes de la historia clínica. Interpretación registrada: el patrón de referencia para hipersensibilidad mediada por IgE; la negatividad descarta anafilaxia con seguridad casi absoluta.'
  - texto: Sin efecto discriminativo
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medible». LR no medible Motivo: es el estándar de referencia (gold standard) contra el que se calculan los cocientes de la historia clínica. Interpretación registrada: el patrón de referencia para hipersensibilidad mediada por IgE; la negatividad descarta anafilaxia con seguridad casi absoluta.'
---

# Alergia a penicilina

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Penicillin allergy

## Sinónimos

hipersensibilidad a penicilina mediada por IgE

reacción alérgica a betalactámicos

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Probabilidad basal

Valor: 0.15; IC del 95 %: 0.1 / 0.2; Población: pacientes que autorreportan antecedentes de alergia a penicilina confirmados por pruebas cutáneas; Referencia: pmid:11368703

## Hallazgos clínicos

### Prueba cutánea a determinantes de penicilina (HM:3126)

**Rol:** Prueba específica

**Estado del LR:** LR no medible

**Motivo:** es el estándar de referencia (gold standard) contra el que se calculan los cocientes de la historia clínica

**Decisión:** el patrón de referencia para hipersensibilidad mediada por IgE; la negatividad descarta anafilaxia con seguridad casi absoluta

### Antecedente referido de alergia a penicilina (HM:3125)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 1.9; IC del 95 %: 1.5 / 2.5; Referencia: pmid:11368703

**LR negativo:** Valor: 0.5; IC del 95 %: 0.4 / 0.6; Referencia: pmid:11368703

**Decisión:** el autorreporte de alergia tiene muy baja exactitud discriminativa (LR+ 1.9); solo un 10-20% son verdaderos alérgicos

## Conclusión de la fuente

Solo el 10% al 20% de los pacientes que refieren antecedentes de alergia a la penicilina son verdaderamente alérgicos al evaluarse mediante pruebas cutáneas. La historia clínica referida desplaza poco la probabilidad (LR+ 1.9), mientras que una prueba cutánea negativa descarta con seguridad secuelas graves.

## Referencias y procedencia

**pmid:11368703:** The rational clinical examination. Is this patient allergic to penicillin? An evidence-based analysis of the likelihood of penicillin allergy. JAMA, 2001. DOI: 10.1001/jama.285.19.2498.

Fuente clínica: medsemiotics-db, condición HM:6028.
