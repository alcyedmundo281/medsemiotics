---
id: HM6041-01
slug: absceso-de-partes-blandas-precision-semiotica
title: 'Absceso de partes blandas: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-09-18'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- absceso-de-partes-blandas
- medicina_interna
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: 1db38dcd49a911196aa7c2f30bd8ad0e6cb17c54
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6041-absceso-de-partes-blandas.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM3166-coleccion-de-partes-blandas-en-ecografia.yaml: 84f9731d01658e9e254d134f515c73948778b9c351fccbb28061c8c1596c36a0
    condiciones/HM6041-absceso-de-partes-blandas.yaml: b010eca416816aed8aad0e869d0ec455efa93540297ede7a86f1ed23935848b0
    referencias/pmid-28073795.yaml: 34414d3cb382d8a6153cdfc6ee51cbf0d018320cb102c03782c4258cb9d81619
    referencias/pmid-32081383.yaml: 93b9a9c75593bb9ba0d20983c254ee2fa36c6a94de4a04cf21c72497d85d4a68
    referencias/pmid-34379709.yaml: fc71b08758d1230b66485b83ce555b363f89b0661faac03a7ea2bc7b051c7235
grounding:
  condicion_id: HM:6041
  condicion_nombre: Absceso de partes blandas
  concepto_id: HM:3166
  concepto_nombre: Colección de partes blandas en ecografía
  estado_lr: medido
  lr_positivo: 10.9
  lr_negativo: 0.01
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: adultos en urgencias con infección de piel y partes blandas, sospecha de absceso o celulitis; subgrupo de adultos de un metaanálisis de 14 estudios prospectivos (2 656 pacientes en total)
  referencia_id: pmid:32081383
  referencia_cita: 'Gottlieb M, Avila J, Chottiner M, Peksa GD Point-of-Care Ultrasonography for the Diagnosis of Skin and Soft Tissue Abscesses: A Systematic Review and Meta-analysis Ann Emerg Med 2020'
  pmid: '32081383'
  doi: 10.1016/j.annemergmed.2020.01.004
  sensibilidad: 0.987
  especificidad: 0.91
triada:
  significante: 'Colección de bordes irregulares dentro del tejido blando, anecoica o con ecos internos en suspensión, con refuerzo acústico posterior, que deforma sus bordes al comprimir con la sonda y cuyo contenido se arremolina. Alrededor, la celulitis da el patrón en empedrado: tabiques hipoecoicos entre lobulillos de grasa.'
  significado: 'Pus colectado: un espacio ocupado por material líquido y detritos que no se resuelve con antibiótico solo. El refuerzo posterior aparece porque el contenido atenúa menos que el tejido vecino: ese artefacto es la prueba de que hay líquido, no tejido.'
  decision: 'colección confirmada: drena o deriva para drenaje. Sin colección, solo empedrado: antibiótico y control, no incisión a ciegas. Y antes de cortar, Doppler color: un seudoaneurisma o un vaso pueden verse como una colección'
evidencia:
- concepto: HM:3166
  rol: imagen
  estado_lr: medido
  poblacion: adultos en urgencias con infección de piel y partes blandas, sospecha de absceso o celulitis; subgrupo de adultos de un metaanálisis de 14 estudios prospectivos (2 656 pacientes en total)
  ref: pmid:32081383
  sensibilidad: 0.987
  ic95_sensibilidad:
  - 0.953
  - 0.998
  especificidad: 0.91
  ic95_especificidad:
  - 0.844
  - 0.954
  lr_positivo: &id001
    valor: 10.9
    ic95:
    - 6.2
    - 19.2
    ref: pmid:32081383
  lr_negativo:
    valor: 0.01
    ic95:
    - 0.001
    - 0.06
    ref: pmid:32081383
  decision: 'colección confirmada: drena o deriva para drenaje. Sin colección, solo empedrado: antibiótico y control, no incisión a ciegas. Y antes de cortar, Doppler color: un seudoaneurisma o un vaso pueden verse como una colección'
  advertencia: estos cocientes son del subgrupo de ADULTOS y no se trasladan al niño. El mismo metaanálisis da en pediatría cocientes peores, que no entran todavía porque esperan la comprobación de Marin 2013
autoevaluacion:
- id: q1
  pregunta: 'En Absceso de partes blandas, ¿cuál es el resultado documentado del LR positivo para «Colección de partes blandas en ecografía»? Población: adultos en urgencias con infección de piel y partes blandas, sospecha de absceso o celulitis; subgrupo de adultos de un metaanálisis de 14 estudios prospectivos (2 656 pacientes en total).'
  concepto_id: HM:3166
  referencia_id: pmid:32081383
  pmid: '32081383'
  doi: 10.1016/j.annemergmed.2020.01.004
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6041
    concepto_id: HM:3166
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: adultos en urgencias con infección de piel y partes blandas, sospecha de absceso o celulitis; subgrupo de adultos de un metaanálisis de 14 estudios prospectivos (2 656 pacientes en total)
    motivo: null
    decision: 'colección confirmada: drena o deriva para drenaje. Sin colección, solo empedrado: antibiótico y control, no incisión a ciegas. Y antes de cortar, Doppler color: un seudoaneurisma o un vaso pueden verse como una colección'
    advertencia: estos cocientes son del subgrupo de ADULTOS y no se trasladan al niño. El mismo metaanálisis da en pediatría cocientes peores, que no entran todavía porque esperan la comprobación de Marin 2013
  opciones:
  - texto: 'LR positivo: 10.9.'
    correcta: true
    feedback: 'LR positivo: 10.9. IC del 95 %: 6.2 a 19.2. Población: adultos en urgencias con infección de piel y partes blandas, sospecha de absceso o celulitis; subgrupo de adultos de un metaanálisis de 14 estudios prospectivos (2 656 pacientes en total). Interpretación registrada: colección confirmada: drena o deriva para drenaje. Sin colección, solo empedrado: antibiótico y control, no incisión a ciegas. Y antes de cortar, Doppler color: un seudoaneurisma o un vaso pueden verse como una colección. Advertencia: estos cocientes son del subgrupo de ADULTOS y no se trasladan al niño. El mismo metaanálisis da en pediatría cocientes peores, que no entran todavía porque esperan la comprobación de Marin 2013.'
  - texto: El valor 10.9 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 10.9. IC del 95 %: 6.2 a 19.2. Población: adultos en urgencias con infección de piel y partes blandas, sospecha de absceso o celulitis; subgrupo de adultos de un metaanálisis de 14 estudios prospectivos (2 656 pacientes en total). Interpretación registrada: colección confirmada: drena o deriva para drenaje. Sin colección, solo empedrado: antibiótico y control, no incisión a ciegas. Y antes de cortar, Doppler color: un seudoaneurisma o un vaso pueden verse como una colección. Advertencia: estos cocientes son del subgrupo de ADULTOS y no se trasladan al niño. El mismo metaanálisis da en pediatría cocientes peores, que no entran todavía porque esperan la comprobación de Marin 2013.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 10.9. LR positivo: 10.9. IC del 95 %: 6.2 a 19.2. Población: adultos en urgencias con infección de piel y partes blandas, sospecha de absceso o celulitis; subgrupo de adultos de un metaanálisis de 14 estudios prospectivos (2 656 pacientes en total). Interpretación registrada: colección confirmada: drena o deriva para drenaje. Sin colección, solo empedrado: antibiótico y control, no incisión a ciegas. Y antes de cortar, Doppler color: un seudoaneurisma o un vaso pueden verse como una colección. Advertencia: estos cocientes son del subgrupo de ADULTOS y no se trasladan al niño. El mismo metaanálisis da en pediatría cocientes peores, que no entran todavía porque esperan la comprobación de Marin 2013.'
---

# Absceso de partes blandas

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Skin and soft tissue abscess

## Sinónimos

absceso cutáneo

absceso de piel y partes blandas

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Hallazgos clínicos

### Colección de partes blandas en ecografía (HM:3166)

**Significante:** Colección de bordes irregulares dentro del tejido blando, anecoica o con ecos internos en suspensión, con refuerzo acústico posterior, que deforma sus bordes al comprimir con la sonda y cuyo contenido se arremolina. Alrededor, la celulitis da el patrón en empedrado: tabiques hipoecoicos entre lobulillos de grasa.

**Significado:** Pus colectado: un espacio ocupado por material líquido y detritos que no se resuelve con antibiótico solo. El refuerzo posterior aparece porque el contenido atenúa menos que el tejido vecino: ese artefacto es la prueba de que hay líquido, no tejido.

**Falsos positivos:** Ganglio linfático reactivo: ovalado, con hilio ecogénico central y vascularización hiliar al Doppler / Quiste epidérmico o sebáceo no infectado: bordes definidos, sin hiperemia perilesional / Vaso, seudoaneurisma o malformación vascular: el Doppler color los separa en un segundo, y aquí el error se paga caro / Hematoma o seroma: colección sin infección; el contexto y la clínica los distinguen, la imagen sola no / Celulitis con edema marcado que crea espacios hipoecoicos entre lobulillos, sin pus colectada / Bursitis o derrame articular vecino tomado por colección de partes blandas / Absceso muy ecogénico o con gas: puede verse casi isoecoico al tejido y pasar por celulitis; es un falso negativo, no un falso positivo / Colección profunda fuera del alcance de la sonda lineal: un absceso que no se ve no es un absceso ausente

**Rol:** Imagen

**Estado del LR:** LR medido

**Población:** adultos en urgencias con infección de piel y partes blandas, sospecha de absceso o celulitis; subgrupo de adultos de un metaanálisis de 14 estudios prospectivos (2 656 pacientes en total)

**Referencia:** pmid:32081383

**Sensibilidad:** 0.987

**Ic95 sensibilidad:** 0.953 / 0.998

**Especificidad:** 0.91

**Ic95 especificidad:** 0.844 / 0.954

**LR positivo:** Valor: 10.9; IC del 95 %: 6.2 / 19.2; Referencia: pmid:32081383

**LR negativo:** Valor: 0.01; IC del 95 %: 0.001 / 0.06; Referencia: pmid:32081383

**Decisión:** colección confirmada: drena o deriva para drenaje. Sin colección, solo empedrado: antibiótico y control, no incisión a ciegas. Y antes de cortar, Doppler color: un seudoaneurisma o un vaso pueden verse como una colección

**Advertencia:** estos cocientes son del subgrupo de ADULTOS y no se trasladan al niño. El mismo metaanálisis da en pediatría cocientes peores, que no entran todavía porque esperan la comprobación de Marin 2013

## Aspectos pendientes de documentación

EL GLOBAL Y TRES SUBGRUPOS ESPERAN LA COMPROBACIÓN DE MARIN 2013. El abstract de pmid:32081383 da: global Se 94.6% (IC95% 89.4-97.4), Sp 85.4% (78.9-90.2), LR+ 6.5 (4.4-9.6), LR− 0.06 (0.03-0.13); sospecha clínica alta LR+ 8.6 (4.1-18.1), LR− 0.07 (0.05-0.12); casos clínicamente dudosos LR+ 4.0 (2.5-6.3), LR− 0.11 (0.03-0.32); pediatría Se 89.9% (81.8-94.6), Sp 79.9% (71.5-86.3), LR+ 4.5 (3.1-6.4), LR− 0.13 (0.07-0.23). Cualquiera de ellos puede incluir a Marin 2013 (Acad Emerg Med 2013;20:545-53), el estudio pediátrico de 755 pacientes que barbic2017 extrajo mal y que en su agrupación fue el más influyente (distancia de Cook > 1). Para desbloquear hace falta la tabla de estudios incluidos de Gottlieb: si trae a Marin, su fila debe coincidir con el recuento corregido de la errata de barbic2017 (VP 193, FP 37, FN 27, VN 95).

LOS DOS COCIENTES DE barbic2017 (pmid:28073795) SIGUEN BLOQUEADOS. Su corrección cambia la sensibilidad y la especificidad agrupadas, pero no recalcula el LR+ 5.63 ni el LR− 0.05 del abstract. No entran aquí, y la referencia no se cita en ninguna arista.

## Notas de uso

LAS CIFRAS CORREGIDAS DE barbic2017 NO SON COCIENTES. Tras su errata, 8 estudios dan sensibilidad 95.5% (IC95% 88.9-98.3) y especificidad 80.3% (56.4-92.7), frente a los 96.2% y 82.9% originales. Se anotan como rendimiento de la prueba; convertirlas en un LR sería calcular un cociente que la fuente corregida no publica.

EL PEDIÁTRICO DE wu2022 (pmid:34379709) NO ES UNA SEGUNDA CONFIRMACIÓN. Sus cifras agrupadas en 7 estudios y 870 niños —LR+ 4.5 (IC95% 3.1-6.4), LR− 0.13 (0.07-0.23)— son idénticas, intervalos incluidos, al subgrupo pediátrico de Gottlieb 2020. Dos metaanálisis que coinciden hasta el segundo decimal comparten casi con seguridad sus estudios, incluido probablemente Marin, así que la comprobación pendiente les afecta a los dos. Wu mide además la exploración física en 4 estudios: Se 0.84 (IC95% 0.80-0.88), Sp 0.69 (0.62-0.76).

## Conclusión de la fuente

El POCUS tiene buena exactitud diagnóstica para distinguir absceso de celulitis y llevó a un cambio correcto de manejo en el 10% de los casos.

## Referencias y procedencia

**pmid:28073795:** In patients presenting to the emergency department with skin and soft tissue infections what is the diagnostic accuracy of point-of-care ultrasonography for the diagnosis of abscess compared to the current standard of care? A systematic review and meta-analysis. BMJ Open, 2017. DOI: 10.1136/bmjopen-2016-013688.

**pmid:32081383:** Point-of-Care Ultrasonography for the Diagnosis of Skin and Soft Tissue Abscesses: A Systematic Review and Meta-analysis. Ann Emerg Med, 2020. DOI: 10.1016/j.annemergmed.2020.01.004.

**pmid:34379709:** Role of point-of-care ultrasound (POCUS) in the diagnosis of an abscess in paediatric skin and soft tissue infections: a systematic review and meta-analysis. Med Ultrason, 2022. DOI: 10.11152/mu-3166.

Fuente clínica: medsemiotics-db, condición HM:6041.
