# Bank Marketing Prediction - Streamlit App

Aplicación web para predecir la suscripción de clientes a depósitos a plazo utilizando Machine Learning.

## 🚀 Despliegue

Esta aplicación está desplegada en Streamlit Community Cloud.

## 📋 Características

- **Predicción en Vivo**: Formulario interactivo para predecir si un cliente se suscribirá
- **Visualización de Métricas**: ROC Curve, Matriz de Confusión y Feature Importance
- **Modelo**: Random Forest optimizado con SMOTE (AUC ~0.91)

## 🛠️ Tecnologías

- Python 3.10
- Streamlit
- Scikit-learn
- Pandas
- Joblib

## 📦 Estructura

```
streamlit_app/
├── app.py              # Aplicación principal
├── model.joblib        # Modelo entrenado
├── preprocessor.joblib # Pipeline de preprocesamiento
├── features.joblib     # Metadata del modelo
├── requirements.txt    # Dependencias
└── images/            # Gráficos estáticos
```

## 👥 Autora

Maria Elena Irribarra Aguilera - Magíster en Data Science, Universidad San Sebastián
