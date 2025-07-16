# blog/api/serializers.py

# 장고 기본에서 지원해주는 User 모델
#  - 우리 프로젝트에서 사용하지 않을 수도 있어요. 다른 User 모델 클래스를 사용하고 있을 수도 있죠.
#  - 커스텀 User 모델은 이름이 반드시 User가 아니어도 되요.
#    settings.AUTH_USER_MODEL 설정에만 반영해주면 됩니다.
#  - 장고 프로젝트에서 사용하는(활성화된) User 모델은 단 1개입니다.
#  - 현재의 앱이 다른 장고 프로젝트에서 활용될 수도 있어요. => 다른 경로의 User 환경일 수도 있다는 거죠.
# from django.contrib.auth.models import User

from django.conf import settings  # settings.AUTH_USER_MODEL = "auth.User"
from django.contrib.auth import get_user_model

from rest_framework import serializers
from blog.models import Post, Comment


User = get_user_model()  # 현재 프로젝트에 활성화된 User 모델 클래스


# 변환 (read), 유효성 검사 (write, create/update)
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "status",
            "created_at",
            "updated_at",
        ]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class PostListSerializer(serializers.ModelSerializer):
    # ModelSerializer가 생성해준 필드를 덮어쓰기 (ModelForm도 마찬가지)

    # author = serializers.SerializerMethodField()
    # def get_author(self, post) -> str:
    #     return str(post.author)

    # author = serializers.StringRelatedField(read_only=True)

    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = [
            "id",
            "author",  # 외래키 값만 노출하는 구나.
            "title",
            # "content",  # content 필드는 노출하지 않습니다.
            "status",
            "created_at",
            "updated_at",
        ]
