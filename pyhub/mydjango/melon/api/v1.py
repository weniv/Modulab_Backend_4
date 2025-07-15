import json
from django.db.models.functions import Length
from django.http import HttpResponse
from django.urls import path
from melon.models import Song
from melon.api.serializers import SongSerializer

# View 단에서는 데이터가 어떻게 변환되는 지에 대해서 관심을 두지 않습니다.
#  - 관심사의 분리

def song_list(request):
    # Database Function 을 호출해서, title 길이 계산을 요청하는 거죠.
    qs = Song.objects.all()
    qs = qs.annotate(title_length=Length("title"))

    # 데이터 변환의 기능을 제공 (시리얼라이저 오리지널 기능)
    #  - 입력 데이터에 대한 유효성 검사 및 저장 (ModelForm의 기능)
    serializer = SongSerializer(
        instance=qs,  # Model Instance 또는 QuerySet
        many=True,  # Model Instance 시에는 False, QuerySet 시에는 True
    )

    # JSON 문자열로 변환 (Serialize)해서, 해당 문자열을 반환
    # song_list_data = [
    #     {
    #         "uid": song.uid,
    #         "rank": song.rank,
    #         "title": song.title,
    #         "artist": song.artist,
    #         # 이 계산을 누가 할래 ??? (BE, FE, 혹은 어느 누군가?)
    #         "title_length": len(song.title),  # 계산된 속성
    #     }
    #     for song in qs
    # ]
    song_list_data = serializer.data  # 자동 변환을 즉시 수행.

    # DRF, Renderer
    json_string = json.dumps(song_list_data, ensure_ascii=False)

    # 응답
    return HttpResponse(json_string, content_type="application/json")


urlpatterns = [
    path("songs/", song_list),
]
