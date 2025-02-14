from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

# SuperAdmin Registration
class SuperAdminRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        request.data['role'] = 'superadmin'
        return super().create(request, *args, **kwargs)

# Admin Creation (Only SuperAdmin can do this)
class AdminRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.role != 'superadmin':
            return Response({"error": "Only SuperAdmin can create Admins."}, status=403)

        request.data['role'] = 'admin'
        return super().create(request, *args, **kwargs)

# User Registration (SuperAdmin & Admin can create Users)
class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.role not in ['superadmin', 'admin']:
            return Response({"error": "Only SuperAdmin or Admin can create Users."}, status=403)

        request.data['role'] = 'user'
        return super().create(request, *args, **kwargs)

# Login to get tokens
from rest_framework_simplejwt.views import TokenObtainPairView
class CustomTokenObtainPairView(TokenObtainPairView):
    pass
