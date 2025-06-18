# chat/models.py

from django.db import models

# 데이터베이스 생성 (1개) + 테이블 생성 (N개) => SQL 언어 !!!
#  cf. 엑셀 : 워크북 생성 (1개) + 워크시트 생성 (N개)


# ORM
class PuzzleRoom(models.Model):
    LEVEL_CHOICES = [
        (3, 'Level 3'),
        (4, 'Level 4'),
        (5, 'Level 5'),
    ]

    # 이미지를 확인하고, 이미지를 특정 폴더에 저장하고 나서, 저장 경로를 DB에 저장
    image_file = models.ImageField(upload_to='chat/puzzle/')
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class ChatMessage(models.Model):
#     message = models.TextField()
