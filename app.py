import streamlit as st
from PIL import Image

st.set_page_config(page_title="Validador de Certificados", layout="wide")
st.title("🩺 Validador de Certificados Médicos")

uploaded_file = st.file_uploader("Sube la foto del certificado...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Certificado subido', use_container_width=True)
    
    st.subheader("Acciones de Auditoría")
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("Estado: Pendiente de OCR y Análisis de Integridad")
    
    with col2:
        st.link_button("Validar matrícula en REFEPS", 
                       "https://www.argentina.gob.ar/salud/buscador-nacional-de-profesionales-de-la-salud")
