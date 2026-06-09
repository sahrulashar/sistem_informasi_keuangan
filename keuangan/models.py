from django.db import models


class KasMasuk(models.Model):
    tanggal = models.DateField()
    jam = models.TimeField()

    keterangan = models.TextField()

    jumlah = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )

    users = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.keterangan
    
class KasKeluar(models.Model):
    tanggal = models.DateField()
    jam = models.TimeField()

    keterangan = models.TextField()

    jumlah = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )

    users = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.keterangan
    
class Karyawan(models.Model):
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100)
    tgl_bergabung = models.DateField()

    def __str__(self):
        return self.nama