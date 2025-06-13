# 배주완 프로젝트 코드 리뷰

## 프로젝트 소개
점메추리알은 매일 점심 메뉴 선택으로 고민하는 직장인과 학생들을 위한 AI 기반 맞춤형 메뉴 추천 서비스입니다. 사용자의 현재 위치, 식사 목적(회식, 데이트, 혼밥 등), 선호하는 음식 종류, 예산 등을 종합적으로 고려하여 ChatGPT가 최적의 점심 메뉴를 추천합니다. 귀여운 메추리알 캐릭터와 함께하는 친근한 UI로 즐거운 점심 시간을 만들어갑니다.

## 프로젝트 정보
- **프로젝트명**: 점메추리알 - 점심메뉴 추천 프로그램
- **저장소**: https://github.com/배주완/lunch-menu-recommender
- **기술 스택**: FastAPI, Jinja2 Templates, Tailwind CSS, OpenAI API
- **목표**: 사용자의 위치, 용도, 음식 종류 등을 고려하여 점심 메뉴를 추천하는 챗봇

## 잘된 점 👍

### 1. UI/UX 디자인
- Tailwind CSS를 활용한 모던하고 깔끔한 디자인
- 모바일 스타일의 챗봇 UI로 사용자 친화적
- 애니메이션 효과로 생동감 있는 인터페이스
- 직관적인 로그인/회원가입 화면 구성

### 2. 기능 구현
- 회원가입 시 비밀번호 복잡도 검증 (길이, 특수문자, 영문자)
- localStorage를 활용한 채팅 기록 저장
- 비동기 처리를 통한 사용자 경험 개선
- 채팅 초기화 및 로그아웃 기능

### 3. 코드 구조
- 라우팅이 명확하게 분리되어 있음
- Pydantic 모델을 사용한 데이터 검증
- httpx를 사용한 비동기 HTTP 요청 처리

## 개선이 필요한 점 및 보완 방법 ⚠️

### 1. 보안 취약점
**문제점**:
- 비밀번호를 평문으로 저장
- 쿠키 기반 인증의 보안 취약성
- XSS 공격에 취약한 innerHTML 사용
- 테스트용 계정의 약한 비밀번호

**보완 방법**:
```python
# 비밀번호 해시화
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 회원가입 시
hashed_password = pwd_context.hash(data.password)
users[data.username] = {"password": hashed_password, "email": data.email}

# 로그인 시
if user and pwd_context.verify(data.password, user["password"]):
    # JWT 토큰 생성
    from jose import jwt
    from datetime import datetime, timedelta
    
    token_data = {
        "sub": data.username,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }
    token = jwt.encode(token_data, SECRET_KEY, algorithm="HS256")
    return JSONResponse({"success": True, "token": token})
```

### 2. XSS 방지
**문제점**: innerHTML을 사용하여 사용자 입력을 직접 삽입

**보완 방법**:
```javascript
// 안전한 텍스트 삽입 함수
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// 메시지 추가 함수
function addMessage(sender, message) {
    const messageDiv = document.createElement('div');
    messageDiv.className = sender === 'user' ? 'text-right' : '';
    
    const bubble = document.createElement('span');
    bubble.className = sender === 'user' 
        ? 'bg-pink-200 px-3 py-2 rounded-full inline-block mb-1'
        : 'bg-purple-100 px-3 py-2 rounded-full inline-block';
    
    const icon = sender === 'user' ? '👤' : '🐤';
    const label = sender === 'user' ? '나' : '점메추리';
    
    bubble.innerHTML = `${icon} <strong>${label}:</strong> `;
    bubble.appendChild(document.createTextNode(message));
    
    messageDiv.appendChild(bubble);
    chatBox.appendChild(messageDiv);
}
```

### 3. 데이터 영속성
**문제점**: 메모리에만 데이터를 저장하여 서버 재시작 시 데이터 손실

**보완 방법**:
```python
# SQLite 데이터베이스 사용
import sqlite3
from contextlib import contextmanager

@contextmanager
def get_db():
    conn = sqlite3.connect('chatbot.db')
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        conn.close()

# 테이블 생성
def init_db():
    with get_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                message TEXT NOT NULL,
                response TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (username) REFERENCES users (username)
            )
        ''')
```

### 4. 환경 변수 관리
**문제점**: API URL과 설정값이 하드코딩되어 있음

**보완 방법**:
```python
# .env 파일
GPT_API_URL=https://dev.wenivops.co.kr/services/openai-api
GPT_API_KEY=your-api-key
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///./chatbot.db

# main.py
from dotenv import load_dotenv
import os

load_dotenv()

GPT_API_URL = os.getenv("GPT_API_URL")
GPT_API_KEY = os.getenv("GPT_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
```

### 5. 점심 메뉴 추천 특화
**문제점**: 범용 챗봇으로 구현되어 점심 메뉴 추천에 특화되지 않음

**보완 방법**:
```python
# 구조화된 메뉴 추천 시스템
class MenuRequest(BaseModel):
    location: str
    purpose: str  # 직장동료, 부서회식, 여행 등
    cuisine_type: str  # 한식, 양식, 일식 등
    preferences: str  # 미슐랭, 노포, 줄 없는 곳 등

@app.post("/recommend")
async def recommend_menu(request: MenuRequest):
    prompt = f"""
    다음 조건에 맞는 점심 메뉴를 추천해주세요:
    - 위치: {request.location}
    - 용도: {request.purpose}
    - 음식 종류: {request.cuisine_type}
    - 선호사항: {request.preferences}
    
    구체적인 식당 이름과 메뉴, 가격대, 특징을 포함해서 추천해주세요.
    """
    
    # GPT API 호출
    # ...
```

### 6. 에러 처리 개선
**문제점**: 클라이언트 측 에러 처리가 미흡

**보완 방법**:
```javascript
// 에러 처리 개선
async function sendMessage(question) {
    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        return data.answer;
    } catch (error) {
        console.error('Error:', error);
        
        if (error.message.includes('404')) {
            return "요청하신 서비스를 찾을 수 없습니다.";
        } else if (error.message.includes('500')) {
            return "서버 오류가 발생했습니다. 잠시 후 다시 시도해주세요.";
        } else if (error.name === 'TypeError') {
            return "네트워크 연결을 확인해주세요.";
        }
        
        return "알 수 없는 오류가 발생했습니다.";
    }
}
```

### 7. 채팅 기록 개선
**문제점**: localStorage에 HTML을 저장하는 것은 보안상 위험

**보완 방법**:
```javascript
// 채팅 데이터 구조화
const chatHistory = [];

function saveMessage(sender, message) {
    chatHistory.push({
        sender,
        message,
        timestamp: new Date().toISOString()
    });
    localStorage.setItem(localStorageKey, JSON.stringify(chatHistory));
}

function loadChatHistory() {
    const saved = localStorage.getItem(localStorageKey);
    if (saved) {
        const history = JSON.parse(saved);
        history.forEach(item => {
            addMessage(item.sender, item.message);
        });
    }
}
```

### 8. CORS 설정
**문제점**: CORS 미들웨어가 설정되지 않음

**보완 방법**:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 프로덕션에서는 특정 도메인만
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

## 추가 개선 아이디어 💡
1. **위치 기반 추천**: 사용자의 실제 위치를 받아 주변 맛집 추천
2. **추천 히스토리**: 이전에 추천받은 메뉴 기록 및 평가 기능
3. **음식 이미지**: 추천 메뉴의 이미지를 함께 제공
4. **가격 필터**: 예산에 맞는 메뉴 추천
5. **그룹 추천**: 여러 사람의 선호도를 고려한 추천

## 추천 학습 자료 📚
1. **FastAPI 보안**: https://fastapi.tiangolo.com/tutorial/security/
2. **OWASP XSS 방지**: https://owasp.org/www-community/attacks/xss/
3. **JWT 인증**: https://jwt.io/introduction
4. **SQLAlchemy**: https://docs.sqlalchemy.org/
5. **웹 보안 기초**: https://developer.mozilla.org/en-US/docs/Web/Security

## 종합 평가
프로젝트의 기본 구조와 UI/UX 디자인이 잘 되어있으며, 기본적인 기능 구현도 완성되어 있습니다. 특히 Tailwind CSS를 활용한 디자인이 인상적입니다. 다만 보안 측면에서 개선이 필요하며, 점심 메뉴 추천이라는 목적에 더 특화된 기능을 추가하면 좋겠습니다. 전반적으로 초보자 수준을 넘어선 구현력을 보여주고 있으며, 제안된 개선사항들을 적용하면 실제 서비스로도 활용 가능한 수준이 될 것입니다.