# blog/urls.py

from django.urls import path
from . import views

# 장고의 urls.py에게 장고가 요구하는 것은 단 하나 !!
# urlpatterns 이름의 리스트 => 이름에 오타가 있으면 안 되요.
urlpatterns = [
    path("", views.post_list),
    path("<int:pk>/", views.post_detail),
]
