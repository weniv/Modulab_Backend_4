# chat/forms.py

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 전체 필드를 지정할 때에는 [] 를 쓰지 않아요.
        fields = "__all__"
