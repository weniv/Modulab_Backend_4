from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path('accounts/', include('accounts.urls')),
    # chat/urls에 있는 모든 URL 패턴에 일괄적으로
    #  chat/ 라는 prefix 주소를 부여하겠다.
    path('chat/', include('chat.urls')),
    path('blog/', include('blog.urls')),  # 별도의 tuple
    path('baemin/', include('baemin.urls')),
    path('melon/', include('melon.urls')),
    # 어떤 응답을 할까?
    #  - 1) Template을 통해 HTML 응답을 할까?
    #  - 2) 다른 페이지로 이동을 시켜볼 수도 있겠습니다.
    path('', lambda request: redirect("/baemin/")),
]

# 유저가 업로드한 파일을 서빙하는 View 설정 (View <- 장고 개발서버에서 제공)
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

from django.apps import apps

# if settings.DEBUG:
if apps.is_installed("debug_toolbar"):
    urlpatterns += debug_toolbar_urls()
