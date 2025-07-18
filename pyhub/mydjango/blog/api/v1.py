# blog/api/v1.py

from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from blog.api.permissions import IsAuthorOrReadonly
from blog.api.serializers import PostSerializer, PostListSerializer
from blog.models import Post


# 5개 API를 지원합니다.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()  # 고정. 가변적으로 줄려면 get_queryset 메서드를 구현.
    serializer_class = PostSerializer  # 고정. 가변적으로 줄려면 get_serializer_class 메서드를 구현.
    permission_classes = [IsAuthorOrReadonly]

    def get_queryset(self):
        if self.action == "list":
            return PostListSerializer.get_optimized_queryset()
        # 아래 코드는 클래스 변수의 queryset 설정을 반환합니다.
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer
        # 아래 코드가 수행되면, 클래스 변수의 serializer_class 설정을 반환합니다.
        return super().get_serializer_class()


router = DefaultRouter()
router.register("posts", PostViewSet)
# router.urls  # router가 자동 생성해낸 urlpatterns 리스트


urlpatterns = router.urls
