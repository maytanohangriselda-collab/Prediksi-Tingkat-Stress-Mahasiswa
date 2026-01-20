# Student Academic Stress Prediction

**Nama** : Mayta Nohan Griselda  
**NIM** : 2441044  
**Program Studi** : Sistem Informasi  
**Perguruan Tinggi** : STMIK AMIK Bandung  
**Mata Kuliah** : Machine Learning  

---

## Pendahuluan

Student Academic Stress Prediction merupakan sebuah aplikasi berbasis web yang dikembangkan untuk memprediksi tingkat stres akademik mahasiswa dengan memanfaatkan metode Machine Learning. Aplikasi ini dirancang sebagai media pembelajaran untuk memahami bagaimana data akademik sederhana dapat digunakan dalam proses prediksi menggunakan model pembelajaran mesin.

Proyek ini dibuat sebagai bagian dari tugas mata kuliah Machine Learning dengan tujuan menerapkan konsep teori ke dalam bentuk sistem nyata yang dapat dijalankan dan diakses melalui web. Sistem ini mengintegrasikan antarmuka pengguna (frontend), layanan backend berbasis API, serta model Machine Learning sebagai inti dari proses prediksi.

Stres akademik merupakan kondisi yang umum dialami oleh mahasiswa akibat tekanan tugas, ujian, manajemen waktu, serta kurangnya waktu istirahat. Oleh karena itu, sistem ini diharapkan dapat memberikan gambaran awal mengenai tingkat stres akademik yang dialami mahasiswa berdasarkan beberapa faktor yang sering terjadi di lingkungan perkuliahan.

---

## Tujuan dan Manfaat Sistem

Tujuan utama dari pengembangan Student Academic Stress Prediction adalah membangun sebuah aplikasi berbasis web yang mampu memprediksi tingkat stres akademik mahasiswa menggunakan pendekatan Machine Learning. Sistem ini bertujuan untuk menunjukkan alur lengkap penerapan Machine Learning, mulai dari pengolahan data hingga integrasi model ke dalam aplikasi web.

Manfaat dari sistem ini antara lain membantu mahasiswa memperoleh gambaran awal mengenai kondisi stres akademik yang dialami. Dari sisi akademik, proyek ini dapat digunakan sebagai contoh implementasi Machine Learning secara sederhana namun terstruktur, khususnya dalam pengembangan sistem berbasis web.

---

## Fitur Sistem

Aplikasi Student Academic Stress Prediction menyediakan fitur input data akademik melalui antarmuka web yang interaktif. Pengguna dapat memasukkan tingkat tekanan akademik, jumlah jam tidur per malam, serta faktor utama penyebab stres akademik.

Setelah data dimasukkan, sistem akan menampilkan hasil prediksi berupa skor tingkat stres akademik. Selain skor numerik, sistem juga menampilkan kategori tingkat stres seperti rendah, sedang, atau tinggi agar hasil prediksi lebih mudah dipahami oleh pengguna.

Aplikasi ini juga dilengkapi dengan visualisasi grafik untuk membantu pengguna memahami kontribusi masing-masing faktor terhadap tingkat stres. Efek visual dan musik latar ditambahkan untuk meningkatkan pengalaman pengguna tanpa mengganggu fungsi utama sistem.

---

## Metode Machine Learning

Metode Machine Learning yang digunakan dalam sistem ini adalah Linear Regression. Algoritma ini dipilih karena memiliki konsep yang sederhana, mudah dipahami, serta sesuai untuk kebutuhan pembelajaran dasar Machine Learning.

Linear Regression bekerja dengan memodelkan hubungan linear antara beberapa variabel input dengan satu variabel output. Dalam sistem ini, hubungan tersebut digunakan untuk memprediksi skor tingkat stres akademik mahasiswa berdasarkan faktor-faktor akademik yang dimasukkan.

---

## Dataset dan Variabel

Dataset yang digunakan dalam proyek ini merupakan dataset simulasi yang disusun untuk merepresentasikan kondisi stres akademik mahasiswa. Dataset ini dibuat dengan mempertimbangkan faktor-faktor yang umum memengaruhi tingkat stres dalam lingkungan perkuliahan.

Variabel input yang digunakan meliputi tingkat tekanan akademik, jumlah jam tidur per malam, serta faktor utama penyebab stres akademik. Variabel output dari sistem ini adalah skor tingkat stres akademik yang digunakan sebagai target dalam proses pelatihan model Machine Learning.

---

## Proses Training Model

Proses pelatihan model dilakukan menggunakan bahasa pemrograman Python dengan bantuan library Pandas dan Scikit-learn. Dataset dibagi menjadi data latih dan data uji untuk memastikan bahwa model dapat mempelajari pola data dengan baik.

Model Linear Regression dilatih menggunakan data latih, kemudian diuji menggunakan data uji untuk melihat kestabilan hasil prediksi. Setelah proses pelatihan selesai, model disimpan dalam bentuk file agar dapat digunakan kembali pada backend tanpa perlu melakukan proses training ulang.

---

## Evaluasi Model

Evaluasi model dilakukan dengan membandingkan hasil prediksi model terhadap data uji yang telah disiapkan. Proses evaluasi ini bertujuan untuk memastikan bahwa model mampu menghasilkan prediksi yang masuk akal berdasarkan data input yang diberikan.

Evaluasi dilakukan secara sederhana karena fokus utama proyek ini adalah pembelajaran konsep Machine Learning dan implementasinya ke dalam aplikasi web, bukan pada optimasi akurasi model secara mendalam.

---

## Arsitektur Sistem

Arsitektur sistem Student Academic Stress Prediction terdiri dari tiga komponen utama, yaitu frontend, backend, dan model Machine Learning. Frontend berfungsi sebagai antarmuka pengguna untuk memasukkan data dan menampilkan hasil prediksi.

Backend berperan sebagai penghubung antara frontend dan model Machine Learning melalui REST API. Model Machine Learning digunakan sebagai inti sistem untuk melakukan proses prediksi tingkat stres akademik.

---

## Backend dengan FastAPI

Backend aplikasi dibangun menggunakan framework FastAPI. FastAPI dipilih karena memiliki performa yang cepat, ringan, serta mendukung pengembangan REST API dengan struktur yang jelas.

Backend bertugas menerima data input dari frontend, memproses data menggunakan model Machine Learning yang telah dilatih, dan mengembalikan hasil prediksi ke frontend dalam format JSON.

---

## Frontend Aplikasi

Frontend aplikasi dikembangkan menggunakan HTML, Tailwind CSS, dan JavaScript. Antarmuka dirancang agar mudah digunakan dan interaktif sehingga pengguna dapat dengan mudah memasukkan data dan melihat hasil prediksi.

Hasil prediksi ditampilkan secara real-time disertai grafik visualisasi untuk membantu pengguna memahami hasil yang diberikan oleh sistem.

---

## Alur Penggunaan Aplikasi

Pengguna membuka halaman web aplikasi dan mengisi data faktor stres akademik yang tersedia. Setelah itu, pengguna menekan tombol prediksi untuk memulai proses perhitungan.

Data yang dimasukkan dikirim ke backend melalui API untuk diproses oleh model Machine Learning. Backend kemudian mengembalikan hasil prediksi yang selanjutnya ditampilkan pada halaman web.

---

## Cara Menjalankan Aplikasi

Aplikasi dapat dijalankan secara lokal dengan menjalankan server backend menggunakan FastAPI. Setelah backend aktif, frontend dapat dibuka melalui browser dan dihubungkan ke endpoint API yang tersedia.

Dengan konfigurasi tersebut, aplikasi siap digunakan untuk melakukan prediksi tingkat stres akademik mahasiswa.

---

## Keterbatasan Sistem

Sistem ini masih memiliki beberapa keterbatasan, seperti penggunaan dataset simulasi dan jumlah variabel input yang masih terbatas. Model Machine Learning yang digunakan juga masih bersifat sederhana.

Oleh karena itu, hasil prediksi dari sistem ini tidak dimaksudkan sebagai alat diagnosis, melainkan sebagai media pembelajaran dan simulasi penerapan Machine Learning.

---

## Pengembangan Sistem ke Depan

Pengembangan selanjutnya dapat dilakukan dengan menambahkan dataset yang lebih besar dan menggunakan data nyata. Variabel input juga dapat diperluas dengan menambahkan faktor lain yang memengaruhi stres akademik mahasiswa.

Selain itu, metode Machine Learning yang lebih kompleks dapat digunakan untuk meningkatkan kualitas dan akurasi prediksi sistem.

---

## Kesimpulan

Student Academic Stress Prediction merupakan aplikasi berbasis web yang berhasil mengimplementasikan konsep Machine Learning untuk memprediksi tingkat stres akademik mahasiswa. Sistem ini menunjukkan alur lengkap penerapan Machine Learning mulai dari pengolahan data hingga integrasi ke dalam aplikasi web.

Proyek ini diharapkan dapat menjadi sarana pembelajaran dan dasar pengembangan sistem prediksi yang lebih kompleks di masa mendatang.
