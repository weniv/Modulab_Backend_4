from openai import OpenAI

# TODO: 각자의 업스테이지 api key를 지정해주세요.
#  - https://console.upstage.ai/api-keys
# api_key = ""  # 끝에 콤마 제거. 반드시 !!!

client = OpenAI(
    api_key=api_key,  # CHANGED
    base_url="https://api.upstage.ai/v1",  # ADDED
)

completion = client.chat.completions.create(
    # model="solar-mini",  # CHANGED
    model="solar-pro2-preview",  # 7/15까지 무료
    messages=[
        {
            "role": "user",
            "content": "hello",
        }
    ]
)

print(completion.choices[0].message.content)
