# 코드 리뷰 - 운세 GPT 챗봇 프로젝트

## 프로젝트 소개
운세 GPT 챗봇은 일상 속 위로와 조언이 필요한 사람들을 위한 AI 기반 맞춤형 운세 서비스입니다. 사용자의 이름, 생년월일, 성별, 고민을 입력받아 ChatGPT가 별자리, 사주, 타로카드 등을 종합한 개인 맞춤 운세를 제공합니다. 귀여운 네잎클로버 캐릭터와 함께하는 감성적인 UI로 운세를 보는 재미를 더하고, 모든 대화와 운세 결과를 저장하여 나만의 운세 일기를 만들 수 있습니다.

## 프로젝트 정보
- **프로젝트명**: 운세 GPT 챗봇
- **저장소**: https://github.com/hyoeunjeong/chatbot-fastapi
- **기술 스택**: FastAPI, SQLite, httpx, Weniv OpenAI Proxy API
- **목표**: 사용자의 정보(이름, 생년월일, 성별, 고민)를 입력받아 AI가 맞춤 운세를 제공하고 기록을 저장하는 웹 애플리케이션

## 현재 상태 ✅
- **구현 완료**: 회원가입/로그인, GPT 챗봇, 대화 기록 저장, 운세 결과 조회
- **백엔드**: FastAPI + SQLite + httpx (Weniv OpenAI Proxy API 사용)
- **프론트엔드**: HTML/CSS/JavaScript (클로버 테마의 감성적인 UI)
- **데이터베이스**: SQLite (chat_logs.db) - 대화 기록과 운세 결과 저장

## 구현된 주요 기능 ✨

### 1. 인증 시스템 (auth.py)
- SHA256 해시를 사용한 비밀번호 암호화
- UUID 기반 세션 관리
- 메모리 기반 사용자 데이터베이스

### 2. 데이터베이스 (SQLite)
- `chat_messages`: 대화 기록 저장
- `chat_results`: 운세 결과 저장
- 사용자별 기록 분리 저장

### 3. API 엔드포인트
- `/register`, `/login`, `/logout`: 사용자 인증
- `/chats`: 대화 메시지 저장/조회
- `/results`: 운세 결과 저장/조회
- `/chat/send`: GPT API 연동
- `/my-results`: 개인 운세 기록 조회

### 4. 프론트엔드
- 실시간 채팅 인터페이스
- 3가지 랜덤 인트로 메시지
- 운세 결과 보기 및 초기화 기능
- 클로버 테마의 감성적인 디자인

## 보완이 필요한 부분 🔧

### 1. 보안 강화
```python
# [리뷰] SHA256은 비밀번호 해싱에 적합하지 않습니다
# [보완] bcrypt 또는 argon2 사용 권장
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
```

### 2. 데이터베이스 개선
```python
# [리뷰] 사용자 정보가 메모리에만 저장되어 서버 재시작 시 소실됨
# [보완] SQLAlchemy 또는 SQLModel 사용하여 영구 저장
from sqlmodel import Field, SQLModel, Session, create_engine

class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

engine = create_engine("sqlite:///chat_logs.db")
SQLModel.metadata.create_all(engine)
```

### 3. 환경 변수 관리
```python
# [리뷰] API 키가 하드코딩되어 있음
# [보완] .env 파일 사용 및 환경 변수로 관리
from dotenv import load_dotenv
import os

load_dotenv()

WENIV_API_KEY = os.getenv("WENIV_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///chat_logs.db")
```

### 4. 에러 처리 개선
```python
# [리뷰] 일반적인 except 절은 모든 예외를 잡아 디버깅이 어려움
# [보완] 구체적인 예외 처리
@app.post("/chat/send")
async def chatbot_response(request: ChatMessage):
    try:
        async with httpx.AsyncClient() as client:
            res = await client.post(
                BOOTCAMP_API_URL, 
                json=request.messages, 
                timeout=20.0
            )
            res.raise_for_status()
            data = res.json()
            return {"answer": data["choices"][0]["message"]["content"]}
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="API 요청 시간 초과")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="API 요청 실패")
    except KeyError:
        raise HTTPException(status_code=500, detail="API 응답 형식 오류")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="서버 내부 오류")
```

### 5. 프론트엔드 개선사항
```javascript
// [리뷰] sessionStorage 사용으로 새로고침 시 데이터 유지 안 됨
// [보완] localStorage 또는 서버 세션 활용
const STORAGE_KEY = 'fortune_history';

function saveFortune(fortune) {
    const history = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
    history.push({
        fortune: fortune,
        timestamp: new Date().toISOString(),
        username: USERNAME
    });
    localStorage.setItem(STORAGE_KEY, JSON.stringify(history));
}

// [리뷰] XSS 공격 위험 (textContent 사용은 좋음)
// [보완] 사용자 입력 검증 추가
function validateInput(input) {
    const maxLength = 500;
    if (input.length > maxLength) {
        throw new Error(`메시지는 ${maxLength}자 이내로 입력해주세요.`);
    }
    return input.trim();
}
```

### 6. 성능 최적화
```python
# [리뷰] 동기적 DB 작업으로 인한 성능 저하
# [보완] 비동기 데이터베이스 드라이버 사용
from databases import Database
from sqlalchemy.ext.asyncio import create_async_engine

# 비동기 DB 연결
database = Database("sqlite+aiosqlite:///chat_logs.db")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# [리뷰] 대화 기록이 많아질수록 느려짐
# [보완] 페이지네이션 구현
@app.get("/chats")
async def get_chats(
    username: Optional[str] = None,
    skip: int = 0,
    limit: int = 50
):
    query = chat_messages.select()
    if username:
        query = query.where(chat_messages.c.username == username)
    query = query.offset(skip).limit(limit)
    return await database.fetch_all(query)
```

## 추가 개선 사항 📝

### 1. 테스트 코드 작성
```python
# tests/test_auth.py
import pytest
from auth import create_user, authenticate_user

def test_create_user():
    result = create_user("testuser", "test@email.com", "password123")
    assert result["success"] == True
    assert result["user"].username == "testuser"

def test_duplicate_user():
    create_user("testuser", "test@email.com", "password123")
    result = create_user("testuser", "test2@email.com", "password456")
    assert result["success"] == False
```

### 2. API 문서화
```python
# [보완] OpenAPI 스키마에 더 자세한 설명 추가
app = FastAPI(
    title="운세 GPT 챗봇 API",
    description="AI 기반 맞춤 운세 제공 서비스",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.post(
    "/chat/send",
    summary="운세 질문 전송",
    description="사용자의 질문을 받아 AI가 운세를 분석하여 응답합니다.",
    response_description="AI의 운세 분석 결과"
)
```

### 3. 로깅 시스템
```python
import logging
from logging.handlers import RotatingFileHandler

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler('app.log', maxBytes=10485760, backupCount=5),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
```

### 4. 배포 설정
```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 잘 구현된 부분 👍
1. **완성도 높은 MVP**: 핵심 기능이 모두 동작하는 완성된 프로젝트
2. **감성적인 UI**: 클로버 테마와 3가지 인트로 메시지로 재미있는 사용자 경험
3. **체계적인 구조**: auth, models, main으로 모듈화된 구조
4. **데이터 영속성**: SQLite를 활용한 대화 기록 저장
5. **RESTful API**: 명확한 엔드포인트 설계

## 프로젝트 회고 반영 💭
작성자가 README에서 언급한 회고 내용을 보면:
- ✅ 세션 기반 로그인 구현 성공
- ✅ GPT와 실시간 대화 가능
- ✅ 사용자별 기록 분리 저장
- ✅ 예쁜 UI (클로버 테마)
- ⚠️ AI 의존도가 높아 직접적인 코드 이해 부족

이는 프로젝트를 통해 실무 경험을 쌓은 좋은 사례입니다. 다음 프로젝트에서는 위에서 제안한 보완사항들을 하나씩 직접 구현해보면서 더 깊은 이해를 얻을 수 있을 것입니다.

## 다음 단계 제안 🚀
1. **보안 강화**: bcrypt로 비밀번호 해싱 변경
2. **데이터베이스 개선**: SQLAlchemy로 사용자 정보도 영구 저장
3. **테스트 작성**: pytest로 단위 테스트 추가
4. **비동기 처리**: aiosqlite로 성능 개선
5. **배포**: Docker + Cloud Run/Heroku로 실제 서비스화

## 결론
운세 챗봇 프로젝트가 성공적으로 구현되었습니다! 웹 개발의 전체 흐름을 경험한 의미 있는 프로젝트이며, 제안된 개선사항들을 적용하면 더욱 견고하고 확장 가능한 서비스가 될 것입니다.