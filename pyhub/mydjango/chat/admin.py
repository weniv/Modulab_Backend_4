# chat/admin.py

from django.contrib import admin
from .models import PuzzleRoom


# PuzzleRoom 모델을 통해서, 데이터베이스 조회/추가/수정/삭제 수행 가능
# PuzzleRoom 모델을 admin에 등록하면, 이 것 만으로 관리 UI 제공
#  => 장고의 독보적인 기능.

@admin.register(PuzzleRoom)
class PuzzleRoomAdmin(admin.ModelAdmin):
    pass
