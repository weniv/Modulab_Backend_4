# blog/admin.py

from django.contrib import admin
from .models import Post


# 모델을 admin에 등록하는 첫번째 방법
#  - 디폴트 admin 옵션으로 등록할 때
# admin.site.register(Post)


# 두번째 방법
# class PostAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(Post, PostAdmin)

# 세번째 방법
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
