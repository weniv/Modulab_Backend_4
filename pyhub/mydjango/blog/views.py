# blog/views.py
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect, resolve_url
from .models import Post

# 최소한의 동작을 하는 Post 모델에 대한 View (Class Based View 활용)
#  - .as_view 호출을 통해, View 함수를 만들어주는 클래스

# 설정 보다는 관례 문화

# 목록 조회 : 모델 클래스

post_list = ListView.as_view(
    model=Post,  # 필수
    # 생략하면, "앱이름/모델명소문자_list.html" 을 자동으로 찾아요.
    # template_name="blog/post_list.html",
)

# 단건 조회 : 모델 클래스

post_detail = DetailView.as_view(
    model=Post,
)

# def post_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, "blog/post_detail.html", {"post": post})

# 생성 : 모델 클래스, 폼 클래스

from blog.forms import CommentForm
from blog.models import Comment

# View 구현에서 반복을 줄일 수 있도록 도와주는 장고의 기능 : Class Based View

# comment_new = CreateView.as_view(
#     model=Comment,
#     form_class=CommentForm,
#     success_url="/blog/",  # TODO: 포스팅 detail 로 이동.
# )


# Form 요청을 위해, 하나의 주소에서 GET 요청과 POST 요청을 같이 받습니다. => Django Style
#  - django도 주소에 기반해서 호출된 View를 매핑 => 하나의 주소 => 하나의 View
#  - java spring : /blog/comments/form/ GET 요청 /blog/comments/submit/ POST 요청
#                  2개의 함수를 구현하게 되는 거죠.

def comment_new(request: HttpRequest, post_pk: int) -> HttpResponse:
    # html <form> 요청에서는 method는 단 2가지 : GET or POST (항상 대문자)
    #  <form method="post"> 라고 썼다고 해도, 장고 서버에서는 항상 대문자.

    if request.method == "GET":
        form = CommentForm()

    else:  # POST
        # 제출받은 값들을 장고 Form에게 제출
        # Django View에서 요청받은 데이터 참조하는 법
        #  1) request.GET
        #  2) request.POST : 파일을 제외한 POST 데이터
        #  3) request.FILES : 파일로만 구성된 POST 데이터
        form = CommentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            # django Form은 아래의 사전을 생성해주는 것 까지가 책임의 끝.
            #  - No DB 저장
            # form.cleaned_data  # dict 타입 : 유효성 검사에 통과한 값들
            # django ModelForm : + DB로의 저장도 지원 (save 메서드 지원)

            # ModelForm => fields = ["content"] 지정
            #  - 아래의 .save() 에서는 content 필드만 지정해서 데이터베이스로의 저장을 시도
            #  - commit=False : form.save 내부에서 모델.save()를 호출하지 않습니다.
            #                   모델 인스턴스만 생성하고 반환만 합니다.
            #                   아직 모델.save 메서드를 호출하지 않은 상황.
            unsaved_comment: Comment = form.save(commit=False)  # ModelForm의 save

            # 유저로부터 Post를 지정받지 않는다라고 해서 !!!
            #   - Post 필드 값을 지정하지 않아도 되는 것은 아닙니다.
            #   - 프로그램 코드를 통해 자동 지정되도록 해야합니다.
            unsaved_comment.post = Post.objects.get(id=post_pk)
            # 유사한 예: 유저의 아이피 주소, 유저의 웹브라우저 종류 (사용하는 OS)
            unsaved_comment.save()  # Model의 save

            # Model의 save()
            #  - 데이터베이스로 지정 필드 구성으로 저장을 시도.
            # ModelForm의 save
            #  - .cleaned_data 사전값을 기반으로
            #    Model 인스턴스를 만들어서 모델의 save 를 호출합니다.

            # 대개의 서비스 기획 : 생성 폼에서 생성에 성공하면, 다른 페이지로 이동
            # post_url = f"/blog/{post_pk}/"  # python, f-string 문법

            # 가장 기본이 되는 URL Reverse 함수 : reverse
            # post_url = reverse("blog:post_detail", args=[post_pk])
            # post_url = reverse("blog:post_detail", kwargs={"pk": post_pk})

            # reverse 함수를 래핑해서, 보다 편리하게 만든 함수
            # django.shortcuts
            post_url = resolve_url("blog:post_detail", pk=post_pk)

            return redirect(post_url)  # 브라우저에게 이동을 하라고, 지시

    return render(request, "blog/comment_form.html", {
        "form": form,
    })


# 수정 : 모델 클래스, 폼 클래스

# 삭제 : 모델 클래스


# def post_list(request):
#     qs = Post.objects.all()
#     return render(request, "blog/post_list.html", { "post_list": qs })
#
# def article_list(request):
#     qs = Article.objects.all()
#     return render(request, "blog/article_list.html", { "article_list": qs })
#
# def comment_list(request):
#     qs = Comment.objects.all()
#     return render(request, "blog/comment_list.html", { "comment_list": qs })
