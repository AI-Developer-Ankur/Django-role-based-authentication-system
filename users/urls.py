from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import SuperAdminRegisterView, AdminRegisterView, UserRegisterView, CustomTokenObtainPairView

urlpatterns = [
    path('register/superadmin/', SuperAdminRegisterView.as_view(), name='register_superadmin'),
    path('register/admin/', AdminRegisterView.as_view(), name='register_admin'),
    path('register/user/', UserRegisterView.as_view(), name='register_user'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
