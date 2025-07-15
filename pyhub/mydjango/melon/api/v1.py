import json
from django.db.models.functions import Length
from django.http import HttpResponse
from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from melon.models import Song
from melon.api.serializers import SongSerializer


# Django View -> APIView 기반으로 래핑 (Wrapping)

@api_view(["GET"])
def song_list(request):
    qs = Song.objects.all()
    qs = qs.annotate(title_length=Length("title"))

    serializer = SongSerializer(
        instance=qs,  # Model Instance 또는 QuerySet
        many=True,  # Model Instance 시에는 False, QuerySet 시에는 True
    )
    song_list_data = serializer.data  # 자동 변환을 즉시 수행.

    # Renderer
    #  - 디폴트 DRF Renderer : HTML Renderer, JSON Renderer

    return Response(song_list_data)


urlpatterns = [
    path("songs/", song_list),
]
