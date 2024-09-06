from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.
# authapp/views.py
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            user = authenticate(username=username, password=password)
            nik = user.warga.nik
            refresh = RefreshToken.for_user(user)
            if user:
                return Response({"message": "Login successful","user":{"nik":nik,"username":user.username,"email":user.email}, "token":str(refresh.access_token)}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully","id_user":user.pk}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PembangunanListView(generics.ListAPIView):
    queryset = Pembangunan.objects.all()
    serializer_class = PembangunanSerializer

class WilayahListView(generics.ListAPIView):
    queryset = Wilayah.objects.all()
    serializer_class = WilayahSerializer

class WargaDetail(generics.RetrieveAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer
    lookup_field = 'nik'
    
class WargaCreateView(generics.CreateAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class WargaUpdateView(generics.UpdateAPIView):
    queryset = Warga.objects.all()
    serializer_class = UpdateWargaSerializer
    lookup_field = 'nik'

class AspirasiListCreateView(generics.ListCreateAPIView):
    queryset = Aspirasi.objects.all()
    serializer_class = AspirasiSerializer
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Password berhasil diubah."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateProfileView(generics.UpdateAPIView):
    serializer_class = UpdateProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Mengembalikan pengguna yang saat ini sedang terautentikasi
        return self.request.user

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class VerifyTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Token is valid"}, status=200)