# blog/forms.py

from django import forms
from .models import Comment, Post


# forms.Form
#  - GET 요청 : 지정된 필드 구성으로 유저에게 입력폼 HTML 생성/응답
#  - POST 요청 : 지정된 필드 구성으로 유저로부터 제출(submit)받은 값들에 대한
#               유효성 검사를 수행
#                -> valid : 유효성 검사에 통과한 값들을 dict 타입으로 제공받고, 다른 주소로 이동
#                -> invalid : 유저에게 다시 오류 내역이 포함된 HTML 생성/응답


# # Form : 모델처럼 유저로부터 입력받을 값에 대한 필드 구성을 하나 하나 구성해야만 합니다.
# class CommentForm(forms.Form):
#     content = forms.CharField()


# ModeForm
#  - 지정 모델의 지정 필드들의 정보를 읽어와서
#    폼 필드 구성을 자동으로 수행해줍니다.
#  - 모델 구성이 바뀌면, 알아서 폼 필드 구성도 변경됩니다.
#    (서버 재시작)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 전체 필드를 지정할 때에는 [] 를 쓰지 않아요.
        # fields = "__all__"

        # 유저로부터 입력받을 필드만 명시.
        fields = ["content"]


# forms.Form  # models.Model은 별개
# forms.ModelForm


# 모델이 바뀌면, 모델폼도 자동으로 변경됩니다.
#  - 의도치않게 영향을 끼치지 않아야할 곳에 영향을 끼쳐서 로직을 망가뜨린다.

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

# 모델이 바뀌면, 그 모델을 참조하는 코드를 모두 찾아서 수정을 해줘야 하는 거죠.

# class PostForm(forms.Form):
#     STATUS_CHOICES = [
#         # DB에 저장될 값, 유저에게 보여질 레이블
#         ('draft', '임시'),
#         ('published', '공개'),
#         ('private', '비공개'),
#     ]
#
#     title = forms.CharField()
#     content = forms.CharField()
#     status = forms.ChoiceField(choices=STATUS_CHOICES)