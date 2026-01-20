# Student Academic Stress Prediction

## Pendahuluan

Student Academic Stress Prediction merupakan aplikasi berbasis web yang dirancang untuk memprediksi tingkat stres akademik mahasiswa dengan memanfaatkan metode Machine Learning. Aplikasi ini dibuat sebagai bagian dari tugas perkuliahan yang bertujuan untuk mengimplementasikan konsep pembelajaran mesin ke dalam sistem nyata berbasis web. Melalui sistem ini, pengguna dapat memperoleh gambaran awal mengenai kondisi stres akademik berdasarkan beberapa faktor yang sering dialami oleh mahasiswa dalam kehidupan perkuliahan sehari-hari.

Stres akademik merupakan permasalahan yang cukup umum terjadi di lingkungan pendidikan tinggi. Tekanan dari tugas, ujian, serta tuntutan akademik lainnya sering kali memengaruhi kondisi fisik dan mental mahasiswa. Jika tidak ditangani dengan baik, stres akademik dapat berdampak pada menurunnya motivasi belajar, konsentrasi, hingga performa akademik. Oleh karena itu, sistem ini diharapkan dapat menjadi alat bantu sederhana untuk memahami tingkat stres akademik mahasiswa berdasarkan faktor-faktor tertentu.

## Metode Machine Learning

Metode Machine Learning yang digunakan dalam proyek ini adalah Linear Regression. Pemilihan metode ini didasarkan pada kesederhanaan konsep serta kemampuannya dalam memodelkan hubungan linear antara variabel input dan output. Linear Regression juga mudah diinterpretasikan karena setiap variabel memiliki koefisien yang menunjukkan seberapa besar pengaruhnya terhadap hasil prediksi.

Selain itu, Linear Regression memiliki kompleksitas yang rendah dan relatif stabil ketika digunakan pada dataset berukuran kecil hingga menengah. Hal ini menjadikan metode ini cocok untuk diintegrasikan ke dalam aplikasi web tanpa memerlukan sumber daya komputasi yang besar. Dengan metode ini, proses prediksi dapat dilakukan secara cepat dan efisien.

## Dataset dan Variabel

Dataset yang digunakan pada proyek ini merupakan dataset simulasi yang disusun berdasarkan referensi umum mengenai stres akademik mahasiswa. Penggunaan dataset simulasi dilakukan karena keterbatasan akses terhadap dataset asli, namun tetap dirancang agar mencerminkan kondisi yang realistis. Dataset ini berisi beberapa variabel yang dianggap relevan terhadap tingkat stres akademik mahasiswa.

Variabel input yang digunakan meliputi tingkat tekanan akademik, jumlah jam tidur per malam, serta tekanan akibat ujian. Variabel-variabel tersebut dipilih karena sering menjadi faktor utama yang memengaruhi kondisi stres mahasiswa. Output dari dataset ini berupa skor tingkat stres akademik yang digunakan sebagai target prediksi oleh model Machine Learning.

## Proses Training Model

Proses pelatihan model dilakukan menggunakan bahasa pemrograman Python dengan bantuan library seperti Pandas dan Scikit-learn. Dataset yang telah disiapkan terlebih dahulu dipisahkan menjadi data latih dan data uji. Data latih digunakan untuk melatih model agar dapat mempelajari pola hubungan antar variabel, sedangkan data uji digunakan untuk mengevaluasi performa model.

Setelah proses pelatihan selesai, model Linear Regression yang telah terbentuk kemudian diuji untuk memastikan bahwa model mampu menghasilkan prediksi dengan baik. Model yang sudah dilatih selanjutnya disimpan dalam bentuk file agar dapat digunakan kembali tanpa perlu melakukan proses training ulang setiap kali aplikasi dijalankan.

## Backend dengan FastAPI

Backend aplikasi ini dibangun menggunakan framework FastAPI. Backend berfungsi sebagai penghubung antara frontend dan model Machine Learning. Data yang dimasukkan oleh pengguna melalui antarmuka web akan dikirim ke backend dalam format JSON, kemudian diproses oleh model yang telah dilatih.

FastAPI dipilih karena memiliki performa yang cepat, ringan, serta mudah digunakan untuk membangun REST API. Backend ini akan mengembalikan hasil prediksi berupa skor tingkat stres akademik yang selanjutnya akan ditampilkan pada frontend. Dengan adanya backend ini, proses prediksi dapat dilakukan secara terstruktur dan terpisah dari tampilan antarmuka pengguna.

## Frontend Aplikasi

Frontend aplikasi dikembangkan menggunakan HTML, Tailwind CSS, dan JavaScript. Desain antarmuka dibuat sederhana namun tetap interaktif agar mudah digunakan oleh pengguna. Pengguna dapat memasukkan nilai faktor-faktor stres akademik melalui form yang tersedia, kemudian menekan tombol prediksi untuk melihat hasilnya.

Selain menampilkan hasil prediksi dalam bentuk angka, frontend juga menampilkan kategori tingkat stres seperti rendah, sedang, atau tinggi. Visualisasi grafik digunakan untuk membantu pengguna memahami kontribusi setiap faktor yang dimasukkan terhadap hasil prediksi. Dengan tampilan yang interaktif, diharapkan pengguna dapat lebih mudah memahami hasil yang diberikan oleh sistem.

## Alur Kerja Sistem

Alur kerja sistem dimulai ketika pengguna mengakses halaman web dan mengisi data faktor stres akademik. Data tersebut kemudian dikirim ke backend melalui request HTTP. Backend akan memproses data tersebut menggunakan model Machine Learning yang telah dilatih sebelumnya.

Setelah proses prediksi selesai, backend akan mengirimkan hasil prediksi kembali ke frontend. Frontend kemudian menampilkan hasil tersebut kepada pengguna dalam bentuk skor dan kategori tingkat stres. Seluruh proses ini berjalan secara real-time sehingga pengguna dapat langsung melihat hasil prediksi setelah memasukkan data.

## Kesimpulan

Berdasarkan hasil implementasi yang dilakukan, sistem Student Academic Stress Prediction mampu memberikan prediksi tingkat stres akademik mahasiswa berdasarkan faktor-faktor sederhana. Proyek ini menunjukkan bahwa konsep Machine Learning dapat diimplementasikan ke dalam aplikasi web dengan cara yang relatif sederhana dan mudah dipahami.

Meskipun masih memiliki keterbatasan, terutama pada jumlah dan jenis dataset yang digunakan, sistem ini sudah cukup untuk menggambarkan alur kerja Machine Learning mulai dari pengolahan data, pelatihan model, hingga penerapan ke dalam aplikasi berbasis web. Diharapkan proyek ini dapat menjadi dasar untuk pengembangan sistem yang lebih kompleks di masa mendatang.
