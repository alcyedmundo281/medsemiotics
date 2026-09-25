---
id: HM6002-01
slug: sindrome-de-intestino-irritable-precision-semiotica
title: 'Síndrome de intestino irritable: hallazgos y evidencia clínica'
subtitle: Hallazgos y criterios clínicos sin cocientes de verosimilitud medidos.
date: '2026-09-02'
author: Dr. Alcy Torres
category: gastroenterologia
category_label: Gastroenterología
tags:
- gastroenterologia
- semiologia
- sindrome-de-intestino-irritable
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: 9505ae00ca47576b3cd86bdec1357bc816f9cf91
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6002-sindrome-intestino-irritable.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0100-signo-vital-alterado.yaml: 3e0914bff0c0dc8f1a07185d49c70c4ee7dcf11cfa7ebc3281d611f5abb4f504
    conceptos/HM0101-fiebre.yaml: d8367b5824cbb321094893d8dde57e082205ace1ba21a89144af01209279e45e
    conceptos/HM0200-dolor.yaml: 583f1c01f2eeeed369469010e4b7d24d73d883bc3ef40266f80eaa0db0089463
    conceptos/HM0201-dolor-abdominal.yaml: adbaa4992613e08871e7e4d6259066ab9da4d9696dd256e274007f5965dd7813
    conceptos/HM0300-sintoma-digestivo.yaml: 2c9dfe41462c5927070d1020039bd0dac823bcf998d53ac0a7d8e04ccab240aa
    conceptos/HM0303-diarrea.yaml: 2ef61a3793ffed62c719a7e065bbe91d9031917a2806facb2c7ec00a89900625
    conceptos/HM0304-estrenimiento.yaml: a8374e94963cab8e9be684044d7ab151fac96f60ecf163ecd056738eac5ebcb8
    conceptos/HM0310-melena.yaml: 56ea476133e21be467cd68f7bb9a8a9b3f9a7623d63fbf3e4e37810fe2d87081
    conceptos/HM0710-alteracion-hematologica.yaml: 8779ebf74773e0648f4a534cb7c6528ec05cfc16c33123eb06d539cc1aa0e3ad
    conceptos/HM0711-anemia.yaml: c338972f0322d30f8cc652238e28f0d141409666b6d0f1bf27bc2e7b532c24d5
    conceptos/HM0800-sintoma-general.yaml: 39761069b5de091733e7864bb0c96f68755b6d3fa5e59003f5f8c7949b0c4827
    conceptos/HM0803-perdida-de-peso.yaml: 78cd9514f8137e60f123c191cb3939fa57bc11c77dcda85c914e82e8eac1d22e
    conceptos/HM3060-hematoquecia.yaml: 3859f875c15207194d1bc498152f293a810c21faeb51c3ae1ce78ba459cbd338
    condiciones/HM6002-sindrome-intestino-irritable.yaml: 361961cdc2583861c1d77bb2ee3c1557c2ebfb096681ba3d806ee565145f69db
    referencias/pmid-15082584.yaml: bed79febe6875717f56dda071ab3d22da080c14d2f6552a0c7803e9eb9dc4a27
    referencias/pmid-18441863.yaml: d9f899b7a68ba1799bfaae19fadfcc97108841be6db29c7632e00ce769237478
    referencias/pmid-18854541.yaml: 346d1ed8a98252e1510532df3d42fe94cc4f1f615405c73ae66d6f1103365c3c
    referencias/pmid-20697190.yaml: 5acfa5ff915443623dc06031e8065400f6ab0f27d72e95e35e365d825b88b3ad
    referencias/pmid-22426087.yaml: c87b06190f964b235168dbd5ca0ac3c084d4c23daee34d716735dd5cfd1fb271
    referencias/pmid-23055768.yaml: 6ff183a65d1b0bb695846f2ae115ec0e7c0b18ca72b18f8cf6eb2ae158f926ec
    referencias/pmid-26076071.yaml: a61301d02454279af8cff7bb3563a08720b970345e5cf0c0366ffedf07c2364f
    referencias/pmid-27144627.yaml: 8fee779f41d1a67e9a989383a7d43687d62c6d28617e004730efe3b075dafadf
    referencias/pmid-28069350.yaml: d714a89eb710f87b3d1a5bd391780c6800b7dee436021a91d9a3609d3e85587d
    referencias/pmid-9299672.yaml: 54cb78bb9753e2087083d3becc6b105739fa364217c5a12c140c127f50a3a94d
grounding:
  condicion_id: HM:6002
  condicion_nombre: Síndrome de intestino irritable
  concepto_id: HM:0201
  concepto_nombre: Dolor abdominal
  estado_lr: no_medido
  lr_positivo: null
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:15082584
  referencia_cita: Hammer J, Eslick GD, Howell SC, Altiparmak E, Talley NJ Diagnostic yield of alarm features in irritable bowel syndrome and functional dyspepsia Gut 2004
  pmid: '15082584'
  doi: 10.1136/gut.2003.021857
triada:
  significante: Dolor referido por el paciente en el abdomen. Se caracteriza por su localización (cuadrante o región), carácter, cronología, irradiación y los factores que lo modifican; la localización es el punto de partida de la evaluación (pmid:18441863).
  significado: Estímulo nociceptivo de origen visceral (distensión, inflamación o isquemia de una víscera, mal localizado y de línea media), parietal (irritación del peritoneo, bien localizado) o referido desde estructuras extraabdominales (pmid:23055768). En los trastornos funcionales intestinales se asocia a la defecación o a cambios del hábito intestinal (pmid:27144627).
  decision: su relación con la defecación y con los cambios del hábito intestinal es el núcleo de los criterios diagnósticos; por sí solo no cuantifica la probabilidad
evidencia:
- concepto: HM:0201
  rol: manifestacion
  estado_lr: no_medido
  decision: su relación con la defecación y con los cambios del hábito intestinal es el núcleo de los criterios diagnósticos; por sí solo no cuantifica la probabilidad
  ref: pmid:27144627
- concepto: HM:0303
  rol: manifestacion
  estado_lr: no_medido
- concepto: HM:0304
  rol: manifestacion
  estado_lr: no_medido
autoevaluacion:
- id: q1
  pregunta: En Síndrome de intestino irritable, ¿qué estado de la evidencia corresponde a «Dolor abdominal» según la fuente?
  concepto_id: HM:0201
  referencia_id: pmid:27144627
  pmid: '27144627'
  doi: 10.1053/j.gastro.2016.02.031
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6002
    concepto_id: HM:0201
    estado_lr: no_medido
    campo: null
    dato: null
    poblacion: null
    motivo: null
    decision: su relación con la defecación y con los cambios del hábito intestinal es el núcleo de los criterios diagnósticos; por sí solo no cuantifica la probabilidad
    advertencia: null
  opciones:
  - texto: LR no medido
    correcta: true
    feedback: 'LR no medido Interpretación registrada: su relación con la defecación y con los cambios del hábito intestinal es el núcleo de los criterios diagnósticos; por sí solo no cuantifica la probabilidad.'
  - texto: LR no medible
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medido». LR no medido Interpretación registrada: su relación con la defecación y con los cambios del hábito intestinal es el núcleo de los criterios diagnósticos; por sí solo no cuantifica la probabilidad.'
  - texto: Sin efecto discriminativo
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medido». LR no medido Interpretación registrada: su relación con la defecación y con los cambios del hábito intestinal es el núcleo de los criterios diagnósticos; por sí solo no cuantifica la probabilidad.'
- id: q2
  pregunta: En Síndrome de intestino irritable, ¿qué estado de la evidencia corresponde a «Diarrea» según la fuente?
  concepto_id: HM:0303
  referencia_id: null
  pmid: null
  doi: null
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6002
    concepto_id: HM:0303
    estado_lr: no_medido
    campo: null
    dato: null
    poblacion: null
    motivo: null
    decision: null
    advertencia: null
  opciones:
  - texto: LR no medible
    correcta: false
    feedback: La fuente clasifica este hallazgo como «LR no medido». LR no medido
  - texto: Sin efecto discriminativo
    correcta: false
    feedback: La fuente clasifica este hallazgo como «LR no medido». LR no medido
  - texto: LR no medido
    correcta: true
    feedback: LR no medido
---

# Síndrome de intestino irritable

Hallazgos y criterios clínicos sin cocientes de verosimilitud medidos.

## Nombre en inglés

Irritable bowel syndrome

## Sinónimos

colon irritable

SII

intestino irritable

## Códigos

Snomed: 10743008; Cie10: K58

## Probabilidad basal

Valor: 0.57; Población: adultos con síntomas gastrointestinales bajos estudiados antes de su investigación (10 estudios prospectivos, 2355 pacientes); prevalencia resumida de SII tras la investigación del tracto gastrointestinal bajo; Referencia: pmid:18854541

## Factores de riesgo

**Enteritis infecciosa en los 12 meses previos** (pmid:28069350): riesgo relativo 4.2 (IC95% 3.1-5.7) frente a quien no la tuvo; 2.3 (IC95% 1.8-3.0) si fue hace más de 12 meses. Metaanálisis de 45 estudios de cohortes

**Sexo femenino** (pmid:22426087): OR 1.67 (IC95% 1.53-1.82) frente a varones en la población general; 80 poblaciones, 260 960 adultos

**Edad menor de 50 años** (pmid:22426087): en mayores de 50 años la prevalencia es menor, OR 0.75 (IC95% 0.62-0.92) frente a menores de 50

## Hallazgos clínicos

### Dolor abdominal (HM:0201)

**Significante:** Dolor referido por el paciente en el abdomen. Se caracteriza por su localización (cuadrante o región), carácter, cronología, irradiación y los factores que lo modifican; la localización es el punto de partida de la evaluación (pmid:18441863).

**Significado:** Estímulo nociceptivo de origen visceral (distensión, inflamación o isquemia de una víscera, mal localizado y de línea media), parietal (irritación del peritoneo, bien localizado) o referido desde estructuras extraabdominales (pmid:23055768). En los trastornos funcionales intestinales se asocia a la defecación o a cambios del hábito intestinal (pmid:27144627).

**Falsos positivos:** Dolor de pared abdominal (musculoesquelético o neuropático), que no procede de las vísceras / Dolor referido desde el tórax, como el de origen cardiaco o pleural

**Rol:** Manifestación

**Estado del LR:** LR no medido

**Decisión:** su relación con la defecación y con los cambios del hábito intestinal es el núcleo de los criterios diagnósticos; por sí solo no cuantifica la probabilidad

**Referencia:** pmid:27144627

### Diarrea (HM:0303)

**Significante:** Deposiciones de consistencia disminuida, blandas o líquidas, con o sin aumento de su frecuencia. La forma de las heces se registra con la escala de Bristol, cuyos tipos 6 y 7 corresponden a heces blandas o líquidas (pmid:9299672, pmid:27144627).

**Significado:** Aceleración del tránsito intestinal o alteración de la absorción o la secreción de agua y electrolitos; la forma de las heces se correlaciona con el tiempo de tránsito intestinal mejor que la frecuencia de las deposiciones (pmid:9299672).

**Falsos positivos:** Seudodiarrea, con deposiciones frecuentes pero de consistencia normal / Incontinencia fecal referida como diarrea / Diarrea por rebosamiento alrededor de un fecaloma

**Rol:** Manifestación

**Estado del LR:** LR no medido

### Estreñimiento (HM:0304)

**Significante:** Deposiciones infrecuentes, duras o difíciles de evacuar, con esfuerzo, sensación de evacuación incompleta o de obstrucción anorrectal. La forma de las heces se registra con la escala de Bristol, cuyos tipos 1 y 2 corresponden a heces duras (pmid:9299672, pmid:27144627).

**Significado:** Enlentecimiento del tránsito colónico o trastorno de la evacuación; la forma de las heces se correlaciona con el tiempo de tránsito intestinal (pmid:9299672).

**Falsos positivos:** Deposiciones infrecuentes pero blandas y sin dificultad para evacuar / Ingesta escasa, con poco volumen fecal y sin trastorno del tránsito

**Rol:** Manifestación

**Estado del LR:** LR no medido

## Signos de alarma

### Anemia (HM:0711)

**Efecto:** Signo de alarma

**Dispara si:** presente

**Estado del LR:** LR no medido

**Sostiene:** Afirmación respaldada por consenso

**Referencia:** pmid:20697190

**Nota:** Park afirma que la anemia, pese a su sensibilidad pobre para enfermedad orgánica, ofrece muy buena especificidad. No publica cifras: ninguna sensibilidad, especificidad, OR ni cociente acompaña a esa frase, así que se queda en consenso_con_afirmacion y no sube a discriminacion_medida. Solo subiría si alguien lee el texto completo, que está en coreano y no tiene versión en PMC. Registrado para que el próximo no repita la búsqueda.

### Pérdida de peso (HM:0803)

**Efecto:** Signo de alarma

**Dispara si:** presente

**Estado del LR:** LR no medido

**Sostiene:** Afirmación respaldada por consenso

**Referencia:** pmid:20697190

**Nota:** Misma afirmación de Park y mismas condiciones que la anemia: buena especificidad para enfermedad orgánica, sin cifras publicadas.

## Relaciones no incorporadas y sus motivos

### Fiebre (HM:0101)

**Motivo:** Solo la sostiene consenso_de_lista: aparece en enumeraciones de síntomas de alarma sin que ninguna reseña mida su poder discriminativo. Y una fiebre en un paciente con síntomas de intestino irritable no CONTRADICE el diagnóstico: simplemente no es de su territorio. Obliga a explicar la fiebre, no a abandonar la hipótesis. Declararla bandera roja afirmaría algo más fuerte de lo que consta.

**Nota:** No hace falta la bandera para que se vea: una fiebre validada que ningún signo del protocolo declara cae en el resto no simbolizado, baja el acoplamiento y aparece en la indagación.

### Melena (HM:0310)

**Motivo:** La evidencia disponible es de OTRO hallazgo. Hammer midió sangre en el papel higiénico, que es sangrado bajo; la melena es sangre digerida, de origen alto. Atribuirle ese dato daría una cita que resuelve y habla de otra cosa.

**Nota:** Por eso se acuñó «Hematoquecia», que es el concepto que Hammer sí midió. Su arista tampoco se emite: ver la discrepancia más abajo.

## Discrepancias entre fuentes

### Hematoquecia (HM:3060)

**Resumen:** Las dos fuentes se contradicen sobre este mismo hallazgo.

**A favor:** Referencia: pmid:15082584; Dice: Hammer 2004, regresión logística sobre 568 pacientes: la sangre en el papel higiénico discrimina enfermedad orgánica baja frente a intestino irritable, con OR 2.7 (IC95% 1.4-5.1), p=0.002.

**En contra:** Referencia: pmid:20697190; Dice: Park 2010, revisión sistemática: las alarm features como el sangrado rectal aportan poco valor discriminativo.

**Decisión:** No se emite la arista. Ante dos fuentes que se contradicen no se afirma un poder discriminativo, que es lo consistente con la parsimonia que ya dejó fuera a la fiebre. El hallazgo se recogerá igualmente como resto no simbolizado, así que no desaparece: solo no se le atribuye una fuerza que no consta.

**Para reabrirla:** Habría que leer el texto completo de Hammer (PMC1774043 está disponible) y comprobar que su modelo y su población coinciden con los de esta condición. Si se emitiera, el OR va en campo aparte y NUNCA dentro de lr_positivo, con sus covariables leídas del texto completo —el modelo incluye edad de inicio, sexo y criterios de Manning—, porque sin esa lista un OR de regresión no significa nada.

## Aspectos pendientes de documentación

Los criterios diagnósticos tienen cocientes medidos que este índice aún no estructura como reglas, porque sus componentes no existen como conceptos. En pacientes con síntomas gastrointestinales bajos (pmid:18854541): Manning, LR+ 2.9 (IC95% 1.3-6.4) y LR− 0.29 (IC95% 0.12-0.71); Roma I, LR+ 4.8 (IC95% 3.6-6.5) y LR− 0.34 (IC95% 0.29-0.41); Kruis, LR+ 8.6 (IC95% 2.9-26.0) y LR− 0.26 (IC95% 0.17-0.41). Roma III, en un metaanálisis posterior (pmid:26076071): LR+ 3.35 (IC95% 2.97-3.79) y LR− 0.39 (IC95% 0.34-0.46). Roma IV no consta validado en estas fuentes. Modelarlos exige acuñar sus componentes (dolor aliviado por la defecación, heces más blandas o frecuentes al inicio del dolor, moco rectal, distensión, sensación de evacuación incompleta) y leer el texto completo.

Los síntomas individuales tienen LR+ de 1.2 a 2.1 y LR− de 0.29 a 0.88 (pmid:18854541), pero el abstract no los atribuye uno a uno salvo en los extremos: el LR− 0.29 (IC95% 0.12-0.72) corresponde a la AUSENCIA de dolor abdominal BAJO, un hallazgo más estrecho que el dolor abdominal. No se asigna a dolor abdominal para no atribuirle la cifra de otro hallazgo; requiere acuñar el concepto y leer el texto completo.

## Referencias y procedencia

**pmid:15082584:** Diagnostic yield of alarm features in irritable bowel syndrome and functional dyspepsia. Gut, 2004. DOI: 10.1136/gut.2003.021857.

**pmid:18854541:** Will the history and physical examination help establish that irritable bowel syndrome is causing this patient's lower gastrointestinal tract symptoms?. JAMA, 2008. DOI: 10.1001/jama.300.15.1793.

**pmid:20697190:** [Diagnosis of irritable bowel syndrome: a systematic review]. Korean J Gastroenterol, 2010. DOI: 10.4166/kjg.2010.55.5.308.

**pmid:22426087:** Global prevalence of and risk factors for irritable bowel syndrome: a meta-analysis. Clin Gastroenterol Hepatol, 2012. DOI: 10.1016/j.cgh.2012.02.029.

**pmid:26076071:** Systematic review with meta-analysis: the accuracy of diagnosing irritable bowel syndrome with symptoms, biomarkers and/or psychological markers. Aliment Pharmacol Ther, 2015. DOI: 10.1111/apt.13283.

**pmid:27144627:** Bowel Disorders. Gastroenterology, 2016. DOI: 10.1053/j.gastro.2016.02.031.

**pmid:28069350:** Prevalence, Risk Factors, and Outcomes of Irritable Bowel Syndrome After Infectious Enteritis: A Systematic Review and Meta-analysis. Gastroenterology, 2017. DOI: 10.1053/j.gastro.2016.12.039.

**pmid:18441863:** Evaluation of acute abdominal pain in adults. Am Fam Physician, 2008. DOI: no documentado.

**pmid:23055768:** Evaluation and management of acute abdominal pain in the emergency department. Int J Gen Med, 2012. DOI: 10.2147/IJGM.S25936.

**pmid:9299672:** Stool form scale as a useful guide to intestinal transit time. Scand J Gastroenterol, 1997. DOI: 10.3109/00365529709011203.

Fuente clínica: medsemiotics-db, condición HM:6002.
