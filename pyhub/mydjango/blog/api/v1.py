# blog/api/v1.py

from django.urls import path
from rest_framework.generics import ListAPIView, RetrieveAPIView
from blog.models import Post
from blog.api.serializers import PostSerializer, PostListSerializer


post_list = ListAPIView.as_view(
    # queryset=Post.objects.filter(status=Post.Status.PUBLISHED),
    queryset=Post.objects.published().defer("content").select_related("author"),
    serializer_class=PostListSerializer,  # 고정. but 동적 지정도 가능.
)


post_detail = RetrieveAPIView.as_view(
    queryset=Post.objects.published(),
    serializer_class=PostSerializer,
)


urlpatterns = [
    path("posts/", post_list),
    path("posts/<int:pk>/", post_detail),
]
