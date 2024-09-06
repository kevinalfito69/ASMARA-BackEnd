# authapp/admin.py
from django.contrib import admin
from .models import Pembangunan, Wilayah, Warga, Aspirasi
from django.contrib.staticfiles.storage import staticfiles_storage
admin.site.site_header = "ASMARA"
admin.site.site_title = "ASMARA"
admin.site.index_title = "Admin"
class CustomAdminSite(admin.AdminSite):
    class Media:
        css = {
            'all': (staticfiles_storage.url('css/custom_admin.css'),)
        }

admin_site = CustomAdminSite(name='custom_admin')
@admin.register(Pembangunan)
class PembangunanAdmin(admin.ModelAdmin):
    list_display = ('bidang_pembangunan', 'lokasi', 'tanggal_mulai', 'tanggal_selesai', 'anggaran')
    search_fields = ('bidang_pembangunan', 'lokasi')
    list_filter = ('tanggal_mulai', 'tanggal_selesai')

@admin.register(Wilayah)
class WilayahAdmin(admin.ModelAdmin):
    list_display = ('dusun', 'rt', 'rw')
    search_fields = ('dusun', 'rt', 'rw')

@admin.register(Warga)
class WargaAdmin(admin.ModelAdmin):
    list_display = ('nik', 'nama_lengkap', 'alamat', 'tanggal_lahir', 'nomor_telepon')
    search_fields = ('nik', 'nama_lengkap')
    list_filter = ('tanggal_lahir',)
    

@admin.register(Aspirasi)
class AspirasiAdmin(admin.ModelAdmin):
    list_display = ('warga', 'pembangunan', 'wilayah', 'bidang', 'sub_bidang', 'kegiatan', 'tanggal')
    search_fields = ('warga__nama_lengkap', 'pembangunan__bidang_pembangunan', 'wilayah__dusun', 'bidang', 'sub_bidang', 'kegiatan')
    list_filter = ('tanggal',)
