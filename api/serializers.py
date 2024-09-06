from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Aspirasi, Warga, Wilayah, Pembangunan
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import check_password

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user

class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        fields = "__all__"

class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        fields = ['user', 'nik', 'nama_lengkap', 'alamat', 'tanggal_lahir', 'nomor_telepon']

class UpdateWargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        fields = ['nik', 'nama_lengkap', 'alamat', 'tanggal_lahir', 'nomor_telepon']


class PembangunanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembangunan
        fields = ['id', 'bidang_pembangunan']  # Adjust fields as necessary

class WilayahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wilayah
        fields = ['id', 'dusun']  # Adjust fields as necessary

class AspirasiSerializer(serializers.ModelSerializer):
    pembangunan = PembangunanSerializer()
    wilayah = WilayahSerializer()

    class Meta:
        model = Aspirasi
        fields = '__all__'
        
    def create(self, validated_data):
        warga = validated_data.pop('warga')
        pembangunan_data = validated_data.pop('pembangunan')
        wilayah_data = validated_data.pop('wilayah')

        try:
            pembangunan = Pembangunan.objects.get(**pembangunan_data)
        except Pembangunan.DoesNotExist:
            raise ValidationError({'pembangunan': 'Pembangunan object does not exist'})

        try:
            wilayah = Wilayah.objects.get(**wilayah_data)
        except Wilayah.DoesNotExist:
            raise ValidationError({'wilayah': 'Wilayah object does not exist'})

        aspirasi = Aspirasi.objects.create(
            warga=warga, 
            pembangunan=pembangunan, 
            wilayah=wilayah, 
            **validated_data
        )
        return aspirasi
    

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = self.context['request'].user

        # Verifikasi password lama
        if not check_password(data['old_password'], user.password):
            raise ValidationError({"old_password": "Password lama tidak sesuai."})

        return data

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'email']

    def validate_username(self, value):
        # Check if the username is unique, but exclude the current user's username
        user = self.instance
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError("Username is already taken.")
        return value

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']