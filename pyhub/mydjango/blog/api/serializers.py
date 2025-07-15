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
