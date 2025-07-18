from django.urls import path
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response


# IsAuthenticated 권한
#  - 미인증 상황의 HTTP 요청을 받았다면, 401 Unauthorized 응답

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request: Request) -> Response:
    return Response({
        "username": request.user.username,
        "email": request.user.email,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
    })


urlpatterns = [
    path("profile/", profile),
]
