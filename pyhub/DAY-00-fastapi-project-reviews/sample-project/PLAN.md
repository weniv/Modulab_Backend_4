# FastAPI 샘플 프로젝트 구현 계획

## 프로젝트 개요
각 학생 프로젝트의 우수 사례를 참고하여 최선의 FastAPI 애플리케이션을 구현합니다.

### 주요 원칙
- Jinja2 템플릿 사용
- HTML form 전송 최대 활용
- JavaScript 코드 최소화
- 메모리 기반 세션
- SQLModel + SQLite 데이터베이스

## 프로젝트 구조

```
sample/
├── TODO.md                 # 작업 내역 및 진행 상황
├── PLAN.md                # 프로젝트 계획 (현재 파일)
├── main.py                # FastAPI 메인 애플리케이션
├── models.py              # SQLModel 데이터베이스 모델
├── schemas.py             # Pydantic 검증 스키마
├── auth.py                # 인증 관련 기능
├── database.py            # 데이터베이스 설정
├── requirements.txt       # 의존성 패키지
├── .env.example          # 환경 변수 예시
├── templates/            # Jinja2 템플릿
│   ├── base.html        # 기본 레이아웃
│   ├── index.html       # 메인 페이지
│   ├── login.html       # 로그인 페이지
│   ├── register.html    # 회원가입 페이지
│   └── chat.html        # 채팅 페이지
└── static/              # 정적 파일
    └── style.css        # 스타일시트
```

## 핵심 기능

### 1. 사용자 인증 시스템
- 회원가입 (bcrypt 해싱)
- 로그인/로그아웃
- 세션 기반 인증 (메모리)

### 2. 채팅 기능
- OpenAI API 연동
- 대화 히스토리 저장
- 사용자별 채팅 관리

### 3. 데이터 관리
- SQLModel ORM 사용
- SQLite 데이터베이스
- 사용자 정보 및 채팅 기록 저장

### 4. 웹 인터페이스
- Jinja2 템플릿 엔진
- HTML form 기반 상호작용
- 반응형 디자인

## 참고할 우수 사례

### 1. 유수진 프로젝트
- 한글 주석과 명확한 함수명
- 상세한 docstring
- 재시도 로직을 포함한 에러 처리

### 2. 배근호 프로젝트
- Pydantic 모델을 활용한 데이터 검증
- 체계적인 프로젝트 구조
- 프론트엔드/백엔드 분리

### 3. 최나영 프로젝트
- JWT 대신 세션 기반 인증으로 변경
- 모듈화된 코드 구조
- 채팅 히스토리 관리

### 4. 심희현 프로젝트
- 체계적인 라우터 분리
- 세션 기반 인증 시스템
- CRUD 기능 구현

## 작업 순서

### Phase 1: 프로젝트 초기 설정
1. 프로젝트 디렉토리 구조 생성
2. requirements.txt 작성
3. .env.example 파일 생성
4. TODO.md 파일 작성

### Phase 2: 데이터베이스 설정
5. database.py - SQLModel 설정
6. models.py - User, ChatMessage 모델 정의
7. schemas.py - Pydantic 스키마 정의

### Phase 3: 인증 시스템
8. auth.py - 비밀번호 해싱, 세션 관리
9. 로그인/회원가입 라우터 구현

### Phase 4: 메인 애플리케이션
10. main.py - FastAPI 앱 설정
11. 채팅 기능 라우터 구현
12. 템플릿 렌더링 설정

### Phase 5: 프론트엔드
13. base.html - 기본 레이아웃
14. 각 페이지 템플릿 작성
15. style.css - 스타일 추가

### Phase 6: 테스트 및 문서화
16. 기능 테스트
17. README.md 작성
18. 코드 리뷰 및 최적화

## 기술 스택

### Backend
- FastAPI 0.115.0
- SQLModel 0.0.16
- python-jose[cryptography] (세션 토큰)
- passlib[bcrypt] (비밀번호 해싱)
- python-multipart (form 데이터)
- jinja2 (템플릿 엔진)
- python-dotenv (환경 변수)
- httpx (API 호출)

### Frontend
- HTML5
- CSS3 (최소한의 스타일)
- Jinja2 템플릿
- HTML forms (JavaScript 최소화)

## 보안 고려사항
1. bcrypt를 사용한 안전한 비밀번호 해싱
2. 환경 변수를 통한 민감 정보 관리
3. CORS 설정 (필요시 특정 도메인만 허용)
4. SQL 인젝션 방지 (SQLModel ORM 사용)
5. XSS 방지 (Jinja2 자동 이스케이핑)

## 성능 최적화
1. 비동기 처리 (async/await)
2. 데이터베이스 연결 풀링
3. 정적 파일 캐싱
4. 효율적인 쿼리 작성

## 예상 결과물
- 완전히 작동하는 채팅 애플리케이션
- 사용자 인증 및 세션 관리
- 채팅 히스토리 저장 및 조회
- 깔끔한 웹 인터페이스
- 모범 사례를 따른 코드 구조