---
id: HM6037-01
slug: sobrecarga-de-volumen-precision-semiotica
title: 'Sobrecarga de volumen: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-09-18'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- medicina_interna
- semiologia
- sobrecarga-de-volumen
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: 9c9015322734168fe0328362950237f8ad296a55
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6037-sobrecarga-de-volumen.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0400-sintoma-respiratorio.yaml: 437414db42a3586a5896d3f91e90ee8ed51c7baef7b67741067b3ee04ca7a53b
    conceptos/HM0406-crepitantes.yaml: 5025b2d5cad42255302233528cb6c75479881002078b78baff67dae058475083
    conceptos/HM0600-signo-de-exploracion.yaml: 86a2ac9babe66028eecc797ddbf4d9ea382a6fd685e9cb8df91bb959029d62bf
    conceptos/HM0604-edema-en-miembros-inferiores.yaml: ca8df008ba56ddf2a9a2d6786ecd624e2d1e8ded2adb5a20c6b86adff479c0e9
    conceptos/HM0700-alteracion-analitica.yaml: 855280729989c53c674d74df1d9d1459df52ecfe46d1bb650f6bf3b590383f5b
    conceptos/HM0900-hallazgo-de-imagen.yaml: 0b40c9368c746533cc335071c04e027c4465fb29158ed2cc747d65b9bb573e67
    conceptos/HM3146-ingurgitacion-yugular.yaml: 68f00e3333cd5790afa7a4f9a6a550b2feee50898fb40eda646b356d00312ab0
    conceptos/HM3147-congestion-vascular-en-radiografia-de-torax.yaml: 740f5e92a92e8a63c9c5cb4d68bd83b7dae9cf7aaaa646a7c0a418ed1ad7de5d
    conceptos/HM3148-lineas-b-pulmonares-bilaterales.yaml: bf438bf8faf27db643fbcfa947ad803782ce7e30b057ddcd3e21790d952d516e
    conceptos/HM3149-colapsabilidad-reducida-de-la-vena-cava-inferior.yaml: 4ecb426dd940030438b55098a70a345224f1f74377bd1b7b0082f88d43d217b7
    conceptos/HM3150-presion-venosa-yugular-elevada-por-ecografia.yaml: 14123abf7c9a13905022e5cf5ce2d07cd179a9c60fff58883b5bf109d21c0ccc
    conceptos/HM3151-peptido-natriuretico-cerebral-elevado.yaml: 67c8cf440251c504880f70bde0dce1ea5b332e82a46c97beaa37fe6b1cc9c151
    conceptos/HM3160-perfil-a-pulmon-seco.yaml: f014ba950c8c3ccaa756c4ff3932886d6468c531a58e0a3d3a9d1cd1877006f5
    condiciones/HM6037-sobrecarga-de-volumen.yaml: eca41c49d71742acef49b4319fc79da95905d97155a2dbaec845d342004a615f
    referencias/pmid-22392031.yaml: 167a3ea8e8037ca94a29ecff6c379200f402babf474159c1a9b6a94336ee5e7b
    referencias/pmid-41729549.yaml: a3b8210b679e9dff1f5671c3127d08ad54fcd26329cfe6735e29183e0cc98937
grounding:
  condicion_id: HM:6037
  condicion_nombre: Sobrecarga de volumen
  concepto_id: HM:3147
  concepto_nombre: Congestión vascular en la radiografía de tórax
  estado_lr: medido
  lr_positivo: 5.8
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: null
  referencia_id: pmid:41729549
  referencia_cita: 'Drum B, La Course B, Kelly M, York A, Worrall E, Martins J, Johnson S, Liles EA Jr Does This Patient Have Volume Overload?: The Rational Clinical Examination JAMA 2026'
  pmid: '41729549'
  doi: 10.1001/jama.2026.0446
  especificidad: 0.91
triada:
  significante: Congestión vascular en la radiografía de tórax
  significado: El mecanismo fisiopatológico no está documentado en esta fuente.
  decision: con las cifras corregidas es el cociente positivo más alto de los doce, por encima del BNP. La conclusión de la fuente los nombra juntos como las dos pruebas más útiles para identificar la sobrecarga.
evidencia:
- concepto: HM:3147
  rol: imagen
  estado_lr: medido
  lr_positivo: &id001
    valor: 5.8
    ic95:
    - 2.9
    - 11.5
    ref: pmid:41729549
  especificidad: 0.91
  decision: con las cifras corregidas es el cociente positivo más alto de los doce, por encima del BNP. La conclusión de la fuente los nombra juntos como las dos pruebas más útiles para identificar la sobrecarga.
- concepto: HM:3151
  rol: prueba_sensible
  estado_lr: medido
  lr_positivo: &id002
    valor: 4.2
    ic95:
    - 1.8
    - 10
    umbral: BNP ≥ 100 ng/mL
    ref: pmid:41729549
  lr_negativo:
    valor: 0.09
    ic95:
    - 0.06
    - 0.16
    umbral: BNP < 100 ng/mL
    ref: pmid:41729549
  sensibilidad: 0.93
  especificidad: 0.78
  efecto: excluye
  dispara_si: ausente
  sostiene: discriminacion_medida
  ref: pmid:41729549
  decision: 'la conclusión de la fuente lo señala, junto con la ausencia de líneas B, como lo más útil para EXCLUIR la sobrecarga: un BNP normal la hace muy poco probable'
  advertencia: la unidad del corte es la que imprime la fuente, ng/mL, y no se convierte. La literatura habitual sitúa el mismo corte en 100 pg/mL. Ver la advertencia del concepto HM:3151 antes de usar este umbral.
  nota: 'es el hallazgo cuyas cifras más movió la corrección: LR+ pasó de 6.9 a 4.2 y LR− de 0.14 a 0.09. Las de aquí son las corregidas.'
- concepto: HM:3146
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 4.1
    ic95:
    - 2.9
    - 5.6
    umbral: punto máximo de pulsación > 3 cm sobre el ángulo esternal
    ref: pmid:41729549
  especificidad: 0.92
  decision: el hallazgo de exploración física con mejor rendimiento de la serie, y el más específico de los doce
  advertencia: 'es la ingurgitación que se INSPECCIONA. La presión venosa yugular medida con ecografía es otra arista (HM:3150) con otro cociente: 2.9 frente a 4.1, y especificidad 73% frente a 92%. No son intercambiables.'
- concepto: HM:3148
  rol: imagen
  estado_lr: medido
  lr_positivo:
    valor: 4.0
    ic95:
    - 2.7
    - 6.1
    ref: pmid:41729549
  lr_negativo:
    valor: 0.09
    ic95:
    - 0.04
    - 0.23
    ref: pmid:41729549
  sensibilidad: 0.93
  especificidad: 0.77
  efecto: excluye
  dispara_si: ausente
  sostiene: discriminacion_medida
  ref: pmid:41729549
  decision: 'su AUSENCIA es lo que la conclusión de la fuente convierte en decisión: junto con un BNP normal, es lo más útil para excluir la sobrecarga'
  advertencia: el cociente es el de las líneas B BILATERALES. Unas líneas B focales son otro hallazgo y no llevan este número.
- concepto: HM:3149
  rol: imagen
  estado_lr: medido
  lr_positivo:
    valor: 3.9
    ic95:
    - 2.5
    - 6.1
    umbral: índice de colapsabilidad < 50%
    ref: pmid:41729549
  lr_negativo:
    valor: 0.22
    ic95:
    - 0.11
    - 0.45
    umbral: índice de colapsabilidad ≥ 50%
    ref: pmid:41729549
  sensibilidad: 0.82
  especificidad: 0.79
  ref: pmid:41729549
  advertencia: 'el corte va al revés que la intuición: lo que indica sobrecarga es colapsar POCO. Un índice por debajo del 50% la hace más probable; por encima, menos.'
- concepto: HM:3150
  rol: imagen
  estado_lr: medido
  lr_positivo:
    valor: 2.9
    ic95:
    - 2.3
    - 3.7
    umbral: PVY ecográfica > 8 cm
    ref: pmid:41729549
  lr_negativo:
    valor: 0.27
    ic95:
    - 0.21
    - 0.34
    umbral: PVY ecográfica ≤ 8 cm
    ref: pmid:41729549
  sensibilidad: 0.8
  especificidad: 0.73
  ref: pmid:41729549
  advertencia: no confundir con la ingurgitación yugular de la inspección (HM:3146), que la fuente mide aparte y con mejor cociente
- concepto: HM:0406
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 2.7
    ic95:
    - 0.7
    - 4.5
    ref: pmid:41729549
  especificidad: 0.82
  advertencia: EL INTERVALO CORREGIDO CRUZA EL 1. La corrección cambió el límite inferior de 1.7 a 0.7, así que el cociente ya no es distinguible de la ausencia de efecto. Se transcribe tal como lo publica la fuente corregida, sin redondear ni recortar. Quien lo consuma no debe tratarlo como un hallazgo que desplaza la probabilidad.
  nota: 'el intervalo es además el único de los doce que no es simétrico en escala logarítmica: la distancia al límite inferior es 2.6 veces la distancia al superior. Se anota porque se comprobó, no porque autorice a corregirlo.'
- concepto: HM:0604
  rol: apoyo
  estado_lr: medido
  lr_positivo:
    valor: 2.2
    ic95:
    - 1.5
    - 3.1
    ref: pmid:41729549
  especificidad: 0.8
  decision: 'el más débil de los hallazgos de exploración con efecto medible: mueve la probabilidad, pero poco'
autoevaluacion:
- id: q1
  pregunta: En Sobrecarga de volumen, ¿cuál es el resultado documentado del LR positivo para «Congestión vascular en la radiografía de tórax»?
  concepto_id: HM:3147
  referencia_id: pmid:41729549
  pmid: '41729549'
  doi: 10.1001/jama.2026.0446
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6037
    concepto_id: HM:3147
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: null
    motivo: null
    decision: con las cifras corregidas es el cociente positivo más alto de los doce, por encima del BNP. La conclusión de la fuente los nombra juntos como las dos pruebas más útiles para identificar la sobrecarga.
    advertencia: null
  opciones:
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 5.8. LR positivo: 5.8. IC del 95 %: 2.9 a 11.5. Interpretación registrada: con las cifras corregidas es el cociente positivo más alto de los doce, por encima del BNP. La conclusión de la fuente los nombra juntos como las dos pruebas más útiles para identificar la sobrecarga.'
  - texto: 'LR positivo: 5.8.'
    correcta: true
    feedback: 'LR positivo: 5.8. IC del 95 %: 2.9 a 11.5. Interpretación registrada: con las cifras corregidas es el cociente positivo más alto de los doce, por encima del BNP. La conclusión de la fuente los nombra juntos como las dos pruebas más útiles para identificar la sobrecarga.'
  - texto: El valor 5.8 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 5.8. IC del 95 %: 2.9 a 11.5. Interpretación registrada: con las cifras corregidas es el cociente positivo más alto de los doce, por encima del BNP. La conclusión de la fuente los nombra juntos como las dos pruebas más útiles para identificar la sobrecarga.'
- id: q2
  pregunta: 'En Sobrecarga de volumen, ¿cuál es el resultado documentado del LR positivo para «Péptido natriurético cerebral elevado»? Umbral: BNP ≥ 100 ng/mL.'
  concepto_id: HM:3151
  referencia_id: pmid:41729549
  pmid: '41729549'
  doi: 10.1001/jama.2026.0446
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6037
    concepto_id: HM:3151
    estado_lr: medido
    campo: lr_positivo
    dato: *id002
    poblacion: null
    motivo: null
    decision: 'la conclusión de la fuente lo señala, junto con la ausencia de líneas B, como lo más útil para EXCLUIR la sobrecarga: un BNP normal la hace muy poco probable'
    advertencia: la unidad del corte es la que imprime la fuente, ng/mL, y no se convierte. La literatura habitual sitúa el mismo corte en 100 pg/mL. Ver la advertencia del concepto HM:3151 antes de usar este umbral.
  opciones:
  - texto: 'LR positivo: 4.2.'
    correcta: true
    feedback: 'LR positivo: 4.2. IC del 95 %: 1.8 a 10. Umbral: BNP ≥ 100 ng/mL. Interpretación registrada: la conclusión de la fuente lo señala, junto con la ausencia de líneas B, como lo más útil para EXCLUIR la sobrecarga: un BNP normal la hace muy poco probable. Advertencia: la unidad del corte es la que imprime la fuente, ng/mL, y no se convierte. La literatura habitual sitúa el mismo corte en 100 pg/mL. Ver la advertencia del concepto HM:3151 antes de usar este umbral.'
  - texto: El valor 4.2 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 4.2. IC del 95 %: 1.8 a 10. Umbral: BNP ≥ 100 ng/mL. Interpretación registrada: la conclusión de la fuente lo señala, junto con la ausencia de líneas B, como lo más útil para EXCLUIR la sobrecarga: un BNP normal la hace muy poco probable. Advertencia: la unidad del corte es la que imprime la fuente, ng/mL, y no se convierte. La literatura habitual sitúa el mismo corte en 100 pg/mL. Ver la advertencia del concepto HM:3151 antes de usar este umbral.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 4.2. LR positivo: 4.2. IC del 95 %: 1.8 a 10. Umbral: BNP ≥ 100 ng/mL. Interpretación registrada: la conclusión de la fuente lo señala, junto con la ausencia de líneas B, como lo más útil para EXCLUIR la sobrecarga: un BNP normal la hace muy poco probable. Advertencia: la unidad del corte es la que imprime la fuente, ng/mL, y no se convierte. La literatura habitual sitúa el mismo corte en 100 pg/mL. Ver la advertencia del concepto HM:3151 antes de usar este umbral.'
---

# Sobrecarga de volumen

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Volume overload

## Sinónimos

sobrecarga hídrica

hipervolemia

congestión volémica

## Códigos

Snomed: No documentado.; Cie10: No documentado.

## Probabilidad basal

Rango documentado: 0.35 / 0.69; Población: adultos que respiran espontáneamente con sospecha de sobrecarga de volumen, en 40 estudios y 11 490 pacientes; 33 de los 40 estudiaron pacientes con disnea; Referencia: pmid:41729549; Nota: es la dispersión entre entornos asistenciales, no un intervalo de incertidumbre sobre un mismo valor; quien puebla un protocolo elige según dónde atiende

## Hallazgos clínicos

### Congestión vascular en la radiografía de tórax (HM:3147)

**Rol:** Imagen

**Estado del LR:** LR medido

**LR positivo:** Valor: 5.8; IC del 95 %: 2.9 / 11.5; Referencia: pmid:41729549

**Especificidad:** 0.91

**Decisión:** con las cifras corregidas es el cociente positivo más alto de los doce, por encima del BNP. La conclusión de la fuente los nombra juntos como las dos pruebas más útiles para identificar la sobrecarga.

### Péptido natriurético cerebral elevado (HM:3151)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**LR positivo:** Valor: 4.2; IC del 95 %: 1.8 / 10; Umbral: BNP ≥ 100 ng/mL; Referencia: pmid:41729549

**LR negativo:** Valor: 0.09; IC del 95 %: 0.06 / 0.16; Umbral: BNP < 100 ng/mL; Referencia: pmid:41729549

**Sensibilidad:** 0.93

**Especificidad:** 0.78

**Efecto:** excluye

**Dispara si:** ausente

**Sostiene:** Discriminación medida

**Referencia:** pmid:41729549

**Decisión:** la conclusión de la fuente lo señala, junto con la ausencia de líneas B, como lo más útil para EXCLUIR la sobrecarga: un BNP normal la hace muy poco probable

**Advertencia:** la unidad del corte es la que imprime la fuente, ng/mL, y no se convierte. La literatura habitual sitúa el mismo corte en 100 pg/mL. Ver la advertencia del concepto péptido natriurético cerebral elevado antes de usar este umbral.

**Nota:** es el hallazgo cuyas cifras más movió la corrección: LR+ pasó de 6.9 a 4.2 y LR− de 0.14 a 0.09. Las de aquí son las corregidas.

### Ingurgitación yugular (HM:3146)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 4.1; IC del 95 %: 2.9 / 5.6; Umbral: punto máximo de pulsación > 3 cm sobre el ángulo esternal; Referencia: pmid:41729549

**Especificidad:** 0.92

**Decisión:** el hallazgo de exploración física con mejor rendimiento de la serie, y el más específico de los doce

**Advertencia:** es la ingurgitación que se INSPECCIONA. La presión venosa yugular medida con ecografía es otra arista (presión venosa yugular elevada por ecografía) con otro cociente: 2.9 frente a 4.1, y especificidad 73% frente a 92%. No son intercambiables.

### Líneas B pulmonares bilaterales (HM:3148)

**Significante:** Artefactos verticales hiperecoicos, en cola de cometa, que nacen en la línea pleural, borran las líneas A y se mueven con la respiración.

**Significado:** Engrosamiento del intersticio por líquido. Síndrome intersticial.

**Falsos positivos:** Fibrosis pulmonar / Neumonía / SDRA / Contusión pulmonar

**Rol:** Imagen

**Estado del LR:** LR medido

**LR positivo:** Valor: 4.0; IC del 95 %: 2.7 / 6.1; Referencia: pmid:41729549

**LR negativo:** Valor: 0.09; IC del 95 %: 0.04 / 0.23; Referencia: pmid:41729549

**Sensibilidad:** 0.93

**Especificidad:** 0.77

**Efecto:** excluye

**Dispara si:** ausente

**Sostiene:** Discriminación medida

**Referencia:** pmid:41729549

**Decisión:** su AUSENCIA es lo que la conclusión de la fuente convierte en decisión: junto con un BNP normal, es lo más útil para excluir la sobrecarga

**Advertencia:** el cociente es el de las líneas B BILATERALES. Unas líneas B focales son otro hallazgo y no llevan este número.

### Colapsabilidad reducida de la vena cava inferior (HM:3149)

**Rol:** Imagen

**Estado del LR:** LR medido

**LR positivo:** Valor: 3.9; IC del 95 %: 2.5 / 6.1; Umbral: índice de colapsabilidad < 50%; Referencia: pmid:41729549

**LR negativo:** Valor: 0.22; IC del 95 %: 0.11 / 0.45; Umbral: índice de colapsabilidad ≥ 50%; Referencia: pmid:41729549

**Sensibilidad:** 0.82

**Especificidad:** 0.79

**Referencia:** pmid:41729549

**Advertencia:** el corte va al revés que la intuición: lo que indica sobrecarga es colapsar POCO. Un índice por debajo del 50% la hace más probable; por encima, menos.

### Presión venosa yugular elevada por ecografía (HM:3150)

**Rol:** Imagen

**Estado del LR:** LR medido

**LR positivo:** Valor: 2.9; IC del 95 %: 2.3 / 3.7; Umbral: PVY ecográfica > 8 cm; Referencia: pmid:41729549

**LR negativo:** Valor: 0.27; IC del 95 %: 0.21 / 0.34; Umbral: PVY ecográfica ≤ 8 cm; Referencia: pmid:41729549

**Sensibilidad:** 0.8

**Especificidad:** 0.73

**Referencia:** pmid:41729549

**Advertencia:** no confundir con la ingurgitación yugular de la inspección, que la fuente mide aparte y con mejor cociente

### Crepitantes (HM:0406)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 2.7; IC del 95 %: 0.7 / 4.5; Referencia: pmid:41729549

**Especificidad:** 0.82

**Advertencia:** EL INTERVALO CORREGIDO CRUZA EL 1. La corrección cambió el límite inferior de 1.7 a 0.7, así que el cociente ya no es distinguible de la ausencia de efecto. Se transcribe tal como lo publica la fuente corregida, sin redondear ni recortar. Quien lo consuma no debe tratarlo como un hallazgo que desplaza la probabilidad.

**Nota:** el intervalo es además el único de los doce que no es simétrico en escala logarítmica: la distancia al límite inferior es 2.6 veces la distancia al superior. Se anota porque se comprobó, no porque autorice a corregirlo.

### Edema en miembros inferiores (HM:0604)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR medido

**LR positivo:** Valor: 2.2; IC del 95 %: 1.5 / 3.1; Referencia: pmid:41729549

**Especificidad:** 0.8

**Decisión:** el más débil de los hallazgos de exploración con efecto medible: mueve la probabilidad, pero poco

## Notas de uso

Todos los cocientes se leen en pacientes que RESPIRAN ESPONTÁNEAMENTE. La revisión excluye a los intubados, y ninguna cifra se puede trasladar a ventilación mecánica: la colapsabilidad de la vena cava, en particular, cambia de significado.

Treinta y tres de los cuarenta estudios reclutaron pacientes con disnea, así que la serie describe sobre todo el problema de decidir si una disnea es por sobrecarga.

Las cuatro pruebas de doble cara —líneas B, vena cava, PVY ecográfica y BNP— son coherentes consigo mismas dentro del 3%: la sensibilidad y la especificidad que declaran predicen sus propios cocientes. Es una comprobación que se hizo, no una fuente de datos.

Con las cifras corregidas, la ecografía a pie de cama (líneas B 4.0, vena cava 3.9, PVY 2.9) rinde por encima de la exploración física salvo por la ingurgitación yugular (4.1), que sigue siendo el mejor hallazgo de la mano.

## Aspectos pendientes de documentación

La discrepancia de unidad del BNP —100 ng/mL en la fuente frente a los 100 pg/mL habituales en la literatura— no se puede resolver sin el texto completo. Está declarada en péptido natriurético cerebral elevado y en la arista, y no se reconcilia aquí.

El intervalo de los crepitantes, 0.7-4.5 sobre un valor puntual de 2.7, es marcadamente asimétrico en escala logarítmica y cruza el 1. Es el valor corregido y así se transcribe, pero conviene confirmarlo contra el texto completo antes de que ningún consumidor lo trate como definitivo.

## Conclusión de la fuente

Un BNP de 100 ng/mL o más y la presencia de congestión vascular en la radiografía de tórax pueden ser las pruebas más útiles para identificar a los pacientes con sobrecarga de volumen. La ausencia de líneas B pulmonares en la ecografía a pie de cama, o un BNP menor de 100 ng/mL, pueden ser lo más útil para excluirla.

## Referencias y procedencia

**pmid:41729549:** Does This Patient Have Volume Overload?: The Rational Clinical Examination. JAMA, 2026. DOI: 10.1001/jama.2026.0446.

**pmid:22392031:** International evidence-based recommendations for point-of-care lung ultrasound. Intensive Care Med, 2012. DOI: 10.1007/s00134-012-2513-4.

Fuente clínica: medsemiotics-db, condición HM:6037.
