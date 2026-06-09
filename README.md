# 📊 Sistem Informasi Kas dan Data Karyawan

Aplikasi berbasis Django yang dirancang untuk membantu pengelolaan transaksi keuangan perusahaan secara terkomputerisasi. Sistem ini menyediakan fitur pencatatan kas masuk, kas keluar, pengelolaan data karyawan, buku besar, neraca saldo, serta pembuatan laporan dalam format PDF dan Excel.

## ✨ Fitur Utama

### 🔐 Autentikasi Pengguna

* Login pengguna
* Logout pengguna
* Proteksi halaman menggunakan sistem autentikasi Django

### 💰 Manajemen Kas Masuk

* Menampilkan data kas masuk
* Menambahkan transaksi kas masuk
* Mengubah data kas masuk
* Menghapus data kas masuk
* Export laporan PDF
* Export laporan Excel

### 💸 Manajemen Kas Keluar

* Menampilkan data kas keluar
* Menambahkan transaksi kas keluar
* Mengubah data kas keluar
* Menghapus data kas keluar
* Filter transaksi berdasarkan rentang tanggal
* Export laporan PDF
* Export laporan Excel

### 👨‍💼 Manajemen Data Karyawan

* Menampilkan data karyawan
* Menambahkan data karyawan
* Mengubah data karyawan
* Menghapus data karyawan

### 📚 Buku Besar

* Menampilkan seluruh transaksi kas masuk dan kas keluar
* Perhitungan saldo berjalan (running balance)
* Menampilkan total debit
* Menampilkan total kredit
* Menampilkan saldo akhir

### 📈 Neraca Saldo

* Menampilkan total debit
* Menampilkan total kredit
* Menampilkan saldo akhir

### 📋 Dashboard

* Total kas masuk
* Total kas keluar
* Saldo kas
* Total transaksi
* Daftar transaksi terbaru
* Ringkasan kondisi keuangan perusahaan

## 🛠️ Teknologi yang Digunakan

* Python 3
* Django
* Bootstrap 5
* SQLite
* OpenPyXL
* ReportLab

## 🚀 Instalasi

Clone repository:

```bash
git clone https://github.com/sahrulashar/sistem_informasi_keuangan.git
```

Masuk ke direktori proyek:

```bash
cd nama-repository
```

Buat virtual environment:

```bash
python -m venv venv
```

Aktifkan virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/MacOS:

```bash
source venv/bin/activate
```

Install dependency:

```bash
pip install -r requirements.txt
```

Jalankan migrasi database:

```bash
python manage.py migrate
```

Jalankan server:

```bash
python manage.py runserver
```

Akses aplikasi melalui browser:

```text
http://127.0.0.1:8000/
```

## 📂 Struktur Fitur Sistem

```text
Dashboard
│
├── Kas Masuk
│   ├── Data Kas Masuk
│   ├── Tambah Kas Masuk
│   ├── Edit Kas Masuk
│   ├── Hapus Kas Masuk
│   ├── Export PDF
│   └── Export Excel
│
├── Kas Keluar
│   ├── Data Kas Keluar
│   ├── Tambah Kas Keluar
│   ├── Edit Kas Keluar
│   ├── Hapus Kas Keluar
│   ├── Filter Tanggal
│   ├── Export PDF
│   └── Export Excel
│
├── Data Karyawan
│   ├── Data Karyawan
│   ├── Tambah Karyawan
│   ├── Edit Karyawan
│   └── Hapus Karyawan
│
├── Buku Besar
└── Neraca Saldo
```

## 🎯 Tujuan Pengembangan

Sistem ini dikembangkan untuk membantu perusahaan dalam mengelola transaksi keuangan secara lebih efektif, terstruktur, dan akurat. Dengan adanya sistem ini, proses pencatatan kas, pengelolaan data karyawan, serta penyusunan laporan keuangan dapat dilakukan dengan lebih cepat dibandingkan metode pencatatan manual.

## 👨‍💻 Developer

**Sahrul Ztacker**

* Python Developer
* Django Developer
* Machine Learning Enthusiast

Jika proyek ini bermanfaat, jangan lupa memberikan ⭐ pada repository ini.
