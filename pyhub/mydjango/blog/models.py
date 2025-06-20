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


# 모델에 기본 키를 지정해서 기본키를 변경하는 방법이 있습니다.
# 이를 지정하지 않으면, id 필드가 자동 생성됩니다.

class Comment(models.Model):
    # 댓글 길이 제한을 두지 않으려면.
    # content = models.TextField()

    # Post의 기본키를 가리키는 필드 => 외래키 (Foreign Key)
    post = models.ForeignKey(
        Post,
        # 바라보고 있는 Post이 삭제되었을 때, 관련된 댓글은
        # 어떤 처리를 해야할까?
        on_delete=models.CASCADE,  # 관련 댓글 자동 삭제
        # 이 외에도 Post 삭제 막기, etc.
    )
    content = models.CharField(
        max_length=1000,
    )
