import json
from django.db.models.functions import Length
from django.http import HttpResponse
from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
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
#     # Renderer : 플러그인 방식으로 쉽게 지원을 붙일 수 있어요.
#     #  - 디폴트 DRF Renderer : HTML Renderer, JSON Renderer
#     #  - 추가로 구현해본다면 : PDF Renderer, Xlsx Renderer, CSV Renderer 등
#
#     return Response(song_list_data)


# CBV 버전의 DRF API
song_list = ListAPIView.as_view(
    # 데이터 조회
    queryset=Song.objects.all().annotate(title_length=Length("title")),
    # 데이터 조정
    serializer_class=SongSerializer,
)


#
# todos/
#

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# ViewSet의 .as_view() 메서드는 일반적인 CBV의 as_view와 인자가 다릅니다.
#  - 최소 5개의 View 함수를 만들 수 있습니다.
todo_list_or_new = TodoViewSet.as_view({
    # CBV에는 get, post 메서드가 있고
    # GET 요청에서는 get 메서드를 호출해서 요청을 처리합니다.
    "get": "list",
    "post": "create",
})

todo_detail_or_edit_or_delete = TodoViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

#
#
#
# todo_list = ListAPIView.as_view(
#     queryset=Todo.objects.all(),
#     serializer_class=TodoSerializer,
# )
#
# # Form 처리에서는 GET 요청과 POST 요청을 지원했습니다.
# # API 에서는 생성에 대해서는 POST 요청만을 받습니다.
# #  - UI 부분은 API에서 신경쓰지 않아요. 단지 생성 요청 만을 받을 뿐.
# todo_new = CreateAPIView.as_view(
#     queryset=Todo.objects.all(),
#     serializer_class=TodoSerializer,  # Form과 유사한 역할로서 유효성 검사/저장
# )
#
# @api_view(["GET", "POST"])
# def todo_list_or_new(request):
#     if request.method == "GET":
#         return todo_list(request)
#     else:
#         return todo_new(request)
#
#
#
# todo_detail = RetrieveAPIView.as_view(
#     queryset=Todo.objects.all(),
#     serializer_class=TodoSerializer,
# )
#
# todo_edit = UpdateAPIView.as_view(
#     queryset=Todo.objects.all(),
#     serializer_class=TodoSerializer,  # Form과 유사한 역할로서 유효성 검사/저장
# )
#
# todo_delete = DestroyAPIView.as_view(
#     queryset=Todo.objects.all(),
#     # serializer_class=TodoSerializer,
# )


urlpatterns = [
    path("songs/", song_list),
    path("todos/", todo_list_or_new),
    path("todos/<int:pk>/", todo_detail_or_edit_or_delete),
]
