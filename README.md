https://dhea-anggrayningsih41-naiki.pbp.cs.ui.ac.id

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