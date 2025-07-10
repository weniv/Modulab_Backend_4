# blog/urls.py

from django.urls import path
from . import views

app_name = "blog"  # 앱 이름과 동일하게 지정하시면 되요.

# 장고의 urls.py에게 장고가 요구하는 것은 단 하나 !!
# urlpatterns 이름의 리스트 => 이름에 오타가 있으면 안 되요.
urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("create/", views.post_new, name="post_new"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("<int:post_pk>/comments/new/", views.comment_new, name="comment_new"),
]
