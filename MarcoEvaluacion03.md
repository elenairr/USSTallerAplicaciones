Publicación de datos y resultados
Objetivo: Publicación de los datos y de los resultados del trabajo desarrollado en el curso.
Actividades:

1. Realice una presentación de los datos que uso para el Marco Evaluación 02 usando Tableau Public. 
Use al menos 4 controles distintos. Verifique que los datos visualizados cuadran con lo datos ingresados.

2. Realice una visualización de los resultados del clasificador desarrollado Streamlit Cloud. Incluya la posibilidad de que el usuario pruebe el modelo para clasificar un dato ingresado por pantalla. 

3. Prepare para entrega los datos en Excel, la ppt del trabajo previo, el link 
del proyecto usando Tableau Public y el programa usando Streamlit Cloud.

4. La rúbrica más abajo.

Rubrica:

1.- Presentación de Datos en Tableau Public

1.1 Presentación de datos: La presentación de los datos es clara, concisa, estéticamente agradable y revela insights significativos de los datos.

1.2 Uso de al menos 4 controles distintos: Integra fluidamente 4 o más controles distintos que enriquecen 
significativamente la interactividad y el análisis de los datos.

1.3 Verificación de datos (visualizados vs. ingresados): Los datos visualizados son una representación exacta y verificable de los datos ingresados, sin discrepancias. El Excel incluye la verificacion de los 
totales.

2.- Visualización del Clasificador en Streamlit Cloud.

2.1 Visualización de resultados del clasificador trabajo anterior: La visualización de los resultados del 
clasificador es clara, informativa y facilita la comprensión del rendimiento y las predicciones del modelo.

2.2 Interactividad para prueba de modelo por el usuario: La funcionalidad para que el usuario pruebe el modelo con datos nuevos es implementada de forma excelente, intuitiva y funciona sin errores.


---

# Especificación Técnica de Implementación (Plan de Trabajo)

Basado en el análisis de los requerimientos y la rúbrica, se define la siguiente especificación técnica para el cumplimiento del Marco de Evaluación 03.

## 1. Módulo de Datos (Tableau Public)

### 1.1 Fuente de Datos (`data/processed/bank_marketing_tableau.xlsx`)
Se generará un archivo Excel dedicado con dos hojas:
*   **Hoja `Data`**: Contendrá el dataset limpio utilizado en el Marco 02 (previo a OneHotEncoding para facilitar visualización en Tableau).
    *   *Features*: Todas las variables categóricas originales y numéricas.
    *   *Target*: Columna `y` (deposit) clara.
*   **Hoja `Verificacion`**: Tabla de control para auditoría de datos (Rúbrica 1.3).
    *   *Filas*: Conteo total de registros, Suma de `age`, Suma de `balance`, Conteo de `y=yes`, Conteo de `y=no`.
    *   *Propósito*: Permitir al evaluador validar rápidamente que los números en Tableau coinciden con el origen.

### 1.2 Dashboard en Tableau
Diseño propuesto para cumplir con el requisito de "4 controles distintos" (Rúbrica 1.2):
*   **KPIs Superiores**: Total Clientes, Tasa de Conversión, Balance Promedio.
*   **Gráficos Principales**:
    1.  Barras: Distribución de Job vs Target (¿Qué profesiones contratan más?).
    2.  Histograma/Boxplot: Distribución de Edad por Status Civil.
    3.  Mapa (si hay datos geográficos) o Treemap: Educación.
*   **Controles de Interactividad**:
    1.  *Filtro de Lista Desplegable*: `Education` (Selección única/múltiple).
    2.  *Deslizador (Slider)*: Rango de `Age`.
    3.  *Botones de Opción (Radio Buttons)*: `Marital Status`.
    4.  *Filtro de Fecha/Mes*: Basado en `month` (si aplica) o `campaign`.

## 2. Módulo de Implementación del Modelo (Streamlit Cloud)

### 2.1 Artefactos del Modelo Backend
Se exportarán los siguientes archivos serializados desde el Jupyter Notebook (`models/`):
*   `rf_model_optimized.joblib`: Modelo Random Forest optimizado (con SMOTE y Threshold Tuning si aplica).
*   `preprocessor.joblib`: Pipeline de Scikit-learn (ColumnTransformer) preservando la lógica de escalado (MinMax/Standard) y codificación (OneHot).
*   `model_metadata.json`: Diccionario con el orden exacto de columnas esperadas, umbral de decisión óptimo y métricas clave (AUC, F1).

### 2.2 Aplicación Frontend (`app.py`)
La aplicación tendrá dos secciones principales accesibles vía barra lateral (`st.sidebar`):

#### A. Sección "Análisis del Modelo" (Rúbrica 2.1)
Visualización estática de las métricas obtenidas durante el entrenamiento:
*   **Métricas Clave**: Mostrar Accuracy, Precision, Recall y AUC en tarjetas grandes (`st.metric`).
*   **Gráficos**:
    *   *Curva ROC*: Imagen estática generada en el notebook (`class_roc_curves.png`).
    *   *Matriz de Confusión*: Imagen estática (`class_confusion_matrix.png`).
    *   *Feature Importance*: Gráfico de barras de las variables más influyentes.

#### B. Sección "Simulador de Predicción" (Rúbrica 2.2)
Formulario interactivo para inferencia en tiempo real:
*   **Inputs**:
    *   Numéricos: `Age` (Slider), `Balance` (Number Input), `Duration` (Number Input), `Campaign` (Slider).
    *   Categóricos: `Job`, `Marital`, `Education`, `Default`, `Housing`, `Loan`, `Contact`, `Month` (Selectbox con opciones extraídas del dataset original).
*   **Procesamiento**:
    1.  Recibir inputs.
    2.  Crear DataFrame de una fila.
    3.  Aplicar `preprocessor.transform()`.
    4.  Inferir probabilidad con `model.predict_proba()`.
*   **Output**:
    *   Mensaje de éxito/fracaso ("Cliente propenso a depósito" vs "No propenso").
    *   Puntaje de probabilidad (ej. "Probabilidad de éxito: 87%").

## 3. Entregables Físicos
1.  **Código Fuente**: Estructura de carpetas en GitHub (`streamlit_app/`, `data/`, `notebooks/`).
2.  **Enlace Tableau Public**: URL al dashboard publicado.
3.  **Enlace Streamlit Cloud**: URL a la aplicación funcional.
4.  **Presentación**: PPT actualizada (pdf) en carpeta `presentation/`.
