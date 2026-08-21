---
id: "HM6008-01"
slug: "hipovolemia-aguda-signos-vitales-posturales"
title: "Evaluación clínica de la hipovolemia: ¿Cuándo sirven los signos posturales?"
subtitle: "Diferenciación semiótica entre hemorragia aguda y deshidratación digestiva según el Rational Clinical Examination."
date: "2026-08-21"
author: "Dr. Alcy Torres"
category: "medicina_y_datos"
category_label: "Medicina y Datos"
tags: ["urgencias", "hemodinamia", "hipovolemia", "semiologia"]
reading_time: "6 min"
difficulty: "Intermedio"
grounding:
  condicion_id: "HM:6008"
  condicion_nombre: "Hipovolemia aguda"
  concepto_id: "HM:3019"
  concepto_nombre: "Mareo postural intenso e hipotensión ortostática"
  sensibilidad: 0.97
  especificidad: 0.98
  lr_positivo: 48.5
  lr_negativo: 0.03
  poblacion: "Adultos con sospecha de pérdida sanguínea aguda grave (>600 mL)"
  referencia_id: "pmid:10086438"
  referencia_cita: "McGee S, Abernethy WB 3rd, Simel DL. The rational clinical examination. Is this patient hypovolemic? JAMA. 1999;281(11):1022-9."
  doi: "10.1001/jama.281.11.1022"
  pmid: "10086438"

triada:
  significante: "Incapacidad del paciente para permanecer de pie o mareo postural intenso e invalidante asociado a taquicardia ortostática (aumento ≥ 30 lpm) o caída de presión sistólica ≥ 20 mmHg tras 2 minutos en bipedestación."
  significado: "Reducción crítica del volumen intravascular circulante con compromiso del retorno venoso y fallo de los mecanismos barorreceptores compensatorios."
  decision: "En hemorragia aguda moderada-grave, el mareo postural intenso es el signo de mayor especificidad (98%) y sensibilidad (97%); en pérdidas digestivas subagudas, la sequedad mucosa de lengua y axilas aporta la mayor discriminación."

autoevaluacion:
  - id: "q1"
    pregunta: "En un paciente joven que acude a urgencias tras un episodio de sangrado digestivo alto, la tensión arterial supina es normal (120/80 mmHg). Al ponerse de pie, experimenta mareo postural intenso y la frecuencia cardíaca sube de 75 a 112 lpm (incremento ≥ 30 lpm). Según McGee et al. en JAMA (PMID: 10086438), ¿cuál es el significado clínico de este hallazgo?"
    opciones:
      - texto: "Presenta una pérdida hemática significativa (frecuentemente >600–1000 mL) con una especificidad del 98% a pesar de la presión supina normal."
        correcta: true
        feedback: "¡Correcto! McGee et al. demostraron que el incremento de pulso ≥30 lpm o el mareo postural severo tienen una especificidad del 98% para pérdida sanguínea aguda significativa, superando con creces a la presión supina."
      - texto: "Descarta hipovolemia porque la presión arterial sistólica supina se mantiene en rangos normales."
        correcta: false
        feedback: "Incorrecto. Los mecanismos compensatorios mantienen la presión en decúbito normal hasta fases avanzadas de choque."
      - texto: "Indica un síncope vasovagal psicógeno que no requiere monitorización hemodinámica."
        correcta: false
        feedback: "Incorrecto. En contexto de sangrado evidente, el ortostatismo franco es un signo de alarma hemodinámica."

  - id: "q2"
    pregunta: "En pacientes ancianos con deshidratación por diarrea o vómitos (pérdidas digestivas), ¿cuál de los siguientes signos físicos tiene la MENOR utilidad diagnóstica debido a su alta tasa de falsos positivos en esta población?"
    opciones:
      - texto: "Disminución de la turgencia cutánea (signo del pliegue) en dorso de la mano o antebrazo."
        correcta: true
        feedback: "¡Exacto! En adultos mayores, la pérdida fisiológica de elastina y tejido celular subcutáneo produce pliegue cutáneo positivo en ausencia de hipovolemia. La sequedad de mucosas y axilas es más fiable."
      - texto: "Sequedad de la mucosa yugal y surcos longitudinales de la lengua."
        correcta: false
        feedback: "Incorrecto. La sequedad de la lengua y mucosas tiene mejor rendimiento en el anciano que la turgencia cutánea periférica."
---

## El peligro de subestimar la depleción de volumen

La hipovolemia aguda es una de las emergencias clínicas más engañosas. En pacientes jóvenes y previamente sanos, los mecanismos vasomotores compensatorios (taquicardia y vasoconstricción periférica) pueden sostener una presión arterial supina completamente normal hasta haber perdido más del **20% al 30% del volumen sanguíneo**.

---

## Dos Poblaciones, Dos Enfoques Semióticos

La revisión sistemática de la serie *The Rational Clinical Examination* (JAMA 1999) advierte una regla de oro: **no mezclar las poblaciones**.

### 1. Pérdida Sanguínea Aguda (Hemorragia)
- **Signo cardinal:** Mareo postural severo o incremento del pulso $\ge 30\text{ lpm}$ al ponerse de pie.
- **Rendimiento:** Especificidad del **98%** (IC95% 97–99%) y sensibilidad del **97%** en pérdidas $>1000\text{ mL}$.

### 2. Pérdidas Digestivas Subagudas (Vómitos, Diarrea, Golpe de Calor)
- **Signos cardinales:** Sequedad de mucosas orales, sequedad en la bóveda axilar y ojos hundidos.
- **Precaución:** La turgencia cutánea periférica en ancianos es poco fiable por pérdida senil de elasticidad dérmica.

```
                    [ Sospecha de Hipovolemia Aguda ]
                                   │
              ┌────────────────────┴────────────────────┐
              ▼                                         ▼
     Pérdida Hemática Aguda                   Pérdidas Digestivas
   (Sangrado digestivo / trauma)              (Diarrea / vómitos)
              │                                         │
    Evaluar Ortostatismo                      Evaluar Mucosas y Axilas
   (ΔFC ≥ 30 lpm o mareo severo)             (Lengua seca, axila seca)
   Especificidad 98% en pérdidas >600 mL     Mejor discriminación en geriatría
```

---

## Evidencia Cuantitativa y Fuentes

Parámetros diagnósticos validados en la literatura médica (serie *The Rational Clinical Examination*, JAMA):

- **Sensibilidad en pérdida sanguínea grande (>1000 mL):** 0.97 (97%)
- **Especificidad del mareo postural severo / ΔFC ≥ 30 lpm:** 0.98 (98%)
- **Cociente de Verosimilitud Positivo derivado:** ~48.5 [McGee et al., JAMA 1999]
- **Cociente de Verosimilitud Negativo en grandes pérdidas:** ~0.03 [McGee et al., JAMA 1999]
- **Población evaluada:** Adultos con pérdidas sanguíneas cuantificadas y pacientes con depleción hídrica en urgencias.

---

## Conclusión Semiótica

Nunca confíes en una **tensión arterial supina normal**. El examen de signos vitales posturales es el detector precoz más sensible y específico de hemorragia aguda en el paciente consciente.
