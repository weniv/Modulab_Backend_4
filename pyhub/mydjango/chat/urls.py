from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("messages/new/", views.chat_message_new),

    #
    # /chat/puzzle/mario/
    # /chat/puzzle/toy/
    # /chat/puzzle/running/

    path("puzzle/", views.puzzleroom_list),

    # puzzle/ 주소 에 문자열 패턴이 있고, 뒤에 / 가 있으면

    # 가급적이면 이 패턴은 타이트하게 지정하시기를 권장.
    # => 엉뚱하게 예상치못한 URL 패턴까지 잡아버리는 상황을 막을 수 있어요.
    path("puzzle/<int:id>/", views.puzzleroom_play),  # ADDED

    path("puzzle/new/", views.puzzleroom_new),

    path("puzzle/<int:id>/edit/", views.puzzleroom_edit),

    # FastAPI
    # @app.get("/chat/puzzle/{name}")
    # def room(name: str): pass
]
