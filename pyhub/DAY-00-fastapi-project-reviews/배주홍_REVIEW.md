# 배주홍 프로젝트 코드 리뷰

## 프로젝트 소개
6월 제철음식 추천 서비스는 건강한 식생활을 추구하는 사람들을 위한 계절별 음식 가이드 플랫폼입니다. 6월에 가장 맛있고 영양가 높은 제철 식재료들을 해산물, 야채, 과일 카테고리로 분류하여 소개하고, 각 식재료의 효능과 요리법을 제공합니다. 사용자 인증 시스템을 통해 개인별 선호도를 저장하고 맞춤형 추천을 받을 수 있습니다.

## 프로젝트 정보
- **프로젝트명**: 6월 제철음식 추천 서비스
- **저장소**: https://github.com/배주홍/seasonal-food-june
- **기술 스택**: FastAPI, HTML/CSS/JavaScript, bcrypt (비밀번호 해싱)
- **목표**: 6월 제철 음식(해산물, 야채, 과일)을 카테고리별로 추천하는 서비스

## 잘된 점 👍

### 1. 코드 구조와 모듈화
- auth.py와 bootcamp_api.py로 기능별 모듈 분리
- 라우터를 사용한 깔끔한 API 구조
- 백엔드와 프론트엔드의 명확한 분리

### 2. 보안 구현
- bcrypt를 사용한 비밀번호 해싱
- 적절한 HTTP 상태 코드 사용
- Pydantic을 통한 입력 데이터 검증

### 3. API 설계
- RESTful API 원칙 준수
- 다양한 추천 기능 구현 (카테고리별, 랜덤)
- 채팅 기록 저장 및 조회 기능

### 4. 프론트엔드 구현
- 깔끔한 UI 디자인
- 비동기 fetch API 활용
- 응답 데이터의 적절한 파싱 및 표시

## 개선이 필요한 점 및 보완 방법 ⚠️

### 1. 아키텍처 문제
**문제점**: 프론트엔드에서 외부 API를 직접 호출하여 백엔드의 추천 API가 활용되지 않음

**보완 방법**:
```javascript
// 002.js 수정
async function fetchRecommendation(category) {
    const username = localStorage.getItem('username');
    if (!username) {
        alert('로그인이 필요합니다.');
        window.location.href = 'index.html';
        return;
    }
    
    try {
        // 백엔드 API 사용
        const response = await fetch("http://localhost:8000/recommend", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                category: category,
                username: username
            })
        });
        
        const result = await response.json();
        displayRecommendation(result);
        
        // 추천 기록 저장
        await saveToHistory(username, category, result);
    } catch (error) {
        console.error("추천 요청 실패:", error);
    }
}
```

### 2. 인증 및 세션 관리
**문제점**: 로그인 후 사용자 상태 관리가 없음

**보완 방법**:
```python
# JWT 토큰 기반 인증 구현
from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/login")
async def login(user: UserLogin):
    # ... 기존 검증 로직 ...
    
    access_token = create_access_token(data={"sub": user.username})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username
    }
```

### 3. 데이터 영속성
**문제점**: 메모리 기반 저장으로 서버 재시작 시 데이터 손실

**보완 방법**:
```python
# SQLite 데이터베이스 사용
import sqlite3
from contextlib import contextmanager

def init_db():
    conn = sqlite3.connect('food_recommend.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            email TEXT NOT NULL,
            hashed_password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            category TEXT NOT NULL,
            recommendation TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (username) REFERENCES users (username)
        )
    ''')
    
    conn.commit()
    conn.close()
```

### 4. 환경 변수 관리
**문제점**: API 키와 설정값이 하드코딩되어 있음

**보완 방법**:
```python
# .env 파일
DATABASE_URL=sqlite:///./food_recommend.db
SECRET_KEY=your-secret-key-here
OPENAI_API_KEY=your-api-key-here
API_BASE_URL=https://dev.wenivops.co.kr/services/openai-api

# config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    openai_api_key: str
    api_base_url: str
    
    class Config:
        env_file = ".env"

settings = Settings()
```

### 5. 프론트엔드 보안
**문제점**: XSS 취약점이 있는 innerHTML 사용

**보완 방법**:
```javascript
// 안전한 DOM 조작
function displayRecommendation(content) {
    const foodResultElement = document.getElementById("foodresult");
    
    // 기존 내용 제거
    while (foodResultElement.firstChild) {
        foodResultElement.removeChild(foodResultElement.firstChild);
    }
    
    // 안전하게 리스트 생성
    const lines = content.split("\n").filter(line => line.trim());
    if (lines.length > 1) {
        const ul = document.createElement('ul');
        lines.forEach(line => {
            const li = document.createElement('li');
            li.textContent = line;
            ul.appendChild(li);
        });
        foodResultElement.appendChild(ul);
    } else {
        foodResultElement.textContent = content;
    }
}
```

### 6. 에러 처리 개선
**문제점**: 에러 메시지가 기술적이고 사용자 친화적이지 않음

**보완 방법**:
```python
# 커스텀 예외 클래스
class UserNotFoundException(Exception):
    pass

class InvalidCredentialsException(Exception):
    pass

# 예외 핸들러
@app.exception_handler(UserNotFoundException)
async def user_not_found_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": "사용자를 찾을 수 없습니다."}
    )

@app.exception_handler(InvalidCredentialsException)
async def invalid_credentials_handler(request: Request, exc: InvalidCredentialsException):
    return JSONResponse(
        status_code=401,
        content={"message": "아이디 또는 비밀번호가 올바르지 않습니다."}
    )
```

### 7. API 문서화
**문제점**: API 엔드포인트에 대한 설명이 부족

**보완 방법**:
```python
@router.post("/recommend", 
    summary="제철 음식 추천",
    description="카테고리별 6월 제철 음식을 추천합니다.",
    response_description="추천된 음식 정보"
)
async def get_recommendation(
    category: str = Query(..., description="추천 카테고리 (seafood, vegetable, fruit, random)"),
    username: str = Depends(get_current_user)
):
    """
    카테고리별 6월 제철 음식을 추천합니다.
    
    - **seafood**: 제철 해산물
    - **vegetable**: 제철 야채
    - **fruit**: 제철 과일
    - **random**: 랜덤 추천
    """
    pass
```

### 8. 프론트엔드 개선
**문제점**: 
- 로딩 상태 표시 없음
- 반응형 디자인 미적용
- 중복 클릭 방지 없음

**보완 방법**:
```javascript
// 버튼 상태 관리
async function fetchRecommendation(category) {
    const buttons = document.querySelectorAll('button');
    const resultElement = document.getElementById("foodresult");
    
    // 버튼 비활성화
    buttons.forEach(btn => btn.disabled = true);
    
    // 로딩 표시
    resultElement.innerHTML = '<div class="loading">추천 음식을 찾고 있습니다...</div>';
    
    try {
        const response = await fetch(...);
        // ... 처리 로직
    } finally {
        // 버튼 재활성화
        buttons.forEach(btn => btn.disabled = false);
    }
}
```

```css
/* 반응형 디자인 추가 */
@media (max-width: 768px) {
    .container {
        width: 95%;
        padding: 10px;
    }
    
    .button-group {
        flex-direction: column;
    }
    
    button {
        width: 100%;
        margin: 5px 0;
    }
}

/* 로딩 애니메이션 */
.loading {
    text-align: center;
    color: #666;
}

.loading::after {
    content: '';
    animation: dots 1.5s steps(3, end) infinite;
}

@keyframes dots {
    0% { content: ''; }
    33% { content: '.'; }
    66% { content: '..'; }
    100% { content: '...'; }
}
```

## 추가 개선 아이디어 💡
1. **추천 히스토리**: 사용자별 추천 기록 저장 및 조회
2. **평가 기능**: 추천받은 음식에 대한 평가 및 피드백
3. **레시피 연동**: 추천 음식의 간단한 레시피 제공
4. **영양 정보**: 제철 음식의 영양 성분 표시
5. **지역별 추천**: 사용자 위치 기반 지역 특산물 추천

## 추천 학습 자료 📚
1. **FastAPI 공식 문서**: https://fastapi.tiangolo.com/ko/
2. **JWT 인증**: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
3. **SQLAlchemy**: https://docs.sqlalchemy.org/
4. **프론트엔드 보안**: https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html
5. **반응형 웹 디자인**: https://developer.mozilla.org/ko/docs/Learn/CSS/CSS_layout/Responsive_Design

## 종합 평가
프로젝트의 기본 구조와 기능 구현이 잘 되어있으며, 특히 모듈화와 API 설계가 깔끔합니다. 다만 프론트엔드가 백엔드 API를 활용하지 않는 점과 데이터 영속성 문제를 개선하면 실제 서비스로 발전시킬 수 있는 좋은 프로젝트가 될 것입니다. 보안 측면에서 bcrypt를 사용한 점은 좋으나, JWT 토큰 기반 인증을 추가하면 더욱 완성도가 높아질 것입니다.