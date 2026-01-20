# 🎓 Student Academic Stress Prediction  
Web-Based Student Academic Stress Prediction Using Machine Learning

---

## 📌 Latar Belakang

Stres akademik merupakan permasalahan yang sering dialami oleh mahasiswa. Tekanan akademik yang tinggi, jam tidur yang kurang, serta tuntutan akademik seperti ujian dan tugas dapat memengaruhi kondisi mental mahasiswa. Apabila kondisi ini tidak diperhatikan, stres akademik dapat berdampak pada penurunan konsentrasi, prestasi akademik, dan kesehatan mental.

Berdasarkan permasalahan tersebut, proyek ini dikembangkan untuk memprediksi tingkat stres akademik mahasiswa menggunakan pendekatan Machine Learning. Sistem ini diimplementasikan dalam bentuk aplikasi web agar hasil prediksi dapat ditampilkan secara interaktif dan mudah dipahami oleh pengguna.

---

## 🎯 Tujuan Proyek

Tujuan dari pembuatan proyek ini adalah:
1. Membangun model Machine Learning untuk memprediksi tingkat stres akademik mahasiswa
2. Mengimplementasikan model Machine Learning ke dalam aplikasi web
3. Menyediakan tampilan hasil prediksi yang interaktif dan informatif
4. Memberikan contoh penerapan Machine Learning berbasis web menggunakan FastAPI

---

## 🧠 Metode yang Digunakan

Metode Machine Learning yang digunakan dalam proyek ini adalah Linear Regression.

Alasan pemilihan Linear Regression antara lain:
- Hubungan antara variabel input dan tingkat stres bersifat cukup linear
- Model mudah dipahami dan diinterpretasikan
- Cocok untuk dataset berukuran kecil hingga menengah
- Memiliki kompleksitas rendah dan efisien
- Mudah diintegrasikan dengan sistem backend berbasis web

---

## 📊 Dataset

Dataset yang digunakan dalam proses training merupakan dataset simulasi yang dibuat untuk merepresentasikan kondisi stres akademik mahasiswa. Dataset ini disusun berdasarkan referensi dataset stres akademik mahasiswa dari Kaggle dan telah disesuaikan dalam bentuk numerik.

Dataset simulasi digunakan karena keterbatasan akses terhadap data asli, namun tetap menggambarkan hubungan logis antara faktor akademik dan tingkat stres.

### Variabel Input
- academic_pressure  
  Menunjukkan tingkat tekanan akademik yang dirasakan mahasiswa
- sleep_hours  
  Menunjukkan rata-rata jam tidur mahasiswa per malam
- exam_pressure  
  Menunjukkan tingkat tekanan yang berasal dari ujian

### Variabel Target
- stress_score  
  Menunjukkan skor tingkat stres akademik mahasiswa

---

## ⚙️ Proses Training Model

Proses training model dilakukan menggunakan bahasa pemrograman Python dan library Scikit-Learn dengan tahapan sebagai berikut:
1. Membuat dataset dalam bentuk DataFrame menggunakan library pandas
2. Memisahkan data menjadi data training dan data testing
3. Melatih model menggunakan algoritma Linear Regression
4. Melakukan pengujian prediksi untuk memastikan model berjalan dengan baik
5. Menyimpan model hasil training ke dalam file dengan format .pkl menggunakan joblib

Model hasil training disimpan dengan nama stress_prediction_model.pkl dan digunakan kembali oleh backend FastAPI untuk proses prediksi.

---

## 🚀 Backend (FastAPI)

Backend aplikasi dibangun menggunakan framework FastAPI. Backend berfungsi sebagai penghubung antara frontend dan model Machine Learning.

### Fungsi Backend
- Menerima data input dari frontend
- Mengolah data input menggunakan model Machine Learning
- Menghasilkan nilai prediksi tingkat stres akademik
- Mengirim hasil prediksi ke frontend dalam format JSON

### Endpoint API
Endpoint utama yang digunakan pada backend adalah:
POST /predict

CORS diaktifkan agar frontend dapat mengakses backend tanpa batasan origin.

---

## 🌐 Frontend

Frontend aplikasi dibangun menggunakan HTML, Tailwind CSS, JavaScript, dan Chart.js. Tampilan frontend dirancang agar menarik, interaktif, dan mudah digunakan.

### Fitur Frontend
- Tampilan web modern dengan background animasi
- Musik latar yang dapat diaktifkan atau dimatikan oleh pengguna
- Input faktor stres berupa slider dan dropdown
- Tombol untuk melakukan prediksi tingkat stres
- Tampilan hasil prediksi berupa skor numerik
- Kategori tingkat stres (Low, Moderate, High)
- Grafik batang faktor stres menggunakan Chart.js

Frontend mengirim data input ke backend FastAPI menggunakan metode POST, kemudian menampilkan hasil prediksi yang diterima.

---

## 🔁 Alur Kerja Sistem

Alur kerja sistem secara keseluruhan adalah sebagai berikut:
1. Pengguna membuka halaman web
2. Pengguna mengisi faktor-faktor stres akademik
3. Pengguna menekan tombol prediksi
4. Frontend mengirim data ke backend FastAPI
5. Backend memproses data menggunakan model Machine Learning
6. Model menghasilkan nilai prediksi tingkat stres
7. Backend mengirim hasil prediksi ke frontend
8. Frontend menampilkan hasil prediksi dan visualisasi grafik

---

## ▶️ Cara Menjalankan Aplikasi

Langkah-langkah menjalankan aplikasi:
1. Jalankan file train.py untuk melakukan training model
2. Jalankan backend FastAPI menggunakan perintah uvicorn
3. Buka file index.html melalui browser untuk mengakses frontend

---

## 📈 Output Aplikasi

Output yang dihasilkan oleh aplikasi ini meliputi:
- Skor tingkat stres akademik mahasiswa
- Kategori tingkat stres (Low, Moderate, High)
- Grafik visualisasi faktor stres akademik

---

## ⚠️ Keterbatasan Sistem

Beberapa keterbatasan dari sistem ini antara lain:
- Dataset yang digunakan masih berupa dataset simulasi
- Jumlah data relatif terbatas
- Model Linear Regression belum mampu menangkap hubungan non-linear
- Faktor stres yang digunakan masih terbatas pada beberapa variabel

---

## 🔮 Pengembangan Selanjutnya

Pengembangan yang dapat dilakukan di masa mendatang antara lain:
- Menggunakan dataset asli dengan jumlah data yang lebih besar
- Menambahkan variabel lain seperti beban tugas dan waktu belajar
- Menggunakan algoritma Machine Learning lain untuk meningkatkan akurasi
- Menambahkan fitur penyimpanan riwayat prediksi pengguna

---

## 📚 Referensi

Scikit-Learn Documentation  
FastAPI Documentation  
Chart.js Documentation
