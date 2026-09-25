---
id: HM6048-01
slug: bocio-inspeccion-palpacion-precision
title: 'Bocio: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-09-21'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- bocio
- medicina_interna
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: 9505ae00ca47576b3cd86bdec1357bc816f9cf91
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6048-bocio.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0600-signo-de-exploracion.yaml: 86a2ac9babe66028eecc797ddbf4d9ea382a6fd685e9cb8df91bb959029d62bf
    conceptos/HM3187-agrandamiento-tiroideo-palpable-en-posicion-neutra.yaml: 1d793434c05ab2831964fc1d1f654b97e7d3e2996836348af6071f283928d41a
    conceptos/HM3188-lobulo-tiroideo-mayor-que-falange-distal.yaml: 599c45292d1527aa32bc82a0cbbc70ee66839078b4760da97143be6d5e596773
    condiciones/HM6048-bocio.yaml: 2c4123fde69dc3715157657e067345e9c99cd25d3ddb88cc687380b17bc6af65
    referencias/pmid-16235152.yaml: 8441106cf5ae24c229b62b6ad50fed3c8eaf1cccd1c74b47161db7ee24c9366f
    referencias/pmid-21893493.yaml: 0762e0c6ff44a424aac80b4deb12f696850bdbe52cb5e894737569672b5f8d1f
    referencias/pmid-7861577.yaml: 0632453a74ec44556429ab0cc29797121a1498a85c42e5b9464c630c101343e5
    referencias/pmid-8320430.yaml: 1ccc4de90821e8ea3d3fbec6d265de5b8efaa3f2dd4a330e489e927e173a9e93
grounding:
  condicion_id: HM:6048
  condicion_nombre: Bocio
  concepto_id: HM:3187
  concepto_nombre: Agrandamiento tiroideo palpable en posición neutra
  estado_lr: medido
  lr_positivo: 26.3
  lr_negativo: 0.4
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: adultos evaluados mediante inspección y palpación con el cuello en posición neutra frente a ecografía tiroidea como estándar de referencia
  referencia_id: pmid:7861577
  referencia_cita: Siminoski K The rational clinical examination. Does this patient have a goiter? JAMA 1995
  pmid: '7861577'
  doi: null
triada:
  significante: Tiroides visible o palpable con el cuello en posición neutra o relajada (sin hiperextensión forzada), que asciende con los movimientos de deglución al palpar los lóbulos laterales o el istmo tiroideo.
  significado: Aumento patológico del volumen o masa de la glándula tiroides (bocio o tiromegalia) por encima de los límites fisiológicos del adulto.
  decision: un tiroides netamente visible o palpable con el cuello en posición neutra confirma bocio con muy alta probabilidad clínica (LR+ 26.3)
evidencia:
- concepto: HM:3187
  rol: prueba_especifica
  estado_lr: medido
  poblacion: adultos evaluados mediante inspección y palpación con el cuello en posición neutra frente a ecografía tiroidea como estándar de referencia
  ref: pmid:7861577
  lr_positivo: &id001
    valor: 26.3
    ref: pmid:7861577
  lr_negativo:
    valor: 0.4
    ref: pmid:7861577
  decision: un tiroides netamente visible o palpable con el cuello en posición neutra confirma bocio con muy alta probabilidad clínica (LR+ 26.3)
  advertencia: la ausencia de bocio evidente en posición neutra no descarta bocio leve o de localización intratorácica/retroesternal (LR- 0.40)
- concepto: HM:3188
  rol: prueba_sensible
  estado_lr: medido
  poblacion: niños en edad escolar evaluados según el criterio de falange distal del pulgar de la OMS frente a ecografía tiroidea
  ref: pmid:7861577
  lr_positivo: &id002
    valor: 3.0
    ic95:
    - 2.5
    - 3.5
    ref: pmid:7861577
  lr_negativo:
    valor: 0.3
    ic95:
    - 0.24
    - 0.37
    ref: pmid:7861577
  decision: en cribado pediátrico, un lóbulo que supera la falange distal del pulgar triplica la probabilidad de bocio confirmado por ultrasonido
- concepto: HM:3188
  rol: prueba_sensible
  estado_lr: medido
  poblacion: mujeres gestantes evaluadas según el criterio de falange distal del pulgar de la OMS frente a ecografía tiroidea
  ref: pmid:7861577
  lr_positivo:
    valor: 4.7
    ic95:
    - 3.6
    - 6.0
    ref: pmid:7861577
  lr_negativo:
    valor: 0.08
    ic95:
    - 0.02
    - 0.27
    ref: pmid:7861577
  decision: en gestantes, la ausencia de lóbulos tiroideos que superen la falange distal descarta bocio con excelente fiabilidad (LR- 0.08)
autoevaluacion:
- id: q1
  pregunta: 'En Bocio, ¿cuál es el resultado documentado del LR positivo para «Agrandamiento tiroideo palpable en posición neutra»? Población: adultos evaluados mediante inspección y palpación con el cuello en posición neutra frente a ecografía tiroidea como estándar de referencia.'
  concepto_id: HM:3187
  referencia_id: pmid:7861577
  pmid: '7861577'
  doi: null
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6048
    concepto_id: HM:3187
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: adultos evaluados mediante inspección y palpación con el cuello en posición neutra frente a ecografía tiroidea como estándar de referencia
    motivo: null
    decision: un tiroides netamente visible o palpable con el cuello en posición neutra confirma bocio con muy alta probabilidad clínica (LR+ 26.3)
    advertencia: la ausencia de bocio evidente en posición neutra no descarta bocio leve o de localización intratorácica/retroesternal (LR- 0.40)
  opciones:
  - texto: El valor 26.3 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 26.3. Población: adultos evaluados mediante inspección y palpación con el cuello en posición neutra frente a ecografía tiroidea como estándar de referencia. Interpretación registrada: un tiroides netamente visible o palpable con el cuello en posición neutra confirma bocio con muy alta probabilidad clínica (LR+ 26.3). Advertencia: la ausencia de bocio evidente en posición neutra no descarta bocio leve o de localización intratorácica/retroesternal (LR- 0.40).'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 26.3. LR positivo: 26.3. Población: adultos evaluados mediante inspección y palpación con el cuello en posición neutra frente a ecografía tiroidea como estándar de referencia. Interpretación registrada: un tiroides netamente visible o palpable con el cuello en posición neutra confirma bocio con muy alta probabilidad clínica (LR+ 26.3). Advertencia: la ausencia de bocio evidente en posición neutra no descarta bocio leve o de localización intratorácica/retroesternal (LR- 0.40).'
  - texto: 'LR positivo: 26.3.'
    correcta: true
    feedback: 'LR positivo: 26.3. Población: adultos evaluados mediante inspección y palpación con el cuello en posición neutra frente a ecografía tiroidea como estándar de referencia. Interpretación registrada: un tiroides netamente visible o palpable con el cuello en posición neutra confirma bocio con muy alta probabilidad clínica (LR+ 26.3). Advertencia: la ausencia de bocio evidente en posición neutra no descarta bocio leve o de localización intratorácica/retroesternal (LR- 0.40).'
- id: q2
  pregunta: 'En Bocio, ¿cuál es el resultado documentado del LR positivo para «Lóbulo tiroideo palpable mayor que la falange distal del pulgar»? Población: niños en edad escolar evaluados según el criterio de falange distal del pulgar de la OMS frente a ecografía tiroidea.'
  concepto_id: HM:3188
  referencia_id: pmid:7861577
  pmid: '7861577'
  doi: null
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6048
    concepto_id: HM:3188
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: niños en edad escolar evaluados según el criterio de falange distal del pulgar de la OMS frente a ecografía tiroidea
    motivo: null
    decision: en cribado pediátrico, un lóbulo que supera la falange distal del pulgar triplica la probabilidad de bocio confirmado por ultrasonido
    advertencia: null
  opciones:
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 3.0. LR positivo: 3.0. IC del 95 %: 2.5 a 3.5. Población: niños en edad escolar evaluados según el criterio de falange distal del pulgar de la OMS frente a ecografía tiroidea. Interpretación registrada: en cribado pediátrico, un lóbulo que supera la falange distal del pulgar triplica la probabilidad de bocio confirmado por ultrasonido.'
  - texto: 'LR positivo: 3.0.'
    correcta: true
    feedback: 'LR positivo: 3.0. IC del 95 %: 2.5 a 3.5. Población: niños en edad escolar evaluados según el criterio de falange distal del pulgar de la OMS frente a ecografía tiroidea. Interpretación registrada: en cribado pediátrico, un lóbulo que supera la falange distal del pulgar triplica la probabilidad de bocio confirmado por ultrasonido.'
  - texto: El valor 3.0 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 3.0. IC del 95 %: 2.5 a 3.5. Población: niños en edad escolar evaluados según el criterio de falange distal del pulgar de la OMS frente a ecografía tiroidea. Interpretación registrada: en cribado pediátrico, un lóbulo que supera la falange distal del pulgar triplica la probabilidad de bocio confirmado por ultrasonido.'
---

# Bocio

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Goiter

## Sinónimos

tiromegalia

agrandamiento tiroideo

hipertrofia de la glándula tiroides

bocio tiroideo

## Códigos

Snomed: 3716002; Cie10: E04.9

## Factores de riesgo

Factor: Gestación o periodo puerperal; Referencia: pmid:8320430; Nota: en Bruselas, con aporte de yodo en el límite bajo, cerca del 10% de las gestantes tenía bocio en el parto, solo en parte reversible en el posparto. Sin grupo de no gestantes, así que es un riesgo absoluto en una zona con poco yodo

Factor: Edad avanzada; Referencia: pmid:16235152; Nota: asociación independiente con el bocio ecográfico en varones y en mujeres; el resumen no da su OR. SHIP, 3915 adultos de 20 a 79 años de una región antes deficiente en yodo

Factor: Tabaquismo actual; Referencia: pmid:16235152; Nota: asociación independiente y, según la fuente, fuerte en varones y en mujeres; el resumen no da su OR. SHIP, 3915 adultos

## Hallazgos clínicos

### Agrandamiento tiroideo palpable en posición neutra (HM:3187)

**Significante:** Tiroides visible o palpable con el cuello en posición neutra o relajada (sin hiperextensión forzada), que asciende con los movimientos de deglución al palpar los lóbulos laterales o el istmo tiroideo.

**Significado:** Aumento patológico del volumen o masa de la glándula tiroides (bocio o tiromegalia) por encima de los límites fisiológicos del adulto.

**Falsos positivos:** Cuello marcadamente delgado con cartílago tiroides o cricoides prominente / Quiste del conducto tirogloso o adenopatía de la cadena cervical anterior / Tejido adiposo pretraqueal o lipoma cervical

**Rol:** Prueba específica

**Estado del LR:** LR medido

**Población:** adultos evaluados mediante inspección y palpación con el cuello en posición neutra frente a ecografía tiroidea como estándar de referencia

**Referencia:** pmid:7861577

**LR positivo:** Valor: 26.3; Referencia: pmid:7861577

**LR negativo:** Valor: 0.4; Referencia: pmid:7861577

**Decisión:** un tiroides netamente visible o palpable con el cuello en posición neutra confirma bocio con muy alta probabilidad clínica (LR+ 26.3)

**Advertencia:** la ausencia de bocio evidente en posición neutra no descarta bocio leve o de localización intratorácica/retroesternal (LR- 0.40)

### Lóbulo tiroideo palpable mayor que la falange distal del pulgar (HM:3188)

**Significante:** A la palpación tiroidea bimanual o anterior, el volumen estimado de cada uno de los lóbulos laterales de la glándula tiroides supera el volumen de la falange distal del dedo pulgar de la persona examinada.

**Significado:** Criterio semiológico estandarizado por la Organización Mundial de la Salud (OMS) para la graduación táctil y cribado de bocio endémico o tiromegalia en niños y gestantes.

**Falsos positivos:** Variabilidad en la técnica de palpación entre exploradores noveles / Cuello corto o bocio de implantación retroesternal / Variaciones fisiológicas individuales en la morfología de la falange distal

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**Población:** niños en edad escolar evaluados según el criterio de falange distal del pulgar de la OMS frente a ecografía tiroidea

**Referencia:** pmid:7861577

**LR positivo:** Valor: 3.0; IC del 95 %: 2.5 / 3.5; Referencia: pmid:7861577

**LR negativo:** Valor: 0.3; IC del 95 %: 0.24 / 0.37; Referencia: pmid:7861577

**Decisión:** en cribado pediátrico, un lóbulo que supera la falange distal del pulgar triplica la probabilidad de bocio confirmado por ultrasonido

### Lóbulo tiroideo palpable mayor que la falange distal del pulgar (HM:3188)

**Significante:** A la palpación tiroidea bimanual o anterior, el volumen estimado de cada uno de los lóbulos laterales de la glándula tiroides supera el volumen de la falange distal del dedo pulgar de la persona examinada.

**Significado:** Criterio semiológico estandarizado por la Organización Mundial de la Salud (OMS) para la graduación táctil y cribado de bocio endémico o tiromegalia en niños y gestantes.

**Falsos positivos:** Variabilidad en la técnica de palpación entre exploradores noveles / Cuello corto o bocio de implantación retroesternal / Variaciones fisiológicas individuales en la morfología de la falange distal

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**Población:** mujeres gestantes evaluadas según el criterio de falange distal del pulgar de la OMS frente a ecografía tiroidea

**Referencia:** pmid:7861577

**LR positivo:** Valor: 4.7; IC del 95 %: 3.6 / 6.0; Referencia: pmid:7861577

**LR negativo:** Valor: 0.08; IC del 95 %: 0.02 / 0.27; Referencia: pmid:7861577

**Decisión:** en gestantes, la ausencia de lóbulos tiroideos que superen la falange distal descarta bocio con excelente fiabilidad (LR- 0.08)

## Aspectos pendientes de documentación

Factor retirado por ser causa y no factor con grupo control: deficiencia crónica de yodo en la dieta. Vanderpump 2011 (pmid:21893493) la da como la causa más frecuente de enfermedad tiroidea en el mundo, que lleva al bocio, sin medida de riesgo. Si se registra, será como causa.

Factores retirados: sexo femenino y antecedentes familiares de patología tiroidea o autoinmune. Búsqueda en PubMed del 2026-09-24. Consulta «(goiter[Title] OR goitre[Title] OR thyroid nodules[Title]) AND (prevalence[Title] OR risk factors[Title]) AND (population-based OR Study of Health in Pomerania OR ultrasound survey) AND (women OR female sex)»: 27 resultados, cribados por título los 10 primeros. Völzke 2005 (pmid:16235152; SHIP, 3915 adultos de una región antes deficiente en yodo) analiza por separado a varones y mujeres, y solo halla la edad avanzada y el tabaquismo actual como factores independientes en ambos sexos, que entran como factores; el resumen no da sus OR. Ninguna fuente cuantifica el sexo ni el antecedente familiar para el bocio.

## Referencias y procedencia

**pmid:16235152:** Risk factors for goiter in a previously iodine-deficient region. Exp Clin Endocrinol Diabetes, 2005. DOI: 10.1055/s-2005-865741.

**pmid:21893493:** The epidemiology of thyroid disease. Br Med Bull, 2011. DOI: 10.1093/bmb/ldr030.

**pmid:7861577:** The rational clinical examination. Does this patient have a goiter?. JAMA, 1995. DOI: no documentado.

**pmid:8320430:** Maternal thyroid function in pregnancy. J Endocrinol Invest, 1993. DOI: 10.1007/BF03348861.

Fuente clínica: medsemiotics-db, condición HM:6048.
