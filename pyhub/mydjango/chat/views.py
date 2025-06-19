from urllib import request

from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect
from chat.forms import PuzzleRoomForm, PuzzleRoomEditForm
from chat.models import PuzzleRoom


# django view : http 요청을 받아 요청을 처리하는 함수 (Function Based View, FBV)
#   => 장고에서는 클래스로 View를 만들거예요. => 클래스 기반 뷰 (Class Based View, CBV)

# 채팅 기본 화면을 보여주겠습니다.
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "chat/index.html")


# 매 채팅 메시지를 받아, 응답 메시지를 만들고, 응답하겠어요.
# HTTP Methods : GET, POST, PUT/PATCH, DELETE, OPTIONS
#  - HTTP: 웹 페이지, 웹 문서를 위한 프로토콜
#  - <form method=""> 태그(유저로부터 입력을 받아 지정 서버로 전송)에서는 GET, POST 만 지원
#    - GET : 조회 목적 => 요청해도 데이터는 변하지 않는다. 안전하다. => 검색엔진은 항상 GET 요청.
#    - POST : 파괴적인 액션 (추가/수정/삭제 등)
#      - 조회목적인데 POST 요청을 하는 서비스가 있어요. (물론 필요하면 하면 됩니다.)
#        가급적이면 조회에서는 GET 요청을 쓰시면, 서비스를 최적화를 여지가 많고, 이를 도와주는 서비스/프로그램도 많아요.
#  - JS API를 통해서 PUT/PATCH, DELETE 등의 요청을 할 수 있어요.
def chat_message_new(request: HttpRequest) -> HttpResponse:
    # Query Parameters
    request.GET   # QueryDict 타입 (Dict 으로 보여도 90% 무방)  # POST 요청에서도 있을 수 있어요.
    request.POST  # POST 데이터 (QueryDict)

    question = request.POST.get("question", "")
    if question:
        answer = f"당신의 질문 : {question}"
    else:
        answer = "질문이 없으시네요."
    
    return HttpResponse(answer)


# url encoding = "key=value&key&value=key&value"
# url encoding 문자열이 요청 주소 뒤에 물음표(?) 뒤에 붙으면 => 그걸 Query Parameters
# https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=python&ackey=4rvenuph

# """
# where=nexearch
# sm=top_hty
# fbm=0
# ie=utf8
# query=python
# ackey=4rvenuph
# """


# TODO: 왜 puzzle_room_list가 아니라 puzzleroom_list 인가요?

def puzzleroom_list(request):
    # puzzle room 테이블에 있는 모든 레코드를 가져올 준비
    qs = PuzzleRoom.objects.all()  # QuerySet 타입
    return render(
        request,
        template_name="chat/puzzleroom_list.html",
        context={ "puzzleroom_list": qs })


# chat/views.py

# chat/urls.py 에서 name 인자를 추출해서
# View 함수 호출 시에 자동으로 인자를 전달해줍니다.

def puzzleroom_play(request: HttpRequest, id: int) -> HttpResponse:

    # id 값을 통해서, 아래 값을 찾아서 할당을 할 겁니다.

    room = PuzzleRoom.objects.get(id=id)
    image_url = room.image_file.url
    level = room.level

    # toy, mario, flower, game
    return render(
        request,
        # 이 템플릿 내의 코드는 모두 그냥 문자열 !!!
        template_name="chat/puzzle.html",
        # "image_url" 이라는 이름으로 image_url 값을 전달합니다.
        # 대개 같은 이름으로 지정합니다.
        context={
            "image_url": image_url,
            "level": level,
        },
    )


# 1개의 PuzzleRoom 생성을 위해서, 최소 2번의 요청을 받을 겁니다.
#  1) GET 요청 : 빈 입력 서식을 보여줘야 합니다.
#  2) POST 요청 : 유저가 서식에 값을 채우고, 전송(저장)버튼을 눌렀을 때, 유저의 입력값을 전송 (반복)
def puzzleroom_new(request: HttpRequest) -> HttpResponse:

    if request.method == "GET":  # "GET" or "POST" 뿐. (항상 대문자)
        # 1) 빈 입력 서식을 보여주겠습니다.
        form = PuzzleRoomForm()

    else:  # "POST" : 유저가 입력한 값에 대한 유효성 검사, pass(저장), fail(에러 응답)
        # request.POST   # POST 요청에서의 데이터 (파일 제외)
        # request.FILES  # POST 요청에서의 데이터 (파일 만)

        # Form에게 유저의 모든 입력 데이터를 전달
        form = PuzzleRoomForm(data=request.POST, files=request.FILES)
        # form : 유저가 전달한 값을 모두 알고 있습니다. + 입력 필드 구성도 모두 알고 있습니다.

        # 호출 즉시, 유효성 검사를 수행합니다.
        # 단 1개의 유효성 검사라도 실패하면, False 반환. 모두 통과하면 True 반환
        if form.is_valid():
            form.save()  # 데이터베이스에 저장합니다. (ModleForm 만의 기능)
            # TODO: 성공 메시지, 저장된 게임룸으로 즉시 이동
            return redirect("/chat/puzzle/")  # django.shortcuts
        else:
            pass  # 그냥 아래 템플릿 렌더링을 합니다. + 에러 출력 기능까지 있습니다.

    # 장고의 문화 대로, 파일명과 View 이름을 쓰고 있어요.
    return render(request, "chat/puzzleroom_form.html", {
        "form": form,
    })


def puzzleroom_edit(request: HttpRequest, id: int) -> HttpResponse:
    # 수정 대상을 데이터베이스에서 조회
    room = PuzzleRoom.objects.get(id=id)

    if request.method == "GET":
        form = PuzzleRoomEditForm(instance=room)

    else:
        form = PuzzleRoomEditForm(instance=room, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/chat/puzzle/")

    return render(request, "chat/puzzleroom_form.html", {
        "form": form,
    })
