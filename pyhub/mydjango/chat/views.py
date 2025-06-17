from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# django view : http 요청을 받아 요청을 처리하는 함수
#  - 항상 1개 인자가 있고, request를 통해 모든 요청 내역을 조회 가능
# @app.get("/chat/")  # FastAPI style
def index(request: HttpRequest) -> HttpResponse:
    # query parameters, form data, files, headers, etc.

    # str (html, text), image data, pdf data, streaming, etc.
    return HttpResponse("hello django")
