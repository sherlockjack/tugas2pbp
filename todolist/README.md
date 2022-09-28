https://reioudjangopbp.herokuapp.com/todolist/


## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

Digunakan untuk menangkal serangan CSRF atau cross-site request forgery. csrf token sendiri membuat kita mendapatkan kode unik untuk setiap user. Nilai token ini dibuat unik secara random untuk melindungi user dari serangan CSRF. Serangan CSRF adalah serangan dimana situs lain menggunakan domain lain mengirim perintah atas nama user disitus tersebut. Jika kita tidak menggunakan csrf token kita tidak bisa mengetahui apakah itu benar benar user

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Tentu saja! Kita membuat formnya secara manual dengan cara membuat inputnya sendiri...
Akan tetapi hal pentingnya bukan disitu!! Tetapi pada views.py kita membuat POST baru dan membuat sebuah key baru yaitu form yang saya ambil dari fungsi Taskforms.


## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

1. User mengirim request 
2. View mendapatkan hasil dari request yang diambil oleh POST
3. Request akan diambil kedalam CRUD yang ada di views.py
4. View dapat data yang udah termanipulasi pada context
5. Data dari views akan dirender dan diberikan kedalam template

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Membuat django-admin startapp todolist
2. Membuat di settings.py yang ada di INSTALED_APPS
3. Menambahkan URLS di project_django
4. Membuat models.py sesuai kebutuhan
5. Jalananin makemigration dan migrate
6. Mengimplementasikan login register dan utama di models.py, dan membuat halaman utama login dan register di templates
7. Membuat tombol task baru dan logout
8. Membuat halaman pembuatan task dan membuat fungsinya di views.py
9. Menambah path alamat yang diperlukan (fungsi) ke urls.py todolist
10. Deploy ke heroku
11. Selesai
