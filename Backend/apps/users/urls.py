from django.urls import path


from . import views



urlpatterns = [
    path("api/v0/register", views.RegisterUser),
    path("api/v0/login", views.LoginCheck)
]
