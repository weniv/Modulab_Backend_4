# chat/views.py
from django.http import HttpResponse
from django.shortcuts import render

# chat/templates/chat/index.html 에서
# chat 경로명은 2번 씁니다 !!! 1번 쓰면 안되나요? 안 되요 !!
# 그 이유는, 나중에 !!!

# django view : http 요청을 받아 요청을 처리하는 함수
#  - 항상 1개 인자가 있고, request를 통해 모든 요청 내역을 조회 가능
def index(request) -> HttpResponse:
    # django template < jinja2

    # text, image, pdf, excel, video streaming 등등 다양한 응답이 가능
    # return HttpResponse("hello django")
    return render(request, "chat/index.html")
