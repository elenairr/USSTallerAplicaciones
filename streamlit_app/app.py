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
    
    # Ejemplos precargados
    st.subheader("📋 Prueba con Ejemplos")
    col_ex1, col_ex2 = st.columns(2)
    
    with col_ex1:
        st.markdown("**Ejemplos de Suscripción (YES)**")
        if st.button("👤 Estudiante (25 años)", key="ex_yes1"):
            st.session_state.update({
                'age': 25, 'job': 'student', 'marital': 'single', 'education': 'tertiary',
                'balance': 500, 'default': 'no', 'housing': 'no', 'loan': 'no',
                'contact': 'cellular', 'day': 10, 'month': 'may', 'duration': 450,
                'campaign': 2, 'pdays': -1, 'previous': 0, 'poutcome': 'unknown'
            })
            st.rerun()
        
        if st.button("👔 Gerente (42 años)", key="ex_yes2"):
            st.session_state.update({
                'age': 42, 'job': 'management', 'marital': 'married', 'education': 'tertiary',
                'balance': 3500, 'default': 'no', 'housing': 'yes', 'loan': 'no',
                'contact': 'cellular', 'day': 15, 'month': 'sep', 'duration': 600,
                'campaign': 1, 'pdays': 180, 'previous': 2, 'poutcome': 'success'
            })
            st.rerun()
        
        if st.button("🏖️ Jubilado (68 años)", key="ex_yes3"):
            st.session_state.update({
                'age': 68, 'job': 'retired', 'marital': 'married', 'education': 'secondary',
                'balance': 8000, 'default': 'no', 'housing': 'no', 'loan': 'no',
                'contact': 'cellular', 'day': 20, 'month': 'mar', 'duration': 500,
                'campaign': 1, 'pdays': -1, 'previous': 0, 'poutcome': 'unknown'
            })
            st.rerun()
    
    with col_ex2:
        st.markdown("**Ejemplos de No Suscripción (NO)**")
        if st.button("🔧 Técnico (28 años)", key="ex_no1"):
            st.session_state.update({
                'age': 28, 'job': 'technician', 'marital': 'single', 'education': 'secondary',
                'balance': -200, 'default': 'no', 'housing': 'yes', 'loan': 'yes',
                'contact': 'telephone', 'day': 5, 'month': 'may', 'duration': 80,
                'campaign': 5, 'pdays': -1, 'previous': 0, 'poutcome': 'unknown'
            })
            st.rerun()
        
        if st.button("👷 Obrero (35 años)", key="ex_no2"):
            st.session_state.update({
                'age': 35, 'job': 'blue-collar', 'marital': 'married', 'education': 'primary',
                'balance': 100, 'default': 'no', 'housing': 'yes', 'loan': 'yes',
                'contact': 'cellular', 'day': 12, 'month': 'aug', 'duration': 120,
                'campaign': 3, 'pdays': 999, 'previous': 1, 'poutcome': 'failure'
            })
            st.rerun()
        
        if st.button("🏢 Administrativo (50 años)", key="ex_no3"):
            st.session_state.update({
                'age': 50, 'job': 'admin.', 'marital': 'divorced', 'education': 'secondary',
                'balance': 1000, 'default': 'no', 'housing': 'yes', 'loan': 'no',
                'contact': 'unknown', 'day': 8, 'month': 'nov', 'duration': 60,
                'campaign': 8, 'pdays': -1, 'previous': 0, 'poutcome': 'unknown'
            })
            st.rerun()
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Datos del Cliente")
        age = st.number_input("Edad", min_value=18, max_value=100, value=st.session_state.get('age', 30))
        job = st.selectbox("Trabajo", ['management', 'technician', 'entrepreneur', 'blue-collar', 'retired', 'admin.', 'services', 'self-employed', 'unemployed', 'housemaid', 'student', 'unknown'], index=['management', 'technician', 'entrepreneur', 'blue-collar', 'retired', 'admin.', 'services', 'self-employed', 'unemployed', 'housemaid', 'student', 'unknown'].index(st.session_state.get('job', 'management')))
        marital = st.selectbox("Estado Civil", ['married', 'single', 'divorced'], index=['married', 'single', 'divorced'].index(st.session_state.get('marital', 'married')))
        education = st.selectbox("Educación", ['tertiary', 'secondary', 'primary', 'unknown'], index=['tertiary', 'secondary', 'primary', 'unknown'].index(st.session_state.get('education', 'tertiary')))
        
    with col2:
        st.subheader("Datos Financieros")
        balance = st.number_input("Balance Anual Promedio (€)", value=st.session_state.get('balance', 0), step=100, min_value=-10000, max_value=200000)
        default = st.selectbox("¿Tiene crédito en default?", ['no', 'yes'], index=['no', 'yes'].index(st.session_state.get('default', 'no')))
        housing = st.selectbox("¿Tiene préstamo hipotecario?", ['yes', 'no'], index=['yes', 'no'].index(st.session_state.get('housing', 'yes')))
        loan = st.selectbox("¿Tiene préstamo personal?", ['no', 'yes'], index=['no', 'yes'].index(st.session_state.get('loan', 'no')))
        
    with col3:
        st.subheader("Datos de Contacto")
        contact = st.selectbox("Tipo de Contacto", ['cellular', 'telephone', 'unknown'], index=['cellular', 'telephone', 'unknown'].index(st.session_state.get('contact', 'cellular')))
        day = st.slider("Día del mes (último contacto)", 1, 31, st.session_state.get('day', 15))
        month = st.selectbox("Mes de contacto", ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'], index=['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'].index(st.session_state.get('month', 'jan')))
        duration = st.number_input("Duración última llamada (segundos)", min_value=0, value=st.session_state.get('duration', 120))
    
    st.subheader("Historial de Campaña")
    c1, c2, c3 = st.columns(3)
    with c1:
        campaign = st.number_input("Número de contactos en esta campaña", min_value=1, value=st.session_state.get('campaign', 1))
    with c2:
        pdays = st.number_input("Días desde último contacto (-1 si nunca)", value=st.session_state.get('pdays', -1))
    with c3:
        previous = st.number_input("Número de contactos previos", min_value=0, value=st.session_state.get('previous', 0))
        poutcome = st.selectbox("Resultado campaña anterior", ['unknown', 'failure', 'other', 'success'], index=['unknown', 'failure', 'other', 'success'].index(st.session_state.get('poutcome', 'unknown')))

    # Prediction Logic
    if st.button("🔮 Predecir Suscripción", type="primary"):
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

