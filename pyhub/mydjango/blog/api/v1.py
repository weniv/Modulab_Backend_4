# blog/api/v1.py

from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from blog.api.serializers import PostSerializer
from blog.models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()  # 고정. 가변적으로 줄려면 get_queryset 메서드를 구현.
    serializer_class = PostSerializer  # 고정. 가변적으로 줄려면 get_serializer_class 메서드를 구현.


router = DefaultRouter()
router.register("posts", PostViewSet)
# router.urls  # router가 자동 생성해낸 urlpatterns 리스트


urlpatterns = router.urls
