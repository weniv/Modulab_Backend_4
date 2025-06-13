# LLM CheatSheet

## 라이브러리 설치

```
python -m pip install "pyhub-llm[all]"
```

## LLM 선택

### OpenAI 활용

```python
from pyhub.llm import OpenAILLM
from pyhub.llm.types import Reply

api_key = None  # TODO: UPSTAGE_API_KEY 지정하기
# 디폴트 model : gpt-4o-mini
llm = OpenAILLM(api_key=api_key)

reply: Reply = llm.ask("hello")
print(reply.text)
```

### 업스테이지 활용

```python
from pyhub.llm import UpstageLLM
from pyhub.llm.types import Reply

api_key = None  # TODO: UPSTAGE_API_KEY 지정하기
# 디폴트 model : solar-mini
llm = UpstageLLM(
    api_key=api_key,
    # model="solar-mini",  # default
    # model="solar-pro2-preview",  # 7월 15일까지 무료
)

reply: Reply = llm.ask("hello")
print(reply.text)
```

## 스트리밍 출력

```python
from pyhub.llm import UpstageLLM

api_key = None  # TODO: UPSTAGE_API_KEY 지정하기
llm = UpstageLLM(api_key=api_key)

for chunk in llm.ask("hello", stream=True):
    print(chunk.text, end="")
print()
```

## 분류 1

`choices` 인자 지정 만으로 별도의 프롬프트없이 지정 선택지 중에 하나만 선택해주기를 LLM에게 요청.

```python
from pyhub.llm import UpstageLLM

# 시스템 프롬프트없이도, LLM이 똑똑하기에 선택을 해줍니다.
llm = UpstageLLM()  #system_prompt="유저 메시지의 감정은?")

reply = llm.ask("우울해서 빵을 샀어.", choices=["기쁨", "슬픔", "분노", "불안", "무기력함"])
print(reply.choice)        # "슬픔"
print(reply.choice_index)  # 1
```

### 감정 분류에 따라, 잠언 구절 추천

```python
import csv
import random
from collections import defaultdict
from pyhub.llm import UpstageLLM

csv_path = "개역개정_잠언_전서_감정.csv"
감정에_따른_잠언_사전 = defaultdict(list)
with open(csv_path, "rt", encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        잠언_구절 = row["구절"]
        for 감정 in {word.strip() for word in row["감정"].split(",")}:
            감정에_따른_잠언_사전[감정].append(잠언_구절)

감정_목록 = list(감정에_따른_잠언_사전.keys())

def 잠언_구절_추천(s: str) -> str:
    llm = UpstageLLM(system_prompt="What is the emotion of the user message?")
    reply = llm.ask(s, choices=감정_목록)
    감정 = reply.choice
    if 감정 is None:
        return "감정을 알 수 없네요."
    else:
        잠언_구절_리스트: list[str] = 감정에_따른_잠언_사전[reply.choice]
        return random.choice(잠언_구절_리스트)

print(잠언_구절_추천("우울해서 빵을 샀어."))
```

## 다국어 응답 생성

```python
from pydantic import BaseModel
from pyhub.llm import UpstageLLM

class ReplySchema(BaseModel):
    korean: str
    english: str

llm = UpstageLLM(system_prompt="감정에 맞는 철학자 명언을 추천하고, 한국어와 영어로 제공해줘.")
reply = llm.ask("기쁨", schema=ReplySchema)
print(reply)
obj: ReplySchema = reply.structured_data
print(obj)  # ReplySchema(korean='행복이란 자기가 좋아하는 일을 하는 것이다. - 마하트마 간디', english='Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi')
print(obj.korean)  # 행복이란 자기가 좋아하는 일을 하는 것이다. - 마하트마 간디
print(obj.english)  # Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi
```

## 분류 2

```python
from pyhub.llm import UpstageLLM

def 요리_질문_여부(s: str) -> bool:
    llm = UpstageLLM(system_prompt="요리 관련 질문인지 여부를 판정")
    reply = llm.ask(s, choices=["t", "f"])
    return reply.choice_index == 0

요리_질문_여부("자전거 타는 법")
```
