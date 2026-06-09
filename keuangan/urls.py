from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('kas-masuk/', views.kas_masuk, name='kas_masuk'),
    path(
        'kas-masuk/tambah/',
        views.tambah_kas_masuk,
        name='tambah_kas_masuk'
    ),
    path(
        'kas-masuk/edit/<int:id>/',
        views.edit_kas_masuk,
        name='edit_kas_masuk'
    ),
    path(
        'kas-masuk/hapus/<int:id>/',
        views.hapus_kas_masuk,
        name='hapus_kas_masuk'
    ),

    path(
        'kas-keluar/',
        views.kas_keluar,
        name='kas_keluar'
    ),

    path(
        'kas-keluar/tambah/',
        views.tambah_kas_keluar,
        name='tambah_kas_keluar'
    ),

    path(
        'kas-keluar/edit/<int:id>/',
        views.edit_kas_keluar,
        name='edit_kas_keluar'
    ),

    path(
        'kas-keluar/hapus/<int:id>/',
        views.hapus_kas_keluar,
        name='hapus_kas_keluar'
    ),
    path(
        'karyawan/',
        views.list_karyawan,
        name='list_karyawan'
    ),

    path(
        'karyawan/tambah/',
        views.tambah_karyawan,
        name='tambah_karyawan'
    ),

    path(
        'karyawan/edit/<int:id>/',
        views.edit_karyawan,
        name='edit_karyawan'
    ),

    path(
        'karyawan/hapus/<int:id>/',
        views.hapus_karyawan,
        name='hapus_karyawan'
    ),

    path(
    'buku-besar/',
    views.buku_besar,
    name='buku_besar'
    ),

    path(
    'neraca-saldo/',
    views.neraca_saldo,
    name='neraca_saldo'
    ),

    path(
        'kas-masuk/export/excel/',
        views.export_excel_kas_masuk,
        name='export_excel_kas_masuk'
    ),

    path(
        'kas-masuk/export/pdf/',
        views.export_pdf_kas_masuk,
        name='export_pdf_kas_masuk'
    ),

    path(
        'kas-keluar/export/excel/',
        views.export_excel_kas_keluar,
        name='export_excel_kas_keluar'
    ),

    path(
        'kas-keluar/export/pdf/',
        views.export_pdf_kas_keluar,
        name='export_pdf_kas_keluar'
    ),

]

