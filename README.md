Tautan aplikasi: https://safarei-park.adaptable.app/main/

1. Langkah-langkah mengimplementasikan:
- Membuat repositori baru di GitHub
- Membuat repositori lokal untuk proyek ini
- Melakukan konfigurasi Git untuk repositori lokal
- Menghubungkan repositori lokal dengan repositori GitHub dengan ``git branch -M main`` dan ``git remote add origin https://github.com/reikathr/safarei-park``
- Mengaktivasikan virtual environment
- Menambahkan requirements.txt ke repositori lokal dan menginstall dependencies
- Membuat proyek django dengan command ``django-admin startproject safarei_park.``
- Mengatur ALLOWED_HOSTS dengan mengisinya dengan wildcard '*' agar proyek bisa diakses host/domain apapun.
- Menjalankan server untuk memeriksa bahwa aplikasi saya berhasil dibuat
- Keluar dari virtual environment
- Menambahkan file .gitignore untuk menyertakan nama file yang tidak diinginkan di Git
- Add, commit, dan push ke repositori GitHub yang sudah dibuat
- Menambahkan aplikasi ke adaptable.io dengan New App > Connect Git Repository > Pilih reikathr/safarei-park > Choose a branch to deploy: main > Choose a Deploy Template > Pilih Python App Template > Pilih PostgreSQL > Masukkan versi Python yang sesuai: 3.9 > Isi Start Command dengan `python manage.py migrate && gunicorn safarei_park.wsgi`
- Mengaktivasikan virtual environment
- Membuat aplikasi main dengan `python manage.py startapp main`
- Menambahkan 'main' ke list INSTALLED_APPS di settings.py (dalam direktori proyek)
- Membuat direktori templates dalam main dan membuat main.html
- Membuat berkas models.py di direktori aplikasi main yang memiliki class Items(models.Model) dengan atribut name, amount, description, dan category.
- Mengupdate model dengan `python manage.py makemigrations` dan `python manage.py migrations`
- Mengisi views.py di direktori aplikasi main yang akan menyambungkan antara models dan template
- Memodifikasi template dengan atribut dalam models
- Melakukan routing di urls.py dalam direktori aplikasi main dan direktori proyek safarei_park
- Menjalankan dan membuka proyek
- Membuat tests.py di main dan menambahkan test untuk memastikan path url ke /main/ dapat diakses dan sudah menggunakan template main.html
- Menjalankan test dengan `python manage.py test`
- Add, commit, dan push ke GitHub

2. Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya yang menjelaskan kaitan antara urls.py, views.py, models.py, dan berkas html.

3. Mengapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa virtual environment?
Kita menggunakan virtual environment untuk memastikan dependencies untuk setiap proyek terisolasi karena proyek-proyek berbeda dapat menggunakan dependecies yang berbeda sehingga kita harus mencegah dependencies tersebut bertabrakan. Kita dapat membuat aplikasi web berbasis Django tanpa virtual environment, tetapi tidak dianjurkan untuk alasan tersebut.

4. Apa MVC, MVT, MVVM?
- MVC (Model-View-Controller): Model menyimpan data yang diperlukan sebuah aplikasi, View menyimpan komponen yang akan ditampilkan pada layar (UI), dan Controller menyambungkan Model dan View.
- MVT (Model-View-Template): Model menyimpan data, View dapat mengambil data dalam model dan merender suatu template dengan data tersebut, Template menyimpan komponen yang akan ditampilkan (UI).
- MVVM (Model-View-ViewModel): Model menyimpan data, View menyimpan komponen yang ditampilkan (UI), ViewModel menyambungkan View dan Model.
