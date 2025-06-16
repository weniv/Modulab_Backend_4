
# .env 파일을 읽어서, 환경변수로서 로딩
#  - python-dotenv
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
env.read_env(ENV_PATH, overwrite=True)

# 환경변수 값을 읽어서 별도의 변수에 할당
#  - 여러 로직에서 매번 환경변수 값에 직접 접근하는 것보다
#    환경변수 접근은 특정 로직에서만 해서
#    그 로직에서 설정 변수를 만들고 다른 로직에서 참조토록 하면
#    훨씬 관리성이 좋습니다.

# 환경변수 값은 항상 문자열(str)
# import os
# UPSTAGE_API_KEY = os.environ["UPSTAGE_API_KEY"]

from pyhub.llm import UpstageLLM

# 내부적으로 UPSTAGE_API_KEY 환경변수 값이 있으면,
# 자동으로 활용합니다.
llm = UpstageLLM()
reply = llm.ask("hello")
print(reply)
print(reply.usage)
