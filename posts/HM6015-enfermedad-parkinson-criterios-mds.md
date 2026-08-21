---
id: "HM6015-01"
slug: "enfermedad-parkinson-criterios-clinicos-mds"
title: "Diagnóstico clínico de la Enfermedad de Parkinson: El rigor de los Criterios MDS"
subtitle: "Del parkinsonismo motor nuclear a la búsqueda sistemática de banderas rojas y criterios de apoyo."
date: "2026-08-21"
author: "Dr. Alcy Torres"
category: "neurologia"
category_label: "Neurología"
tags: ["neurologia", "parkinson", "semiologia", "movimientos-anormales"]
reading_time: "7 min"
difficulty: "Avanzado"
grounding:
  condicion_id: "HM:6015"
  condicion_nombre: "Enfermedad de Parkinson"
  concepto_id: "HM:3061"
  concepto_nombre: "Bradicinesia con decremento progresivo"
  sensibilidad: 0.90
  especificidad: 0.88
  lr_positivo: 7.5
  lr_negativo: 0.11
  poblacion: "Adultos con sospecha de trastorno del movimiento parkinsoniano"
  referencia_id: "pmid:26474316"
  referencia_cita: "Postuma RB, Berg D, Stern M, Poewe W, Olanow CW, Peng W, et al. MDS clinical diagnostic criteria for Parkinson's disease. Mov Disord. 2015;30(12):1591-601."
  doi: "10.1002/mds.26424"
  pmid: "26474316"

triada:
  significante: "Bradicinesia caracterizada por lentitud de movimiento combinada con decremento progresivo en velocidad y amplitud durante maniobras repetitivas (finger tapping), asociada a temblor de reposo de 4-6 Hz o rigidez en rueda dentada."
  significado: "Degeneración progresiva de las neuronas dopaminérgicas de la sustancia negra pars compacta con disfunción de los circuitos corticoestriatales."
  decision: "El diagnóstico requiere constatar el núcleo motor, ausencia de criterios de exclusión absoluta, y un balance favorable entre banderas rojas y criterios de apoyo (excelente respuesta a L-dopa o discinesias inducidas)."

autoevaluacion:
  - id: "q1"
    pregunta: "Según los criterios diagnósticos clínicos oficiales de la MDS 2015 (PMID: 26474316), ¿cuál es el signo semiológico OBLIGATORIO que debe estar presente de forma ineludible para definir parkinsonismo motor?"
    opciones:
      - texto: "Bradicinesia (lentitud motora con decremento progresivo en amplitud o velocidad durante movimientos repetitivos)."
        correcta: true
        feedback: "¡Correcto! La MDS establece la bradicinesia como el rasgo nuclear indispensable, que debe coexistir con temblor de reposo O rigidez muscular."
      - texto: "Temblor postural bilateral simétrico en miembros superiores."
        correcta: false
        feedback: "Incorrecto. El temblor postural aislado orienta más a Temblor Esencial y no constituye el núcleo obligatorio."
      - texto: "Inestabilidad postural con caídas frecuentes durante el primer año."
        correcta: false
        feedback: "Incorrecto. Las caídas precoces en el primer año son una 'bandera roja' que sugiere Parálisis Supranuclear Progresiva (PSP), no Enfermedad de Parkinson típica."

  - id: "q2"
    pregunta: "¿Cuál de los siguientes hallazgos se considera un CRITERIO DE EXCLUSIÓN ABSOLUTA para Enfermedad de Parkinson idiopática?"
    opciones:
      - texto: "Tratamiento activo con antagonistas dopaminérgicos (antipsicóticos o antieméticos tipo metoclopramida) que justifique parkinsonismo farmacológico inducido."
        correcta: true
        feedback: "¡Exacto! El bloqueo dopaminérgico farmacológico es una causa secundaria que excluye formalmente la enfermedad idiopática."
      - texto: "Excelente respuesta motora y funcional al tratamiento con levodopa."
        correcta: false
        feedback: "Incorrecto. La respuesta marcada a levodopa es el criterio de apoyo positivo más potente de la enfermedad."
      - texto: "Presencia de asimetría motora al inicio del cuadro clínico."
        correcta: false
        feedback: "Incorrecto. El inicio unilateral o asimétrico es característico de la Enfermedad de Parkinson."
---

## El desafío del diagnóstico clínico en la Enfermedad de Parkinson

A diferencia de otras entidades neurológicas con biomarcadores séricos definitivos, el diagnóstico de la **Enfermedad de Parkinson (EP)** continúa descansando primordialmente en la exploración física meticulosa y el seguimiento longitudinal.

En 2015, la *International Parkinson and Movement Disorder Society (MDS)* publicó los criterios clínicos contemporáneos para maximizar la precisión diagnóstica frente a parkinsonismos atípicos (PSP, AMS, DCB).

---

## Estructura Diagnóstica en 3 Pasos (MDS)

1. **Paso 1: Definir Parkinsonismo Motor (Núcleo Ineludible):**
   - **Bradicinesia obligatoria** (disminución de velocidad y amplitud en maniobras como *finger tapping*, apertura/cierre de mano o golpeteo de talón).
   - Más al menos uno de los siguientes:
     - **Temblor de reposo** (4 a 6 Hz, tildado a menudo como "cuenta de monedas").
     - **Rigidez muscular** (fenómeno de rueda dentada).

2. **Paso 2: Evaluar Criterios de Exclusión Absoluta:**
   - Signos cerebelosos francos, parálisis de la mirada vertical supranuclear, demencia frontotemporal precoz, o parkinsonismo farmacológico.

3. **Paso 3: Balance de Banderas Rojas vs. Criterios de Apoyo:**
   - **Banderas Rojas (*Red Flags*):** Caídas tempranas (<3 años), disautonomía severa precoz, progresión motora acelerada con silla de ruedas temprana.
   - **Criterios de Apoyo:** Respuesta dramática a levodopa, discinesias inducidas por L-dopa, hiposmia documentada, alucinaciones visuales no psicóticas.

```
                   [ Sospecha de Trastorno del Movimiento ]
                                      │
                                      ▼
                      ¿Cumple Núcleo Motor MDS?
                      (Bradicinesia + Temblor/Rigidez)
                                      │
                      ┌───────────────┴───────────────┐
                      ▼                               ▼
                     NO                              SÍ
             (No es parkinsonismo)                    │
                                                      ▼
                                       ¿Criterios de Exclusión Absoluta?
                                                      │
                                      ┌───────────────┴───────────────┐
                                      ▼                               ▼
                                     SÍ                              NO
                             (Causa secundaria /                      │
                              Parkinsonismo plus)                     ▼
                                                       Evaluar Balance:
                                                       Criterios de Apoyo vs Red Flags
                                                       (EP Establecida vs EP Probable)
```

---

## Evidencia Cuantitativa y Fuentes

Parámetros diagnósticos validados en la literatura médica (*Movement Disorder Society*, 2015):

- **Referencia estándar:** Criterios diagnósticos clínicos MDS para Enfermedad de Parkinson.
- **Sensibilidad global de la bradicinesia nuclear:** ~0.90 (90%)
- **Especificidad del núcleo con criterios de apoyo:** ~0.88 - 0.95
- **Fuente validada:** Postuma RB, Berg D, et al. *MDS clinical diagnostic criteria for Parkinson's disease*. Mov Disord. 2015;30(12):1591-601. [PMID: 26474316]

---

## Conclusión Semiótica

La bradicinesia es el **eje cardinal**. Ningún paciente debe diagnosticarse de Parkinson por temblor o rigidez aislados si no se constata la lentitud y el decremento progresivo de amplitud motora.
