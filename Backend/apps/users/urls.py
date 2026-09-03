from django.urls import path
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views


urlpatterns = [
    path("api/v0/register", views.RegisterUser),
    path("api/v0/login", views.LoginCheck),
    path("token/refresh/", TokenRefreshView.as_view()) 
]