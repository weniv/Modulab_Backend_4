from rest_framework.pagination import CursorPagination


class PkCursorPagination(CursorPagination):
    # 커서 기반 페이징을 위해 정렬 순서 지정
    #  - 고유성, 불변성, 인덱싱
    ordering = "-id"
