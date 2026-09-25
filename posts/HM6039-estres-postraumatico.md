---
id: HM6039-01
slug: trastorno-de-estres-postraumatico-precision-semiotica
title: 'Trastorno de estrés postraumático: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-09-18'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- medicina_interna
- semiologia
- trastorno-de-estres-postraumatico
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: 9505ae00ca47576b3cd86bdec1357bc816f9cf91
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6039-estres-postraumatico.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0001-hallazgo-clinico.yaml: 5cf5cbb0a6ce5c773fd60ad80c8b467259ad4d480cd2cd60aa1335d5c8b65329
    conceptos/HM3153-trauma-screening-questionnaire-positivo.yaml: 2b723c3ecd63806c897092b32412cab381754a741c9a458452299ffe36773049
    condiciones/HM6037-sobrecarga-de-volumen.yaml: eca41c49d71742acef49b4319fc79da95905d97155a2dbaec845d342004a615f
    condiciones/HM6039-estres-postraumatico.yaml: 8cafa5f4b6857f8b3ce169444a5043a95c04f9c8328a718a17473053b037542d
    referencias/pmid-26241601.yaml: ce57c07f613a42e7c63eeb0f42dec5c35414e5e3e290c3af7250cd9b71ab55b2
grounding:
  condicion_id: HM:6039
  condicion_nombre: Trastorno de estrés postraumático
  concepto_id: HM:3153
  concepto_nombre: Trauma Screening Questionnaire positivo
  estado_lr: medido
  lr_positivo: 1.3
  lr_negativo: 0.2
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: 152 pacientes, los de la fila del Trauma Screening Questionnaire; la corrección publica además VPP 44 y VPN 89 para esa misma fila
  referencia_id: pmid:26241601
  referencia_cita: 'Spoont MR, Williams JW Jr, Kehle-Forbes S, Nieuwsma JA, Mann-Wrobel MC, Gross R Does This Patient Have Posttraumatic Stress Disorder?: Rational Clinical Examination Systematic Review JAMA 2015'
  pmid: '26241601'
  doi: 10.1001/jama.2015.7877
  sensibilidad: 0.95
  especificidad: 0.26
triada:
  significante: Trauma Screening Questionnaire positivo
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: 'solo decide cuando es NEGATIVO. Con sensibilidad del 95% y LR− 0.20, un TSQ negativo hace el trastorno bastante improbable. Un TSQ positivo no decide nada: LR+ 1.3 sobre una especificidad del 26% apenas mueve la probabilidad, así que cribar positivo obliga a la entrevista diagnóstica y no la sustituye.'
evidencia:
- concepto: HM:3153
  rol: prueba_sensible
  estado_lr: medido
  poblacion: 152 pacientes, los de la fila del Trauma Screening Questionnaire; la corrección publica además VPP 44 y VPN 89 para esa misma fila
  lr_positivo: &id001
    valor: 1.3
    ic95:
    - 1.2
    - 1.4
    ref: pmid:26241601
  lr_negativo:
    valor: 0.2
    ic95:
    - 0.1
    - 0.41
    ref: pmid:26241601
  sensibilidad: 0.95
  ic95_sensibilidad:
  - 0.9
  - 0.97
  especificidad: 0.26
  ic95_especificidad:
  - 0.22
  - 0.3
  efecto: excluye
  dispara_si: ausente
  sostiene: discriminacion_medida
  ref: pmid:26241601
  decision: 'solo decide cuando es NEGATIVO. Con sensibilidad del 95% y LR− 0.20, un TSQ negativo hace el trastorno bastante improbable. Un TSQ positivo no decide nada: LR+ 1.3 sobre una especificidad del 26% apenas mueve la probabilidad, así que cribar positivo obliga a la entrevista diagnóstica y no la sustituye.'
  advertencia: 'las cuatro cifras son las de la CORRECCIÓN (doi 10.1001/jama.2015.16955), no las del eAppendix 5 original, que la corrección declara erróneo. No se transcriben del abstract: el abstract ni siquiera nombra este instrumento.'
  nota: 'la fila corregida es coherente consigo misma, y se comprobó: Se/(1−Sp) = 0.95/0.74 = 1.28, que redondea al LR+ 1.3 publicado, y (1−Se)/Sp = 0.05/0.26 = 0.19, que redondea al LR− 0.20. Es una comprobación que se hizo, no una fuente de datos.'
autoevaluacion:
- id: q1
  pregunta: 'En Trastorno de estrés postraumático, ¿cuál es el resultado documentado del LR positivo para «Trauma Screening Questionnaire positivo»? Población: 152 pacientes, los de la fila del Trauma Screening Questionnaire; la corrección publica además VPP 44 y VPN 89 para esa misma fila.'
  concepto_id: HM:3153
  referencia_id: pmid:26241601
  pmid: '26241601'
  doi: 10.1001/jama.2015.7877
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6039
    concepto_id: HM:3153
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: 152 pacientes, los de la fila del Trauma Screening Questionnaire; la corrección publica además VPP 44 y VPN 89 para esa misma fila
    motivo: null
    decision: 'solo decide cuando es NEGATIVO. Con sensibilidad del 95% y LR− 0.20, un TSQ negativo hace el trastorno bastante improbable. Un TSQ positivo no decide nada: LR+ 1.3 sobre una especificidad del 26% apenas mueve la probabilidad, así que cribar positivo obliga a la entrevista diagnóstica y no la sustituye.'
    advertencia: 'las cuatro cifras son las de la CORRECCIÓN (doi 10.1001/jama.2015.16955), no las del eAppendix 5 original, que la corrección declara erróneo. No se transcriben del abstract: el abstract ni siquiera nombra este instrumento.'
  opciones:
  - texto: El valor 1.3 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 1.3. IC del 95 %: 1.2 a 1.4. Población: 152 pacientes, los de la fila del Trauma Screening Questionnaire; la corrección publica además VPP 44 y VPN 89 para esa misma fila. Interpretación registrada: solo decide cuando es NEGATIVO. Con sensibilidad del 95% y LR− 0.20, un TSQ negativo hace el trastorno bastante improbable. Un TSQ positivo no decide nada: LR+ 1.3 sobre una especificidad del 26% apenas mueve la probabilidad, así que cribar positivo obliga a la entrevista diagnóstica y no la sustituye. Advertencia: las cuatro cifras son las de la CORRECCIÓN (doi 10.1001/jama.2015.16955), no las del eAppendix 5 original, que la corrección declara erróneo. No se transcriben del abstract: el abstract ni siquiera nombra este instrumento.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 1.3. LR positivo: 1.3. IC del 95 %: 1.2 a 1.4. Población: 152 pacientes, los de la fila del Trauma Screening Questionnaire; la corrección publica además VPP 44 y VPN 89 para esa misma fila. Interpretación registrada: solo decide cuando es NEGATIVO. Con sensibilidad del 95% y LR− 0.20, un TSQ negativo hace el trastorno bastante improbable. Un TSQ positivo no decide nada: LR+ 1.3 sobre una especificidad del 26% apenas mueve la probabilidad, así que cribar positivo obliga a la entrevista diagnóstica y no la sustituye. Advertencia: las cuatro cifras son las de la CORRECCIÓN (doi 10.1001/jama.2015.16955), no las del eAppendix 5 original, que la corrección declara erróneo. No se transcriben del abstract: el abstract ni siquiera nombra este instrumento.'
  - texto: 'LR positivo: 1.3.'
    correcta: true
    feedback: 'LR positivo: 1.3. IC del 95 %: 1.2 a 1.4. Población: 152 pacientes, los de la fila del Trauma Screening Questionnaire; la corrección publica además VPP 44 y VPN 89 para esa misma fila. Interpretación registrada: solo decide cuando es NEGATIVO. Con sensibilidad del 95% y LR− 0.20, un TSQ negativo hace el trastorno bastante improbable. Un TSQ positivo no decide nada: LR+ 1.3 sobre una especificidad del 26% apenas mueve la probabilidad, así que cribar positivo obliga a la entrevista diagnóstica y no la sustituye. Advertencia: las cuatro cifras son las de la CORRECCIÓN (doi 10.1001/jama.2015.16955), no las del eAppendix 5 original, que la corrección declara erróneo. No se transcriben del abstract: el abstract ni siquiera nombra este instrumento.'
---

# Trastorno de estrés postraumático

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Posttraumatic stress disorder

## Sinónimos

TEPT

PTSD

estrés postraumático

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Hallazgos clínicos

### Trauma Screening Questionnaire positivo (HM:3153)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**Población:** 152 pacientes, los de la fila del Trauma Screening Questionnaire; la corrección publica además VPP 44 y VPN 89 para esa misma fila

**LR positivo:** Valor: 1.3; IC del 95 %: 1.2 / 1.4; Referencia: pmid:26241601

**LR negativo:** Valor: 0.2; IC del 95 %: 0.1 / 0.41; Referencia: pmid:26241601

**Sensibilidad:** 0.95

**Ic95 sensibilidad:** 0.9 / 0.97

**Especificidad:** 0.26

**Ic95 especificidad:** 0.22 / 0.3

**Efecto:** excluye

**Dispara si:** ausente

**Sostiene:** Discriminación medida

**Referencia:** pmid:26241601

**Decisión:** solo decide cuando es NEGATIVO. Con sensibilidad del 95% y LR− 0.20, un TSQ negativo hace el trastorno bastante improbable. Un TSQ positivo no decide nada: LR+ 1.3 sobre una especificidad del 26% apenas mueve la probabilidad, así que cribar positivo obliga a la entrevista diagnóstica y no la sustituye.

**Advertencia:** las cuatro cifras son las de la CORRECCIÓN (doi 10.1001/jama.2015.16955), no las del eAppendix 5 original, que la corrección declara erróneo. No se transcriben del abstract: el abstract ni siquiera nombra este instrumento.

**Nota:** la fila corregida es coherente consigo misma, y se comprobó: Se/(1−Sp) = 0.95/0.74 = 1.28, que redondea al LR+ 1.3 publicado, y (1−Se)/Sp = 0.05/0.26 = 0.19, que redondea al LR− 0.20. Es una comprobación que se hizo, no una fuente de datos.

## Notas de uso

ESTE COCIENTE NO SE LEE SOBRE UNA PROBABILIDAD PREVIA DE ATENCIÓN PRIMARIA. El VPP 44 y el VPN 89 que publica la corrección solo son compatibles con una prevalencia cercana al 38% en la muestra de 152 pacientes: con Se 0.95 y Sp 0.26, esa prevalencia devuelve VPP 44% y VPN 89%, las dos cifras exactas. Es aritmética de comprobación, no un dato publicado, y por eso no se guarda como probabilidad base; pero basta para advertir que aplicar el LR− 0.20 a una consulta de baja prevalencia es leerlo fuera de donde se midió.

Los dos instrumentos que la fuente recomienda —el PC-PTSD de 4 ítems y el PTSD Checklist de 17— NO ESTÁN EN EL ÍNDICE, y su ausencia no significa que rindan peor que el TSQ: significa que sus cifras están bloqueadas por la corrección. Quien lea esta condición como el rendimiento del cribado del estrés postraumático la estará leyendo mal. Es el instrumento cuyas cifras se pudieron verificar, no el mejor de los evaluados.

El punto de corte del TSQ no consta. La corrección da las cuatro cifras de la fila pero no la puntuación con la que se consideró positivo el cuestionario, y no se adivina. Ver Trauma Screening Questionnaire positivo.

## Aspectos pendientes de documentación

El abstract corregido del artículo (doi 10.1001/jama.2015.7877) desbloquea el PC-PTSD y el PTSD Checklist. El que sirve PubMed sigue siendo el anterior a la corrección —muestra los dos bloques contradictorios—, así que hace falta la página del editor con acceso propio, como en sobrecarga de volumen.

El punto de corte del Trauma Screening Questionnaire vive en el eAppendix 5. Con él, Trauma Screening Questionnaire positivo puede declarar su umbral.

## Conclusión de la fuente

Dos instrumentos de cribado, el PC-PTSD y el PTSD Checklist, muestran características de rendimiento razonables para su uso en consultas de atención primaria o en entornos comunitarios con poblaciones de alto riesgo. Ambos son fáciles de administrar e interpretar y pueden incorporarse sin dificultad a una práctica clínica con poco tiempo.

## Referencias y procedencia

**pmid:26241601:** Does This Patient Have Posttraumatic Stress Disorder?: Rational Clinical Examination Systematic Review. JAMA, 2015. DOI: 10.1001/jama.2015.7877.

Fuente clínica: medsemiotics-db, condición HM:6039.
