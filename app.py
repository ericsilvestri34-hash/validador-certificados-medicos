import streamlit as st
import easyocr
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Validador de Certificados", layout="wide")
st.title("🩺 Validador de Certificados Médicos")

uploaded_file = st.file_uploader("Sube la foto del certificado...", type=["jpg", "png", "jpeg"])

def limpiar_imagen(image):
    # Convertir a formato OpenCV
    img = np.array(image.convert('RGB'))
    # Convertir a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # Aplicar umbral binario (blanco y negro puro)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    return thresh

if uploaded_file:
    image = Image.open(uploaded_file)
    
    col_img, col_acc = st.columns([1, 1])
    
    with col_img:
        st.image(image, caption='Certificado original', use_container_width=True)
    
    with col_acc:
        st.subheader("Acciones de Auditoría")
        if st.button("Analizar Sello y Datos"):
            with st.spinner("Limpiando imagen y procesando..."):
                # Limpiamos la imagen para mejorar la lectura
                imagen_limpia = limpiar_imagen(image)
                
                # Usamos EasyOCR (mejor para reconocer caracteres en sellos)
                reader = easyocr.Reader(['es'])
                resultados = reader.readtext(imagen_limpia, detail=0)
                
                # Mostramos los resultados
                st.subheader("Texto detectado en el sello/documento:")
                st.write(resultados)
                
                st.success("Análisis realizado. Verifica si la matrícula extraída coincide con el sello.")

        st.link_button("Validar matrícula en REFEPS", 
                       "https://www.argentina.gob.ar/salud/buscador-nacional-de-profesionales-de-la-salud")
