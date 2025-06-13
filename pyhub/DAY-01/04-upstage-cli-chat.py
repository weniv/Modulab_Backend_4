from openai import OpenAI

# TODO: 각자의 업스테이지 api key를 지정해주세요.
#  - https://console.upstage.ai/api-keys
# api_key = ""  # 끝에 콤마 제거. 반드시 !!!

client = OpenAI(
    api_key=api_key,
    base_url="https://api.upstage.ai/v1",
)

messages: list[dict] = [
    {
        "role": "system",  # system, user, assistant, function, ...
        "content": "너는 다양한 레시피를 알고 있는 조리사야.",
    },
]  # 주의 : 끝에 콤마(,)가 있으면 안 되요 !!!

# 무한 루프 (break를 만나면 종료됩니다.)
while True:
    # strip : 좌우 화이트 스페이스 (공백, 개행, 탭 문자)를 모두 제거
    human_message = input("Human :").strip()  # 유저로부터 1줄을 입력받아 반환
    if human_message == "종료":
        break
    if human_message:
        # TODO: 현 채팅방의 대화내역 조회 from DB

        messages.append({
            "role": "user",
            "content": human_message,
        })

        # stream 여부에 따라, 반환값이 달라요.
        completion = client.chat.completions.create(
            model="solar-pro2-preview",  # 7/15까지 무료
            messages=messages,
        )

        # assistant 메시지
        ai_message = completion.choices[0].message.content
        # TODO: 현 채팅방의 대화내역으로서 추가 to DB
        messages.append({
            "role": "assistant",
            "content": human_message,
        })
        print("AI :", ai_message)
