from django.db import models


class Post(models.Model):
    # choices 는 2개의 값으로 구성된 tuple의 리스트
    STATUS_CHOICES = [
        # DB에 저장될 값, 유저에게 보여질 레이블
        ('draft', '임시'),
        ('published', '공개'),
        ('private', '비공개'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(
        max_length=10,
        # 모든 모델 필드에서 choices 인자를 지원해줍니다.,
        #  - 유저로부터의 선택지를 제공. 선택지 이외의 값에 대해서 제한.
        #  - 악의적인 목적으로 유저가 Form을 변조해서 다른 값을 보내더라도
        #    유효성 검사 시에 다 걸러집니다.
        choices=STATUS_CHOICES,
        default='draft',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
