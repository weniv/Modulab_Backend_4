# blog/api/v1.py

from django.urls import path
from rest_framework.generics import ListAPIView, RetrieveAPIView
from blog.api.serializers import PostSerializer, PostListSerializer


post_list = ListAPIView.as_view(
    queryset=PostListSerializer.get_optimized_queryset(),
    serializer_class=PostListSerializer,  # 고정. but 동적 지정도 가능.
)


post_detail = RetrieveAPIView.as_view(
    queryset=PostSerializer.get_optimized_queryset(),
    serializer_class=PostSerializer,
)


urlpatterns = [
    path("posts/", post_list),
    path("posts/<int:pk>/", post_detail),
]
