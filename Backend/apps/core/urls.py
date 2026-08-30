from django.urls import path
from . import views


urlpatterns = [
    path("api/v0/health/", views.health_check)
]
