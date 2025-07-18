# accounts/urls.py
from django.urls import include, path
from . import views

urlpatterns = [
    path("login/", views.login),
    path("logout/", views.logout),
    path("profile/", views.profile),
    path("signup/", views.signup),

    path("api/v1/", include("accounts.api.v1")),
]
