# melon/api/serializers.py

# from django import forms
from rest_framework import serializers
from melon.models import Song


# class SongForm(forms.ModelForm):
#     comment = forms.CharField()
#
#     class Meta:
#         model = Song
#         fields = "__all__"

# serializers.Serializer  # forms.Form
# serializers.ModelSerializer  # forms.ModelForm

# 변환 (read), 요청 처리 (write)
class SongSerializer(serializers.ModelSerializer):
    # 모델 필드에는 없는 이름이어야 합니다. 존재하는 이름이면 덮어쓰기가 됩니다.
    # title_length = serializers.SerializerMethodField()
    #
    # # 파이썬 단에서 song.title 을 계산하는 것이 부담되지 않습니다. 충분한 성능.
    # def get_title_length(self, song) -> int:
    #     return len(song.title)

    # 조회 요청에서만 사용되고, 쓰기 요청에서는 이 필드는 무시됩니다.
    title_length = serializers.IntegerField(read_only=True)

    class Meta:
        model = Song
        # fields = "__all__"  # 추천드리지 않아요. 의도치않게 모델 필드가 api로 노출될 수 있습니다.
        # 명시적인 지정을 추천드립니다.
        fields = ["id", "rank", "album", "title", "artist", "title_length"]
