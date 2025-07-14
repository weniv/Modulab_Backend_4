import json
from django.http import HttpResponse
from django.urls import path
from melon.models import Song


def song_list(request):
    qs = Song.objects.all()

    # JSON 문자열로 변환 (Serialize)해서, 해당 문자열을 반환
    song_list_data = [
        {
            "uid": song.uid,
            "rank": song.rank,
            "title": song.title,
            "artist": song.artist,
        }
        for song in qs
    ]
    json_string = json.dumps(song_list_data, ensure_ascii=False)
    return HttpResponse(json_string, content_type="application/json")


urlpatterns = [
    path("songs/", song_list),
]
