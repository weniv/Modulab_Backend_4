import json
from datetime import datetime

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from melon.models import Song

json_path = '20231203.json'

# f = open(json_path, "rt", encoding="utf-8")
# json_string: str = f.read()
# f.close()  # 쓰고난 물품은 항상 정리, 제자리에 !!!

# 위와 같은 방식. close 호출이 자동으로 이뤄집니다.
with open(json_path, "rt", encoding="utf-8") as f:
    json_string: str = f.read()
    song_list = json.loads(json_string)  # De-serialize
    # print(song_list)
    print(f"{len(song_list)} 개의 곡 정보를 로딩했습니다.")

for song_data in song_list:
    release_date_str = song_data['발매일']
    release_date = datetime.strptime(release_date_str, '%Y-%m-%d').date()

    params = dict(
        uid = song_data['곡일련번호'],
        rank = int(song_data['순위']),
        album = song_data['앨범'],
        title = song_data['곡명'],
        artist = song_data['가수'],
        cover_image_url = song_data['커버이미지_주소'],
        lyrics = song_data['가사'],
        genre = song_data['장르'],
        release_date = release_date,
        likes = int(song_data['좋아요']),
    )
    print(params)

    # 수행 즉시 데이터베이스에 INSERT 수행
    song = Song.objects.create(**params)
    print(song)
