# Plan de Trabajo: Proyecto de Ciencia de Datos - Bank Marketing

Este documento detalla el plan de ejecución para el proyecto de análisis del dataset "Bank Marketing", siguiendo la metodología CRISP-DM y cumpliendo con los requerimientos de la evaluación.

## 1. Estructura del Proyecto

Para mantener el orden y facilitar la generación de entregables, se utilizará la siguiente estructura de directorios:

```
/proyme06
├── data/                # Almacenamiento temporal de datos (si fuera necesario)
├── images/              # Figuras generadas por el notebook (PNG)
├── notebooks/           # Jupyter Notebooks (.ipynb)
├── report/              # Archivos fuente del informe LaTeX
└── presentation/        # Archivos fuente de la presentación Beamer
```

## 2. Planificación del Jupyter Notebook

El desarrollo se realizará en un único notebook (`notebooks/analisis_bank_marketing.ipynb`) estructurado en bloques lógicos.

### Bloque 1: Configuración e Importación
*   **Objetivo**: Preparar el entorno.
*   **Librerías**:
    *   `ucimlrepo`: Para la descarga del dataset.
    *   `pandas`, `numpy`: Manipulación de datos.
    *   `matplotlib`, `seaborn`: Visualización.
    *   `sklearn`: Preprocesamiento, Clustering (KMeans, DBSCAN, Agglomerative), Clasificación (DecisionTree, RandomForest, LogisticRegression), Métricas.
    *   `mlxtend`: **Seleccionada para Apriori** (Scikit-learn no incluye implementación nativa de Apriori).
*   **Acción**: Instalar librerías si faltan, importar módulos y configurar estilos de gráficos.

### Bloque 2: Carga y Entendimiento de Datos (Data Understanding)
*   **Carga**: Utilizar `fetch_ucirepo(id=222)` para obtener features (`X`) y targets (`y`).
*   **Revisión Inicial**: `head()`, `info()`, `describe()`, verificación de nulos y duplicados.
*   **Unión**: Crear un DataFrame unificado para el EDA inicial.

### Bloque 3: Análisis Exploratorio de Datos (EDA)
*   **Variables Numéricas**: Histogramas y Boxplots para detectar outliers y distribución (ej. `age`, `balance`, `duration`).
*   **Variables Categóricas**: Gráficos de barras para frecuencias (ej. `job`, `education`, `y`).
*   **Correlaciones**: Heatmap de correlación para variables numéricas.
*   **Relación con el Target**: Visualizar cómo se comportan las variables clave respecto a la variable objetivo (`y`).
*   **Salida**: Guardar figuras clave en `images/` (ej. `eda_distribucion_target.png`, `eda_correlaciones.png`).

### Bloque 4: Preprocesamiento y Transformación de Datos
*   **Limpieza**: Tratamiento de valores nulos (si existen) y duplicados.
*   **Codificación**:
    *   One-Hot Encoding para variables nominales (para modelos de clasificación/clustering que lo requieran).
    *   Label Encoding para variables ordinales si aplica.
*   **Escalado**: Estandarización (StandardScaler) o Normalización (MinMaxScaler) para algoritmos sensibles a la distancia (K-Means, Regresión Logística).
*   **Discretización (Específico para Apriori)**: Convertir variables numéricas (edad, balance) en rangos categóricos (bins) para poder generar reglas de asociación.

### Bloque 5: Agrupamiento (Clustering)
*   **Selección de Variables**: Justificar qué variables se usarán para agrupar.
*   **Método 1: K-Means**:
    *   Determinar K óptimo usando el método del Codo (Elbow Method) y Coeficiente de Silhouette.
    *   Entrenar modelo.
*   **Método 2: Clustering Jerárquico o DBSCAN**: Implementar para comparar.
*   **Interpretación**: Analizar los centroides o características de cada clúster (perfilamiento).
*   **Salida**: Gráficos de codo, silhouette y scatterplots de clústeres (ej. `cluster_elbow.png`, `cluster_profiles.png`).

### Bloque 6: Clasificación
*   **Preparación**: Split Train/Test (ej. 70/30 o 80/20) estratificado.
*   **Modelos**:
    *   Regresión Logística (con y sin regularización).
    *   Árbol de Decisión (ajustando profundidad).
    *   Random Forest (ensamble).
*   **Evaluación**:
    *   Matriz de Confusión.
    *   Métricas: Accuracy, Precision, Recall, F1-Score (foco en la clase minoritaria si hay desbalance).
    *   Curva ROC y AUC.
*   **Salida**: Gráficos de importancia de variables y matrices de confusión (ej. `class_confusion_matrix.png`, `class_feature_importance.png`).

### Bloque 7: Reglas de Asociación (Apriori)
*   **Preparación**: Usar el dataset con variables discretizadas. Transformar a formato transaccional (One-Hot booleano).
*   **Algoritmo**: Aplicar `apriori` de `mlxtend` para encontrar itemsets frecuentes.
*   **Reglas**: Generar reglas de asociación filtrando por métricas de confianza y soporte.
*   **Análisis**: Seleccionar las 6 mejores reglas, analizar el *Lift* y explicar la relación antecedente-consecuente.
*   **Salida**: Tabla o gráfico de reglas (ej. `apriori_rules_scatter.png`).

## 3. Planificación del Informe (LaTeX)

El informe se redactará en formato carta, estructura académica estándar.

1.  **Introducción**: Contexto del problema (Marketing Bancario), objetivos del estudio.
2.  **Metodología**: Descripción del proceso CRISP-DM, descripción del dataset, herramientas utilizadas.
3.  **Análisis Exploratorio**: Resumen de hallazgos principales del EDA, justificación de transformaciones.
4.  **Resultados de Agrupamiento**: Justificación del número de clústeres, caracterización de los perfiles de clientes encontrados.
5.  **Resultados de Clasificación**: Comparativa de modelos, métricas obtenidas, matriz de confusión del mejor modelo.
6.  **Reglas de Asociación**: Presentación de las 6 reglas principales, interpretación del Lift y utilidad para el negocio.
7.  **Conclusiones**: Resumen de hallazgos, respuesta a las preguntas de negocio, limitaciones y trabajo futuro.

## 4. Planificación de la Presentación (Beamer - Tema Metropolis)

Presentación ejecutiva de máximo 10 láminas.

*   **Lámina 1**: Título, Autor, Fecha.
*   **Lámina 2**: Contexto y Objetivo (Optimizar campañas de marketing).
*   **Lámina 3**: Metodología y Datos (Resumen del dataset y flujo de trabajo).
*   **Lámina 4**: Insights del EDA (Gráfico clave de distribución o correlación).
*   **Lámina 5**: Segmentación de Clientes (Resultados de Clustering, gráfico de perfiles).
*   **Lámina 6**: Predicción de Éxito (Resultados de Clasificación, métricas clave).
*   **Lámina 7**: Reglas de Comportamiento (Apriori, visualización de reglas).
*   **Lámina 8**: Interpretación de Reglas (Explicación de las 6 reglas y su Lift).
*   **Lámina 9**: Conclusiones de Negocio (Recomendaciones basadas en los hallazgos).
*   **Lámina 10**: Cierre y Preguntas.
