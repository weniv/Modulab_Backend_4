# .env 파일을 읽어서, 환경변수로서 로딩
#  - python-dotenv  : FastAPI 등에서 활용
#  - django-environ : 장고 편의기능이 있어요.

from environ import Env  # django-environ 라이브러리
from pathlib import Path

# __file__ : 현재 소스파일의 경로
#  cf. __name__ : 현재 소스파일의 모듈명

BASE_DIR = Path(__file__).parent
ENV_PATH = BASE_DIR / ".env"

env = Env()
# 디폴트로 같은 이름의 환경변수가 있다면, 무시합니다.
# 덮어쓸려면 overwrite=True 인자를 지정합니다.
# 지정 경로의 .env 파일이 없어도 예외 발생없이 조용히 무시됩니다.
env.read_env(ENV_PATH, overwrite=True)

# 환경변수 값을 읽어서 별도의 변수에 할당
#  - 여러 로직에서 매번 환경변수 값에 직접 접근하는 것보다
#    환경변수 접근은 특정 로직에서만 해서
#    그 로직에서 설정 변수를 만들고 다른 로직에서 참조토록 하면
#    훨씬 관리성이 좋습니다.

# 환경변수 값은 항상 문자열(str)
# import os
# UPSTAGE_API_KEY = os.environ["UPSTAGE_API_KEY"]
OPENAI_API_KEY = env.str("OPENAI_API_KEY")

from pyhub.llm import UpstageLLM
from pyhub.llm import OpenAILLM

# 내부적으로 UPSTAGE_API_KEY 환경변수 값이 있으면,
# 자동으로 활용합니다.
llm = UpstageLLM()  # solar-mini
# llm = OpenAILLM(model="gpt-4o-mini")  # OPENAI_API_KEY 환경변수가 있으면 자동 활용

# 한 번에 모든 응답을 받아서, 출력 <= 응답까지 느릴 수 밖에 없어요.
# reply = llm.ask("hello")
# print(reply)
# print(reply.usage)

# stream=True 지정하시면, Generator 반환
# for chunk in llm.ask("python의 generator에 대해서 예시와 함께 설명해줘.", stream=True):
#     print(chunk.text, end="")
# print()

reply = llm.ask(
    "우울해서 빵을 샀어.", choices=["기쁨", "슬픔", "분노", "불안", "무기력함"]
)
print(reply.choice)  # "슬픔"
print(reply.choice_index)  # 1
