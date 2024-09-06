
# ASMARA Backend - Django

Ini adalah backend dari aplikasi **ASMARA (Aspirasi Masyarakat)** yang dikembangkan menggunakan **Django**. Backend ini bertanggung jawab untuk menangani API REST, otentikasi pengguna, pengelolaan data aspirasi, dan interaksi dengan basis data.

## Persyaratan Sistem:
- Python 3.8 atau lebih baru
- Django 4.0 atau lebih baru
- PostgreSQL/MySQL/SQLite (pilih sesuai preferensi)
- Git

---

## Cara Instalasi dan Menjalankan Project

### 1. Clone Repository
Clone repository ini dari GitHub:
```bash
https://github.com/kevinalfito69/ASMARA-BackEnd/
cd ASMARA-BackEnd
```


### 2. Install Dependensi
Install semua dependensi proyek yang tercantum di file `requirements.txt`:
```bash
pip install django
```

### 3. Migrasi Database
Setelah konfigurasi database sudah diatur, jalankan migrasi untuk menginisialisasi skema database:
```bash
python manage.py migrate
```

### 4. Buat Superuser (Opsional)
Buat superuser untuk mengakses admin panel Django:
```bash
python manage.py createsuperuser
```

### 5. Jalankan Development Server
Jalankan server lokal untuk memulai pengembangan:
```bash
python manage.py runserver
```
Server akan berjalan di `http://127.0.0.1:8000/` secara default.
