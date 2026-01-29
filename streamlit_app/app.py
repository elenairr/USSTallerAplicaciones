import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os
from PIL import Image

# Setup Page
st.set_page_config(page_title="Bank Marketing Predictor", layout="wide")

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.joblib")
PREPROCESSOR_PATH = os.path.join(BASE_DIR, "preprocessor.joblib")
IMAGES_DIR = os.path.join(BASE_DIR, "images")
FEATURES_PATH = os.path.join(BASE_DIR, "features.joblib")

# Load Assets
@st.cache_resource
def load_assets():
    model = joblib.load(MODEL_PATH)
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    return model, preprocessor

try:
    model, preprocessor = load_assets()
    st.success("Modelo y preprocesador cargados correctamente.")
except Exception as e:
    st.error(f"Error cargando el modelo: {e}")
    st.stop()

# Title and Intro
st.title("🏦 Predicción de Suscripción a Depósito a Plazo")
st.markdown("""
Esta aplicación utiliza un modelo de Machine Learning (**Random Forest**) para predecir si un cliente se suscribirá a un depósito a plazo fijo basado en sus datos demográficos y de contacto.
""")

# Tabs
tab1, tab2 = st.tabs(["🔮 Predicción en Vivo", "📊 Resultados del Modelo"])

with tab1:
    st.header("Formulario de Predicción")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Datos del Cliente")
        age = st.number_input("Edad", min_value=18, max_value=100, value=30)
        job = st.selectbox("Trabajo", ['management', 'technician', 'entrepreneur', 'blue-collar', 'retired', 'admin.', 'services', 'self-employed', 'unemployed', 'housemaid', 'student', 'unknown'])
        marital = st.selectbox("Estado Civil", ['married', 'single', 'divorced'])
        education = st.selectbox("Educación", ['tertiary', 'secondary', 'primary', 'unknown'])
        
    with col2:
        st.subheader("Datos Financieros")
        balance = st.number_input("Balance Anual Promedio (€)", value=0)
        default = st.selectbox("¿Tiene crédito en default?", ['no', 'yes'])
        housing = st.selectbox("¿Tiene préstamo hipotecario?", ['yes', 'no'])
        loan = st.selectbox("¿Tiene préstamo personal?", ['no', 'yes'])
        
    with col3:
        st.subheader("Datos de Contacto")
        contact = st.selectbox("Tipo de Contacto", ['cellular', 'telephone', 'unknown'])
        day = st.slider("Día del mes (último contacto)", 1, 31, 15)
        month = st.selectbox("Mes de contacto", ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
        duration = st.number_input("Duración última llamada (segundos)", min_value=0, value=120)
    
    st.subheader("Historial de Campaña")
    c1, c2, c3 = st.columns(3)
    with c1:
        campaign = st.number_input("Número de contactos en esta campaña", min_value=1, value=1)
    with c2:
        pdays = st.number_input("Días desde último contacto (-1 si nunca)", value=-1)
    with c3:
        previous = st.number_input("Número de contactos previos", min_value=0, value=0)
        poutcome = st.selectbox("Resultado campaña anterior", ['unknown', 'failure', 'other', 'success'])

    # Prediction Logic
    if st.button("Predecir Suscripción", type="primary"):
        # Create DataFrame
        input_data = pd.DataFrame({
            'age': [age],
            'job': [job],
            'marital': [marital],
            'education': [education],
            'default': [default],
            'balance': [balance],
            'housing': [housing],
            'loan': [loan],
            'contact': [contact],
            'day_of_week': [day], # Mapping 'day' input to 'day_of_week' column name as in training
            'month': [month],
            'duration': [duration],
            'campaign': [campaign],
            'pdays': [pdays],
            'previous': [previous],
            'poutcome': [poutcome]
        })
        
        # Preprocess
        try:
            X_processed = preprocessor.transform(input_data)
            
            # Predict
            prediction = model.predict(X_processed)[0]
            probability = model.predict_proba(X_processed)[0][1]
            
            st.divider()
            if prediction == 1:
                st.success(f"### ✅ ¡El cliente PROBABLEMENTE se suscribirá!")
                st.metric("Probabilidad de Éxito", f"{probability:.1%}")
            else:
                st.warning(f"### ❌ El cliente PROBABLEMENTE NO se suscribirá.")
                st.metric("Probabilidad de Éxito", f"{probability:.1%}")
                
        except Exception as e:
            st.error(f"Error en la predicción: {e}")

with tab2:
    st.header("Métricas de Desempeño del Modelo")
    
    # Load metadata if available to show precise AUC
    try:
        features_meta = joblib.load(FEATURES_PATH)
        auc_score = features_meta.get("auc", "N/A")
        st.metric("AUC - ROC Score", f"{auc_score:.4f}" if isinstance(auc_score, float) else auc_score)
    except:
        pass

    col_img1, col_img2 = st.columns(2)
    
    with col_img1:
        st.subheader("Matriz de Confusión")
        try:
            img_cm = Image.open(os.path.join(IMAGES_DIR, "confusion_matrix.png"))
            st.image(img_cm, caption="Matriz de Confusión (Test Set)", use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen de Matriz de Confusión no encontrada.")

    with col_img2:
        st.subheader("Curva ROC")
        try:
            img_roc = Image.open(os.path.join(IMAGES_DIR, "roc_curve.png"))
            st.image(img_roc, caption="Curva ROC (Test Set)", use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen de Curva ROC no encontrada.")
            
    st.markdown("""
    ### Interpretación
    - **Matriz de Confusión**: Muestra cuántos clientes fueron clasificados correctamente. 
    - **Curva ROC**: Evalúa la capacidad del modelo para distinguir entre clases. Un área bajo la curva (AUC) cercana a 1.0 indica un modelo excelente.
    """)

