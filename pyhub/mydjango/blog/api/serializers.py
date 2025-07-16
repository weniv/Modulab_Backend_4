# blog/api/serializers.py

from rest_framework import serializers
from blog.models import Post, Comment


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


class PostListSerializer(serializers.ModelSerializer):
    # ModelSerializer가 생성해준 필드를 덮어쓰기 (ModelForm도 마찬가지)

    author = serializers.SerializerMethodField()
    def get_author(self, post) -> str:
        return str(post.author)

    # author = serializers.StringRelatedField(read_only=True)

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
