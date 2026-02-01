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

### 1.2 Dashboard en Tableau (Procedimiento de Implementación)
La implementación del dashboard sigue una estrategia de construcción por capas para asegurar el cumplimiento de la rúbrica (4 controles, interactividad e insights verificables).

#### Fase 1: Conexión de Datos
1.  **Carga de Datos Principales**: Conectar Tableau al archivo `bank_marketing_tableau.xlsx` y arrastrar únicamente la pestaña `Data` al área de trabajo.
2.  **Carga de Datos de Verificación**: Añadir una **nueva fuente de datos** independiente (Data > New Data Source) cargando el mismo archivo (o `verification_data.json`) y usando exclusivamente la pestaña `Verificacion`. Esto aísla los totales de control para cumplir el punto 1.3 de la rúbrica sin duplicar registros.

#### Fase 2: Construcción de Visualizaciones (Hojas)
Se crearán cuatro hojas de trabajo base alineadas con la estrategia de visualización:
1.  **Hoja `Tasa_Conversion`**:
    *   *Tipo*: Gráfico de Torta (Pie Chart).
    *   *Datos*: Dimensión `y` (target) en Color y Ángulo.
    *   *Objetivo*: Visualizar el desbalance global del embudo (88% No vs 11.7% Yes).
2.  **Hoja `Conversion_Por_Job`**:
    *   *Tipo*: Gráfico de Barras Horizontales.
    *   *Datos*: `job` en Filas, `% del Total` de Conversión en Columnas.
    *   *Objetivo*: Comparar tasas de éxito por profesión.
3.  **Hoja `Scatter_Edad_Balance`**:
    *   *Tipo*: Scatter Plot (Dispersión).
    *   *Datos*: `age` en Columnas, `balance` en Filas. Coloreado por `y`.
    *   *Objetivo*: Identificar patrones de segmentación (clusters visuales).
4.  **Hoja `Verificacion_Datos`**:
    *   *Tipo*: Tabla de Texto.
    *   *Datos*: Usar la fuente secundaria para mostrar `Total Registros`, `Suma Balance` y conteos.

#### Fase 3: Ensamblaje y Controles de Interactividad (Rúbrica 1.2)
En el Dashboard final se integran las hojas y se configuran los 4 controles obligatorios para filtrar todas las visualizaciones simultáneamente:
1.  **Filtro de Lista Desplegable (`Education`)**: Selección única/múltiple para filtrar por nivel educativo.
2.  **Deslizador (`Age`)**: Slider de rango para acotar el análisis a grupos etarios específicos (ej. 30-50 años).
3.  **Botones de Opción (`Marital Status`)**: Selección exclusiva (Radio Buttons) para estado civil.
4.  **Filtro de Selección Múltiple (`Month`)**: Para aislar el rendimiento en meses específicos de campaña.

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

### 2.3 Despliegue en Streamlit Community Cloud (SCC)
El proceso de despliegue requiere sincronización entre el repositorio local, GitHub y el servicio de hosting de Streamlit.

#### Fase 1: Preparación del Repositorio (Local)
La estructura del proyecto debe aislar la aplicación para facilitar su detección por SCC:
*   Carpeta raíz: `streamlit_app/`
*   Archivos esenciales: `app.py`, `requirements.txt`, archivos `.joblib` (modelo), carpeta `images/`.
*   **Acción Realizada**: Se ha ejecutado el script `prepare_model.py` para generar un modelo Random Forest fresco (AUC ~0.91) y serializarlo junto con el preprocesador.

#### Fase 2: Gestión de Versiones (GitHub)
1.  **Commit y Push**: Asegurar que la carpeta `streamlit_app` y todo su contenido (incluyendo los archivos `.joblib` si son <100MB) estén en la rama principal (`main` o `master`).
    *   *Nota*: GitHub tiene un límite de 100MB por archivo. Los modelos generados (~15MB) cumplen este requisito.
2.  **Verificación**: Confirmar en la web de GitHub que el archivo `streamlit_app/app.py` es visible.

#### Fase 3: Configuración en Streamlit Community Cloud
1.  Acceder a `share.streamlit.io` con la cuenta de GitHub vinculada.
2.  Seleccionar **"New App"**.
3.  **Configurar origen**:
    *   Repository: Seleccionar el repo del proyecto.
    *   Branch: `main`.
    *   Main file path: `streamlit_app/app.py` (Crucial especificar la subcarpeta).
4.  **Despliegue**: Hacer clic en "Deploy". SCC instalará automáticamente las dependencias listadas en `streamlit_app/requirements.txt`.

#### Fase 4: Validación Post-Despliegue
*   Verificar que la carga de modelos (`load_assets`) no arroje errores de ruta.
*   Probar una predicción en vivo para confirmar que `scikit-learn` en la nube (definido en requirements) es compatible con la versión usada para entrenar el modelo (ambas deben alinearse, idealmente 1.4+).

## 3. Entregables Físicos
1.  **Código Fuente**: Estructura de carpetas en GitHub (`streamlit_app/`, `data/`, `notebooks/`).
2.  **Enlace Tableau Public**: URL al dashboard publicado.
3.  **Enlace Streamlit Cloud**: URL a la aplicación funcional.
4.  **Presentación**: PPT actualizada (pdf) en carpeta `presentation/`.

# Estrategia de Visualización de Insights

Esta sección consolida los hallazgos analíticos generados en las etapas de clustering, clasificación y reglas de asociación con el objetivo de definir una estrategia de visualización coherente. Estos insights alimentarán directamente la construcción del dashboard en Tableau (Marco Evaluación 03) para permitir la exploración interactiva por parte de los tomadores de decisiones.

La estrategia se estructura en cuatro dimensiones conceptuales que guiarán la narrativa visual:

## Dimensión 1: El Embudo de Conversión (Panorama General)
Analizando la distribución global de la variable objetivo, se establece la línea base de rendimiento.
*   **Insight Clave:** La tasa de conversión global es de solo 11.7%, lo que implica que casi 9 de cada 10 llamadas no resultan en venta. Sin embargo, ciertas subregiones de los datos muestran tasas muy superiores.
*   **Propuesta de Visualización (KPIs):** Indicadores de alto nivel mostrando el volumen total de clientes, el número de conversiones exitosas y la tasa de efectividad general.

## Dimensión 2: Perfilamiento de Segmentos (Clustering)
Los tres clusters identificados proveen una "brújula" para navegar la base de clientes.
*   **Insight Clave:**
    *   **Cluster 0 (Seniors, Alto Balance):** Clientes maduros con capacidad de ahorro.
    *   **Cluster 1 (Jóvenes Trabajadores):** Segmento activo pero con menor capital medio.
    *   **Cluster 2 (Bajo Capital):** Grupo mayoritario con balances bajos y menor respuesta.
*   **Propuesta de Visualización:** Gráficos de dispersión (Scatter Plot) correlacionando Edad vs. Balance, utilizando color para diferenciar los clusters identificados por K-Means.

## Dimensión 3: Determinantes del Éxito (Clasificación)
El modelo Random Forest permitió aislar las variables con mayor poder predictivo.
*   **Insight Clave:** La duración de la llamada es el driver principal, pero variables como el `Mes` de contacto y el `Balance` juegan roles críticos ex-ante.
*   **Propuesta de Visualización:**
    *   Histograma interactivo de `Duration`, permitiendo filtrar llamadas cortas (<3 min) vs largas.
    *   Análisis temporal mostrando la Tasa de Conversión por `Month` para validar la estacionalidad (picos en marzo/septiembre).
    *   Boxplots de `Balance` comparando clientes que aceptaron vs. rechazaron (target `yes` vs `no`).

## Dimensión 4: Micro-segmentación Accionable (Reglas de Asociación)
Las reglas de Apriori con alto Lift revelaron combinaciones específicas de alta probabilidad.
*   **Insight Clave:** El perfil específico "Trabajador manual (blue-collar) + Casado" contactado en Mayo muestra patrones de respuesta distintivos.
*   **Propuesta de Visualización:** Panel de filtros cruzados que permita seleccionar `Job`, `Marital Status` y `Month` para "aislar" visualmente estos micro-segmentos y observar cómo cambia la tasa de conversión en tiempo real.


