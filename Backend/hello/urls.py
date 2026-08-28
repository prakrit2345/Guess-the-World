from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("milan", views.milan, name="milan"),
    path("<str:name>", view=views.greet, name="greet")
]