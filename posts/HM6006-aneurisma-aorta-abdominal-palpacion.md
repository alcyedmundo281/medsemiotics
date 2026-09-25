---
id: HM6006-01
slug: aneurisma-aorta-abdominal-palpacion-semiotica
title: 'Aneurisma de aorta abdominal: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-08-21'
author: Dr. Alcy Torres
category: vascular
category_label: Medicina Vascular y Cirugía
tags:
- aneurisma-de-aorta-abdominal
- semiologia
- vascular
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: 9505ae00ca47576b3cd86bdec1357bc816f9cf91
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6006-aneurisma-aorta-abdominal.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0600-signo-de-exploracion.yaml: 86a2ac9babe66028eecc797ddbf4d9ea382a6fd685e9cb8df91bb959029d62bf
    conceptos/HM3012-pulsacion-aortica-ensanchada.yaml: 54dc1972896e31463bf5d4cc9382967a0589d052c695c8879761be103b481f35
    conceptos/HM3013-obesidad-abdominal.yaml: ee9829407e607153c1968b7b8c15bce01f3e5fe32ff4608bce0d385fe8829a54
    condiciones/HM6006-aneurisma-aorta-abdominal.yaml: 672d3116c31867d0a4243f887508109b8b8898cde49f7292bae864ef502ee379
    referencias/pmid-9072929.yaml: dbb0d3ea0b1080a268e21ac76dd8be2635e3747d5fc3ce7d4d60092c5d6cbd17
    referencias/pmid-9892455.yaml: 781f7d38a1ffdb9e732d07f96d7d375d0b690cc6f5ddd1324d87d3070f981905
grounding:
  condicion_id: HM:6006
  condicion_nombre: Aneurisma de aorta abdominal
  concepto_id: HM:3012
  concepto_nombre: Pulsación aórtica ensanchada a la palpación
  estado_lr: medido
  lr_positivo: 12.0
  lr_negativo: 0.72
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:9892455
  referencia_cita: Lederle FA, Simel DL The rational clinical examination. Does this patient have abdominal aortic aneurysm? JAMA 1999
  pmid: '9892455'
  doi: 10.1001/jama.281.1.77
triada:
  significante: Pulsación aórtica ensanchada a la palpación
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: 'la palpación positiva desplaza con fuerza hacia el diagnóstico, pero la negativa apenas descarta: un LR− de 0.72 deja la probabilidad casi intacta'
evidencia:
- concepto: HM:3012
  rol: prueba_especifica
  estado_lr: medido
  lr_positivo: &id001
    valor: 12.0
    ic95:
    - 7.4
    - 19.5
    umbral_condicion: aneurisma de 3.0 cm o mayor
    ref: pmid:9892455
  lr_negativo:
    valor: 0.72
    ic95:
    - 0.65
    - 0.81
    umbral_condicion: aneurisma de 3.0 cm o mayor
    ref: pmid:9892455
  decision: 'la palpación positiva desplaza con fuerza hacia el diagnóstico, pero la negativa apenas descarta: un LR− de 0.72 deja la probabilidad casi intacta'
  advertencia: no puede usarse para excluir el aneurisma, y menos si la rotura entra en el diferencial. La fuente lo dice de forma explícita.
  graduacion:
    parametro: Diámetro aórtico máximo
    unidad: cm
    lectura: acumulativo
  tramos:
  - umbral_condicion: aneurisma de 3.0 cm o mayor
    desde: 3.0
    lr_positivo: 12.0
    ic95:
    - 7.4
    - 19.5
    lr_negativo: 0.72
    ic95_negativo:
    - 0.65
    - 0.81
    ref: pmid:9892455
  - umbral_condicion: aneurisma de 4.0 cm o mayor
    desde: 4.0
    lr_positivo: 15.6
    ic95:
    - 8.6
    - 28.5
    lr_negativo: 0.51
    ic95_negativo:
    - 0.38
    - 0.67
    ref: pmid:9892455
  sensibilidad_por_diametro:
  - diametro: 3.0 a 3.9 cm
    sensibilidad: 0.29
    ref: pmid:9892455
  - diametro: 4.0 a 4.9 cm
    sensibilidad: 0.5
    ref: pmid:9892455
  - diametro: 5.0 cm o mayor
    sensibilidad: 0.76
    ref: pmid:9892455
autoevaluacion:
- id: q1
  pregunta: En Aneurisma de aorta abdominal, ¿cuál es el resultado documentado del LR positivo para «Pulsación aórtica ensanchada a la palpación»?
  concepto_id: HM:3012
  referencia_id: pmid:9892455
  pmid: '9892455'
  doi: 10.1001/jama.281.1.77
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6006
    concepto_id: HM:3012
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: 'la palpación positiva desplaza con fuerza hacia el diagnóstico, pero la negativa apenas descarta: un LR− de 0.72 deja la probabilidad casi intacta'
    advertencia: no puede usarse para excluir el aneurisma, y menos si la rotura entra en el diferencial. La fuente lo dice de forma explícita.
  opciones:
  - texto: El valor 12.0 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 12.0. IC del 95 %: 7.4 a 19.5. Interpretación registrada: la palpación positiva desplaza con fuerza hacia el diagnóstico, pero la negativa apenas descarta: un LR− de 0.72 deja la probabilidad casi intacta. Advertencia: no puede usarse para excluir el aneurisma, y menos si la rotura entra en el diferencial. La fuente lo dice de forma explícita.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 12.0. LR positivo: 12.0. IC del 95 %: 7.4 a 19.5. Interpretación registrada: la palpación positiva desplaza con fuerza hacia el diagnóstico, pero la negativa apenas descarta: un LR− de 0.72 deja la probabilidad casi intacta. Advertencia: no puede usarse para excluir el aneurisma, y menos si la rotura entra en el diferencial. La fuente lo dice de forma explícita.'
  - texto: 'LR positivo: 12.0.'
    correcta: true
    feedback: 'LR positivo: 12.0. IC del 95 %: 7.4 a 19.5. Interpretación registrada: la palpación positiva desplaza con fuerza hacia el diagnóstico, pero la negativa apenas descarta: un LR− de 0.72 deja la probabilidad casi intacta. Advertencia: no puede usarse para excluir el aneurisma, y menos si la rotura entra en el diferencial. La fuente lo dice de forma explícita.'
---

# Aneurisma de aorta abdominal

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Abdominal aortic aneurysm

## Sinónimos

AAA

aneurisma aórtico abdominal

## Códigos

Snomed: 233985008; Cie10: I71.4

## Probabilidad basal

Valor: 0.014; Población: 73 451 veteranos de 50 a 79 años sin aneurisma conocido, cribados con ecografía en 15 centros de Estados Unidos; 1031 de ellos; Nota: prevalencia de aneurisma de 4.0 cm o mayor, que corresponde al segundo tramo de la palpación; la fuente no da la de 3.0 cm o mayor en su resumen; Referencia: pmid:9072929

## Factores de riesgo

Factor: Tabaquismo; Referencia: pmid:9072929; Nota: OR 5.57 (IC95% 4.24-7.31) para aneurisma de 4.0 cm o mayor frente a aorta normal, en análisis multivariable. Crece con los años fumados y baja con los años sin fumar

Factor: Antecedente familiar de aneurisma de aorta abdominal; Referencia: pmid:9072929; Nota: OR 1.95 (IC95% 1.56-2.43) en análisis multivariable

Factor: Edad; Referencia: pmid:9072929; Nota: asociación independiente; el resumen no da su OR

Factor: Talla alta; Referencia: pmid:9072929; Nota: asociación independiente; el resumen no da su OR

Factor: Enfermedad coronaria o aterosclerosis en otro territorio; Referencia: pmid:9072929; Nota: asociación independiente; el resumen no da su OR

Factor: Hipercolesterolemia; Referencia: pmid:9072929; Nota: asociación independiente; el resumen no da su OR

Factor: Hipertensión arterial; Referencia: pmid:9072929; Nota: asociación independiente; el resumen no da su OR

## Hallazgos clínicos

### Pulsación aórtica ensanchada a la palpación (HM:3012)

**Rol:** Prueba específica

**Estado del LR:** LR medido

**LR positivo:** Valor: 12.0; IC del 95 %: 7.4 / 19.5; Umbral condicion: aneurisma de 3.0 cm o mayor; Referencia: pmid:9892455

**LR negativo:** Valor: 0.72; IC del 95 %: 0.65 / 0.81; Umbral condicion: aneurisma de 3.0 cm o mayor; Referencia: pmid:9892455

**Decisión:** la palpación positiva desplaza con fuerza hacia el diagnóstico, pero la negativa apenas descarta: un LR− de 0.72 deja la probabilidad casi intacta

**Advertencia:** no puede usarse para excluir el aneurisma, y menos si la rotura entra en el diferencial. La fuente lo dice de forma explícita.

**Graduación:** Parámetro: Diámetro aórtico máximo; Unidad: cm; Lectura: acumulativo

**Tramos:** Umbral condicion: aneurisma de 3.0 cm o mayor; Desde: 3.0; LR positivo: 12.0; IC del 95 %: 7.4 / 19.5; LR negativo: 0.72; Ic95 negativo: 0.65 / 0.81; Referencia: pmid:9892455 / Umbral condicion: aneurisma de 4.0 cm o mayor; Desde: 4.0; LR positivo: 15.6; IC del 95 %: 8.6 / 28.5; LR negativo: 0.51; Ic95 negativo: 0.38 / 0.67; Referencia: pmid:9892455

**Sensibilidad por diametro:** Diametro: 3.0 a 3.9 cm; Sensibilidad: 0.29; Referencia: pmid:9892455 / Diametro: 4.0 a 4.9 cm; Sensibilidad: 0.5; Referencia: pmid:9892455 / Diametro: 5.0 cm o mayor; Sensibilidad: 0.76; Referencia: pmid:9892455

## Modificadores

### Obesidad abdominal (HM:3013)

**Efecto:** reduce la sensibilidad de la palpación

**Referencia:** pmid:9892455

**Nota:** la fuente lo respalda con datos limitados

## Notas de uso

Valor predictivo positivo de la palpación para aneurisma de 3.0 cm o mayor en estas series: 43%.

No se ha descrito que la palpación precipite la rotura.

## Referencias y procedencia

**pmid:9072929:** Prevalence and associations of abdominal aortic aneurysm detected through screening. Aneurysm Detection and Management (ADAM) Veterans Affairs Cooperative Study Group. Ann Intern Med, 1997. DOI: 10.7326/0003-4819-126-6-199703150-00004.

**pmid:9892455:** The rational clinical examination. Does this patient have abdominal aortic aneurysm?. JAMA, 1999. DOI: 10.1001/jama.281.1.77.

Fuente clínica: medsemiotics-db, condición HM:6006.
