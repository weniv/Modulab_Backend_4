from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def root(request):
    return render(request, "root.html")


urlpatterns = [
    path("admin/", admin.site.urls),
    # 앞서 지정하는 prefix 주소는
    # accounts.urls 내의 urlpatterns 에 자동 적용
    path("", include("accounts.urls")),
    path("blog", include("blog.urls")),
    path("", root),

]
