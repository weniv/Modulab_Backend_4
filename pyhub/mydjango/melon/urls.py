# melon/urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    path("api/v1/", include("melon.api.v1")),
]
