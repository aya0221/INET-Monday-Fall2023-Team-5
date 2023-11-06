from django.urls import path
from . import views
from .views import GameProgressView

urlpatterns = [
    path(
        "initiate_game_session/",
        views.initiate_game_session,
        name="initiate_game_session",
    ),
    path(
        "game_progress/<uuid:game_id>/",
        GameProgressView.as_view(),
        name="game_progress",
    ),
    path(
        "end_game_session/<uuid:game_id>/",
        views.end_game_session,
        name="end_game_session",
    ),
]
