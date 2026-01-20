import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image

# 1. Judul Aplikasi
st.title("Deteksi Emosi Wajah (Kelompok BalaZ)")
st.write("Upload foto wajah untuk mendeteksi emosi.")

# 2. Load Model
@st.cache_resource
def load_my_model():
    # Ganti dengan path model Anda
    model = tf.keras.models.load_model('best_cnn.keras')
    return model

model = load_my_model()
emotion_labels = ['Marah', 'Jijik', 'Takut', 'Senang', 'Sedih', 'Terkejut', 'Netral']

# 3. Fitur Upload Gambar
uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Tampilkan Gambar
    image = Image.open(uploaded_file)
    st.image(image, caption='Gambar yang diunggah', use_column_width=True)
    
    # Preprocessing (Sesuai dengan training di notebook)
    img = np.array(image.convert('L')) # Ubah ke Grayscale
    img = cv2.resize(img, (48, 48))
    img = img / 255.0
    img = np.reshape(img, (1, 48, 48, 1))

    # Prediksi
    if st.button('Deteksi Emosi'):
        prediction = model.predict(img)
        label = emotion_labels[np.argmax(prediction)]
        confidence = np.max(prediction) * 100
        
        # Tampilkan Hasil
        st.success(f"Hasil Prediksi: **{label}**")
        st.info(f"Tingkat Keyakinan: {confidence:.2f}%")