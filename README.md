# SafareiPark
### An online inventory for a (fictional) safari park.
### Tautan aplikasi: https://safarei-park.adaptable.app/main/
---
### Pertanyaan Tugas 2
1. Langkah-langkah mengimplementasikan:
+ Membuat repositori baru di GitHub
+ Membuat repositori lokal untuk proyek ini
+ Melakukan konfigurasi Git untuk repositori lokal
+ Menghubungkan repositori lokal dengan repositori GitHub dengan ``git branch -M main`` dan ``git remote add origin https://github.com/reikathr/safarei-park``
+ Mengaktivasikan virtual environment
+ Menambahkan requirements.txt ke repositori lokal dan menginstall dependencies
+ Membuat proyek django dengan command ``django-admin startproject safarei_park.``
+ Mengatur ALLOWED_HOSTS dengan mengisinya dengan wildcard '*' agar proyek bisa diakses host/domain apapun.
+ Menjalankan server untuk memeriksa bahwa aplikasi saya berhasil dibuat
+ Keluar dari virtual environment
+ Menambahkan file .gitignore untuk menyertakan nama file yang tidak diinginkan di Git
+ Add, commit, dan push ke repositori GitHub yang sudah dibuat
+ Menambahkan aplikasi ke adaptable.io dengan New App > Connect Git Repository > Pilih reikathr/safarei-park > Choose a branch to deploy: main > Choose a Deploy Template > Pilih Python App Template > Pilih PostgreSQL > Masukkan versi Python yang sesuai: 3.9 > Isi Start Command dengan `python manage.py migrate && gunicorn safarei_park.wsgi`
+ Mengaktivasikan virtual environment
+ Membuat aplikasi main dengan `python manage.py startapp main`
+ Menambahkan 'main' ke list INSTALLED_APPS di settings.py (dalam direktori proyek)
+ Membuat direktori templates dalam main dan membuat main.html
+ Membuat berkas models.py di direktori aplikasi main yang memiliki class Items(models.Model) dengan atribut name, amount, description, dan category.
+ Mengupdate model dengan `python manage.py makemigrations` dan `python manage.py migrations`
+ Mengisi views.py di direktori aplikasi main yang akan menyambungkan antara models dan template
+ Memodifikasi template dengan atribut dalam models
+ Melakukan routing di urls.py dalam direktori aplikasi main dan direktori proyek safarei_park
+ Menjalankan dan membuka proyek
+ Membuat tests.py di main dan menambahkan test untuk memastikan path url ke /main/ dapat diakses dan sudah menggunakan template main.html
+ Menjalankan test dengan `python manage.py test`
+ Add, commit, dan push ke GitHub

2. Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya yang menjelaskan kaitan antara urls.py, views.py, models.py, dan berkas html.
![Bagan](Bagan.png)

3. Mengapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa virtual environment?
Kita menggunakan virtual environment untuk memastikan dependencies untuk setiap proyek terisolasi karena proyek-proyek berbeda dapat menggunakan dependecies yang berbeda sehingga kita harus mencegah dependencies tersebut bertabrakan. Kita dapat membuat aplikasi web berbasis Django tanpa virtual environment, tetapi tidak dianjurkan untuk alasan tersebut.

4. Apa MVC, MVT, MVVM?
+ MVC (Model-View-Controller): Model menyimpan data yang diperlukan sebuah aplikasi, View menyimpan komponen yang akan ditampilkan pada layar (UI), dan Controller menerima dan memproses input dari user lalu membuat perubahan pada Model dan View berdasarkan input tersebut. MVC digunakan dalam berbagai framework.
+ MVT (Model-View-Template): Model menyimpan data, View dapat mengambil data dalam model dan merender suatu template dengan data tersebut, Template menyimpan komponen yang akan ditampilkan (UI). MVT adalah pattern yang spesifik untuk Django. Template dalam MVT berperan seperti VIew dalam MVC dan MVVM.
+ MVVM (Model-View-ViewModel): Model menyimpan data, View menyimpan komponen yang ditampilkan (UI), ViewModel menyambungkan View dan Model. Perubahan pada ViewModel akan automatis berubah di View (dan sebaliknya) dengan data binding. MVVM digunakan dalam berbagai framework.

<hr>

### Pertanyaan Tugas 3
1. Apa perbedaan antara form `POST` dan form `GET` dalam Django? <br>
`POST` dan `GET` adalah dua method HTTP yang paling sering ditemukan. Beberapa perbedaan antara `POST` dan `GET` adalah sebagai berikut (dari [W3Schools](https://www.w3schools.com/tags/ref_httpmethods.asp)): <br>

| POST | GET |
|---|---|
|Tidak bisa di-*cache*|Bisa di-*cache*|
|Tidak tersimpan di riwayat *browser*|Tersimpan di riwayat *browser*|
|Tidak bisa di-*bookmark*|Bisa di-*bookmark*|
|Tidak ada batasan untuk panjang data|Ada batasan untuk panjang data|
|Tidak ada batasan tipe data, data biner pun diperbolehkan|Hanya bisa menyimpan ASCII|
|Tombol kembali dan *reload* akan menyebabkan data terkirim ulang|Tombol kembali dan *reload* tidak berpengaruh|
|Data yang terkirim tidak terlihat di URL|Data yang terkirim adalah bagian dari URL|
|Lebih aman karena data tidak tersimpan di riwayat browser|Kurang aman karena data tersimpan di riwayat *browser* dan data yang terkirim adalah bagian dari URL|

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML dan JSON berfungsi untuk menyimpan dan berinteraksi dengan data, sementara HTML berfungsi untuk menjelaskan bagaimana data tersebut akan ditampilkan. Beberapa perbedaan utama antara XML dan JSON adalah sebagai berikut: <br>

| XML | JSON |
|---|---|
|Menggunakan end tag|Tidak menggunakan end tag|
|Lebih panjang|Lebih *compact*|
|Menyimpan data dalam *tree structure*|Menyimpan data dalam pasangan key-value seperti map|
|Lebih lama untuk di-*parse*|Bisa di-*parse* dengan lebih cepat|
|Tidak bisa menggunakan arrays|Bisa menggunakan arrays|

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena kelebihannya dibandingkan XML, seperti sintaks yang membuat informasi yang disimpan oleh JSON menjadi *compact*, sifat *lightweight*-nya, dan kemudahan untuk di-*parse* tanpa kode tambahan.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
+ Menyalakan virtual environment dengan menjalankan `env\Scripts\activate.bat` di terminal
+ Membuat direktori baru di root directory bernama templates dan membuat berkas base.html di direktori tersebut. base.html ini menjadi template untuk berkas html lain.
+ Menambahkan template tersebut ke list TEMPLATES di direktori proyek safarei_park > settings.py
+ Memodifikasi berkas main.html di direktori app main untuk menyesuaikan dengan base.html
+ Memodifikasi models.py (saya menambahkan atribut baru, yaitu family dan animal_class, dan mengubah nama model menjadi Animal, yang sebelumnya adalah Item)
+ Membuat berkas forms.py di direktori app main yang berisi <br>
    ```python
    from django.forms import ModelForm
    from main.models import Animal

    class AnimalForm(ModelForm):
        class Meta:
            model = Animal
            fields = ["name", "amount", "family", "animal_class", "description"]
    ```
+ Menambahkan beberapa line berikut ke bagian atas berkas views.py di direktori main
    ``` python
    from django.http import HttpResponseRedirect
    from main.forms import AnimalForm
    from main.models import Animal
    from django.urls import reverse
    ```
+ Membuat fungsi baru di views.py yaitu
    ```python
    def create_animal(request):
        form = AnimalForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "create_animal.html", context)
    ```
+ Mengubah fungsi show_main menjadi:
    ``` python
    def show_main(request):
    animals = Animal.objects.all()

    context = {
        'name': 'Athira Reika',
        'class': 'PBP F',
        'animals': animals
    }

    return render(request, "main.html", context)
    ```
+ Membuat berkas create_animal.html di main > templates dengan isi sebagai berikut:
``` html
    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Animal</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Animal"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
```
+ Menambahkan kode berikut ke main.html
```html
    <table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Family</th>
            <th>Class</th>
            <th>Description</th>
            <th>Date Added</th>
        </tr>

        {% for animal in animals %}
            <tr>
                <td>{{animal.name}}</td>
                <td>{{animal.amount}}</td>
                <td>{{animal.family}}</td>
                <td>{{animal.animal_class}}</td>
                <td>{{animal.description}}</td>
                <td>{{animal.date_added}}</td>
            </tr>
        {% endfor %}
    </table>

    <br />

    <a href="{% url 'main:create_animal' %}">
        <button>
            Add New Animal
        </button>
    </a>

{% endblock content %}
```
+ Mengimport create_animal ke urls.py
+ Menambah path berikut ke urlpatterns di main > urls.py
```python
    path('create-animal', create_animal, name='create_animal')
```
+ Melakukan migration karena telah melakukan perubahan pada model dengan menjalankan `python manage.py makemigrations` lalu `python manage.py migrate`
+ Menjalankan proyek dengan menjalankan `python manage.py runserver`, membuka https://localhost:8000, dan menambahkan data di forms
+ Menambahkan import di main > views.py
```python
    from django.http import HttpResponse
    from django.core import serializers
```
+ Menambahkan beberapa fungsi ke views.py untuk melihat objek yang telah ditambahkan di XML, JSON, XML by ID, dan JSON by ID
```python
    ...
    def show_xml(request):
        data = Animal.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = Animal.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Animal.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Animal.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
+ Menambahkan beberapa import di main > urls.py
```python
    from main.views import show_main, create_animal, show_xml, show_json, show_xml_by_id, show_json_by_id 
```
+ Menambahkan beberapa path ke urlpatterns di urls.py
```python
    ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id')
```
+ Routing untuk semua fungsi di main > views.py selesai

### Mengakses create_animal, show_xml, show_json, show_xml_by_id, show_json_by_id dengan Postman.
+ /create-animal <br>
![/create-animal](create-animal.png)
+ /xml <br>
![/xml](xml.png)
+ /json <br>
![/json](json.png)
+ /xml/1 <br>
![/xml/1](xmlbyid.png)
+ /json/1 <br>
![/json/1](jsonbyid.png)
