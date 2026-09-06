from django.urls import path

from .views import CreateGameView


urlpatterns = [
    path("api/v0/games", CreateGameView.as_view(), name="create-game")
]