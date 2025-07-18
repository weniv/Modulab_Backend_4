# blog/permissions.py

from django.db.models import Model
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from rest_framework.views import APIView


class IsAuthorOrReadonly(BasePermission):
    # 지정 APIView를 호출하기 전에, 이를 호출하여 허용여부를 결정합니다.
    def has_permission(self, request, view) -> bool:
        if request.method in SAFE_METHODS:
            return True
        else:  # create, update, destroy
            # 인증된 유저에 한해서만 허용하겠다.
            return request.user.is_authenticated

    # APIView 단에서 지정 모델 인스턴스를 조회하는 get_object 메서드가 있어요.
    # get_object 호출 시에, 해당 object에 대한 접근 허용 여부를 결정합니다.
    def has_object_permission(self, request, view, obj) -> bool:
        if request.method in SAFE_METHODS:
            return True

        # 삭제는 관리자만 허용하겠다.
        # if request.method == "DELETE":
        #     # is_staff, is_superuser
        #     return request.user.is_staff

        # UPDATE, PARTIAL_UPDATE, DESTROY
        if not hasattr(obj, "author"):
            return False

        # 작성자에 한해서, 허용
        return obj.author == request.user
