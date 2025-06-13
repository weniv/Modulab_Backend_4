from openai import OpenAI

# TODO: 각자의 업스테이지 api key를 지정해주세요.
#  - https://console.upstage.ai/api-keys
# api_key = ""  # 끝에 콤마 제거. 반드시 !!!

client = OpenAI(
    api_key=api_key,
    base_url="https://api.upstage.ai/v1",
)

# stream 여부에 따라, 반환값이 달라요.
stream = client.chat.completions.create(
    model="solar-pro2-preview",  # 7/15까지 무료
    messages=[
        {
            "role": "user",
            "content": "맛있는 라면 레시피를 알려줘.",
        }
    ],
    stream=True,  # ADDED
)

# stream=False : 통응답을 받을 때
# print(completion.choices[0].message.content)

# API 서버에서 내려준 Chunk의 개수만큼 반복됩니다.
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        # end 키워드 인자의 디폴트 값 : 개행 ("\n")
        print(chunk.choices[0].delta.content, end="")
