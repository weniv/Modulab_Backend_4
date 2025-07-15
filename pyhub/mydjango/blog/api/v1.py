# blog/api/v1.py

from django.urls import path
from rest_framework.generics import ListAPIView
from blog.models import Post
from blog.api.serializers import PostSerializer


post_list = ListAPIView.as_view(
    # queryset=Post.objects.filter(status=Post.Status.PUBLISHED),
    queryset=Post.objects.published(),
    serializer_class=PostSerializer,  # 고정. but 동적 지정도 가능.
)


urlpatterns = [
    path("posts/", post_list),
]
