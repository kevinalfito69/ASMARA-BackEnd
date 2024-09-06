from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    AspirasiListCreateView, 
    PembangunanListView, 
    WilayahListView, 
    LoginView, 
    RegisterView,
    WargaDetail,
    WargaCreateView,
    WargaUpdateView,
    ChangePasswordView,
    UpdateProfileView,
    UserProfileView,
    VerifyTokenView
)


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('aspirasi/', AspirasiListCreateView.as_view(), name='aspirasi-list-create'),
    path('pembangunan/', PembangunanListView.as_view(), name='pembangunan-list'),
    path('wilayah/', WilayahListView.as_view(), name='wilayah-list'),
    path('warga/<str:nik>/', WargaDetail.as_view(), name='warga-list'),
    path('wargacreate/', WargaCreateView.as_view(), name='warga-create'),
    path('warga/<str:nik>/edit/', WargaUpdateView.as_view(), name='edit-warga'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('update-profile/', UpdateProfileView.as_view(), name='update-profile'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('verify-token/', VerifyTokenView.as_view(), name='verify_token'),
]
