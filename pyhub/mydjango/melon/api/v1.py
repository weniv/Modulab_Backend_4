import json
from django.db.models.functions import Length
from django.http import HttpResponse
from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
)
from rest_framework.response import Response
from melon.models import Song, Todo
from melon.api.serializers import SongSerializer, TodoSerializer

# Django View -> APIView 기반으로 래핑 (Wrapping)

# FBV 버전의 DRF API
# @api_view(["GET"])
# def song_list(request):
#     qs = Song.objects.all()
#     qs = qs.annotate(title_length=Length("title"))
#
#     serializer = SongSerializer(
#         instance=qs,  # Model Instance 또는 QuerySet
#         many=True,  # Model Instance 시에는 False, QuerySet 시에는 True
#     )
#     song_list_data = serializer.data  # 자동 변환을 즉시 수행.
#
#     # Renderer
#     #  - 디폴트 DRF Renderer : HTML Renderer, JSON Renderer
#
#     return Response(song_list_data)


# CBV 버전의 DRF API
song_list = ListAPIView.as_view(
    # 데이터 조회
    queryset=Song.objects.all().annotate(title_length=Length("title")),
    # 데이터 조정
    serializer_class=SongSerializer,
)


# TODO: admin에 Todo 등록하시고 admin에서 Todo를 5개 생성
# TODO: 아래 todo_list api 구현하시고,
# TODO: 아래 urlpatterns에 등록하시고
# TODO: 브라우저로 해당 Todo 목록을 확인하시고, 해당 스샷을 "Todo API를 만들어봅시다." 쓰레드 공유 !!!
todo_list = ListAPIView.as_view(
    queryset=Todo.objects.all(),
    serializer_class=TodoSerializer,
)


urlpatterns = [
    path("songs/", song_list),
    path("todos/", todo_list),
]
