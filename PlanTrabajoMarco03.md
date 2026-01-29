# Plan de Trabajo - Marco Evaluación 03
## Objetivo General
Cumplir con los requerimientos del Marco de Evaluación 03: Publicación de datos en Tableau Public y despliegue del modelo predictivo en Streamlit Cloud.

## Requisitos Previos
- Notebook de análisis (`analisis_bank_marketing.ipynb`) funcional.
- Carpeta `data/` con el dataset original/procesado.
- Dataset limpio del Marco 02.
- Modelo clasificador entrenado (con métricas de desempeño conocidas).

## Fases del Proyecto

### Fase 1: Preparación y Validación de Datos (Para Tableau Public)
**Objetivo:** Generar archivos de datos exportables y verificables.
1. [ ] **Ejecutar Notebook**: Correr el notebook `analisis_bank_marketing.ipynb` para regenerar el dataset final limpio.
2. [ ] **Exportar Datos**: Guardar el DataFrame final en formato Excel (`.xlsx`) en la carpeta `data/`.
3. [ ] **Hoja de Verificación**: Crear un script o celda en el notebook que calcule los totales de control (suma de columnas numéricas, conteos de clases) y guardarlos en una hoja separada del Excel o en un archivo de texto para cumplir con el punto 1.3 de la rúbrica.
4. [ ] **Documentar Totales**: Registrar estos totales en `MEJORAS_IMPLEMENTADAS.md` para referencia rápida.

### Fase 2: Serialización del Modelo (Para Streamlit Cloud)
**Objetivo:** Guardar el modelo y los objetos de preprocesamiento para su uso en la app.
1. [x] **Identificar Mejor Modelo**: Seleccionado el Random Forest (entrenado en `prepare_model.py`).
2. [x] **Entrenamiento Final**: Re-entrenado con SMOTE en el script de preparación.
3. [x] **Serialización**: Usado `joblib` para guardar modelo, preprocesador y metadatos en `streamlit_app/`.
4. [x] **Exportar Gráficos**: Matriz de Confusión y Curva ROC guardadas en `streamlit_app/images/`.

### Fase 3: Desarrollo de la Aplicación Streamlit
**Objetivo:** Crear la interfaz de usuario interactiva.
1. [x] **Estructura de Carpetas**: Carpeta `streamlit_app/` creada.
2. [x] **Script Principal (`app.py`)**: Implementado con formulario de predicción y visualización de resultados.
3. [x] **Dependencias**: `requirements.txt` creado incluyendo todas las librerías necesarias.

### Fase 4: Despliegue y Documentación Final
**Objetivo:** Entregables finales.
1. [ ] **Instructivo Tableau**: Escribir guía rápida de cómo subir el Excel a Tableau Public y sugerir 4 controles (ej. Filtros por año, selectores de rango de edad, etc.).
2. [x] **Preparación Streamlit Cloud**: Código listo en carpeta `streamlit_app` con dependencias verificadas.
3. [x] **Consolidación**:
    - Actualizado `MEJORAS_IMPLEMENTADAS.md` con los detalles de la implementación de Streamlit.
    - Verificar que todo el código esté limpio.

## Próximos Pasos Inmediatos
1. Ejecutar Fase 1 y 2 en el notebook actual.
2. Crear estructura para Fase 3.
