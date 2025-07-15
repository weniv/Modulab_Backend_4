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

# 변환, 요청 처리
class SongSerializer(serializers.ModelSerializer):
    # 모델 필드에는 없는 이름이어야 합니다. 존재하는 이름이면 덮어쓰기가 됩니다.
    title_length = serializers.SerializerMethodField()

    def get_title_length(self, song) -> int:
        return len(song.title)

    class Meta:
        model = Song
        # fields = "__all__"  # 추천드리지 않아요. 의도치않게 모델 필드가 api로 노출될 수 있습니다.
        # 명시적인 지정을 추천드립니다.
        fields = ["id", "rank", "album", "title", "artist", "title_length"]
