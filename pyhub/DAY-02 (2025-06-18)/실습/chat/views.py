# chat/views.py
from django.http import HttpResponse
from django.shortcuts import render


# django view : http 요청을 받아 요청을 처리하는 함수
#  - 항상 1개 인자가 있고, request를 통해 모든 요청 내역을 조회 가능
def index(request):
    return HttpResponse("hello django")
