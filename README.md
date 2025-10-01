https://dhea-anggrayningsih41-naiki.pbp.cs.ui.ac.id

TUGAS 2
----------------------------------------------------------------------------------------------------
1. Langkah-langkahnya sebagai berikut:
- Saya memulai dengan membuat repository Naiki di GitHub lalu melakukan git clone ke lokal
- Menginstall dependencies yang nanti akan digunakan lalu startproject naiki
- Konfigurasi .env dan .env.prod sesuai kredensial database. Kemudian, modifikasi settings.py, khususnya menambahkan ALLOWED_HOST untuk deployment
- Selanjutnya, migrasi database dan runserver django. Buat .gitignore agar hanya file yang dibutuhkan yang di-push ke git
- Create project di PWS, add PWS ke repository, dan tambahkan URL deployment ke ALLOWED_HOST agar projek bisa diakses melalui link tersebut
- Membuat aplikasi main dan didaftarkan ke INSTALLED_APPS
- Memodifikasi isi models.py dengan ketentuan atribut PRODUCT pada tugas. Lalu, mendefinisikan fungsi show_main di views.py untuk dimunculkan ke templates (main.html)
- Terakhir, melakukan URL routing di urls.py milik aplikasi naiki untuk menyambungkan dengan root ke aplikasi main dan urls.py milik main untuk menghubungkan ke views.py

2. https://drive.google.com/file/d/1JCOiGd4KIRMZ0EnfymyfYxwIRPidZboJ/view?usp=drivesdk

3. Settings.py bisa diibaratkan sebagai buku aturan dari projek Django. Isinya konfigurasi elemen-elemen yang dibutuhkan dalam projek tersebut.  Sejauh ini, saya sudah memodifikasi 4 hal dalam settings:
- Import load_dotenv agar bisa load isi .env
- Menambahkan daftar ALLOWED_HOST agar projek diizinkan untuk dilihat melalui host local dan PWS
- Menambah konfigurasi PRODUCTION
- Mengubah konfigurasi database sesuai ketentuan

4. Migrasi model merupakan cara Django tracking perubahan yang dibuat programmer. Tiap kali perubahan dibuat di aplikasi yang termasuk dalam INSTALLED_APP, programmer harus melakukan python3 manage.py makemigrations untuk menciptakan berkas migrasi perubahan model sebelum diimplementasikan ke basis data. Setelah itu, programmer melakukan python3 manage.py migrate untuk mengimplementasikan berkas tadi ke basis data

5. Karena bahasa yang digunakan adalah python yang mana mahasiswa sudah familiar dari DDP1. Selain itu, Django cukup dikenal sebagai framework yang ramah pemula. Framework ini juga sudah dilengkapi banyak fitur bawaan yang siap pakai, seperti proteksi keamanan, routing, dan autentikasi

6. Tidak ada, sudah baik sekali. Semangat kakak-kakak asdosss



TUGAS 3
----------------------------------------------------------------------------------------------------
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
== Karena jika tidak ada data delivery maka tidak akan ada data yang digunakan dalam platform tersebut. User sama sekali tidak berinteraksi pada data di platform sehingga menurunkan fungsionalitas platform. Kalau tidak ada data delivery, platform nya static, padahal platform seharusnya usable agar informasi tersampaikan ke user.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
== JSON. Banyak peramban yang memakai JSON karena keunggulan utamanya adalah ukuran datanya saat dikirim melalui jaringan lebih kecil dibanding XML. Strukturnya juga sederhana, berupa key-value, seperti high-level language pada umumnya.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
== Digunakan untuk cek apakah data yang diinput user. is_valid akan mengeluarkan True jika field required sudah diisi semua, data field sesuai dengan yang sudah di-define, batasan yang diterapkan pada field, dan lainnya. Intinya, is_valid mengecek data input dari user sebelum data tersebut diproses ataupun di-load ke database

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
== csrf_token adalah kode unik yang otomatis di-generate saat session baru dijalankan. Token ini akan expired kalau session sudah habis (misal, logout atau timeout). Token ini dibandingkan oleh Django dengan token sesi user saat ini. Ketika input dari user akan diproses oleh form, jika token berbeda maka input tadi tidak akan diproses (mengembalikan error). Kalau tidak ada csrf_token, website akan memproses apapun yang terjadi tanpa validasi. Penyerang memanfaatkan ini dengan membuat link yang direct sesuai keinginannya sehingga website tetap akan memproses walaupun itu bukan keinginan user. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
== 
- Membuat method show_json dan show_XML yang memungkinkan Django return data dalam format XML dan JSON 
- Method by_id agar Django return data dengan id tertentu dalam format JSON atau XML
- Routing URL di urls.py direktori main dengan import semua method dari views agar Django bisa menentukan views mana yang harus dijalankan saat keadaan tertentu
- Menambahkan method add_product untuk menambahkan produk (direct ke add_product.html) dan show_product (direct ke show_product.html) di views dan melakukan routing
- Membuat template base.html agar template ini bisa 'diimport' template lainnya untuk mendapatkan struktur umum yang sama
- Membuat add_product.html yang akan menjadi halaman bagi forms.py agar user bisa menginput data sesuai fields yang disediakan di sana. Lalu, show_product.html sebagai halaman ketika button Product Details diklik, isinya detail dari product dan keseluruhan product description
- Menambahkan CSRF_TRUSTED_ORIGINS di settings.py agar domain dianggap aman untuk menginput data
- Membuat isi forms.py supaya ketika user klik add_product, user harus mengisi fields "name", "price", "description", "thumbnail", "category", "is_featured" untuk launch product
- Di luar checklists: saya juga melakukan penambahan dan pengurangan pada models, seperti attributes id agar method dalam views bisa mudah mengenali permintaan spesifik, fitur like product (attributes dan methodnya), dan default thumbnail apabila user tidak ingin input gambar apapun. Selain itu, saya menambahkan method like_product di views untuk handle ketika button "love" diklik

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
== Tidak adaa

7. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
== https://drive.google.com/drive/folders/1osWzuRcTFN9mNEVQUTvYGtt3vhIF4FaY?usp=sharing



TUGAS 4
----------------------------------------------------------------------------------------------------
1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
AuthenticationForm adalah form yang handling ketika ada user yang ingin mengakses aplikasi tersebut. Form ini menerima input autentikasi user dan memvalidasi username password dengan database
Kelebihan: praktis karena bisa langsung memakai fitur bawaan dari Django (contoh, login(request, user)), membuat aplikasi lebih aman, terintegrasi langsung dengan Django
Kekurangan: hanya mendukung username dan password, ketentuan untuk username dan password tidak fleksibel (kecuali ingin override), error message default saat terjadi kesalahan login tidak spesifik

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi adalah proses validasi identitas user ke dalam aplikasi sedangkan otorisasi adalah pembatasan oleh aplikasi, seperti hanya user tertentu yang bisa mengakses suatu halaman. Django mengimplementasikan autentikasi dengan mengakomodasi AuthenticationForm yang bisa diimplementasi di fungsi login pada views.py. Django mengimplementasikan otorisasi salah satunya dengan @login_required(login_url='/login') 

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Kelebihan: 
    Session: Kapasitasnya bisa menampung data kompleks, lebih aman karena tersimpan bukan di user, sulit dimodifikasi user secara langsung
    Cookies: Disimpan di browser user sehingga tidak memberatkan server, bisa persistent cookie, mudah diakses
Kekurangan:
    Session: Tempat penyimpanannya di server, hilang saat session expired, kompleksitas lebih tinggi karena harus membagi data session per-user
    Cookies: Kapasitasnya hanya sekitar 4kb, data bisa dilihat user, kurang memungkinkan untuk menyimpan data besar

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Tidak selalu aman karena cookies bisa dengan mudah diakses user, terlebih jika tidak dilakukan enkripsi. Risiko potensialnya adalah pencurian cookie ataupun cross-site scripting. Django menanganinya dengan menyediakan fitur-fitur keamanan bawaan, seperti Secure, CSRF token, ataupun pengaturan expire cookie untuk timeout user

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Pertama, saya membuat fungsi register untuk laman pendaftaran akun user di views.py milik main, lalu dikeluarkan ke register.html
- Membuat fungsi handle login (halaman pertama yang dilihat user untuk mengakses aplikasi), setelahnya menambahkan @login_required ke fungsi-fungsi yang perlu autentikasi sebelum diakses
- Membuat fungsi logout untuk hanlde tombol logout di paling bawah page
- Menambahkan last_login agar browser user bisa menyimpan cookie (sesi) saat ini, kemudian ditampilkan sebagai sesi terakhir login di aplikasi
- Menghubungkan antara Product dan user dengan menambahkan atribut user di models.py. Lalu, membuat nama orang yang login muncul di aplikasi saat create product dengan request.user.username
- Saya memodifikasi dan membuat beberapa file html yang digunakan sebagai tampilan
- Tidak lupa, saya melakukan routing ke fungsi-fungsi views.py yang baru ditambahkan



TUGAS 5
----------------------------------------------------------------------------------------------------
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Browser akan memilih aturan dengan prioritas paling tinggi. Prioritasi ini terjadi karena HTML menggunakan banyak CSS. Urutan pengambilannya adalah inline style (langsung di dalam <>), id selector, class attributes seperti hover:, dan element selector. Jika terdapat aturan dengan tingkat prioritas yang sama, maka aturan yang ditulis paling terakhir di file CSS yang akan digunakan. Selain itu, terdapat juga deklarasi !important yang bisa mengalahkan semua aturan lainnya, bahkan inline style.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa! 
Responsive design memastikan semua tampilannya dalam berbagai device sama dalam artian tetap rapi dan aksesibel walau berbeda device. Contohnya yang menggunakan responsive design adalah YouTube. Contoh yang tidak menggunakan responsive design adalah website latihan saya saat codingcamp... saat itu belum paham mengenai hal ini, jadi website nya kompatibel di laptop saja

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Ketiganya bisa diletakkan di inline CSS ataupun external css (style.css)
Margin adalah jarak antarelemen, misalnya elemen button bisa tidak terlalu pinggir. Bisa diletakkan dengan margin:20px
Border merupakan outline atau garis tepi label. Contohnya border:2px
Padding memberi jarak antara konten dan elemennya, misalnya text dengan label. Contoh penggunaan di padding:15px

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Grid layout membagi halaman web menjadi bagian-bagian tertentu. Berfungsi untuk memudahkan developer dalam untuk menempatkan elemen karena sudah ada petak-petak yang ditentukan
Flexbox digunakan agar elemen-elemennya bisa rapi, tersusun secara fleksibel, dan tidak memerlukan posisi yang di hard code. Contohnya, align-items: center yang membuat elemen diletakkan di center tanpa harus diatur jarak x dan y nya

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- Membuat fungsi edit, beserta konfigurasinya (urls, function di views, dan template html). Setelah itu menambahkan tombol Edit
- Membuat fungsi delete, beserta konfigurasinya (urls, function di views, dan template html). Setelah itu menambah button di sebelah edit yang bisa digunakan oleh user yang memiliki product tersebut
- Modifikasi navbar
- Memodifikasi tampilan pada templates agar website sesuai dengan color palette
- Menambahkan no.png yang menampilkan foto jika belum ada produk yang ditambahkan
