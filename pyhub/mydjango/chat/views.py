from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# django view : http 요청을 받아 요청을 처리하는 함수
#  - 항상 1개 인자가 있고, request를 통해 모든 요청 내역을 조회 가능
# @app.get("/chat/")  # FastAPI style
def index(request: HttpRequest) -> HttpResponse:
    # query parameters, form data, files, headers, etc.

    # str (html, text), image data, pdf data, streaming, etc.

    # html_str = "<html><head></head><body><h1>hello django in html</h1></body>"

    # # return HttpResponse("hello django")  # default content type : text/html
    # return HttpResponse(html_str)

    # html도 장고 입장에서는 그냥 텍스트. 이 외에 다양한 포맷도 문자열이라면 다 가능.
    return render(request, "chat/index.html")
