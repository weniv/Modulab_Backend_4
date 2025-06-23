# baemin/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.shop_list),
    # URL Converter : int (정수 문자열 패턴에 매칭)
    path("<int:pk>/", views.shop_detail),
    path("<int:shop_pk>/reviews/new/", views.review_new),
]
