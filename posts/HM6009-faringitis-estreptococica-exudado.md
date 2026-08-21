---
id: "HM6009-01"
slug: "faringitis-estreptococica-exudado-criterios-centor"
title: "Faringoamigdalitis aguda: Rendimiento semiótico del exudado y los criterios de Centor"
subtitle: "Por qué ningún hallazgo aislado confirma ni descarta la infección por EbhGA y cómo optimizar el uso racional de antibióticos."
date: "2026-08-21"
author: "Dr. Alcy Torres"
category: "farmacoterapia"
category_label: "Farmacoterapia"
tags: ["infecciosas", "faringitis", "antibioticos", "centor", "urgencias"]
reading_time: "5 min"
difficulty: "Básico"
grounding:
  condicion_id: "HM:6009"
  condicion_nombre: "Faringitis estreptocócica"
  concepto_id: "HM:3026"
  concepto_nombre: "Exudado amigdalino"
  sensibilidad: 0.40
  especificidad: 0.88
  lr_positivo: 3.4
  lr_negativo: 0.68
  poblacion: "Pacientes que consultan por odinofagia y dolor faríngeo agudo"
  referencia_id: "pmid:11147989"
  referencia_cita: "Ebell MH, Smith MA, Barry HC, Ives K, Carey M. Does this patient have strep throat? The Rational Clinical Examination. JAMA. 2000;284(22):2912-8."
  doi: "10.1001/jama.284.22.2912"
  pmid: "11147989"

triada:
  significante: "Placas blanquecinas o confluentes de material pultáceo sobre la superficie de las amígdalas palatinas o la pared faríngea posterior."
  significado: "Respuesta inflamatoria neutrofílica intensa con necrosis superficial y formación de detritos fibrinoleucocitarios."
  decision: "Es el hallazgo físico aislado de mayor rendimiento (LR+ 3.4), pero sigue siendo insuficiente por sí solo: requiere puntuación clínica formal (Centor/McIsaac) o test rápido de antígeno antes de iniciar antibióticos."

autoevaluacion:
  - id: "q1"
    pregunta: "Un paciente de 22 años acude por dolor de garganta y fiebre de 38.5 °C. En la exploración se observa exudado amigdalino blanquecino bilateral, pero no tiene adenopatías ni tos. Con un LR+ de 3.4 para el exudado, ¿cuál es el manejo diagnóstico más adecuado según JAMA (PMID: 11147989)?"
    opciones:
      - texto: "Prescribir amoxicilina de inmediato porque el exudado amigdalino confirma 100% etiología bacteriana."
        correcta: false
        feedback: "Incorrecto. Virus respiratorios (como adenovirus, VEB o enterovirus) también producen exudado amigdalino florido; un LR+ de 3.4 no es confirmatorio por sí solo."
      - texto: "Calcular la puntuación de Centor/McIsaac y realizar test rápido de antígeno estreptocócico (o cultivo) para confirmar antes de prescribir antibiótico."
        correcta: true
        feedback: "¡Correcto! Ebell et al. demuestran que ningún signo individual basta para prescribir antibióticos empíricos; la integración en escalas clínicas o test antigénico rápido evita el sobreuso de antibióticos."
      - texto: "Descartar cualquier etiología estreptocócica y enviar a casa sin más estudios."
        correcta: false
        feedback: "Incorrecto. El paciente tiene criterios de sospecha moderada-alta que ameritan confirmación microbiológica rápida."

  - id: "q2"
    pregunta: "¿Cuál de los siguientes síntomas tiene el Likelihood Ratio NEGATIVO (LR-) más favorable para alejar la sospecha de faringitis por estreptococo del grupo A?"
    opciones:
      - texto: "Presencia franca de tos y rinorrea (LR- ≈ 0.60 a favor de etiología viral)."
        correcta: true
        feedback: "¡Exacto! La presencia de tos, coriza o conjuntivitis orienta fuertemente hacia infección viral de vías respiratorias superiores y reduce la probabilidad de estreptococo."
      - texto: "Presencia de cefalea intensa."
        correcta: false
        feedback: "Incorrecto. La cefalea es inespecífica y frecuente en infecciones tanto virales como bacterianas."
---

## El desafío del dolor faríngeo y el sobreuso de antibióticos

La faringoamigdalitis aguda es una de las causas más frecuentes de prescripción antibiótica inadecuada. Aunque el **Estreptococo $\beta$-hemolítico del Grupo A (EbhGA)** es responsable de solo el 10% al 15% de los casos en adultos, con frecuencia se prescriben antibióticos en más del 60% de las consultas.

---

## Discriminación de Hallazgos Individuales

La síntesis metaanalítica de la serie *The Rational Clinical Examination* (JAMA 2000) analizó la capacidad diagnóstica de los signos cardinales:

- **Exudado amigdalino:** LR+ **3.4** (el signo individual más potente).
- **Exudado faríngeo difuso:** LR+ **2.1**.
- **Adenopatías cervicales anteriores dolorosas:** LR+ **1.8**.
- **Historia de fiebre:** LR+ **1.9**.
- **Ausencia de tos:** LR+ **1.5**.

Ninguno de estos hallazgos alcanza un LR+ > 5 por sí solo. Por tanto, la suma de criterios en la regla de **Centor modificada por McIsaac** es la clave para la toma de decisiones.

```
                    [ Paciente con Odinofagia Aguda ]
                                   │
              ┌────────────────────┴────────────────────┐
              ▼                                         ▼
     Centor 0 - 1 Puntos                       Centor ≥ 3 Puntos
  (Probabilidad baja < 10%)                (Probabilidad moderada ~30-50%)
              │                                         │
    Manejo sintomático.                       Realizar Test Rápido (RADT).
    No indicar antibióticos                   Prescribir antibiótico
    ni pruebas diagnósticas.                  solo si el test es positivo.
```

---

## Evidencia Cuantitativa y Fuentes

Parámetros diagnósticos validados en la literatura médica (serie *The Rational Clinical Examination*, JAMA):

- **Cociente de Verosimilitud Positivo del Exudado Amigdalino (LR+):** 3.40 [Ebell et al., JAMA 2000]
- **Cociente de Verosimilitud Negativo del Exudado Amigdalino (LR-):** 0.68 [Ebell et al., JAMA 2000]
- **Sensibilidad del Exudado Amigdalino:** 0.40 (40%)
- **Especificidad del Exudado Amigdalino:** 0.88 (88%)
- **Población evaluada:** Pacientes que consultan por faringitis aguda en atención primaria y urgencias.

---

## Conclusión Semiótica

El exudado amigdalino **orienta pero no sentencia**. El uso racional de antimicrobianos exige combinar la semiología con pruebas rápidas de antígeno en pacientes con 3 o más criterios de Centor.
