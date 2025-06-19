from django import forms
from chat.models import PuzzleRoom


# 상속 (Inheritance) 문법
class PuzzleRoomForm(forms.ModelForm):
    class Meta:
        model = PuzzleRoom
        fields = "__all__"
