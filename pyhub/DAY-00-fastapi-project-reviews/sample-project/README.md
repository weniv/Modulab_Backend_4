# FastAPI 채팅 애플리케이션

최선의 방식으로 구현한 FastAPI 기반 AI 채팅 애플리케이션입니다.

## 특징

- 🔐 **안전한 인증**: bcrypt 해싱과 세션 기반 인증
- 💬 **AI 채팅**: OpenAI GPT-3.5를 활용한 대화
- 📝 **대화 저장**: SQLite 데이터베이스에 모든 대화 저장
- 🎨 **깔끔한 UI**: Jinja2 템플릿과 최소한의 JavaScript
- ⚡ **빠른 응답**: 비동기 처리로 최적화된 성능

## 기술 스택

- **Backend**: FastAPI, SQLModel, Pydantic
- **Database**: SQLite
- **Authentication**: bcrypt, 세션 기반
- **Frontend**: Jinja2, HTML Forms, CSS
- **AI**: OpenAI API

## 설치 방법

### 1. 저장소 클론

```bash
cd sample
```

### 2. 가상환경 생성 및 활성화

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. 의존성 설치

```bash
pip install -r requirements.txt
```

### 4. 환경 변수 설정

```bash
cp .env.example .env
```

`.env` 파일을 열어 다음 값들을 설정하세요:
- `SECRET_KEY`: 랜덤한 문자열 (세션 암호화용)
- `OPENAI_API_KEY`: OpenAI API 키

### 5. 애플리케이션 실행

```bash
uvicorn main:app --reload
```

브라우저에서 http://localhost:8000 접속

## 프로젝트 구조

```
sample/
├── main.py              # FastAPI 메인 애플리케이션
├── models.py            # SQLModel 데이터베이스 모델
├── schemas.py           # Pydantic 검증 스키마
├── auth.py              # 인증 관련 기능
├── database.py          # 데이터베이스 설정
├── requirements.txt     # Python 의존성
├── .env.example        # 환경 변수 예시
├── templates/          # Jinja2 템플릿
│   ├── base.html      # 기본 레이아웃
│   ├── index.html     # 메인 페이지
│   ├── login.html     # 로그인 페이지
│   ├── register.html  # 회원가입 페이지
│   └── chat.html      # 채팅 페이지
└── static/            # 정적 파일
    └── style.css      # 스타일시트
```

## 주요 기능

### 사용자 인증
- 회원가입: 사용자명, 이메일, 비밀번호 검증
- 로그인: 세션 기반 인증 (24시간 유효)
- 로그아웃: 세션 삭제

### 채팅 기능
- AI와 실시간 대화
- 대화 내용 자동 저장
- 사용자별 대화 히스토리 관리

### 보안 기능
- bcrypt를 사용한 비밀번호 해싱
- 세션 토큰 기반 인증
- SQL 인젝션 방지 (SQLModel ORM)
- XSS 방지 (Jinja2 자동 이스케이핑)

## API 엔드포인트

### 페이지 라우트
- `GET /` - 메인 페이지
- `GET /register` - 회원가입 페이지
- `GET /login` - 로그인 페이지
- `GET /chat` - 채팅 페이지 (인증 필요)

### 인증 API
- `POST /register` - 회원가입 처리
- `POST /login` - 로그인 처리
- `POST /logout` - 로그아웃 처리

### 채팅 API
- `POST /api/chat` - 메시지 전송 및 AI 응답

## 개발 시 참고사항

1. **데이터베이스**: SQLite 파일은 `.gitignore`에 추가하세요
2. **환경 변수**: `.env` 파일을 절대 커밋하지 마세요
3. **세션**: 현재 메모리 기반이므로 서버 재시작 시 초기화됩니다
4. **프로덕션**: Redis 등의 영구 세션 저장소 사용을 권장합니다

## 라이선스

MIT License