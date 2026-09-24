---
id: HM6030-01
slug: infarto-agudo-de-miocardio-precision-semiotica
title: 'Infarto agudo de miocardio: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-09-18'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- infarto-agudo-de-miocardio
- medicina_interna
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: fbd5cbf59e75e77b70a630f881ac1c1754e1e063
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6030-infarto-agudo-de-miocardio.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0100-signo-vital-alterado.yaml: 3e0914bff0c0dc8f1a07185d49c70c4ee7dcf11cfa7ebc3281d611f5abb4f504
    conceptos/HM0109-hipotension-arterial.yaml: 934b7dadbc768a08d34a84a322bb11c8008218f7b111b1bba2b766e67f4db7cc
    conceptos/HM0206-dolor-toracico.yaml: b0ab2dde126e6fb4d8543adeb2d5fce843a1ce51a2de62c293deda255cc1973f
    conceptos/HM0600-signo-de-exploracion.yaml: 86a2ac9babe66028eecc797ddbf4d9ea382a6fd685e9cb8df91bb959029d62bf
    conceptos/HM0608-soplo-cardiaco.yaml: 47bf7c076b53036a2d48cedd74b74aaa26ba69f1cb243c07f96afcc8a0068475
    conceptos/HM3014-dolor-irradiado-ambos-brazos.yaml: bdfcf2bc972457bb68f103779293df45277d65f38014fb053b9fe752726915f2
    conceptos/HM3130-elevacion-nueva-del-segmento-st.yaml: 1d658265c2bf4bfc1cdd21c84fcb04c7b7a759452f0391286719fc7945b097da
    conceptos/HM3131-nueva-onda-q-en-ecg.yaml: 4394118565a537b17dc696e47bdd1b7209333e71fe79432ea786c28230f2d157
    conceptos/HM3132-tercer-tono-cardiaco.yaml: 871b5b877625900180cc033eac4c47eebd458ff7f860fa2ccbf757f0d6309cb2
    conceptos/HM3133-dolor-toracico-pleuritico.yaml: 3f1683fbafaa904023e35502ef85c1178268756e609583348f81d467c6547726
    conceptos/HM3134-dolor-toracico-reproducible-a-la-palpacion.yaml: f23a1800f2d73e860ab303a1026f8e90a3aa29f340d037668ba3de3522297ef6
    conceptos/HM3135-dolor-toracico-punzante.yaml: a82cc27a26e2f5c4fdee7225832251f4bf5e1d18fce8c93ed82c0e081f7463c3
    conceptos/HM3136-dolor-toracico-posicional.yaml: 14e7c84d587048ab1b4a61d4b88c29ea6693307a7e4c1e67889e09cdd9eafec3
    condiciones/HM6030-infarto-agudo-de-miocardio.yaml: 92fcbe38a8b1f3b2bc0223fe3eb0bcf09d1641e57bbe160a23ff0941da4e9a8a
    referencias/pmid-9786377.yaml: a744bdfe061bea39eeebdfeb75c36d78c863cb9fb6a8a848d121b42024f1665f
grounding:
  condicion_id: HM:6030
  condicion_nombre: Infarto agudo de miocardio
  concepto_id: HM:3130
  concepto_nombre: Elevación nueva del segmento ST en el ECG
  estado_lr: medido
  lr_positivo: 22.0
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:9786377
  referencia_cita: Panju AA, Hemmelgarn BR, Guyatt GH, Simel DL The rational clinical examination. Is this patient having a myocardial infarction? JAMA 1998
  pmid: '9786377'
  doi: 10.1001/jama.280.14.1256
triada:
  significante: Elevación nueva del segmento ST en el ECG
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: el hallazgo electrocardiográfico individual más potente para confirmar IAM con indicación de reperfusión
evidencia:
- concepto: HM:3130
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id001
    valor: 22.0
    ic95:
    - 5.7
    - 53.9
    ref: pmid:9786377
  decision: el hallazgo electrocardiográfico individual más potente para confirmar IAM con indicación de reperfusión
- concepto: HM:3131
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id002
    valor: 11.0
    ic95:
    - 5.3
    - 24.8
    ref: pmid:9786377
  decision: signo electrocardiográfico de necrosis miocárdica transmisible
- concepto: HM:3014
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo:
    valor: 7.1
    ic95:
    - 3.5
    - 14.2
    ref: pmid:9786377
  decision: el síntoma de irradiación dolorosa con mayor rendimiento discriminativo positivo
- concepto: HM:3132
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 3.2
    ic95:
    - 1.6
    - 6.5
    ref: pmid:9786377
  decision: signo auscultatorio de disfunción ventricular izquierda aguda
- concepto: HM:0109
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 3.1
    ic95:
    - 1.6
    - 6.2
    ref: pmid:9786377
  decision: marcador hemodinámico de compromiso miocárdico o shock cardiogénico
- concepto: HM:3133
  rol: prueba_sensible
  estado_lr: medido
  lr_positivo:
    valor: 0.2
    ic95:
    - 0.1
    - 0.4
    ref: pmid:9786377
  efecto: excluye
  sostiene: discriminacion_medida
  ref: pmid:9786377
  decision: las características pleuríticas reducen fuertemente la probabilidad de IAM (LR 0.2)
- concepto: HM:3134
  rol: prueba_sensible
  estado_lr: medido
  lr_positivo:
    valor: 0.3
    ic95:
    - 0.2
    - 0.4
    ref: pmid:9786377
  efecto: excluye
  sostiene: discriminacion_medida
  ref: pmid:9786377
  decision: el dolor reproducible a la presión de la pared torácica orienta a causa osteomuscular
- concepto: HM:3135
  rol: prueba_sensible
  estado_lr: medido
  lr_positivo:
    valor: 0.3
    ic95:
    - 0.1
    - 0.6
    ref: pmid:9786377
  efecto: excluye
  sostiene: discriminacion_medida
  ref: pmid:9786377
  decision: el dolor punzante desplaza fuertemente la probabilidad en contra de IAM
- concepto: HM:3136
  rol: prueba_sensible
  estado_lr: medido
  lr_positivo:
    valor: 0.3
    ic95:
    - 0.1
    - 0.7
    ref: pmid:9786377
  efecto: excluye
  sostiene: discriminacion_medida
  ref: pmid:9786377
  decision: la modificación postural del dolor aleja la sospecha de isquemia coronaria aguda
autoevaluacion:
- id: q1
  pregunta: En Infarto agudo de miocardio, ¿cuál es el resultado documentado del LR positivo para «Elevación nueva del segmento ST en el ECG»?
  concepto_id: HM:3130
  referencia_id: pmid:9786377
  pmid: '9786377'
  doi: 10.1001/jama.280.14.1256
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6030
    concepto_id: HM:3130
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: el hallazgo electrocardiográfico individual más potente para confirmar IAM con indicación de reperfusión
    advertencia: null
  opciones:
  - texto: El valor 22.0 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 22.0. IC del 95 %: 5.7 a 53.9. Interpretación registrada: el hallazgo electrocardiográfico individual más potente para confirmar IAM con indicación de reperfusión.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 22.0. LR positivo: 22.0. IC del 95 %: 5.7 a 53.9. Interpretación registrada: el hallazgo electrocardiográfico individual más potente para confirmar IAM con indicación de reperfusión.'
  - texto: 'LR positivo: 22.0.'
    correcta: true
    feedback: 'LR positivo: 22.0. IC del 95 %: 5.7 a 53.9. Interpretación registrada: el hallazgo electrocardiográfico individual más potente para confirmar IAM con indicación de reperfusión.'
- id: q2
  pregunta: En Infarto agudo de miocardio, ¿cuál es el resultado documentado del LR positivo para «Nueva onda Q patológica en el ECG»?
  concepto_id: HM:3131
  referencia_id: pmid:9786377
  pmid: '9786377'
  doi: 10.1001/jama.280.14.1256
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6030
    concepto_id: HM:3131
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: null
    motivo: null
    decision: signo electrocardiográfico de necrosis miocárdica transmisible
    advertencia: null
  opciones:
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 11.0. LR positivo: 11.0. IC del 95 %: 5.3 a 24.8. Interpretación registrada: signo electrocardiográfico de necrosis miocárdica transmisible.'
  - texto: 'LR positivo: 11.0.'
    correcta: true
    feedback: 'LR positivo: 11.0. IC del 95 %: 5.3 a 24.8. Interpretación registrada: signo electrocardiográfico de necrosis miocárdica transmisible.'
  - texto: El valor 11.0 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 11.0. IC del 95 %: 5.3 a 24.8. Interpretación registrada: signo electrocardiográfico de necrosis miocárdica transmisible.'
---

# Infarto agudo de miocardio

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Acute myocardial infarction

## Sinónimos

IAM

ataque cardíaco

infarto de miocardio

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Hallazgos clínicos

### Elevación nueva del segmento ST en el ECG (HM:3130)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 22.0; IC del 95 %: 5.7 / 53.9; Referencia: pmid:9786377

**Decisión:** el hallazgo electrocardiográfico individual más potente para confirmar IAM con indicación de reperfusión

### Nueva onda Q patológica en el ECG (HM:3131)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 11.0; IC del 95 %: 5.3 / 24.8; Referencia: pmid:9786377

**Decisión:** signo electrocardiográfico de necrosis miocárdica transmisible

### Dolor torácico irradiado a ambos brazos (HM:3014)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 7.1; IC del 95 %: 3.5 / 14.2; Referencia: pmid:9786377

**Decisión:** el síntoma de irradiación dolorosa con mayor rendimiento discriminativo positivo

### Tercer tono cardíaco (R3) (HM:3132)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 3.2; IC del 95 %: 1.6 / 6.5; Referencia: pmid:9786377

**Decisión:** signo auscultatorio de disfunción ventricular izquierda aguda

### Hipotensión arterial (HM:0109)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 3.1; IC del 95 %: 1.6 / 6.2; Referencia: pmid:9786377

**Decisión:** marcador hemodinámico de compromiso miocárdico o shock cardiogénico

### Dolor torácico pleurítico (HM:3133)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**LR positivo:** Valor: 0.2; IC del 95 %: 0.1 / 0.4; Referencia: pmid:9786377

**Efecto:** excluye

**Sostiene:** Discriminación medida

**Referencia:** pmid:9786377

**Decisión:** las características pleuríticas reducen fuertemente la probabilidad de IAM (LR 0.2)

### Dolor torácico reproducible a la palpación (HM:3134)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**LR positivo:** Valor: 0.3; IC del 95 %: 0.2 / 0.4; Referencia: pmid:9786377

**Efecto:** excluye

**Sostiene:** Discriminación medida

**Referencia:** pmid:9786377

**Decisión:** el dolor reproducible a la presión de la pared torácica orienta a causa osteomuscular

### Dolor torácico punzante o cortante (HM:3135)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**LR positivo:** Valor: 0.3; IC del 95 %: 0.1 / 0.6; Referencia: pmid:9786377

**Efecto:** excluye

**Sostiene:** Discriminación medida

**Referencia:** pmid:9786377

**Decisión:** el dolor punzante desplaza fuertemente la probabilidad en contra de IAM

### Dolor torácico posicional (HM:3136)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**LR positivo:** Valor: 0.3; IC del 95 %: 0.1 / 0.7; Referencia: pmid:9786377

**Efecto:** excluye

**Sostiene:** Discriminación medida

**Referencia:** pmid:9786377

**Decisión:** la modificación postural del dolor aleja la sospecha de isquemia coronaria aguda

## Conclusión de la fuente

La anamnesis dirigida, la exploración física y el ECG son fundamentales para evaluar a pacientes con dolor torácico agudo. La nueva elevación del ST (LR+ 22.0) y la irradiación a ambos brazos (LR+ 7.1) confirman fuertemente el IAM, mientras que el dolor pleurítico, posicional o reproducible a la palpación lo hacen muy improbable (LR 0.2-0.3).

## Referencias y procedencia

**pmid:9786377:** The rational clinical examination. Is this patient having a myocardial infarction?. JAMA, 1998. DOI: 10.1001/jama.280.14.1256.

Fuente clínica: medsemiotics-db, condición HM:6030.
