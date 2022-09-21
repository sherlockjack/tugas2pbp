## Perbedaan JSON, HTML, XML
JSON: Objek Notasi dari Java Script, Berbasis dari Java Script, Selalu mempresentasikan objek, Bisa mensupport Arrays,  Hanya bisa di UTF-8
XML: Extensible Markup Language, berasal dari SGML, Markup language, Tidak mensupport Array, Lebih aman daripada JSON, ada banyak Encoding
HTML: Case tidak sensitif, Beberapa tags tidak memerlukan penutup, Hanya fokus untuk menampilkan Data, Membantu untuk menstruktur situs Web

## Pentingnya Implementasi Data Delivery kedalam Platform
Untuk membawakan sebuah data dari backend ke frontend yaitu User sehingga User bisa menikmati dan melihat data tersebut. Sebaliknya User juga bisa mengirim data dari tempat user ke database.

## Implementasi Checklist Tugas 3
Pertama tama menjalankan ```python manage.py startapp mywatchlist``` untuk membuat aplikasi `mywatchlist`.
mywatchlist akan ada di local, setelah itu saya menambahkan fixtures dan templatesnya saya buat datanya setelah itu saya mengisi data di initial_watchlist_data.json. Membuat template, setelah itu saya mengisi Views dengan beberapa fungsi dan return, setelah itu saya buat di models, nama app dan habis itu saya mengisi path dan saya mengisi procfile.
setelah itu saya ```py manage.py loaddata initial_watchlist_data.json```.
Dan setelah itu
```
python manage.py makemigrations
python manage.py migrate
```
dan setelah itu saya deploy

### Pemeriksaan _Routes_ dengan Postman

1. `~/mywatchlist/html`<br><br>

   ![postman_HTML_Tugas]https://github.com/sherlockjack/tugas2pbp/blob/main/mywatchlist/1pbp.JPG
2. `~/mywatchlist/json`<br><br>
   ![postman_JSON_Tugas]https://github.com/sherlockjack/tugas2pbp/blob/main/mywatchlist/3pbp.JPG

3. `~/mywatchlist/xml`<br><br>
   ![postman_XML_Tugas]https://github.com/sherlockjack/tugas2pbp/blob/main/mywatchlist/2pbp.JPG