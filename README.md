# 🌤️ JakU — Dashboard Kualitas Udara DKI Jakarta

**JakU (Jakarta Kualitas Udara)** adalah platform monitoring kualitas udara (ISPU) DKI Jakarta berbasis **machine learning**, dibangun dengan **Streamlit**. Model klasifikasi dilatih dari dataset ISPU asli (`Data_ISPU.csv`) mengikuti metodologi **CRISP-DM**, dengan **XGBoost** sebagai model utama.

> **Pantau Udara, Jaga Jakarta**

---

## ✨ Fitur

| Halaman | Isi |
|---|---|
| **Dashboard** | Ringkasan ISPU DKI Jakarta, peta interaktif 5 wilayah (Folium), prediksi & tren ISPU 7 hari, pemilih tanggal |
| **Detail Wilayah** | Kondisi per kota administratif: Jakarta Pusat, Utara, Barat, Selatan, Timur, dan Kep. Seribu |
| **Simulasi Prediksi ISPU** | Input 6 polutan + pilih model (XGBoost / Random Forest / SVM) → prediksi kategori real-time |
| **Edukasi & Insight** | Kategori ISPU, dampak kesehatan, sumber polusi, dan tips menjaga kualitas udara |

Popup **"Informasi Polutan"** tersedia pada beberapa halaman untuk menjelaskan tiap parameter.

---

## 📂 Struktur Project

```
JAKU5-main/
├── app.py                       # Aplikasi Streamlit (4 halaman)
├── train_model.py               # Training 3 model dari Data_ISPU.csv (CRISP-DM)
├── generate_dashboard_data.py   # Generate data tampilan dashboard dari Data_ISPU.csv + model
├── Data_ISPU.csv                # Dataset ISPU asli (semicolon-delimited, ±3.350 baris)
├── requirements.txt
├── README.md
├── .gitignore
├── .streamlit/
│   └── config.toml              # Tema & konfigurasi server
├── assets/                      # SVG, PNG, ikon, ilustrasi UI
├── data/                        # Data tampilan (hasil generate dari dataset asli)
│   ├── ringkasan.csv            # Ringkasan ISPU Jakarta terkini (kartu hero)
│   ├── ringkasan.json
│   ├── wilayah.csv              # Kondisi 5 wilayah (peta + Detail Wilayah)
│   ├── tren_harian.csv          # Tren ISPU DKI 7 hari terakhir
│   ├── tren_wilayah.csv         # Tren ISPU per wilayah
│   └── prediksi.csv             # Klasifikasi kategori oleh model XGBoost
└── models/                      # Artefak model terlatih (dari notebook CRISP-DM)
    ├── model_xgboost.pkl        # ⭐ model utama
    ├── model_random_forest.pkl
    ├── model_svm.pkl
    ├── label_encoder.pkl
    ├── standard_scaler.pkl      # dipakai khusus SVM
    └── fitur_polutan.pkl        # urutan fitur polutan
```

---

## ▶️ Menjalankan Lokal

```bash
pip install -r requirements.txt
streamlit run app.py
```

Buka http://localhost:8501

**Dependensi utama:** Streamlit · Pandas · NumPy · Plotly · Folium · streamlit-folium · streamlit-option-menu · scikit-learn · XGBoost · joblib

---

## 🧠 Tentang Model

Model dilatih dari `Data_ISPU.csv` dengan pipeline identik notebook penelitian (CRISP-DM):

1. Filter kategori valid (**BAIK / SEDANG / TIDAK SEHAT**)
2. Normalisasi nama stasiun pemantau
3. Konversi numerik + **imputasi median** untuk nilai kosong
4. **IQR outlier removal** pada 6 fitur polutan
5. Split `test_size=0.2, random_state=42, stratify`
6. Hyperparameter tuning dengan `StratifiedKFold` (k=5):
   - Random Forest & XGBoost → `RandomizedSearchCV`
   - SVM → `GridSearchCV` (dengan `StandardScaler`)

**Urutan fitur (wajib sama saat prediksi):**

```
pm_sepuluh, pm_duakomalima, sulfur_dioksida, karbon_monoksida, ozon, nitrogen_dioksida
```

XGBoost menjadi model utama, dengan **PM2.5** sebagai fitur paling dominan. Random Forest dan SVM disediakan sebagai pembanding di halaman Simulasi.

### Melatih ulang model

```bash
python train_model.py
```

Script membaca `Data_ISPU.csv`, melatih ketiga model, dan menyimpan 6 file `.pkl` ke `models/`.

### Memperbarui data tampilan dashboard

```bash
python generate_dashboard_data.py
```

Membangun ulang seluruh file di `data/` (ringkasan, wilayah, tren, prediksi) dari `Data_ISPU.csv` + model XGBoost. Jalankan setiap kali dataset diperbarui.

---

## 🗺️ Pemetaan Stasiun → Wilayah

| Stasiun Pemantau | Wilayah |
|---|---|
| DKI1 Bunderan HI | Jakarta Pusat |
| DKI2 Kelapa Gading | Jakarta Utara |
| DKI5 Kebon Jeruk | Jakarta Barat |
| DKI3 Jagakarsa | Jakarta Selatan |
| DKI4 Lubang Buaya | Jakarta Timur |

> Kepulauan Seribu ditampilkan di Detail Wilayah namun tidak memiliki stasiun pemantau pada dataset.

---

## 🚀 Deploy ke Streamlit Community Cloud

### 1. Push ke GitHub

```bash
git init
git add .
git commit -m "Initial commit: JakU dashboard kualitas udara"
git branch -M main
git remote add origin https://github.com/USERNAME-ANDA/NAMA-REPO.git
git push -u origin main
```

> Ganti `USERNAME-ANDA` dan `NAMA-REPO`. Saat login, gunakan **Personal Access Token** GitHub sebagai password.

### 2. Deploy

1. Buka [share.streamlit.io](https://share.streamlit.io/) → login dengan GitHub
2. **Create app** → **Deploy a public app from GitHub**
3. Isi:
   - **Repository:** `USERNAME-ANDA/NAMA-REPO`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. **Deploy** — tunggu beberapa menit hingga aplikasi online di `https://<nama-app>.streamlit.app/`

### 3. Update setelah perubahan

```bash
git add .
git commit -m "deskripsi perubahan"
git push
```

Streamlit Cloud otomatis re-deploy. Jika file `.pkl` di `models/` diganti, lakukan **Reboot app** dari menu (⋮) agar cache `@st.cache_resource` ter-clear.

---

## 🛠️ Stack

Streamlit · Pandas · NumPy · Plotly · Folium · scikit-learn · XGBoost · joblib
