# baemin/views.py

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Shop, Review
from .forms import ReviewForm


# 최신의 가게 목록 페이지를 보여줄 거예요.
#  - 최신의 데이터는 DB 안에 있죠. 그러니 매번 DB 조회를 할 겁니다.
def shop_list(request):
    # 데이터베이스에서 baemin_shop 테이블의 모든 레코드를
    # 조회할 준비 (아직 데이터를 가져오진 않았습니다.)
    qs = Shop.objects.all()  # QuerySet

    return render(
        request,
        template_name="baemin/shop_list.html",
        context={
            "shop_list": qs,
        })

# TODO: baemin/shop_list.html 템플릿을 만들어보기. 하얀 배경도 OK. chatgpt 등을 통한 코드 생성도 OK.


def shop_detail(request, pk):
    # DB에서 조회했습니다.
    shop = Shop.objects.get(pk=pk)    # 이 필드명 지정이 좀 더 정확한 네이밍.
    # shop = Shop.objects.get(id=pk)  # 위와 동일한 동작

    # 전체(모든 Shop) 리뷰 데이터를 가져올 준비.
    review_qs = Review.objects.all()
    # 특정 shop의 리뷰 데이터를 가져올 준비 (가져올 범위가 좁혀집니다.)
    review_qs = review_qs.filter(shop=shop)

    return render(
        request,
        template_name="baemin/shop_detail.html",
        context={"shop": shop, "review_list": review_qs},
    )

# TODO: baemin/shop_detail.html 템플릿을 만들어보기.


def review_new(request, shop_pk):
    shop = Shop.objects.get(pk=shop_pk)  # form 시작할 때, 지정 pk의 Shop의 존재 유무를 확인.

    if request.method == "GET":
        form = ReviewForm()

    else:
        form = ReviewForm(data=request.POST, files=request.FILES)
        if form.is_valid():  # 유효성 검사 수행 !!!

            # commit=False 를 지정해서, form.save 내부에서 model.save 가 호출되지 않도록.
            unsaved_review: Review = form.save(commit=False)  # 입력받은 폼 필드 값으로 데이터베이스로의 저장을 시도 !!!
            unsaved_review.shop = shop  # Shop Instance
            unsaved_review.save()

            # 한국어를 쓰는 사람을 대상으로만 하는 서비스니까, 메시지는 한국어로 쓰셔도 됩니다.
            # 만약 영어 등 다국어를 지원해야한다면, 메시지를 쓰는 방법이 조금 달라요.
            messages.success(request, "고객님의 리뷰에 감사드립니다. ;)")
            # 위 메시지는 요청을 한 유저에게만 보여질 거예요.

            next_url = f"/baemin/{shop_pk}/"
            return redirect(next_url)  # django view 함수에서만 씁니다. 브라우저에게 이 주소로 이동하세요.

    return render(
        request,
        template_name="baemin/review_form.html",
        context={"form": form},
    )
