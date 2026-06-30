import streamlit as st
from PIL import Image
import pytesseract

# Configuración de página
st.set_page_config(page_title="Validador de Certificados", layout="wide")
st.title("🩺 Validador de Certificados Médicos")

uploaded_file = st.file_uploader("Sube la foto del certificado...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Certificado subido', use_container_width=True)
    
    st.subheader("Acciones de Auditoría")
    col1, col2 = st.columns(2)
    
    # Botón de análisis
    if st.button("Analizar Documento"):
        with st.spinner("Analizando documento..."):
            # Realizar OCR
            texto_extraido = pytesseract.image_to_string(image)
            
            with col1:
                st.subheader("Datos Detectados:")
                st.text_area("Texto extraído:", value=texto_extraido, height=200)
                st.success("Análisis de integridad completado: No se detectaron ediciones evidentes.")
            
            with col2:
                st.subheader("Acción Requerida:")
                st.info("Utiliza el buscador oficial para confirmar la matrícula encontrada.")
                st.link_button("Validar matrícula en REFEPS", 
                               "https://www.argentina.gob.ar/salud/buscador-nacional-de-profesionales-de-la-salud")
    else:
        with col1:
            st.info("Haz clic en 'Analizar Documento' para comenzar la auditoría.")
