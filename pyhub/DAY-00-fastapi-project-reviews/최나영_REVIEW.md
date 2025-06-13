# 코드 리뷰 - FastAPI ChatGPT 미니 프로젝트

## 프로젝트 소개
FastAPI ChatGPT 미니 프로젝트는 최신 웹 기술과 AI를 결합한 대화형 챗봇 플랫폼입니다. JWT 기반의 안전한 인증 시스템을 통해 사용자별로 개인화된 대화를 관리하고, OpenAI의 ChatGPT API를 활용하여 자연스럽고 지능적인 대화를 제공합니다. 깔끔한 UI와 실시간 응답으로 사용자 친화적인 AI 대화 경험을 구현했습니다.

## 프로젝트 정보
- **프로젝트명**: FastAPI ChatGPT 미니 프로젝트
- **저장소**: https://github.com/최나영/fastapi-chatgpt-mini
- **기술 스택**: FastAPI, JWT 인증, OpenAI ChatGPT API, HTML/CSS/JavaScript
- **목표**: JWT 기반 인증 시스템과 OpenAI ChatGPT API 연동이 구현된 AI 챗봇 애플리케이션

## 잘한 점 👍
1. **모듈화**: 인증(auth.py), 모델(models.py), 메인 로직(main.py)이 잘 분리되어 있습니다.
2. **JWT 인증**: OAuth2 password flow를 사용한 JWT 토큰 기반 인증이 잘 구현되어 있습니다.
3. **비동기 처리**: httpx를 사용한 비동기 API 호출로 성능을 최적화했습니다.
4. **에러 처리**: API 호출 시 타임아웃, HTTP 에러 등을 적절히 처리합니다.
5. **채팅 기록 관리**: 사용자별 채팅 히스토리를 저장하고 불러오는 기능이 구현되어 있습니다.
6. **프론트엔드 UX**: 로딩 상태, 에러 메시지, 자동 로그인 등 사용자 경험을 고려했습니다.

## 개선이 필요한 부분 🔧

### 1. 보안 이슈

#### SECRET_KEY 하드코딩
```python
# 현재 코드
SECRET_KEY = "your-super-secret-key"

# 개선안
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY 환경 변수가 설정되지 않았습니다.")
```

#### localStorage에 토큰 저장
```javascript
// 현재 코드 - XSS 공격에 취약
localStorage.setItem('accessToken', accessToken);

// 개선안 1: httpOnly 쿠키 사용 (백엔드 수정 필요)
// 개선안 2: 메모리에만 저장하고 새로고침 시 재로그인
```

#### CORS 설정
```python
# 프로덕션 환경에서는 특정 도메인만 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type"],
)
```

### 2. 데이터 지속성

#### 메모리 기반 저장소 문제
```python
# 현재 코드
fake_users_db = {}
fake_chat_db = defaultdict(list)

# 개선안: SQLAlchemy + SQLite/PostgreSQL
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    chats = relationship("ChatMessage", back_populates="user")

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    role = Column(String)
    content = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="chats")
```

### 3. 입력 검증 강화

```python
from pydantic import BaseModel, Field, validator

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, regex="^[a-zA-Z0-9_]+$")
    password: str = Field(..., min_length=8, max_length=100)
    
    @validator('password')
    def validate_password(cls, v):
        if not any(char.isdigit() for char in v):
            raise ValueError('비밀번호는 최소 하나의 숫자를 포함해야 합니다')
        if not any(char.isupper() for char in v):
            raise ValueError('비밀번호는 최소 하나의 대문자를 포함해야 합니다')
        return v
```

### 4. 모델 개선

```python
from pydantic import Field
from datetime import datetime

class ChatMessage(BaseModel):
    username: str
    role: str
    content: str
    # Field의 default_factory 사용
    timestamp: datetime = Field(default_factory=datetime.now)
```

### 5. API 재시도 로직

```python
import backoff

@backoff.on_exception(
    backoff.expo,
    httpx.HTTPStatusError,
    max_tries=3,
    max_time=60
)
async def call_bootcamp_api_with_retry(messages: List[Dict]) -> Dict:
    return await call_bootcamp_api(messages)
```

### 6. 백그라운드 태스크 활용

```python
from fastapi import BackgroundTasks

@app.post("/chat/simple")
async def simple_chat(
    request: SimpleChatRequest, 
    background_tasks: BackgroundTasks,
    current_user: UserInDB = Depends(get_current_user)
):
    # ... 기존 코드 ...
    
    # 백그라운드에서 채팅 기록 저장
    background_tasks.add_task(
        save_chat_to_database, 
        current_user.username, 
        user_message, 
        ai_message
    )
    
    return ChatResponse(response=ai_response_content, usage=usage_info)
```

### 7. 프론트엔드 개선

#### API URL 환경 설정
```javascript
const API_BASE_URL = window.location.origin || 'http://localhost:8000';
```

#### 디바운싱 추가
```javascript
let typingTimer;
const doneTypingInterval = 1000;

chatInput.addEventListener('keyup', () => {
    clearTimeout(typingTimer);
    typingTimer = setTimeout(() => {
        // 타이핑 완료 후 동작
    }, doneTypingInterval);
});
```

### 8. 로깅 추가

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/chat/simple")
async def simple_chat(...):
    logger.info(f"User {current_user.username} sent message: {request.message[:50]}...")
    # ... 기존 코드 ...
```

## 추가 권장사항 📝

1. **테스트 코드 작성**
   ```python
   # test_auth.py
   def test_create_user():
       # 사용자 생성 테스트
   
   def test_login():
       # 로그인 테스트
   ```

2. **API 문서화 개선**
   ```python
   app = FastAPI(
       title="ChatGPT API 서버",
       description="AI 챗봇 서비스 API",
       version="1.0.0",
       docs_url="/docs",
       redoc_url="/redoc"
   )
   ```

3. **환경별 설정 분리**
   ```python
   # config.py
   class Settings(BaseSettings):
       secret_key: str
       database_url: str
       openai_api_url: str
       
       class Config:
           env_file = ".env"
   ```

4. **Rate Limiting**
   ```python
   from slowapi import Limiter
   limiter = Limiter(key_func=get_remote_address)
   
   @app.post("/chat/simple")
   @limiter.limit("10/minute")
   async def simple_chat(...):
   ```

## 결론
전체적으로 잘 구조화된 프로젝트입니다. 특히 인증 시스템과 비동기 처리가 잘 구현되어 있습니다. 보안과 데이터 지속성 측면에서 개선하면 프로덕션 환경에서도 사용 가능한 수준의 애플리케이션이 될 것입니다.