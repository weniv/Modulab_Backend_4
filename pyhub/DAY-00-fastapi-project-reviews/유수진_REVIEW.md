# 유수진 프로젝트 코드 리뷰

## 프로젝트 소개
미래 시나리오를 함께 그려주는 힐링 챗봇은 현재의 어려움을 겪고 있는 사람들에게 희망과 위로를 전하는 AI 상담 서비스입니다. 사용자가 자신의 꿈이나 목표, 현재의 고민을 공유하면, AI가 긍정적이고 실현 가능한 미래 시나리오를 그려주며 정서적 지원을 제공합니다. 따뜻한 대화를 통해 자기 긍정감을 높이고, 미래에 대한 희망을 갖도록 돕습니다.

## 프로젝트 정보
- **프로젝트명**: 미래 시나리오를 함께 그려주는 힐링 챗봇
- **저장소**: https://github.com/유수진/healing-future-chatbot
- **기술 스택**: FastAPI, HTML/CSS/JavaScript, ChatGPT API, SHA256 비밀번호 해싱
- **목표**: 정서적 위안, 상상력 자극, 긍정적 자기 이미지 제공하는 AI 챗봇

## 현재 상태 분석 (업데이트)
프로젝트가 **완전히 구현된 상태**입니다. 최근에는 문서화 작업이 진행되었으며(README.md 구조화, 와이어프레임 추가), 백엔드와 프론트엔드가 잘 통합되어 작동합니다. 프로젝트명이 "방구석 힐링 챗봇"으로 브랜딩되었습니다.

### 구현된 주요 기능
1. **사용자 인증 시스템**: 회원가입, 로그인, 로그아웃, 세션 관리
2. **ChatGPT 통합**: 비동기 API 호출로 AI 응답 생성
3. **채팅 인터페이스**: 실시간 메시지 전송 및 표시
4. **에러 처리**: 재시도 로직 및 사용자 친화적 에러 메시지

## 잘된 점 👍

### 1. 완성도 높은 구현
- 백엔드와 프론트엔드가 모두 구현되어 있음
- 회원가입, 로그인, 채팅 기능이 실제로 작동
- 에러 처리와 재시도 로직이 잘 구현됨

### 2. 코드 품질
- **한글 주석과 함수명**: `내정보보기`, `로그아웃` 등 직관적인 네이밍
- **상세한 docstring**: 각 함수의 동작 과정을 단계별로 설명
- **Pydantic 모델**: 타입 안전성 확보
- **코드 리뷰 주석**: 개선점을 미리 표시

### 3. 사용자 경험
- 로딩 인디케이터로 사용자 피드백 제공
- Enter 키와 버튼 클릭 모두 지원
- 깔끔하고 모던한 UI 디자인
- 응답형 디자인으로 모바일 지원

### 4. 비동기 처리
- httpx를 사용한 비동기 API 호출
- async/await 패턴 올바르게 사용
- 타임아웃 설정으로 무한 대기 방지

### 5. 보안 고려사항
- HttpOnly 쿠키 사용
- 세션 기반 인증
- 비밀번호 해싱 (SHA256)
- CORS 설정

## 개선이 필요한 점 및 보완 방법 ⚠️

### 1. 보안 강화
**문제점**: 
- SHA256은 비밀번호 해싱에 적합하지 않음
- 세션 만료 시간 관리 미흡
- CORS 설정이 너무 개방적

**보완 방법**:
```python
# bcrypt 사용
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# 세션 만료 시간 추가
from datetime import datetime, timedelta

def create_session(username: str) -> str:
    session_id = str(uuid.uuid4())
    user_sessions[session_id] = {
        "username": username,
        "expires_at": datetime.now() + timedelta(hours=24)
    }
    return session_id

def get_current_user(session_id: str) -> Optional[dict]:
    session_data = user_sessions.get(session_id)
    if not session_data:
        return None
    
    # 만료 시간 확인
    if datetime.now() > session_data["expires_at"]:
        del user_sessions[session_id]
        return None
    
    username = session_data["username"]
    return users_db.get(username)

# CORS 설정 개선
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://your-domain.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"],
)
```

### 2. 힐링 챗봇 특화 기능
**문제점**: 일반적인 챗봇으로 구현되어 있어 힐링 챗봇의 특성이 부족

**보완 방법**:
```python
# chatgpt_api.py 수정
def get_healing_prompt(user_emotion: str = None) -> str:
    """사용자 감정에 따른 맞춤형 프롬프트 생성"""
    base_prompt = """당신은 따뜻하고 공감적인 힐링 상담사입니다.
    사용자의 현재 상황을 듣고, 긍정적인 미래 시나리오를 함께 그려주세요.
    
    대화 가이드라인:
    1. 먼저 사용자의 감정을 인정하고 공감해주세요
    2. 현재 상황에서 찾을 수 있는 작은 긍정적 요소를 발견해주세요
    3. 1년 후, 5년 후의 희망적인 미래를 구체적으로 그려주세요
    4. 그 미래를 위한 작은 첫걸음을 제안해주세요
    5. 항상 따뜻하고 격려하는 톤을 유지해주세요
    """
    
    emotion_prompts = {
        "sad": "\n특히 슬픔 속에서도 성장의 기회를 찾을 수 있도록 도와주세요.",
        "anxious": "\n불안을 줄이고 안정감을 찾을 수 있는 구체적인 방법을 제시해주세요.",
        "angry": "\n분노의 에너지를 긍정적인 변화의 동력으로 전환할 수 있도록 안내해주세요.",
        "lonely": "\n혼자가 아니며, 연결될 수 있는 방법들을 제시해주세요."
    }
    
    return base_prompt + emotion_prompts.get(user_emotion, "")

# 감정 분석 기능 추가
async def analyze_emotion(text: str) -> str:
    """텍스트에서 감정을 분석"""
    emotion_keywords = {
        "sad": ["슬프", "우울", "힘들", "외로", "눈물", "아프"],
        "anxious": ["불안", "걱정", "두렵", "무서", "긴장", "초조"],
        "angry": ["화나", "짜증", "분노", "열받", "억울", "답답"],
        "lonely": ["외로", "혼자", "쓸쓸", "고독", "그리워"],
        "happy": ["기쁘", "행복", "즐거", "신나", "좋아", "웃"]
    }
    
    text_lower = text.lower()
    for emotion, keywords in emotion_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            return emotion
    return "neutral"

# ask_chatgpt_async 함수 수정
async def ask_chatgpt_async(user_id: str, prompt_content: str) -> str:
    # 감정 분석
    emotion = await analyze_emotion(prompt_content)
    
    # 감정별 맞춤 프롬프트
    system_prompt = get_healing_prompt(emotion)
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt_content}
    ]
    
    # 나머지 코드는 동일...
```

### 3. 데이터 영속성
**문제점**: 메모리 기반 저장으로 서버 재시작 시 데이터 손실

**보완 방법**:
```python
# SQLite 데이터베이스 사용
import sqlite3
from contextlib import contextmanager

def init_db():
    conn = sqlite3.connect('healing_chatbot.db')
    cursor = conn.cursor()
    
    # 사용자 테이블
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 채팅 기록 테이블
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            sender_type TEXT NOT NULL,
            content TEXT NOT NULL,
            emotion TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # 세션 테이블
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            session_id TEXT PRIMARY KEY,
            username TEXT NOT NULL,
            expires_at TIMESTAMP NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (username) REFERENCES users (username)
        )
    ''')
    
    conn.commit()
    conn.close()

@contextmanager
def get_db():
    conn = sqlite3.connect('healing_chatbot.db')
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()
```

### 4. 사용자별 대화 관리
**문제점**: 모든 메시지가 하나의 딕셔너리에 저장되어 관리가 어려움

**보완 방법**:
```python
# 사용자별 대화 관리
from collections import defaultdict
from typing import List

# 사용자별 메시지 저장소
user_messages_db: Dict[str, List[ChatMessage]] = defaultdict(list)

# main.py 수정
@app.post("/chat", response_model=ChatMessage)
async def send_message(request: ChatRequest, session_id: Optional[str] = Cookie(None)):
    # 로그인 확인
    if not session_id:
        raise HTTPException(status_code=401, detail="로그인이 필요합니다")
    
    user = get_current_user(session_id)
    if not user:
        raise HTTPException(status_code=401, detail="유효하지 않은 세션입니다")
    
    user_id = user.username
    user_message_content = request.content
    
    # 사용자 메시지 저장
    user_message = ChatMessage(
        userId=user_id,
        senderType="user",
        content=user_message_content
    )
    user_messages_db[user_id].append(user_message)
    
    try:
        # 대화 컨텍스트 포함
        context = user_messages_db[user_id][-10:]  # 최근 10개 메시지
        bot_response_content = await ask_chatgpt_async(
            user_id=user_id, 
            prompt_content=user_message_content,
            context=context
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"챗봇 서버에서 오류가 발생했습니다: {str(e)}")
    
    # 봇 응답 저장
    bot_message = ChatMessage(
        userId=user_id,
        senderType="ai",
        content=bot_response_content
    )
    user_messages_db[user_id].append(bot_message)
    
    return bot_message

@app.get("/chat/history")
async def get_chat_history(
    session_id: Optional[str] = Cookie(None),
    limit: int = 50
):
    """사용자의 채팅 기록 조회"""
    if not session_id:
        raise HTTPException(status_code=401, detail="로그인이 필요합니다")
    
    user = get_current_user(session_id)
    if not user:
        raise HTTPException(status_code=401, detail="유효하지 않은 세션입니다")
    
    user_messages = user_messages_db.get(user.username, [])
    
    return {
        "messages": user_messages[-limit:],
        "total": len(user_messages)
    }
```

### 5. 환경 변수 관리
**문제점**: API URL과 설정값이 하드코딩되어 있음

**보완 방법**:
```python
# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_url: str = "https://dev.wenivops.co.kr/services/openai-api"
    api_key: str = ""
    session_secret: str = "your-secret-key-here"
    database_url: str = "sqlite:///./healing_chatbot.db"
    session_timeout: int = 3600  # 1시간
    
    class Config:
        env_file = ".env"

settings = Settings()

# .env 파일 생성
API_URL=https://dev.wenivops.co.kr/services/openai-api
SESSION_SECRET=your-secret-key-here
DATABASE_URL=sqlite:///./healing_chatbot.db
SESSION_TIMEOUT=3600
```

### 6. 로깅 시스템
**문제점**: print문으로만 디버깅

**보완 방법**:
```python
import logging
from logging.handlers import RotatingFileHandler

# 로깅 설정
def setup_logging():
    logger = logging.getLogger("healing_chatbot")
    logger.setLevel(logging.INFO)
    
    # 파일 핸들러 (로그 파일 자동 회전)
    file_handler = RotatingFileHandler(
        "app.log",
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    
    # 콘솔 핸들러
    console_handler = logging.StreamHandler()
    
    # 포맷터
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

logger = setup_logging()

# print 대신 logger 사용
logger.info(f"응답 상태 코드: {response.status_code}")
logger.error(f"API 오류: {e}")
```

## 새로운 기능 제안 💡

### 1. 감정 통계 대시보드
```python
@app.get("/stats/emotions")
async def get_emotion_stats(session_id: Optional[str] = Cookie(None)):
    """사용자의 감정 변화 통계"""
    # 구현: 시간대별 감정 분석, 주요 감정 패턴 등
    pass
```

### 2. 미래 일기 기능
```python
class FutureDiary(BaseModel):
    title: str
    content: str
    target_date: datetime
    emotions: List[str]
    
@app.post("/diary/future")
async def create_future_diary(diary: FutureDiary, session_id: Optional[str] = Cookie(None)):
    """미래 시나리오를 일기 형태로 저장"""
    pass
```

### 3. 긍정 알림 기능
```python
@app.post("/reminders/positive")
async def set_positive_reminder(
    time: str,
    message: str,
    session_id: Optional[str] = Cookie(None)
):
    """정기적인 긍정 메시지 알림 설정"""
    pass
```

### 4. 음성 대화 기능
```python
@app.post("/chat/voice")
async def voice_chat(audio_file: UploadFile, session_id: Optional[str] = Cookie(None)):
    """음성을 텍스트로 변환 후 채팅"""
    # STT API 연동
    pass
```

### 5. 감정 시각화
```python
@app.get("/visualization/emotions")
async def get_emotion_visualization(session_id: Optional[str] = Cookie(None)):
    """감정 변화를 차트로 시각화"""
    # Chart.js 데이터 반환
    pass
```

## 성능 최적화 제안 🚀

### 1. 응답 캐싱
```python
from functools import lru_cache
import hashlib

@lru_cache(maxsize=100)
def get_cached_response(prompt_hash: str):
    """자주 묻는 질문에 대한 응답 캐싱"""
    pass

def get_prompt_hash(prompt: str) -> str:
    """프롬프트의 해시값 생성"""
    return hashlib.md5(prompt.encode()).hexdigest()
```

### 2. 비동기 작업 큐
```python
from asyncio import Queue

# 메시지 처리 큐
message_queue = Queue(maxsize=100)

async def process_message_queue():
    """백그라운드에서 메시지 처리"""
    while True:
        message = await message_queue.get()
        # 처리 로직
```

## 테스트 코드 추가 권장 🧪
```python
# test_main.py
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register():
    response = client.post("/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123"
    })
    assert response.status_code == 200
    assert "회원가입이 완료되었습니다" in response.json()["message"]

def test_login():
    response = client.post("/login", json={
        "username": "testuser",
        "password": "testpass123"
    })
    assert response.status_code == 200
    assert "session_id" in response.cookies

@pytest.mark.asyncio
async def test_chat():
    # 로그인 후 채팅 테스트
    pass
```

## 배포 준비사항 📦

### 1. requirements.txt 업데이트
```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
python-multipart==0.0.6
httpx==0.25.1
pydantic==2.5.0
pydantic-settings==2.1.0
passlib[bcrypt]==1.7.4
aiosqlite==0.19.0
pytest==7.4.3
pytest-asyncio==0.21.1
```
**참고**: 기본적인 `requirements.txt` 파일이 이미 추가되었으나, 위의 권장 패키지들로 업데이트하면 더욱 안정적인 운영이 가능합니다.

### 2. Docker 컨테이너화
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 복사
COPY . .

# 포트 노출
EXPOSE 8000

# 실행
CMD ["uvicorn", "back.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 3. docker-compose.yml
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - API_URL=${API_URL}
      - SESSION_SECRET=${SESSION_SECRET}
    volumes:
      - ./data:/app/data
    restart: unless-stopped
```

## 종합 평가
유수진 님의 프로젝트는 **매우 완성도 높게 구현**되었습니다. 특히 다음 점들이 인상적입니다:

1. **완전한 기능 구현**: 인증, 채팅, UI 모두 작동
2. **친절한 코드**: 한글 주석과 직관적인 네이밍
3. **사용자 경험 고려**: 로딩 표시, 에러 처리, 반응형 디자인
4. **개선점 인지**: 코드 내 리뷰 주석으로 개선점 표시

주요 개선 사항으로는:
- **보안 강화**: bcrypt 사용, 세션 만료 관리
- **힐링 챗봇 특화**: 감정 분석, 맞춤형 응답
- **데이터 영속성**: 데이터베이스 연동
- **운영 준비**: 로깅, 환경 변수, 테스트

전체적으로 프로토타입을 넘어 실제 서비스로 발전시킬 수 있는 훌륭한 프로젝트입니다! 👏