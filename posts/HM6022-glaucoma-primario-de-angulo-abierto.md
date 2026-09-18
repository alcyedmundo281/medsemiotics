---
id: HM6022-01
slug: glaucoma-primario-de-angulo-abierto-precision-semiotica
title: 'Glaucoma primario de ángulo abierto: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-09-18'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- glaucoma-primario-de-angulo-abierto
- medicina_interna
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: 1db38dcd49a911196aa7c2f30bd8ad0e6cb17c54
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6022-glaucoma-primario-de-angulo-abierto.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM3088-relacion-copa-disco-aumentada.yaml: 5bb0259e0f6fd3ae574ed32378ed9e99111c1627ecc93deb1f28220860ed68e0
    conceptos/HM3089-asimetria-de-la-relacion-copa-disco.yaml: 2ede5f860716039873d028cb9f8f2b7c7addacdf28bc1931a8781c38e207c5d7
    conceptos/HM3090-hemorragia-en-astilla-del-disco-optico.yaml: 583ac968bd35113ff71f83184e2bdad70ffbe293038bb642c73d316fbf7d9dee
    conceptos/HM3091-presion-intraocular-elevada.yaml: c39c8d51b0c74ccf320b8c3fa0fdc2f995f8a67cc438c560d662a90094c2c8ab
    condiciones/HM6022-glaucoma-primario-de-angulo-abierto.yaml: f7b6eaf74a3a00933ad3281f9ac22b2028dab49180533926ab33a3aa1ba17467
    referencias/pmid-23677315.yaml: d2303bc8eb2ac4ce32a6238ef16bdce5d8b07ca52d1a7842da5ee848fd9f787a
grounding:
  condicion_id: HM:6022
  condicion_nombre: Glaucoma primario de ángulo abierto
  concepto_id: HM:3088
  concepto_nombre: Relación copa-disco aumentada
  estado_lr: medido
  lr_positivo: 14.0
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:23677315
  referencia_cita: Hollands H, Johnson D, Hollands S, Simel DL, Jinapriya D, Sharma S Do findings on routine examination identify patients at risk for primary open-angle glaucoma? The rational clinical examination systematic review JAMA 2013
  pmid: '23677315'
  doi: 10.1001/jama.2013.5099
triada:
  significante: Relación copa-disco aumentada
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: el hallazgo oftalmoscópico aislado más potente para confirmar sospecha de glaucoma
evidencia:
- concepto: HM:3088
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id001
    valor: 14.0
    ic95:
    - 6.3
    - 30.0
    ref: pmid:23677315
  decision: el hallazgo oftalmoscópico aislado más potente para confirmar sospecha de glaucoma
- concepto: HM:3089
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id002
    valor: 7.3
    ic95:
    - 3.4
    - 16.0
    ref: pmid:23677315
  decision: la diferencia de excavación entre ambos ojos aumenta marcadamente la probabilidad
- concepto: HM:3090
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo:
    valor: 12.0
    ic95:
    - 2.9
    - 48.0
    ref: pmid:23677315
  decision: signo patognomónico de daño microvascular y progresión activa de la neuropatía glaucomatosa
- concepto: HM:3091
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 13.0
    ic95:
    - 8.2
    - 21.0
    ref: pmid:23677315
  lr_negativo:
    valor: 0.65
    ic95:
    - 0.55
    - 0.76
    ref: pmid:23677315
  decision: confirma con fuerza pero una PIO normal no descarta (glaucoma de tensión normal)
autoevaluacion:
- id: q1
  pregunta: En Glaucoma primario de ángulo abierto, ¿cuál es el resultado documentado del LR positivo para «Relación copa-disco aumentada»?
  concepto_id: HM:3088
  referencia_id: pmid:23677315
  pmid: '23677315'
  doi: 10.1001/jama.2013.5099
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6022
    concepto_id: HM:3088
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: el hallazgo oftalmoscópico aislado más potente para confirmar sospecha de glaucoma
    advertencia: null
  opciones:
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 14.0. LR positivo: 14.0. IC del 95 %: 6.3 a 30.0. Interpretación registrada: el hallazgo oftalmoscópico aislado más potente para confirmar sospecha de glaucoma.'
  - texto: 'LR positivo: 14.0.'
    correcta: true
    feedback: 'LR positivo: 14.0. IC del 95 %: 6.3 a 30.0. Interpretación registrada: el hallazgo oftalmoscópico aislado más potente para confirmar sospecha de glaucoma.'
  - texto: El valor 14.0 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 14.0. IC del 95 %: 6.3 a 30.0. Interpretación registrada: el hallazgo oftalmoscópico aislado más potente para confirmar sospecha de glaucoma.'
- id: q2
  pregunta: En Glaucoma primario de ángulo abierto, ¿cuál es el resultado documentado del LR positivo para «Asimetría de la relación copa-disco»?
  concepto_id: HM:3089
  referencia_id: pmid:23677315
  pmid: '23677315'
  doi: 10.1001/jama.2013.5099
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6022
    concepto_id: HM:3089
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: null
    motivo: null
    decision: la diferencia de excavación entre ambos ojos aumenta marcadamente la probabilidad
    advertencia: null
  opciones:
  - texto: 'LR positivo: 7.3.'
    correcta: true
    feedback: 'LR positivo: 7.3. IC del 95 %: 3.4 a 16.0. Interpretación registrada: la diferencia de excavación entre ambos ojos aumenta marcadamente la probabilidad.'
  - texto: El valor 7.3 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 7.3. IC del 95 %: 3.4 a 16.0. Interpretación registrada: la diferencia de excavación entre ambos ojos aumenta marcadamente la probabilidad.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 7.3. LR positivo: 7.3. IC del 95 %: 3.4 a 16.0. Interpretación registrada: la diferencia de excavación entre ambos ojos aumenta marcadamente la probabilidad.'
---

# Glaucoma primario de ángulo abierto

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Primary open-angle glaucoma

## Sinónimos

GPAA

glaucoma crónico simple

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Probabilidad basal

Valor: 0.02; IC del 95 %: 0.01 / 0.03; Población: adultos mayores de 40 años en cribado poblacional; Referencia: pmid:23677315

## Hallazgos clínicos

### Relación copa-disco aumentada (HM:3088)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 14.0; IC del 95 %: 6.3 / 30.0; Referencia: pmid:23677315

**Decisión:** el hallazgo oftalmoscópico aislado más potente para confirmar sospecha de glaucoma

### Asimetría de la relación copa-disco (HM:3089)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 7.3; IC del 95 %: 3.4 / 16.0; Referencia: pmid:23677315

**Decisión:** la diferencia de excavación entre ambos ojos aumenta marcadamente la probabilidad

### Hemorragia en astilla del disco óptico (HM:3090)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 12.0; IC del 95 %: 2.9 / 48.0; Referencia: pmid:23677315

**Decisión:** signo patognomónico de daño microvascular y progresión activa de la neuropatía glaucomatosa

### Presión intraocular elevada (HM:3091)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 13.0; IC del 95 %: 8.2 / 21.0; Referencia: pmid:23677315

**LR negativo:** Valor: 0.65; IC del 95 %: 0.55 / 0.76; Referencia: pmid:23677315

**Decisión:** confirma con fuerza pero una PIO normal no descarta (glaucoma de tensión normal)

## Conclusión de la fuente

La evaluación del disco óptico (relación copa-disco >= 0.7, asimetría y hemorragias en astilla) es más informativa que la tonometría aislada para el diagnóstico de glaucoma.

## Referencias y procedencia

**pmid:23677315:** Do findings on routine examination identify patients at risk for primary open-angle glaucoma? The rational clinical examination systematic review. JAMA, 2013. DOI: 10.1001/jama.2013.5099.

Fuente clínica: medsemiotics-db, condición HM:6022.
