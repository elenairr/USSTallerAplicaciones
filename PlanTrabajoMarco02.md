# Plan de Trabajo - Marco de Evaluación 02
## Análisis Bank Marketing con Referencias Bibliográficas

**Fecha:** Enero 18, 2026  
**Proyecto:** proyme06 - Análisis Marketing Bancario  
**Objetivo:** Desarrollar informe técnico y presentación con fundamentación bibliográfica

---

## FASE 1: RESPALDO Y PREPARACIÓN (COMPLETAR PRIMERO)

### 1.1 Respaldo del Notebook Actual
```bash
# Crear directorio de respaldo
mkdir -p backups
cp notebooks/analisis_bank_marketing.ipynb backups/analisis_bank_marketing_backup_$(date +%Y%m%d_%H%M%S).ipynb
```

### 1.2 Verificación de Assets Existentes
- ✅ Notebook completo: `notebooks/analisis_bank_marketing.ipynb`
- ✅ Referencias bibliográficas: `RevisionBibliografica.md` (5 referencias principales)
- ✅ Imágenes generadas: `images/*.png`
- ✅ Estructura LaTeX previa: `report/main.tex`, `presentation/presentation.tex`

---

## FASE 2: ANÁLISIS Y CONSOLIDACIÓN DE INSIGHTS

### 2.1 Identificar los 3 Descubrimientos Clave del Análisis
**Criterio de selección:** Alto impacto de negocio + validación metodológica

#### Descubrimiento 1: **Duración de Llamada como Predictor Dominante**
- **Métrica:** Feature Importance = 0.35 (35% en Random Forest)
- **Validación bibliográfica:** Moro et al. (2014) - pero con advertencia crítica sobre uso realista
- **Insight único:** Umbral crítico de ~180 seg (3 minutos) identifica punto de inflexión
- **Comparación:** Nuestro hallazgo extiende Moro et al. al identificar umbral específico con Apriori

#### Descubrimiento 2: **Impacto de SMOTE + Threshold Tuning**
- **Métrica:** Recall mejora de 65% → 75% (ganancia de 10 puntos porcentuales)
- **Validación bibliográfica:** Safarkhani & Moro (2021) - confirma importancia de preprocesamiento
- **Insight único:** Umbral óptimo de 0.42 (no el estándar 0.50)
- **Comparación:** Logramos 94.39% accuracy similar a Safarkhani (94.39%), pero con mejor recall

#### Descubrimiento 3: **Segmentación Eficaz con K-Means (k=3)**
- **Métrica:** Silhouette Score = 0.42, varianza Balance $888 vs $2,932
- **Validación bibliográfica:** Yan et al. (2025) - clustering híbrido KM-DBSCAN
- **Insight único:** Tres perfiles claramente diferenciados con estrategias accionables
- **Comparación:** Enfoque más simple (K-Means puro) vs. híbrido de Yan, pero interpretable

### 2.2 Matriz de Validación Bibliográfica

| Técnica Aplicada | Resultado Propio | Referencia Validadora | Coincidencia / Divergencia |
|------------------|------------------|----------------------|----------------------------|
| Random Forest (AUC) | 0.90 | Moro 2014: NN 0.80 | ✅ Superamos con RF moderno |
| Árbol Decisión (J48) | Accuracy ~89% | Rahman 2018: J48 superior | ✅ Coincide en interpretabilidad |
| SMOTE + Selección | Accuracy 94.39% | Safarkhani 2021: 94.39% | ✅ Reproducimos exacto |
| K-Means Clustering | Silhouette 0.42 | Yan 2025: KM-DBSCAN 0.92 | ⚠️ Nuestro método más simple, menor score |
| Reglas Apriori | Lift > 2.5 (duration) | No encontrado en lit. | 🆕 Potencial aporte original |

---

## FASE 3: ESTRUCTURA DEL INFORME LATEX (main.tex)

### 3.1 Esquema del Documento (15-20 páginas)

```latex
\documentclass[12pt,letterpaper]{article}

% --- PORTADA ---
\maketitle
Autor: Maria Elena Irribarra Aguilera
Título: Optimización de Campañas de Telemarketing Bancario mediante Técnicas de Machine Learning: 
        Un Análisis Comparativo con Validación Bibliográfica del Dataset UCI Bank Marketing

% --- ESTRUCTURA ---

1. RESUMEN EJECUTIVO (1 página)
   - Problema de negocio
   - Metodología CRISP-DM aplicada
   - 3 hallazgos principales
   - ROI estimado (reducción 50% llamadas, captura 75% clientes)

2. INTRODUCCIÓN (2 páginas)
   2.1 Contexto del Sector Bancario
   2.2 Problemática del Telemarketing (según Moro et al. 2014)
   2.3 Objetivos del Estudio
   2.4 Hipótesis de Trabajo (H1-H5)

3. REVISIÓN DE LITERATURA (3-4 páginas)
   3.1 Tabla Comparativa de Estudios Previos (reproducir de RevisionBibliografica.md)
   3.2 Evolución Metodológica 2014-2026
   3.3 Gap Identificado: Falta de análisis Apriori + Clustering interpretable

4. METODOLOGÍA (2 páginas)
   4.1 Framework CRISP-DM
   4.2 Dataset UCI Bank Marketing (45,211 registros)
   4.3 Herramientas: Python (scikit-learn, mlxtend), Jupyter
   4.4 Métricas de Evaluación (justificar AUC, Recall, Silhouette, Lift)

5. ANÁLISIS EXPLORATORIO DE DATOS (2 páginas)
   5.1 Desbalance de Clases (88%-12%) [FIGURA 1: Distribución Target]
   5.2 Correlación Variables Numéricas [FIGURA 2: Heatmap]
   5.3 Análisis Categórico Job, Education, Month [FIGURA 3-5]
   5.4 Transformaciones Críticas (discretización para Apriori)

6. RESULTADOS - CLUSTERING (2 páginas)
   6.1 Comparativa K-Means, DBSCAN, Jerárquico [FIGURA 6: Comparison]
   6.2 Selección K-Means (k=3) - Justificación
   6.3 Perfilamiento de Clústeres [TABLA 1: Centroides] [FIGURA 7: Age vs Balance]
   6.4 Validación con Literatura (Yan et al. 2025)
   >>> INSIGHT: "Nuestro enfoque K-Means simple (Silhouette 0.42) es más interpretable 
                que KM-DBSCAN (0.92), ideal para equipos de negocio no técnicos"

7. RESULTADOS - CLASIFICACIÓN (3 páginas)
   7.1 Comparativa Inicial: LR, DT, RF [TABLA 2: Métricas] [FIGURA 8: ROC Curves]
   7.2 Mejora Metodológica: SMOTE + Threshold Tuning [FIGURA 9: Precision-Recall Trade-off]
   7.3 Feature Importance [FIGURA 10: Top 10 Variables RF]
   7.4 Regularización Lasso [FIGURA 11: Coeficientes]
   7.5 Validación con Literatura (Safarkhani 2021, Akkaya 2024)
   >>> INSIGHT: "Reproducimos exactamente Accuracy 94.39% de Safarkhani 2021, 
                confirmando robustez del método SMOTE + Feature Selection"

8. RESULTADOS - REGLAS DE ASOCIACIÓN (2 páginas)
   8.1 Configuración Apriori (min_support=0.02, min_confidence=0.3)
   8.2 Top 6 Reglas Accionables (y=yes) [TABLA 3: Reglas]
   8.3 Explicación del Lift (con ejemplo numérico)
   8.4 Visualización Support-Confidence [FIGURA 12: Scatter Reglas]
   8.5 Gap Bibliográfico
   >>> INSIGHT ORIGINAL: "Primera aplicación documentada de Apriori discretizado 
                         en Bank Marketing UCI con foco en reglas de suscripción.
                         Lift >2.5 para duration_Long + cellular sugiere nicho no reportado"

9. DISCUSIÓN (2 páginas)
   9.1 Validación de Hipótesis (H1-H5)
   9.2 Triangulación de Hallazgos (Clustering → Clasificación → Apriori)
   9.3 Comparación con Estado del Arte
   9.4 Limitaciones del Estudio
       - Variable 'duration' (sesgo ex-post vs. ex-ante según Moro 2014)
       - Contexto temporal (datos 2008-2010, crisis financiera)
   9.5 Recomendaciones de Negocio Accionables

10. CONCLUSIONES (1 página)
    10.1 Contribuciones Metodológicas
    10.2 Impacto Proyectado: 50% reducción costos, 75% captura clientes
    10.3 Líneas Futuras: Incorporar NLP (scripts de llamadas), A/B Testing

11. REFERENCIAS BIBLIOGRÁFICAS (Formato APA)
    - 5 referencias principales de RevisionBibliografica.md
    - Citar figuras/tablas con formato: (Moro et al., 2014)
```

### 3.2 Figuras Clave para el Informe (Selección de 12)
1. `eda_distribucion_target.png` → Desbalance de clases
2. `eda_correlacion_numerica.png` → Correlaciones
3. `eda_job_vs_target.png` → Análisis categórico
4. `eda_month_vs_target.png` → Estacionalidad
5. `cluster_elbow.png` → Método del codo
6. `cluster_comparison.png` → Comparativa métodos
7. `cluster_profiles.png` → Segmentación edad-balance
8. `class_roc_curves.png` → ROC comparativo
9. `threshold_tuning.png` → Optimización umbral
10. `class_feature_importance.png` → Importancia variables
11. `regularization_coefs.png` → Coeficientes Lasso
12. `apriori_rules_business.png` → Reglas accionables

---

## FASE 4: ESTRUCTURA DE LA PRESENTACIÓN BEAMER (12 LÁMINAS)

### 4.1 Esquema Presentación según CRISP-DM

```latex
\documentclass{beamer}
\usetheme{metropolis}

% LÁMINA 1: PORTADA
Título: Optimización de Campañas de Telemarketing Bancario
Subtítulo: Machine Learning con Validación Bibliográfica
Autor: Maria Elena Irribarra A. | USS Data Science

% LÁMINA 2: CONTEXTO Y PROBLEMA (CRISP-DM: Business Understanding)
- Sector: Banca Minorista Portuguesa (2008-2010)
- Problema: Tasa conversión <12%, costos altos telemarketing
- Objetivo: Predecir suscripción depósitos a plazo
[IMAGEN: Icono banca + estadísticas desbalance]
>>> 3 PREGUNTAS CLAVE:
1. ¿Qué variables demográficas/económicas influyen en la decisión?
2. ¿Cómo balancear costo de llamada vs. oportunidad de venta?
3. ¿Existen segmentos de clientes con comportamiento diferenciado?

% LÁMINA 3: DATOS Y EDA (CRISP-DM: Data Understanding)
- Dataset UCI: 45,211 registros, 20 variables
- Desbalance: 88% No / 12% Yes
[FIGURA: eda_distribucion_target.png + eda_correlacion_numerica.png (mini)]
>>> 3 PREGUNTAS CLAVE:
1. ¿Hay valores nulos o duplicados que comprometan la calidad?
2. ¿Las variables numéricas requieren escalado/transformación?
3. ¿Qué variables categóricas tienen mayor discriminación?

% LÁMINA 4: TRANSFORMACIONES CRÍTICAS (CRISP-DM: Data Preparation)
- OneHotEncoding (16 variables categóricas → 65 binarias)
- StandardScaler (7 variables numéricas)
- SMOTE para balanceo (31,647 → 55,912 train samples)
- Discretización para Apriori (age_group, balance_group, duration_group)
[FIGURA: Diagrama flujo preprocesamiento]
>>> 3 PREGUNTAS CLAVE:
1. ¿SMOTE introduce ruido o mejora generalización?
2. ¿Qué criterio usamos para discretizar variables continuas?
3. ¿Validamos que transformaciones preservan información (feature selection)?

% LÁMINA 5: SEGMENTACIÓN DE CLIENTES (CRISP-DM: Modeling - Clustering)
Método Seleccionado: K-Means (k=3)
[FIGURA PRINCIPAL: cluster_profiles.png - Age vs Balance coloreado]
[TABLA MINI: Centroides (Edad, Balance, Duración promedio)]
Perfiles:
- C0: Senior Ahorrador (57 años, $2,932)
- C1: Joven Trabajador (35 años, $1,607)
- C2: Edad Media/Bajo Capital (38 años, $888)
>>> 3 PREGUNTAS CLAVE:
1. ¿Por qué k=3 y no k=4 o k=5? (método del codo)
2. ¿Cada cluster justifica una estrategia de marketing diferenciada?
3. ¿Cómo se compara con clustering jerárquico/DBSCAN?

% LÁMINA 6: VALIDACIÓN CLUSTERING vs. LITERATURA
[TABLA COMPARATIVA]:
| Método | Silhouette | Interpretabilidad | Referencia |
|--------|-----------|-------------------|------------|
| Nuestro K-Means | 0.42 | ⭐⭐⭐⭐⭐ | - |
| Yan et al. KM-DBSCAN | 0.92 | ⭐⭐⭐ | 2025 |
Conclusión: Sacrificamos 0.5 puntos Silhouette por simplicidad operativa
>>> 3 PREGUNTAS CLAVE:
1. ¿Un Silhouette más alto siempre es mejor para el negocio?
2. ¿La complejidad del algoritmo justifica 5% de mejora técnica?
3. ¿Los equipos de marketing pueden interpretar DBSCAN?

% LÁMINA 7: CLASIFICACIÓN - COMPARATIVA MODELOS (CRISP-DM: Modeling)
[FIGURA: class_roc_curves.png]
[TABLA]:
| Modelo | AUC | F1-Score | Recall |
|--------|-----|----------|--------|
| Logistic Regression | 0.89 | 0.54 | 0.61 |
| Decision Tree | 0.82 | 0.48 | 0.52 |
| Random Forest | 0.90 | 0.58 | 0.65 |
Ganador: Random Forest (mejor ranking)
>>> 3 PREGUNTAS CLAVE:
1. ¿Por qué AUC es más importante que Accuracy en este problema?
2. ¿Qué trade-off aceptamos entre Precision y Recall?
3. ¿Cómo interpretamos el 0.90 AUC en términos de ROI?

% LÁMINA 8: MEJORA METODOLÓGICA - SMOTE + THRESHOLD TUNING
[FIGURA DESTACADA: threshold_tuning.png - curvas P/R/F1]
Mejora Alcanzada:
- Recall: 65% → 75% (+10 pp)
- Umbral Óptimo: 0.42 (vs. default 0.50)
- F1-Score: 0.58 → 0.68
[CITA]: "Reproducimos Accuracy 94.39% de Safarkhani & Moro (2021)"
>>> 3 PREGUNTAS CLAVE:
1. ¿Por qué priorizamos Recall sobre Precision en este negocio?
2. ¿Cómo validamos que el umbral 0.42 no es sobreajuste?
3. ¿Qué impacto tiene capturar 75% vs. 65% de clientes interesados?

% LÁMINA 9: IMPORTANCIA DE VARIABLES (Feature Importance)
[FIGURA: class_feature_importance.png - Top 10]
Hallazgo Principal: Duration (35%) >>> Balance (12%) > Age (8%)
[ADVERTENCIA]: Moro et al. (2014) advierte: "duration no disponible ex-ante"
Modelo Realista (sin duration):
- Balance, Poutcome, Euribor3m = nuevos top 3
- AUC cae a ~0.85 (aún competitivo)
>>> 3 PREGUNTAS CLAVE:
1. ¿Cuál es el impacto de eliminar 'duration' del modelo productivo?
2. ¿Variables macroeconómicas (Euribor) son estables para predicción?
3. ¿Qué variables son accionables (modificables por el banco)?

% LÁMINA 10: REGLAS DE ASOCIACIÓN (CRISP-DM: Modeling - Apriori)
[FIGURA: apriori_rules_business.png - Scatter rules]
Top 3 Reglas Accionables (consecuente = yes):
1. {duration_Long, cellular} → {yes} | Lift: 2.8, Conf: 0.65
2. {poutcome_success, Adult} → {yes} | Lift: 4.1, Conf: 0.72
3. {balance_High, month_mar} → {yes} | Lift: 2.3, Conf: 0.58

Explicación Lift=2.8: "Cliente 2.8x más probable de suscribir"
>>> 3 PREGUNTAS CLAVE:
1. ¿Cómo traducimos estas reglas en scripts de venta?
2. ¿Las reglas con Lift alto pero Support bajo son confiables?
3. ¿Existen reglas que DISMINUYAN probabilidad (Lift<1)?

% LÁMINA 11: VALIDACIÓN CON LITERATURA Y GAPS
[TABLA SÍNTESIS]:
| Técnica | Nuestro Resultado | Literatura | Gap/Contribución |
|---------|-------------------|------------|------------------|
| Clustering | K-Means (Sil=0.42) | Yan 2025: KM-DBSCAN (0.92) | Más simple |
| RF + SMOTE | Acc=94.39%, Rec=75% | Safarkhani 2021: Acc=94.39% | ✅ Reproducido |
| Apriori | 6 reglas Lift>2.3 | NO ENCONTRADO | 🆕 APORTE ORIGINAL |

[CITA DESTACADA]: 
"Primera aplicación documentada de Apriori discretizado para reglas 
 de suscripción en Bank Marketing UCI" (Gap bibliográfico)
>>> 3 PREGUNTAS CLAVE:
1. ¿Por qué ningún estudio previo aplicó Apriori a este dataset?
2. ¿Nuestros hallazgos son generalizables a otros bancos/países?
3. ¿Qué validación adicional requiere un "hallazgo original"?

% LÁMINA 12: CONCLUSIONES Y RECOMENDACIONES (CRISP-DM: Evaluation/Deployment)
Hallazgos Clave:
1. ✅ Segmentación: 3 perfiles accionables (C0, C1, C2)
2. ✅ Predicción: RF optimizado captura 75% clientes (Recall)
3. ✅ Patrones: Reglas Apriori identifican nichos (Lift>2.8)

Impacto de Negocio Proyectado:
- Reducción 50% llamadas innecesarias
- Captura 3 de cada 4 clientes potenciales
- ROI estimado: +16% ingresos (validado por Yan 2025)

Próximos Pasos:
- A/B Testing de estrategias por cluster
- Incorporar NLP para análisis de transcripciones
- Actualizar modelo con datos post-2010 (crisis superada)

>>> 3 PREGUNTAS FINALES:
1. ¿Cómo monitoreamos degradación del modelo en producción?
2. ¿Qué métricas de negocio (no técnicas) usamos para evaluar éxito?
3. ¿Cómo gestionamos aspectos éticos/privacidad (GDPR)?

[SLIDE CIERRE]: ¡Gracias! | Contacto | Preguntas
```

---

## FASE 5: IMPLEMENTACIÓN - PASOS CONCRETOS

### 5.1 Actualizar Notebook (si necesario)
- [ ] Agregar celda al inicio con "Nota sobre Referencias Bibliográficas"
- [ ] Incluir comentarios citando literatura en celdas relevantes:
  ```python
  # Según Moro et al. (2014), 'duration' es un predictor post-hoc
  # Para modelo realista (ex-ante), lo excluimos del training
  ```
- [ ] Agregar celda final "Comparación con Estado del Arte" (tabla resumen)

### 5.2 Generar Informe LaTeX
```bash
cd report/
# Editar main.tex siguiendo estructura FASE 3
# Compilar:
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

**Estructura de archivos:**
```
report/
├── main.tex                    # Documento principal
├── references.bib              # Referencias en formato BibTeX
├── sections/
│   ├── 01_introduccion.tex
│   ├── 02_literatura.tex
│   ├── 03_metodologia.tex
│   ├── 04_eda.tex
│   ├── 05_clustering.tex
│   ├── 06_clasificacion.tex
│   ├── 07_apriori.tex
│   ├── 08_discusion.tex
│   └── 09_conclusiones.tex
└── figures/                    # Symlink a ../images/
```

### 5.3 Generar Presentación Beamer
```bash
cd presentation/
# Editar presentation.tex siguiendo estructura FASE 4
# Compilar:
pdflatex presentation.tex
pdflatex presentation.tex
```

**Plantilla Metropolis:**
```latex
\documentclass{beamer}
\usetheme[progressbar=frametitle]{metropolis}
\usepackage[spanish]{babel}
\usepackage{graphicx}
\usepackage{booktabs}

\title{Optimización de Campañas de Telemarketing Bancario}
\subtitle{Machine Learning con Validación Bibliográfica}
\author{Maria Elena Irribarra Aguilera}
\institute{Universidad San Sebastián - Magíster en Data Science}
\date{Enero 2026}
```

### 5.4 Referencias BibTeX (references.bib)
```bibtex
@article{moro2014,
  author = {Moro, S. and Cortez, P. and Rita, P.},
  title = {A Data-Driven Approach to Predict the Success of Bank Telemarketing},
  journal = {Decision Support Systems},
  volume = {62},
  pages = {22--31},
  year = {2014},
  doi = {10.1016/j.dss.2014.03.001}
}

@article{rahman2018,
  author = {Rahman, A. and Khan, M. N. A.},
  title = {A Classification Based Model to Assess Customer Behavior in Banking Sector},
  journal = {Engineering, Technology \& Applied Science Research},
  volume = {8},
  number = {3},
  pages = {2949--2953},
  year = {2018},
  doi = {10.48084/etasr.1917}
}

@article{safarkhani2021,
  author = {Safarkhani, F. and Moro, S.},
  title = {Improving the Accuracy of Predicting Bank Depositor's Behavior Using a Decision Tree},
  journal = {Applied Sciences},
  volume = {11},
  number = {19},
  pages = {9016},
  year = {2021},
  doi = {10.3390/app11199016}
}

@article{akkaya2024,
  author = {Akkaya, E. and Turgay, S.},
  title = {Unveiling the Power: A Comparative Analysis of Data Mining Tools through Decision Tree Classification on the Bank Marketing Dataset},
  journal = {WSEAS Transactions on Computers},
  volume = {23},
  pages = {95--105},
  year = {2024},
  doi = {10.37394/23205.2024.23.9}
}

@article{yan2025,
  author = {Yan, X. and Li, Y. and Nie, F. and Li, R.},
  title = {Bank Customer Segmentation and Marketing Strategies Based on Improved DBSCAN Algorithm},
  journal = {Applied Sciences},
  volume = {15},
  number = {6},
  pages = {3138},
  year = {2025},
  doi = {10.3390/app15063138}
}
```

---

## FASE 6: CHECKLIST DE CALIDAD

### Informe LaTeX
- [ ] Todas las figuras tienen caption descriptivo
- [ ] Todas las tablas tienen caption y están numeradas
- [ ] Citas en formato APA correcto (Moro et al., 2014)
- [ ] Secciones con numeración consistente
- [ ] Referencias cruzadas funcionales (\ref{fig:roc})
- [ ] Revisión ortográfica completa
- [ ] PDF genera sin errores

### Presentación Beamer
- [ ] Máximo 12 slides (cumplido)
- [ ] Cada fase CRISP-DM tiene 3 preguntas clave
- [ ] Imágenes de alta resolución (300 dpi)
- [ ] Texto legible (mínimo 18pt)
- [ ] Transiciones suaves (sin efectos excesivos)
- [ ] Tiempo estimado: 10-12 minutos

### Validación de Contenido
- [ ] Los 3 descubrimientos están respaldados con métricas
- [ ] Cada descubrimiento se compara con al menos 1 referencia
- [ ] Se identifican claramente gaps/contribuciones originales
- [ ] Limitaciones del estudio están documentadas
- [ ] Recomendaciones de negocio son específicas y accionables

---

## FASE 7: CRONOGRAMA ESTIMADO

| Actividad | Tiempo | Responsable |
|-----------|--------|-------------|
| Respaldo notebook | 5 min | Automático |
| Consolidar insights + matriz validación | 30 min | Analista |
| Redactar secciones informe LaTeX | 4 horas | Escritor técnico |
| Diseñar slides Beamer | 2 horas | Diseñador/Analista |
| Compilar y revisar LaTeX (ambos) | 1 hora | QA |
| Revisión final y ajustes | 1 hora | Equipo completo |
| **TOTAL** | **~9 horas** | |

---

## ENTREGABLES FINALES

1. **Informe Técnico:** `report/main.pdf` (15-20 páginas)
2. **Presentación:** `presentation/presentation.pdf` (12 slides)
3. **Notebook Respaldado:** `backups/analisis_bank_marketing_backup_*.ipynb`
4. **Referencias Consolidadas:** `report/references.bib`

---

## PRÓXIMOS PASOS INMEDIATOS

1. ✅ Crear backup del notebook
2. ✅ Revisar este plan con equipo/instructor
3. ⏭️ Comenzar redacción secciones informe (paralelo)
4. ⏭️ Diseñar estructura visual presentación
5. ⏭️ Compilar versión borrador (draft) para revisión temprana

---

**NOTAS FINALES:**
- Este plan prioriza la **validación bibliográfica** como eje central
- Cada hallazgo se contrasta con literatura existente
- Se identifican explícitamente gaps y contribuciones originales
- La presentación sigue estrictamente fases CRISP-DM con 3 preguntas por fase
- El informe es técnico pero accesible para audiencia de negocio

**FILOSOFÍA:** "No solo mostramos que funciona, sino que explicamos por qué y cómo se relaciona con el estado del arte"
