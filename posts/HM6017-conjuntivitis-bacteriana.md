---
id: HM6017-01
slug: conjuntivitis-bacteriana-precision-semiotica
title: 'Conjuntivitis bacteriana: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-08-21'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- conjuntivitis-bacteriana
- medicina_interna
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: e654998bddbb8c2b1d22e4da2f3375f9db6bc432
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6017-conjuntivitis-bacteriana.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0600-signo-de-exploracion.yaml: 86a2ac9babe66028eecc797ddbf4d9ea382a6fd685e9cb8df91bb959029d62bf
    conceptos/HM3070-secrecion-ocular-mucopurulenta.yaml: 3bfe58e42533a195ed4c5a0364a3b97703e1146d74d2b98a0189e021bdc4a1e5
    conceptos/HM3071-otitis-media-concomitante.yaml: 0a18de104fa683c09fea5b0e07a9c02ba15220367b82e53dd95ad80fe21fa86b
    condiciones/HM6017-conjuntivitis-bacteriana.yaml: 249ba11c9a4bcd8c2d644056c2ce1178c1e4ba7fad6a298f600044bb240a6c4a
    referencias/pmid-35699701.yaml: d9348ef1222256bb8266c2fcc4df081baad7956845719fe8c927731c65599454
grounding:
  condicion_id: HM:6017
  condicion_nombre: Conjuntivitis bacteriana
  concepto_id: HM:3071
  concepto_nombre: Otitis media concomitante
  estado_lr: medido
  lr_positivo: 2.5
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:35699701
  referencia_cita: 'Johnson D, Liu D, Simel D Does This Patient With Acute Infectious Conjunctivitis Have a Bacterial Infection?: The Rational Clinical Examination Systematic Review JAMA 2022'
  pmid: '35699701'
  doi: 10.1001/jama.2022.7687
  sensibilidad: 0.24
  especificidad: 0.91
triada:
  significante: Otitis media concomitante
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: 'el síndrome otitis-conjuntivitis favorece origen bacteriano, aunque su sensibilidad es baja: su ausencia no descarta nada'
evidencia:
- concepto: HM:3070
  rol: apoyo
  estado_lr: medido
  sensibilidad: 0.76
  ic95_sensibilidad:
  - 0.6
  - 0.87
  especificidad: 0.66
  ic95_especificidad:
  - 0.58
  - 0.73
  lr_positivo: &id002
    valor: 2.1
    ic95:
    - 1.7
    - 2.6
    ref: pmid:35699701
  decision: 'el hallazgo más sensible de la revisión para causa bacteriana, pero su cociente es modesto: no basta por sí solo para decidir antibiótico'
- concepto: HM:3071
  rol: apoyo
  estado_lr: medido
  sensibilidad: 0.24
  ic95_sensibilidad:
  - 0.2
  - 0.29
  especificidad: 0.91
  ic95_especificidad:
  - 0.85
  - 0.94
  lr_positivo: &id001
    valor: 2.5
    ic95:
    - 1.5
    - 4.4
    ref: pmid:35699701
  decision: 'el síndrome otitis-conjuntivitis favorece origen bacteriano, aunque su sensibilidad es baja: su ausencia no descarta nada'
autoevaluacion:
- id: q1
  pregunta: En Conjuntivitis bacteriana, ¿cuál es el resultado documentado del LR positivo para «Otitis media concomitante»?
  concepto_id: HM:3071
  referencia_id: pmid:35699701
  pmid: '35699701'
  doi: 10.1001/jama.2022.7687
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6017
    concepto_id: HM:3071
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: 'el síndrome otitis-conjuntivitis favorece origen bacteriano, aunque su sensibilidad es baja: su ausencia no descarta nada'
    advertencia: null
  opciones:
  - texto: 'LR positivo: 2.5.'
    correcta: true
    feedback: 'LR positivo: 2.5. IC del 95 %: 1.5 a 4.4. Interpretación registrada: el síndrome otitis-conjuntivitis favorece origen bacteriano, aunque su sensibilidad es baja: su ausencia no descarta nada.'
  - texto: El valor 2.5 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 2.5. IC del 95 %: 1.5 a 4.4. Interpretación registrada: el síndrome otitis-conjuntivitis favorece origen bacteriano, aunque su sensibilidad es baja: su ausencia no descarta nada.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 2.5. LR positivo: 2.5. IC del 95 %: 1.5 a 4.4. Interpretación registrada: el síndrome otitis-conjuntivitis favorece origen bacteriano, aunque su sensibilidad es baja: su ausencia no descarta nada.'
- id: q2
  pregunta: En Conjuntivitis bacteriana, ¿cuál es el resultado documentado del LR positivo para «Secreción ocular mucopurulenta»?
  concepto_id: HM:3070
  referencia_id: pmid:35699701
  pmid: '35699701'
  doi: 10.1001/jama.2022.7687
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6017
    concepto_id: HM:3070
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: null
    motivo: null
    decision: 'el hallazgo más sensible de la revisión para causa bacteriana, pero su cociente es modesto: no basta por sí solo para decidir antibiótico'
    advertencia: null
  opciones:
  - texto: El valor 2.1 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 2.1. IC del 95 %: 1.7 a 2.6. Interpretación registrada: el hallazgo más sensible de la revisión para causa bacteriana, pero su cociente es modesto: no basta por sí solo para decidir antibiótico.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 2.1. LR positivo: 2.1. IC del 95 %: 1.7 a 2.6. Interpretación registrada: el hallazgo más sensible de la revisión para causa bacteriana, pero su cociente es modesto: no basta por sí solo para decidir antibiótico.'
  - texto: 'LR positivo: 2.1.'
    correcta: true
    feedback: 'LR positivo: 2.1. IC del 95 %: 1.7 a 2.6. Interpretación registrada: el hallazgo más sensible de la revisión para causa bacteriana, pero su cociente es modesto: no basta por sí solo para decidir antibiótico.'
---

# Conjuntivitis bacteriana

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Bacterial conjunctivitis

## Sinónimos

conjuntivitis bacteriana aguda

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Probabilidad basal

Rango documentado: 0.16 / 0.71; Población: pacientes con conjuntivitis infecciosa aguda: 16% en adultos, 71% en niños (rango de edad 1 mes-18 años); Referencia: pmid:35699701; Nota: la previa se invierte por edad, no es un rango de incertidumbre sobre un mismo valor: en niños predomina la causa bacteriana y en adultos la viral

## Hallazgos clínicos

### Secreción ocular mucopurulenta (HM:3070)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**Sensibilidad:** 0.76

**Ic95 sensibilidad:** 0.6 / 0.87

**Especificidad:** 0.66

**Ic95 especificidad:** 0.58 / 0.73

**LR positivo:** Valor: 2.1; IC del 95 %: 1.7 / 2.6; Referencia: pmid:35699701

**Decisión:** el hallazgo más sensible de la revisión para causa bacteriana, pero su cociente es modesto: no basta por sí solo para decidir antibiótico

### Otitis media concomitante (HM:3071)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**Sensibilidad:** 0.24

**Ic95 sensibilidad:** 0.2 / 0.29

**Especificidad:** 0.91

**Ic95 especificidad:** 0.85 / 0.94

**LR positivo:** Valor: 2.5; IC del 95 %: 1.5 / 4.4; Referencia: pmid:35699701

**Decisión:** el síndrome otitis-conjuntivitis favorece origen bacteriano, aunque su sensibilidad es baja: su ausencia no descarta nada

## Aspectos pendientes de documentación

La fuente mide faringitis concomitante (LR 5.4-9.9), adenopatía preauricular (LR 2.5-5.6) y contacto con otra persona con ojo rojo (LR 2.5, IC95% 1.6-3.7) como signos que apuntan a etiología VIRAL, no bacteriana. Invertir esos cocientes para leerlos «a favor de bacteriana» no es aritmética que el abstract sostenga —viral y bacteriana no son un 2x2 exhaustivo dentro de «conjuntivitis infecciosa aguda», hay más etiologías posibles— así que no se emiten en esta condición. Entrarían, con su signo correcto, en una futura condición «Conjuntivitis viral».

La prevalencia por edad (16% adultos, 71% niños) no se resume en un solo número: quien puebla `probabilidad_base` en un protocolo debe elegir según la edad del paciente, no promediar.

## Conclusión de la fuente

Ningún síntoma o signo aislado distingue con certeza la conjuntivitis bacteriana de la viral. La secreción mucopurulenta y la otitis media concomitante se asocian a causa bacteriana; la faringitis, la adenopatía preauricular y el contacto con otra persona con ojo rojo se asocian a causa viral.

## Referencias y procedencia

**pmid:35699701:** Does This Patient With Acute Infectious Conjunctivitis Have a Bacterial Infection?: The Rational Clinical Examination Systematic Review. JAMA, 2022. DOI: 10.1001/jama.2022.7687.

Fuente clínica: medsemiotics-db, condición HM:6017.
