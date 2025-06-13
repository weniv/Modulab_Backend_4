# 라이브러리 설치 : python -m pip install -U "pyhub-llm[all]"

from pyhub.llm import UpstageLLM, OpenAILLM, GoogleLLM, AnthropicLLM

# TODO: 각자의 업스테이지 api key를 지정해주세요.
#  - https://console.upstage.ai/api-keys
# api_key = ""  # 끝에 콤마 제거. 반드시 !!!

llm = UpstageLLM(api_key=api_key)
# 다양한 LLM을 같은 인터페이스로 사용하실 수 있습니다.
# llm = OpenAILLM()
# llm = GoogleLLM()
# llm = AnthropicLLM()

reply = llm.ask("hello")
print(reply)
