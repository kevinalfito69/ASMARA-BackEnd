# authapp/models.py
from django.db import models
from django.contrib.auth.models import User

class Pembangunan(models.Model):
    bidang_pembangunan = models.CharField(max_length=255)
    lokasi = models.CharField(max_length=255)
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()
    anggaran = models.DecimalField(max_digits=15, decimal_places=2)
    deskripsi = models.TextField()

    def __str__(self):
        return self.bidang_pembangunan

    class Meta:
        verbose_name = 'Pembangunan'
        verbose_name_plural = 'Pembangunan'

class Wilayah(models.Model):
    dusun = models.CharField(max_length=255)
    rt = models.CharField(max_length=3)
    rw = models.CharField(max_length=3)

    def __str__(self):
        return f"Dusun: {self.dusun}, RT: {self.rt}, RW: {self.rw}"

    class Meta:
        verbose_name = 'Wilayah'
        verbose_name_plural = 'Wilayah'

class Warga(models.Model):
    user = models.OneToOneField(User,to_field='username',on_delete=models.CASCADE, primary_key=True)
    nik = models.CharField(max_length=16, unique=True) 
    nama_lengkap = models.CharField(max_length=255)
    alamat = models.TextField()
    tanggal_lahir = models.DateField()
    nomor_telepon = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nama_lengkap

    class Meta:
        verbose_name = 'Warga'
        verbose_name_plural = 'Warga'

class Aspirasi(models.Model):
    warga = models.ForeignKey(Warga, to_field='nik', on_delete=models.CASCADE)
    pembangunan = models.ForeignKey(Pembangunan, on_delete=models.CASCADE)
    wilayah = models.ForeignKey(Wilayah, on_delete=models.CASCADE)
    bidang = models.CharField(max_length=255)
    sub_bidang = models.CharField(max_length=255)
    kegiatan = models.CharField(max_length=255)
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bidang

    class Meta:
        verbose_name = 'Aspirasi'
        verbose_name_plural = 'Aspirasi'
