# urls.py
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView

urlpatterns = [

    # Inscription
    path('register/', RegisterView.as_view(), name='register'),

    # JWT Auth
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # refresh token
    path('password-reset/', include('django_rest_passwordreset.urls')),


]