from django.urls import path
from . import views

urlpatterns = [
    path("/write", views.post_new),
    path("", views.post_list),
    path("/<int:id>", views.post_detail),
    path("/search/<str:tag>", views.post_search),
    path("/edit/<int:id>", views.post_edit),
    path("/delete/<int:id>", views.post_delete),
]
