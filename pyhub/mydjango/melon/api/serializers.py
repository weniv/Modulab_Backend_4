# melon/api/serializers.py

# from django import forms
from rest_framework import serializers
from melon.models import Song


# class SongForm(forms.ModelForm):
#     class Meta:
#         model = Song
#         fields = "__all__"

# serializers.Serializer  # forms.Form
# serializers.ModelSerializer  # forms.ModelForm

# 변환, 요청 처리
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"
