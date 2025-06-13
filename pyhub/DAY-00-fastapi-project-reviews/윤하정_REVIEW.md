# 코드 리뷰 - 기분에 따른 철학 명언 추천 서비스

## 프로젝트 소개
기분에 따른 철학 명언 추천 서비스는 현대인의 정서적 안정과 삶의 지혜를 제공하는 AI 기반 명언 큐레이션 플랫폼입니다. 사용자가 현재의 기분(행복, 슬픔, 화남, 불안 등)을 선택하면, ChatGPT가 그 감정에 맞는 철학자들의 명언을 한국어와 영어로 제공합니다. 명언을 통해 위로받고, 삶의 통찰을 얻으며, 저장 기능으로 나만의 명언 컬렉션을 만들 수 있습니다.

## 프로젝트 정보
- **프로젝트명**: 기분에 따른 철학 명언 추천 서비스
- **저장소**: https://github.com/윤하정/mood-philosophy-quotes
- **기술 스택**: FastAPI, HTML/CSS/JavaScript, ChatGPT API, 세션 기반 인증
- **목표**: 사용자의 기분에 맞는 철학 명언을 한국어와 영어로 제공하는 웹 서비스

## 잘한 점 👍
1. **기능 분리**: 사용자 인증과 GPT 명언 기능을 별도의 라우터로 잘 분리했습니다.
2. **세션 관리**: UUID를 사용한 세션 ID 생성으로 기본적인 인증을 구현했습니다.
3. **비동기 처리**: httpx를 사용한 비동기 API 호출을 적절히 활용했습니다.
4. **데이터 저장**: history.json 파일로 사용자별 명언 기록을 관리합니다.
5. **에러 처리**: 기본적인 예외 처리를 구현했습니다.

## 개선이 필요한 부분 🔧

### 1. 보안 이슈
- **비밀번호 해싱**: SHA256 대신 bcrypt나 argon2 사용 필요
```python
# 현재 코드 (취약함)
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# 개선 예시
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)
```

- **CORS 설정**: `allow_origins=["*"]`는 보안상 위험
```python
# 프로덕션 환경에서는 특정 도메인만 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

### 2. 데이터 지속성
- 메모리 기반 저장소는 서버 재시작 시 데이터 손실
- SQLite나 PostgreSQL 같은 데이터베이스 사용 권장
```python
# SQLAlchemy 사용 예시
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///./app.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
```

### 3. 입력 검증 강화
```python
# Pydantic 모델에 필드 검증 추가
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, regex="^[a-zA-Z0-9_]+$")
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=100)
    
    @validator('password')
    def validate_password(cls, v):
        if not any(char.isdigit() for char in v):
            raise ValueError('비밀번호는 최소 하나의 숫자를 포함해야 합니다')
        if not any(char.isupper() for char in v):
            raise ValueError('비밀번호는 최소 하나의 대문자를 포함해야 합니다')
        return v
```

### 4. 세션 관리 개선
- 세션 만료 시간 추가
- Redis를 사용한 세션 저장소 또는 JWT 토큰 고려
```python
from datetime import datetime, timedelta

sessions = {}  # {session_id: {"username": str, "expires_at": datetime}}

def create_session(username: str) -> str:
    session_id = str(uuid.uuid4())
    sessions[session_id] = {
        "username": username,
        "expires_at": datetime.utcnow() + timedelta(hours=24)
    }
    return session_id

def get_current_user(session_id: str) -> Optional[dict]:
    if session_id not in sessions:
        return None
    
    session = sessions[session_id]
    if datetime.utcnow() > session["expires_at"]:
        del sessions[session_id]
        return None
    
    return users_db.get(session["username"])
```

### 5. API 일관성 개선
- RESTful 원칙에 따라 URL 패턴 통일
- POST 요청에는 쿼리 파라미터 대신 request body 사용
```python
# 현재 코드
@gpt_router.post("/save-quote")
def save_quote(nickname: str, mood: str):

# 개선안
class QuoteCreate(BaseModel):
    nickname: str
    mood: str

@gpt_router.post("/quotes")
async def save_quote(quote_data: QuoteCreate):
```

### 6. 환경 변수 관리
```python
# .env 파일 사용
from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    OPENAI_API_URL: str = os.getenv("OPENAI_API_URL")

settings = Settings()
```

### 7. 프론트엔드 보안
- XSS 방지를 위해 innerHTML 대신 textContent 사용
```javascript
// 현재 코드 (XSS 취약)
output.innerHTML = `<p>${korean}</p>`;

// 개선안
const koreanP = document.createElement('p');
koreanP.textContent = korean;
output.appendChild(koreanP);
```

### 8. 함수명 오타 수정
- `get_jistory` → `get_history`

## 추가 권장사항 📝
1. **로깅**: Python logging 모듈로 에러 및 접근 로그 기록
2. **API 문서화**: FastAPI의 자동 문서 기능 활용
3. **테스트 코드**: pytest를 사용한 단위 테스트 및 통합 테스트
4. **타입 힌트**: 모든 함수에 타입 힌트 추가
5. **백그라운드 작업**: 명언 저장을 백그라운드 태스크로 처리

## 결론
기본적인 기능은 잘 구현되어 있으나, 보안과 데이터 지속성 측면에서 개선이 필요합니다. 특히 비밀번호 해싱 방식과 데이터베이스 사용은 프로덕션 환경에서 필수적으로 개선해야 할 사항입니다.