# Student Academic Stress Prediction

**Nama** : Mayta Nohan Griselda
**NIM** : 2441044  
**Program Studi** : Sistem Informasi  
**Perguruan Tinggi** : STMIK AMIK Bandung  
**Mata Kuliah** : Machine Learning

---

## Pendahuluan

Student Academic Stress Prediction merupakan aplikasi berbasis web yang dirancang untuk memprediksi tingkat stres akademik mahasiswa dengan memanfaatkan metode Machine Learning. Aplikasi ini dikembangkan sebagai bagian dari tugas perkuliahan dengan tujuan menerapkan konsep pembelajaran mesin ke dalam sistem nyata yang dapat diakses dan digunakan secara langsung oleh pengguna. Sistem ini memungkinkan pengguna untuk memasukkan beberapa faktor akademik yang kemudian diproses untuk menghasilkan prediksi tingkat stres.

Stres akademik merupakan permasalahan yang sering dialami oleh mahasiswa, terutama akibat tekanan tugas, ujian, serta tuntutan akademik lainnya. Kondisi ini dapat berdampak pada kesehatan mental, konsentrasi belajar, dan performa akademik. Oleh karena itu, diperlukan sebuah sistem yang mampu memberikan gambaran awal mengenai tingkat stres akademik mahasiswa berdasarkan faktor-faktor yang umum terjadi di lingkungan perkuliahan.

## Tujuan dan Manfaat Sistem

Tujuan utama dari pengembangan sistem ini adalah untuk membangun sebuah aplikasi berbasis web yang mampu memprediksi tingkat stres akademik mahasiswa menggunakan pendekatan Machine Learning. Sistem ini juga dibuat sebagai sarana pembelajaran untuk memahami bagaimana proses Machine Learning diterapkan mulai dari pengolahan data, pembuatan model, hingga integrasi ke dalam aplikasi web.

Manfaat dari sistem ini diharapkan dapat dirasakan oleh mahasiswa dan dari sisi akademik. Bagi mahasiswa, sistem ini dapat membantu memberikan gambaran awal mengenai kondisi stres akademik yang sedang dialami. Dari sisi akademik, proyek ini menjadi contoh penerapan konsep Machine Learning dan pengembangan sistem berbasis web yang terintegrasi antara frontend, backend, dan model prediksi.

## Metode Machine Learning

Metode Machine Learning yang digunakan dalam proyek ini adalah Linear Regression. Metode ini dipilih karena memiliki konsep yang sederhana, mudah dipahami, serta cocok untuk kebutuhan pembelajaran. Linear Regression bekerja dengan memodelkan hubungan linear antara variabel input dan output, sehingga setiap variabel memiliki pengaruh tertentu terhadap hasil prediksi.

Selain itu, Linear Regression memiliki kompleksitas yang rendah dan relatif stabil ketika digunakan pada dataset berukuran kecil hingga menengah. Metode ini juga mudah diinterpretasikan karena hasil prediksi dapat dijelaskan berdasarkan kontribusi masing-masing variabel. Dengan pertimbangan tersebut, Linear Regression dinilai sesuai untuk digunakan dalam sistem ini.

## Dataset dan Variabel

Dataset yang digunakan dalam proyek ini merupakan dataset simulasi yang disusun berdasarkan referensi umum mengenai stres akademik mahasiswa. Dataset simulasi digunakan karena keterbatasan data asli, namun tetap dirancang agar mencerminkan kondisi yang realistis dan relevan dengan permasalahan yang dibahas.

Variabel input yang digunakan meliputi tingkat tekanan akademik, jumlah jam tidur per malam, serta tekanan akibat ujian. Variabel-variabel tersebut dipilih karena sering menjadi faktor utama yang memengaruhi tingkat stres akademik mahasiswa. Output dari dataset ini berupa skor tingkat stres akademik yang digunakan sebagai target dalam proses pelatihan model Machine Learning.

## Proses Training Model

Proses pelatihan model dilakukan menggunakan bahasa pemrograman Python dengan bantuan library Pandas dan Scikit-learn. Dataset yang telah disiapkan kemudian dibagi menjadi data latih dan data uji. Data latih digunakan untuk melatih model agar dapat mempelajari pola hubungan antar variabel, sedangkan data uji digunakan untuk mengevaluasi hasil prediksi model.

Setelah proses pelatihan selesai, model Linear Regression diuji untuk memastikan bahwa model mampu menghasilkan prediksi dengan baik. Model yang telah dilatih kemudian disimpan dalam bentuk file agar dapat digunakan kembali pada sistem backend tanpa perlu melakukan proses training ulang setiap kali aplikasi dijalankan.

## Arsitektur Sistem

Arsitektur sistem pada proyek ini terdiri dari tiga komponen utama, yaitu frontend, backend, dan model Machine Learning. Frontend berperan sebagai antarmuka pengguna yang digunakan untuk memasukkan data faktor stres akademik dan menampilkan hasil prediksi. Backend berfungsi sebagai penghubung antara frontend dan model Machine Learning, sedangkan model Machine Learning digunakan sebagai inti dari proses prediksi.

Frontend dan backend saling terhubung melalui API. Data yang dimasukkan oleh pengguna pada frontend akan dikirim ke backend dalam format JSON. Backend kemudian memproses data tersebut menggunakan model Machine Learning yang telah dilatih dan mengirimkan hasil prediksi kembali ke frontend untuk ditampilkan kepada pengguna.

## Backend dengan FastAPI

Backend aplikasi dibangun menggunakan framework FastAPI. FastAPI dipilih karena memiliki performa yang cepat, ringan, serta mudah digunakan dalam pengembangan REST API. Backend bertanggung jawab dalam menerima data dari frontend, memproses data menggunakan model Machine Learning, dan mengembalikan hasil prediksi kepada frontend.

Model Machine Learning yang telah dilatih sebelumnya dimuat ke dalam backend sehingga proses prediksi dapat dilakukan secara langsung. Dengan pemisahan antara backend dan frontend, sistem menjadi lebih terstruktur dan mudah untuk dikembangkan di masa depan.

## Frontend Aplikasi

Frontend aplikasi dikembangkan menggunakan HTML, Tailwind CSS, dan JavaScript. Antarmuka dirancang dengan tampilan yang sederhana namun tetap interaktif agar mudah digunakan oleh pengguna. Pengguna dapat memasukkan faktor-faktor stres akademik melalui form yang tersedia, kemudian menekan tombol prediksi untuk melihat hasilnya.

Hasil prediksi ditampilkan dalam bentuk skor tingkat stres akademik beserta kategorinya, seperti rendah, sedang, atau tinggi. Selain itu, visualisasi grafik ditambahkan untuk membantu pengguna memahami kondisi faktor-faktor yang dimasukkan. Dengan tampilan yang interaktif, pengguna dapat lebih mudah memahami hasil yang diberikan oleh sistem.

## Alur Kerja Sistem

Alur kerja sistem dimulai ketika pengguna mengakses halaman web dan mengisi data faktor stres akademik. Data tersebut kemudian dikirim ke backend melalui request HTTP. Backend memproses data menggunakan model Machine Learning yang telah dilatih sebelumnya.

Setelah proses prediksi selesai, backend mengirimkan hasil prediksi kembali ke frontend. Frontend kemudian menampilkan hasil tersebut kepada pengguna dalam bentuk skor dan kategori tingkat stres akademik. Seluruh proses ini berjalan secara real-time.

## Evaluasi dan Keterbatasan Sistem

Sistem yang dikembangkan masih memiliki beberapa keterbatasan. Dataset yang digunakan masih bersifat simulasi dan jumlah data yang digunakan relatif terbatas, sehingga hasil prediksi belum sepenuhnya mencerminkan kondisi nyata. Selain itu, variabel yang digunakan dalam sistem ini masih terbatas pada beberapa faktor utama.

Model Machine Learning yang digunakan juga masih menggunakan metode sederhana, sehingga tingkat akurasi prediksi masih dapat ditingkatkan. Oleh karena itu, hasil prediksi dari sistem ini tidak dimaksudkan sebagai alat diagnosis, melainkan sebagai gambaran awal mengenai tingkat stres akademik mahasiswa.

## Pengembangan Sistem ke Depan

Pengembangan sistem di masa depan dapat dilakukan dengan menambahkan dataset yang lebih besar dan menggunakan data asli agar hasil prediksi menjadi lebih akurat. Variabel input juga dapat diperluas dengan menambahkan faktor lain yang berkaitan dengan stres akademik mahasiswa.

Selain itu, metode Machine Learning yang digunakan dapat dikembangkan dengan mencoba algoritma lain yang lebih kompleks. Sistem juga dapat dikembangkan dengan menambahkan fitur rekomendasi atau saran berdasarkan hasil prediksi yang diperoleh.

## Kesimpulan Akhir

Student Academic Stress Prediction merupakan sistem berbasis web yang mengimplementasikan konsep Machine Learning untuk memprediksi tingkat stres akademik mahasiswa. Sistem ini menunjukkan bahwa Machine Learning dapat diterapkan ke dalam aplikasi web secara sederhana namun tetap fungsional.

Meskipun masih memiliki keterbatasan, sistem ini telah berhasil menggambarkan alur kerja Machine Learning mulai dari pengolahan data, pelatihan model, hingga implementasi ke dalam aplikasi berbasis web. Proyek ini diharapkan dapat menjadi dasar pembelajaran dan pengembangan sistem yang lebih kompleks di masa mendatang.
