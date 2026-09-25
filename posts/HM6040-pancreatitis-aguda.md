---
id: HM6040-01
slug: pancreatitis-aguda-precision-semiotica
title: 'Pancreatitis aguda: hallazgos y evidencia clínica'
subtitle: Hallazgos y criterios clínicos sin cocientes de verosimilitud medidos.
date: '2026-09-18'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- medicina_interna
- pancreatitis-aguda
- semiologia
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: 9505ae00ca47576b3cd86bdec1357bc816f9cf91
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6040-pancreatitis-aguda.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0201-dolor-abdominal.yaml: adbaa4992613e08871e7e4d6259066ab9da4d9696dd256e274007f5965dd7813
    conceptos/HM0202-dolor-epigastrico.yaml: 284406d6397caf6b3b25e539e0237ddf1d424b846f97b94cbb2ff75b2c1ef99a
    conceptos/HM0205-dolor-abdominal-en-cinturon.yaml: 0f13e881a8d29bac46d58b3c6664e9414fd2ba135075822528317bf09e1fb47b
    conceptos/HM0300-sintoma-digestivo.yaml: 2c9dfe41462c5927070d1020039bd0dac823bcf998d53ac0a7d8e04ccab240aa
    conceptos/HM0302-vomitos.yaml: c2a3e83028a5dbb8b5d22771c6f413648cbe087e1f3dffa381f416e6bc5a12c9
    conceptos/HM0600-signo-de-exploracion.yaml: 86a2ac9babe66028eecc797ddbf4d9ea382a6fd685e9cb8df91bb959029d62bf
    conceptos/HM0601-irritacion-peritoneal.yaml: 05237c0ae13ba1c349514b2e63ecc620a13a04defc2b7219c2e9c0313ac9eb21
    conceptos/HM0611-signo-de-cullen.yaml: 62e0a5988b00f41af3b6ed75aa0592dc4a79051730d1a35351c642294a0064ac
    conceptos/HM0730-alteracion-enzimatica.yaml: eaace3c0ef5fc70eda08396c77e4b145c690302347b2c6dca54ffe7c2ceb5298
    conceptos/HM0731-hiperamilasemia.yaml: 1b410460c87df8c6666cb99675252d225a10ef6f58bd871a82229c183236ef74
    conceptos/HM0732-hiperlipasemia.yaml: b12f57b2eeca3e2cd72c9d2d39a02f46b456322b5845692f3abfe329c027f275
    conceptos/HM0900-hallazgo-de-imagen.yaml: 0b40c9368c746533cc335071c04e027c4465fb29158ed2cc747d65b9bb573e67
    conceptos/HM0901-hallazgos-de-imagen-compatibles-con-pancreatitis.yaml: 556099a1a0c2481e4eb806459f1ba00a07749282e3e74ce4efeb6a92d009e23a
    condiciones/HM6040-pancreatitis-aguda.yaml: 94b5db0ea8c4f0d499e3eaf47866b480c8385aabda8242d591bde27b29636dad
    referencias/pmid-23100216.yaml: 43d6b498ae28cb9451014d13d219e7caa00ea9fc8107af092b8c171438a26abd
    referencias/pmid-25088919.yaml: b0be6e2c04299a8adea4085e3e6b28f10849d8bd0118e734da36efa36e1bef81
    referencias/pmid-26844279.yaml: 6c58e2666a253432e0cfa871160a02df14cacdcfc95e2f1425a8c29071db45b9
    referencias/pmid-27820614.yaml: 0d9f1a12fd2c091c5b8dceb4b30aa62f209df443d05df3417253626d2660b596
grounding:
  condicion_id: HM:6040
  condicion_nombre: Pancreatitis aguda
  concepto_id: HM:0732
  concepto_nombre: Hiperlipasemia
  estado_lr: no_medido
  lr_positivo: null
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:23100216
  referencia_cita: 'Banks PA, Bollen TL, Dervenis C, Gooszen HG, Johnson CD, Sarr MG, Tsiotos GG, Vege SS Classification of acute pancreatitis--2012: revision of the Atlanta classification and definitions by international consensus Gut 2013'
  pmid: '23100216'
  doi: 10.1136/gutjnl-2012-302779
triada:
  significante: Hiperlipasemia
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: 'es el criterio de referencia de laboratorio y el que holonmed considera más discriminante, por encima de la amilasa: se eleva más tiempo y es más específica del páncreas'
evidencia:
- concepto: HM:0732
  rol: prueba_especifica
  estado_lr: no_medido
  decision: 'es el criterio de referencia de laboratorio y el que holonmed considera más discriminante, por encima de la amilasa: se eleva más tiempo y es más específica del páncreas'
  nota: el corte que usa el protocolo es más de tres veces el límite alto, que es también el que exige Atlanta. El cociente que holonmed le asigna no entra por falta de procedencia; ver «Fuera de alcance».
- concepto: HM:0731
  rol: prueba_especifica
  estado_lr: no_medido
  decision: 'el mismo papel que la lipasa pero menos específica: se eleva también en patología salival y en otras causas, y se normaliza antes'
  advertencia: no se confunde con la lipasa ni se sustituye por ella. Son enzimas distintas con especificidad distinta, y el propio protocolo de holonmed bloquea el emparejamiento.
- concepto: HM:0202
  rol: manifestacion
  estado_lr: no_medido
  decision: fija la sospecha de partida. Sensible y poco específico, así que lo que holonmed aprovecha de él es sobre todo su ausencia
- concepto: HM:0302
  rol: apoyo
  estado_lr: no_medido
  decision: aporta poca certeza por sí solo
- concepto: HM:0601
  rol: apoyo
  estado_lr: no_medido
  decision: signo de Blumberg; apoya, no decide
- concepto: HM:0611
  rol: apoyo
  estado_lr: no_medido
  decision: 'raro pero llamativo: orienta a pancreatitis necrotizante o hemorrágica'
  advertencia: su AUSENCIA no descarta nada, y por eso el protocolo de holonmed no le declara cociente negativo. Es infrecuente incluso dentro de la enfermedad.
- concepto: HM:0901
  rol: imagen
  estado_lr: no_medido
  decision: es el tercero de los tres criterios de Atlanta, y el que permite diagnosticar cuando las enzimas no llegan al corte
  nota: la referencia es la tomografía con contraste; la ecografía sirve sobre todo para buscar la causa biliar, no para confirmar la pancreatitis
autoevaluacion:
- id: q1
  pregunta: En Pancreatitis aguda, ¿qué estado de la evidencia corresponde a «Hiperlipasemia» según la fuente?
  concepto_id: HM:0732
  referencia_id: null
  pmid: null
  doi: null
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6040
    concepto_id: HM:0732
    estado_lr: no_medido
    campo: null
    dato: null
    poblacion: null
    motivo: null
    decision: 'es el criterio de referencia de laboratorio y el que holonmed considera más discriminante, por encima de la amilasa: se eleva más tiempo y es más específica del páncreas'
    advertencia: null
  opciones:
  - texto: Sin efecto discriminativo
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medido». LR no medido Interpretación registrada: es el criterio de referencia de laboratorio y el que holonmed considera más discriminante, por encima de la amilasa: se eleva más tiempo y es más específica del páncreas.'
  - texto: LR no medido
    correcta: true
    feedback: 'LR no medido Interpretación registrada: es el criterio de referencia de laboratorio y el que holonmed considera más discriminante, por encima de la amilasa: se eleva más tiempo y es más específica del páncreas.'
  - texto: LR no medible
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medido». LR no medido Interpretación registrada: es el criterio de referencia de laboratorio y el que holonmed considera más discriminante, por encima de la amilasa: se eleva más tiempo y es más específica del páncreas.'
- id: q2
  pregunta: En Pancreatitis aguda, ¿qué estado de la evidencia corresponde a «Hiperamilasemia» según la fuente?
  concepto_id: HM:0731
  referencia_id: null
  pmid: null
  doi: null
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6040
    concepto_id: HM:0731
    estado_lr: no_medido
    campo: null
    dato: null
    poblacion: null
    motivo: null
    decision: 'el mismo papel que la lipasa pero menos específica: se eleva también en patología salival y en otras causas, y se normaliza antes'
    advertencia: no se confunde con la lipasa ni se sustituye por ella. Son enzimas distintas con especificidad distinta, y el propio protocolo de holonmed bloquea el emparejamiento.
  opciones:
  - texto: LR no medido
    correcta: true
    feedback: 'LR no medido Interpretación registrada: el mismo papel que la lipasa pero menos específica: se eleva también en patología salival y en otras causas, y se normaliza antes. Advertencia: no se confunde con la lipasa ni se sustituye por ella. Son enzimas distintas con especificidad distinta, y el propio protocolo de holonmed bloquea el emparejamiento.'
  - texto: LR no medible
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medido». LR no medido Interpretación registrada: el mismo papel que la lipasa pero menos específica: se eleva también en patología salival y en otras causas, y se normaliza antes. Advertencia: no se confunde con la lipasa ni se sustituye por ella. Son enzimas distintas con especificidad distinta, y el propio protocolo de holonmed bloquea el emparejamiento.'
  - texto: Sin efecto discriminativo
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medido». LR no medido Interpretación registrada: el mismo papel que la lipasa pero menos específica: se eleva también en patología salival y en otras causas, y se normaliza antes. Advertencia: no se confunde con la lipasa ni se sustituye por ella. Son enzimas distintas con especificidad distinta, y el propio protocolo de holonmed bloquea el emparejamiento.'
---

# Pancreatitis aguda

Hallazgos y criterios clínicos sin cocientes de verosimilitud medidos.

## Nombre en inglés

Acute pancreatitis

## Sinónimos

inflamación aguda del páncreas

## Códigos

Snomed: 197456007; Cie10: No documentado.

## Factores de riesgo

Factor: Consumo de alcohol por encima de 40 g/día; Referencia: pmid:26844279; Nota: relación dosis-respuesta monótona en varones y no lineal en mujeres. Por debajo de 40 g/día no aumenta el riesgo frente a la abstención: RR 1.1 (IC95% 0.69-1.74) en varones y 0.76 (IC95% 0.60-0.97) en mujeres; por encima, el riesgo crece. El resumen no da el RR de pancreatitis aguda a dosis altas. Metaanálisis de 7 estudios con 157 026 participantes

Factor: Hipertrigliceridemia; Referencia: pmid:27820614; Nota: triglicéridos no en ayunas de 5 mmol/L o más frente a menos de 1 mmol/L, HR 8.7 (IC95% 3.7-20.0) ajustado; ya de 2.00 a 2.99 mmol/L, HR 2.3 (IC95% 1.3-4.0). HR 1.17 (IC95% 1.10-1.24) por cada 1 mmol/L. Dos cohortes de Copenhague con 116 550 personas y 434 casos

Factor: Colangiopancreatografía retrógrada endoscópica previa; Referencia: pmid:25088919; Nota: incidencia de pancreatitis tras la CPRE del 9.7% y del 14.7% en pacientes de alto riesgo, en los brazos placebo o sin prótesis de 108 ensayos (13 296 pacientes). La fuente no tiene grupo sin CPRE, así que es un riesgo absoluto, no un cociente

## Hallazgos clínicos

### Hiperlipasemia (HM:0732)

**Rol:** Prueba específica

**Estado del LR:** LR no medido

**Decisión:** es el criterio de referencia de laboratorio y el que holonmed considera más discriminante, por encima de la amilasa: se eleva más tiempo y es más específica del páncreas

**Nota:** el corte que usa el protocolo es más de tres veces el límite alto, que es también el que exige Atlanta. El cociente que holonmed le asigna no entra por falta de procedencia; ver «Fuera de alcance».

### Hiperamilasemia (HM:0731)

**Rol:** Prueba específica

**Estado del LR:** LR no medido

**Decisión:** el mismo papel que la lipasa pero menos específica: se eleva también en patología salival y en otras causas, y se normaliza antes

**Advertencia:** no se confunde con la lipasa ni se sustituye por ella. Son enzimas distintas con especificidad distinta, y el propio protocolo de holonmed bloquea el emparejamiento.

### Dolor epigástrico (HM:0202)

**Rol:** Manifestación

**Estado del LR:** LR no medido

**Decisión:** fija la sospecha de partida. Sensible y poco específico, así que lo que holonmed aprovecha de él es sobre todo su ausencia

### Vómitos (HM:0302)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR no medido

**Decisión:** aporta poca certeza por sí solo

### Irritación peritoneal (HM:0601)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR no medido

**Decisión:** signo de Blumberg; apoya, no decide

### Signo de Cullen (HM:0611)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR no medido

**Decisión:** raro pero llamativo: orienta a pancreatitis necrotizante o hemorrágica

**Advertencia:** su AUSENCIA no descarta nada, y por eso el protocolo de holonmed no le declara cociente negativo. Es infrecuente incluso dentro de la enfermedad.

### Hallazgos de imagen compatibles con pancreatitis (HM:0901)

**Rol:** Imagen

**Estado del LR:** LR no medido

**Decisión:** es el tercero de los tres criterios de Atlanta, y el que permite diagnosticar cuando las enzimas no llegan al corte

**Nota:** la referencia es la tomografía con contraste; la ecografía sirve sobre todo para buscar la causa biliar, no para confirmar la pancreatitis

## Notas de uso

LOS CRITERIOS DE ATLANTA NO ESTÁN AQUÍ COMO REGLA, solo descritos abajo en prosa, y la razón es el propio validador. Una `regla` exige `ref`, su única fuente posible es Atlanta 2012 (pmid:23100216), y esa referencia entró en el índice con la errata sin comprobar porque la red desde la que se importó no alcanzaba PubMed. build.py falla si una referencia así sostiene un dato, y una regla de clasificación es un dato. Se añade sola en cuanto alguien corra `scripts/9_desbloquear_referencias.py` desde una red que sí lo alcance.

NINGUNA DE LAS SIETE ARISTAS TRAE COCIENTE, y no es un descuido de la migración: es que el protocolo de origen no declara procedencia para ninguno. Quien lea esta condición esperando cifras con las que mover una probabilidad no las va a encontrar aquí todavía, y ésa es la respuesta honesta hasta que aparezcan las fuentes.

Lo único cuantificado que entra es la regla de Atlanta, que no es un cociente sino un criterio de clasificación: dice cuándo el diagnóstico está hecho, no cuánto se mueve la probabilidad con cada hallazgo.

## Aspectos pendientes de documentación

Factor retirado: litiasis biliar, incluida la coledocolitiasis. Es la causa más frecuente de pancreatitis aguda, pero no hay fuente con grupo control que la cuantifique como factor. Búsqueda en PubMed del 2026-09-24. Consulta «(gallstone disease OR gallstones OR cholelithiasis) AND (acute pancreatitis) AND (hazard ratio OR relative risk OR odds ratio) AND (population-based cohort OR prospective cohort OR UK Biobank OR Mendelian randomization)»: 125 resultados, cribados por título los 15 primeros. Ninguno da el riesgo de pancreatitis en portadores de litiasis frente a no portadores. Si se registra, será como causa, con la fuente que dé su frecuencia.

LOS COCIENTES QUE HOLONMED USA Y AQUÍ NO ENTRAN, para que quien busque la fuente sepa qué busca: hiperlipasemia LR+ 26.6 y LR− 0.1; hiperamilasemia LR+ 12.5 y LR− 0.3; dolor epigástrico LR+ 2.1 y LR− 0.2; vómitos LR+ 1.6; irritación peritoneal LR+ 2.2; signo de Cullen LR+ 8.0; hallazgos de imagen LR+ 9.0. Se anotan aquí y NO en las aristas justamente para que no se lean como dato del índice.

EL ORIGEN DE LOS SIETE YA NO ES UNA INCÓGNITA: GetTheDiagnosis.org, confirmado por el autor del protocolo el 16/09/2026. Lo que falta no es averiguar de dónde salieron, sino llegar al artículo que cada uno resume. GetTheDiagnosis cita sus fuentes por estudio, así que la vía es abrir la ficha de pancreatitis de ese sitio y recuperar el PMID de cada cociente.

Dos atajos que NO valen, y conviene dejarlos escritos para no repetirlos: la serie Rational Clinical Examination no tiene artículo de pancreatitis —comprobado contra PubMed—, y los metaanálisis de pancreatitis POST-CPRE miden otra cosa, con cocientes que rondan 8 y 6 en vez de 26.6 y 12.5.

LA REGLA DE ATLANTA, que es lo único cuantificado y bien citado de todo el protocolo. Está escrita y comprobada; solo espera a que se coteje la errata de pmid:23100216. Sus componentes son dolor abdominal en cinturón y dolor epigástrico (dolor), hiperamilasemia y hiperlipasemia (enzimas) y hallazgos de imagen compatibles con pancreatitis (imagen), con el criterio de dos de tres.

Los cuatro factores de riesgo entran sin `ref`. La asociación es conocida, pero este índice guarda hechos con procedencia y todavía no la tienen.

## Conclusión de la fuente

El diagnóstico de pancreatitis aguda se establece con dos de tres criterios: dolor abdominal característico, elevación de las enzimas pancreáticas por encima de tres veces el límite alto de la normalidad, o hallazgos de imagen compatibles.

## Referencias y procedencia

**pmid:23100216:** Classification of acute pancreatitis--2012: revision of the Atlanta classification and definitions by international consensus. Gut, 2013. DOI: 10.1136/gutjnl-2012-302779.

**pmid:25088919:** Incidence, severity, and mortality of post-ERCP pancreatitis: a systematic review by using randomized, controlled trials. Gastrointest Endosc, 2015. DOI: 10.1016/j.gie.2014.06.045.

**pmid:26844279:** Alcohol Consumption as a Risk Factor for Acute and Chronic Pancreatitis: A Systematic Review and a Series of Meta-analyses. EBioMedicine, 2015. DOI: 10.1016/j.ebiom.2015.11.023.

**pmid:27820614:** Nonfasting Mild-to-Moderate Hypertriglyceridemia and Risk of Acute Pancreatitis. JAMA Intern Med, 2016. DOI: 10.1001/jamainternmed.2016.6875.

Fuente clínica: medsemiotics-db, condición HM:6040.
