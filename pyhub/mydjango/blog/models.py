from django.db import models
from django.urls import reverse

# 장고 기본에서 지원하는 User 모델
#  - 다른 User 모델로 바꿀 수 있습니다. => Ultra Tip : 초기 migrate 하기 전에 바꾸세요.
#  - 매 요청을 처리할 때마다, DB에서 관련 User를 조회합니다. => request.user 속성
#  - 그 유저 관련한 필드들은 별도의 모델을 통해서 관리하시는 것을 추천드립니다.
#    - 기존 User 확장 모델 => Profile 모델 = 1:1 관계 (models.OneToOneField)
# from django.contrib.auth.models import User  # auth.User


# 개발하시다보면, 자주 만드는 쿼리셋 패턴이 다들 몇 개씩 있어요.
#
# Post.objects.filter(status=Post.Status.DRAFT)
# Post.objects.filter(status=Post.Status.PUBLISHED)
# Post.objects.filter(status=Post.Status.PRIVATE)


class PostQuerySet(models.QuerySet):
    def draft(self):
        return self.filter(status=Post.Status.DRAFT)

    def published(self):
        return self.filter(status=Post.Status.PUBLISHED)

    def private(self):
        return self.filter(status=Post.Status.PRIVATE)


class Post(models.Model):
    # choices 는 2개의 값으로 구성된 tuple의 리스트
    # STATUS_CHOICES = [
    #     # DB에 저장될 값, 유저에게 보여질 레이블
    #     ('draft', '임시'),
    #     ('published', '공개'),
    #     ('private', '비공개'),
    # ]
    class Status(models.TextChoices):
        DRAFT = "draft", "임시"
        PUBLISHED = 'published', '공개'
        PRIVATE = 'private', '비공개'

    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(
        max_length=10,
        # 모든 모델 필드에서 choices 인자를 지원해줍니다.,
        #  - 유저로부터의 선택지를 제공. 선택지 이외의 값에 대해서 제한.
        #  - 악의적인 목적으로 유저가 Form을 변조해서 다른 값을 보내더라도
        #    유효성 검사 시에 다 걸러집니다.
        choices=Status.choices,
        default=Status.DRAFT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PostQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self) -> str:
        """Post 모델에 대한 detail 주소 문자열을 반환"""
        return reverse("blog:post_detail", kwargs={"pk": self.pk})


# 모델에 기본 키를 지정해서 기본키를 변경하는 방법이 있습니다.
# 이를 지정하지 않으면, id 필드가 자동 생성됩니다.

# 장고에서 지원하는 ORM : Django Model
#  - SQL을 직접 작성하지 않아도 데이터베이스에 대한 조회, 생성, 수정, 삭제 등의 요청을 할 수 있게 됩니다.
#    SQL은 지금은 잘 몰라도, 하면서 이해도를 높이면 보다 효율적인 애플리케이션을 서비스할 수 있습니다.
#    1) 서비스 개발 비용과 유지 보수 비용 => 개발된 코드를 내가/우리가 커버할 수 있나?
#    2) 서버 운영 비용을 낮출 수 있고, 유저에게 보다 빠른 서비스 응답을 줄 수 있게 됩니다.

# comment = Comment.objects.all()[0]  # Comment Instance
# comment.post  # Post Instance

# post = Post.objects.all()[0]  # Post Instance
# comment_qs = Comment.objects.filter(post=post)

# 관계 필드에서 related_name 속성을 지원
# comment_qs = post.comment_set.all()

class Comment(models.Model):
    # 댓글 길이 제한을 두지 않으려면.
    # content = models.TextField()

    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        # 아래 두 필드 모두 False이면 => 이 필드는 필수필드가 됩니다.
        # blank=False,  # Form 입장 : 빈 입력필드를 허용할 여부
        # null=False,   # DB 입장 : 값이 없는 상황 (NULL)을 허용할지 여부
        # default=1,
    )

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
    tags = models.CharField(max_length=100, default="")
