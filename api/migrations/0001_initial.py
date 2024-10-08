# Generated by Django 5.0.6 on 2024-08-19 05:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pembangunan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidang_pembangunan', models.CharField(max_length=255)),
                ('lokasi', models.CharField(max_length=255)),
                ('tanggal_mulai', models.DateField()),
                ('tanggal_selesai', models.DateField()),
                ('anggaran', models.DecimalField(decimal_places=2, max_digits=15)),
                ('deskripsi', models.TextField()),
            ],
            options={
                'verbose_name': 'Pembangunan',
                'verbose_name_plural': 'Pembangunan',
            },
        ),
        migrations.CreateModel(
            name='Warga',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nik', models.CharField(max_length=16, unique=True)),
                ('nama_lengkap', models.CharField(max_length=255)),
                ('alamat', models.TextField()),
                ('tanggal_lahir', models.DateField()),
                ('nomor_telepon', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'verbose_name': 'Warga',
                'verbose_name_plural': 'Warga',
            },
        ),
        migrations.CreateModel(
            name='Wilayah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dusun', models.CharField(max_length=255)),
                ('rt', models.CharField(max_length=3)),
                ('rw', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name': 'Wilayah',
                'verbose_name_plural': 'Wilayah',
            },
        ),
        migrations.CreateModel(
            name='Aspirasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidang', models.CharField(max_length=255)),
                ('sub_bidang', models.CharField(max_length=255)),
                ('kegiatan', models.CharField(max_length=255)),
                ('tanggal', models.DateTimeField(auto_now_add=True)),
                ('pembangunan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pembangunan')),
                ('warga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.warga', to_field='nik')),
                ('wilayah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.wilayah')),
            ],
            options={
                'verbose_name': 'Aspirasi',
                'verbose_name_plural': 'Aspirasi',
            },
        ),
    ]
