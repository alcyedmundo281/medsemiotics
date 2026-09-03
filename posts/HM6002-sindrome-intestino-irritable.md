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
  revision: a6b2afeb208457aaf6ce2d86ff78304f45071d5b
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6002-sindrome-intestino-irritable.yaml
  archivos:
    CITATION.cff: e2840db4d37cfb43ebe9835e23c1acfef6352e730051918fa0cbd9fe6fad77d7
    conceptos/HM0101-fiebre.yaml: fb16183d00cc93f60aff82d7904798fe984a3cef751a56e41e3d4f82bd58cc93
    conceptos/HM0201-dolor-abdominal.yaml: 564819078999f876e7aa0107eaa37bedc03a6e883b9722492cede175c5cb7bda
    conceptos/HM0303-diarrea.yaml: 0d5ca16fa30e66c063ee51a787ddae512941d0600d783e12fbd847482a224ced
    conceptos/HM0304-estrenimiento.yaml: 144e3ac249c42c3c2b9a726e28a4fc596afc88b32b7266ad8906ed7fd157899f
    conceptos/HM0310-melena.yaml: 56ea476133e21be467cd68f7bb9a8a9b3f9a7623d63fbf3e4e37810fe2d87081
    conceptos/HM0711-anemia.yaml: 33c2de9e06e96c38c950b2cdc270e1acd8a60d7953e04b9c6224303f28628410
    conceptos/HM0803-perdida-de-peso.yaml: 78cd9514f8137e60f123c191cb3939fa57bc11c77dcda85c914e82e8eac1d22e
    conceptos/HM3060-hematoquecia.yaml: 3859f875c15207194d1bc498152f293a810c21faeb51c3ae1ce78ba459cbd338
    condiciones/HM6002-sindrome-intestino-irritable.yaml: de99a8c5755f450792d575897902bde932154119c4318ee30d916dbec0bd11f5
    referencias/pmid-15082584.yaml: bed79febe6875717f56dda071ab3d22da080c14d2f6552a0c7803e9eb9dc4a27
    referencias/pmid-20697190.yaml: 5acfa5ff915443623dc06031e8065400f6ab0f27d72e95e35e365d825b88b3ad
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
  significante: Dolor abdominal
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: La fuente no documenta una decisión específica para este hallazgo.
evidencia:
- concepto: HM:0201
  rol: manifestacion
  estado_lr: no_medido
- concepto: HM:0303
  rol: manifestacion
  estado_lr: no_medido
- concepto: HM:0304
  rol: manifestacion
  estado_lr: no_medido
autoevaluacion:
- id: q1
  pregunta: ¿Cómo está documentado el LR de Dolor abdominal en Síndrome de intestino irritable?
  concepto_id: HM:0201
  referencia_id: null
  pmid: null
  doi: null
  opciones:
  - texto: LR no medido
    correcta: true
    feedback: 'Registro HM:6002: LR no medido'
  - texto: Hay una estimación numérica única disponible para calcular la probabilidad posterior.
    correcta: false
    feedback: 'El registro documenta: LR no medido'
- id: q2
  pregunta: ¿Cómo está documentado el LR de Diarrea en Síndrome de intestino irritable?
  concepto_id: HM:0303
  referencia_id: null
  pmid: null
  doi: null
  opciones:
  - texto: Hay una estimación numérica única disponible para calcular la probabilidad posterior.
    correcta: false
    feedback: 'El registro documenta: LR no medido'
  - texto: LR no medido
    correcta: true
    feedback: 'Registro HM:6002: LR no medido'
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

Snomed: No documentado.; Cie10: No documentado.

## Hallazgos clínicos

### Dolor abdominal (HM:0201)

**Rol:** Manifestación

**Estado del LR:** LR no medido

### Diarrea (HM:0303)

**Rol:** Manifestación

**Estado del LR:** LR no medido

### Estreñimiento (HM:0304)

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

**Nota:** Por eso se acuñó HM:3060 «Hematoquecia», que es el concepto que Hammer sí midió. Su arista tampoco se emite: ver la discrepancia más abajo.

## Discrepancias entre fuentes

### Hematoquecia (HM:3060)

**Resumen:** Las dos fuentes se contradicen sobre este mismo hallazgo.

**A favor:** Referencia: pmid:15082584; Dice: Hammer 2004, regresión logística sobre 568 pacientes: la sangre en el papel higiénico discrimina enfermedad orgánica baja frente a intestino irritable, con OR 2.7 (IC95% 1.4-5.1), p=0.002.

**En contra:** Referencia: pmid:20697190; Dice: Park 2010, revisión sistemática: las alarm features como el sangrado rectal aportan poco valor discriminativo.

**Decisión:** No se emite la arista. Ante dos fuentes que se contradicen no se afirma un poder discriminativo, que es lo consistente con la parsimonia que ya dejó fuera a la fiebre. El hallazgo se recogerá igualmente como resto no simbolizado, así que no desaparece: solo no se le atribuye una fuerza que no consta.

**Para reabrirla:** Habría que leer el texto completo de Hammer (PMC1774043 está disponible) y comprobar que su modelo y su población coinciden con los de esta condición. Si se emitiera, el OR va en campo aparte y NUNCA dentro de lr_positivo, con sus covariables leídas del texto completo —el modelo incluye edad de inicio, sexo y criterios de Manning—, porque sin esa lista un OR de regresión no significa nada.

## Referencias y procedencia

**pmid:15082584:** Diagnostic yield of alarm features in irritable bowel syndrome and functional dyspepsia. Gut, 2004. DOI: 10.1136/gut.2003.021857.

**pmid:20697190:** [Diagnosis of irritable bowel syndrome: a systematic review]. Korean J Gastroenterol, 2010. DOI: 10.4166/kjg.2010.55.5.308.

Fuente clínica: medsemiotics-db, condición HM:6002.
