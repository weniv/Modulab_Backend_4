# melon/models.py

from django.db import models


class Song(models.Model):
    uid = models.CharField(max_length=20, unique=True, verbose_name="곡일련번호")
    rank = models.IntegerField(verbose_name="순위")
    album = models.CharField(max_length=200, verbose_name="앨범")
    title = models.CharField(max_length=200, verbose_name="곡명")
    artist = models.CharField(max_length=200, verbose_name="가수")
    cover_image_url = models.URLField(max_length=500, verbose_name="커버이미지 주소")
    lyrics = models.TextField(verbose_name="가사")
    genre = models.CharField(max_length=100, verbose_name="장르")
    release_date = models.DateField(verbose_name="발매일")
    likes = models.IntegerField(verbose_name="좋아요")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['rank']  # 순위 기준으로 정렬
        verbose_name = '노래'
        verbose_name_plural = '노래들'

    def __str__(self):
        return f"[{self.rank}] {self.title} - {self.artist}"


class Todo(models.Model):
    content = models.TextField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
