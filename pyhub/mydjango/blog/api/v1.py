# blog/api/v1.py

from django.urls import path
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from blog.api.serializers import PostSerializer, PostListSerializer, PostCreateSerializer


post_list = ListAPIView.as_view(
    queryset=PostListSerializer.get_optimized_queryset(),
    serializer_class=PostListSerializer,  # 고정. but 동적 지정도 가능.
)


# 아래 모델 시리얼라이저에 지정된 필드 만으로 데이터베이스 저장이 가능할 때에는
# 아래 코드 만으로 충분합니다.
# 그런데, 데이터베이스 저장 전에 추가로 할당해야할 필드 (ex: author)가 있다면
# 데이터베이스 저장 전에 할당을 해줘야겠죠.

class PostCreateAPIView(CreateAPIView):
    serializer_class = PostCreateSerializer

    # 웹페이지에서 로그인된 상황에서 테스트해봅시다.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


post_new = PostCreateAPIView.as_view()


post_detail = RetrieveAPIView.as_view(
    queryset=PostSerializer.get_optimized_queryset(),
    serializer_class=PostSerializer,
)


urlpatterns = [
    # path("posts/", post_list),
    path("posts/", post_new),
    path("posts/<int:pk>/", post_detail),
]
