# accounts/views.py

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render


def register(request):
    pass


# def login(request):
#     pass

login = LoginView.as_view()
