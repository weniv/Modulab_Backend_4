from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("messages/new/", views.chat_message_new),
    path("puzzle/toy/", views.puzzle_room),  # ADDED
]
