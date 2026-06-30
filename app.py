import streamlit as st
import easyocr # Librería especializada en manuscritos
from PIL import Image
import numpy as np

# ... (resto de tu configuración)

if st.button("Analizar Documento"):
    with st.spinner("Leyendo manuscrito... esto puede tardar un poco"):
        # Convertimos la imagen de PIL a formato compatible con EasyOCR
        img_array = np.array(image)
        reader = easyocr.Reader(['es']) # Cargamos el motor en español
        resultado = reader.readtext(img_array, detail=0)
        
        texto_final = "\n".join(resultado)
        st.text_area("Texto detectado:", value=texto_final, height=200)
