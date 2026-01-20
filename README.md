# Face Emotion Recognition - UAS Machine Learning 🎭

Proyek ini adalah aplikasi deteksi emosi wajah berbasis Web menggunakan **Streamlit** dan **Deep Learning**. Aplikasi ini mampu mengklasifikasikan ekspresi wajah ke dalam 7 kategori emosi secara real-time melalui unggahan gambar.

## 👥 Kelompok BalaZ
Proyek ini disusun untuk memenuhi tugas besar (UAS) mata kuliah Machine Learning.

## 🚀 Fitur Utama
* **Multi-Model Support**: Menggunakan arsitektur Custom CNN dan MobileNetV2.
* **Web Interface**: Antarmuka pengguna yang interaktif dan mudah digunakan.
* **Pre-processing Otomatis**: Gambar yang diunggah akan secara otomatis diubah ke grayscale dan di-resize ke (48x48) sesuai kebutuhan input model.

## 📊 Dataset
Model dilatih menggunakan dataset emosi wajah (seperti FER-2013) yang mencakup 7 label emosi:
1. Marah (Angry)
2. Jijik (Disgust)
3. Takut (Fear)
4. Senang (Happy)
5. Sedih (Sad)
6. Terkejut (Surprise)
7. Netral (Neutral)

## 🛠️ Instalasi

1. **Clone Repositori**
   ```bash
   git clone [https://github.com/MiguellMiguell/UAS_ML_Face-Emotion-Recognition-.git](https://github.com/MiguellMiguell/UAS_ML_Face-Emotion-Recognition-.git)
   cd UAS_ML_Face-Emotion-Recognition-
   
2. Install Library yang Dibutuhkan Pastikan Anda sudah menginstal Python, lalu jalankan:

pip install -r requirements.txt

💻 Cara Menjalankan Aplikasi
Pastikan file model (best_cnn.keras atau best_mobilenet.keras) berada di folder yang sama dengan app.py.

Jika ingin mengganti model yang digunakan, buka file app.py dan ubah bagian berikut:

def load_my_model():
    # Ganti nama file sesuai model yang ingin digunakan
    model = tf.keras.models.load_model('best_cnn.keras') 
    return model
Jalankan aplikasi dengan perintah:

streamlit run app.py
📁 Struktur Folder
Plaintext

.
├── app.py                # File utama aplikasi Streamlit
├── best_cnn.keras        # Model Custom CNN
├── best_mobilenet.keras  # Model Transfer Learning MobileNetV2
├── requirements.txt      # Daftar library/dependencies
├── .gitignore            # File yang diabaikan oleh Git
└── README.md             # Dokumentasi proyek
📝 Kesimpulan Model
Proyek ini membandingkan dua arsitektur:

Custom CNN: Arsitektur yang dirancang khusus untuk data ekspresi wajah skala kecil.

MobileNetV2: Menggunakan teknik Transfer Learning untuk akurasi dan efisiensi performa yang lebih baik.

© 2026 Kelompok BalaZ - Proyek UAS Machine Learning
