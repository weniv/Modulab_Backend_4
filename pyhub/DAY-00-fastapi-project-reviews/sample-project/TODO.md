# FastAPI 샘플 프로젝트 TODO 리스트

## 작업 내역 추적
각 작업을 완료하면 [x]로 표시하고 관련 내용을 기록합니다.

---

## Phase 1: 프로젝트 초기 설정

### [x] 1. 프로젝트 디렉토리 구조 생성
- [x] templates 폴더 생성
- [x] static 폴더 생성

### [x] 2. requirements.txt 작성
필요한 패키지:
- fastapi==0.115.0
- uvicorn[standard]==0.30.0
- sqlmodel==0.0.16
- python-jose[cryptography]==3.3.0
- passlib[bcrypt]==1.7.4
- python-multipart==0.0.7
- jinja2==3.1.3
- python-dotenv==1.0.0
- httpx==0.27.0

### [x] 3. .env.example 파일 생성
필요한 환경 변수:
- SECRET_KEY (세션 암호화용)
- OPENAI_API_KEY (ChatGPT API)
- DATABASE_URL (SQLite 경로)

---

## Phase 2: 데이터베이스 설정

### [x] 4. database.py - SQLModel 설정
- [x] SQLite 데이터베이스 연결 설정
- [x] 세션 관리자 생성
- [x] 데이터베이스 초기화 함수

### [x] 5. models.py - 데이터 모델 정의
- [x] User 모델 (id, username, email, hashed_password, created_at)
- [x] ChatMessage 모델 (id, user_id, role, content, created_at)
- [x] 관계 설정 (User ↔ ChatMessage)

### [x] 6. schemas.py - Pydantic 스키마 정의
- [x] UserCreate (회원가입용)
- [x] UserLogin (로그인용)
- [x] ChatRequest (채팅 요청)
- [x] ChatResponse (채팅 응답)

---

## Phase 3: 인증 시스템

### [x] 7. auth.py - 인증 기능 구현
- [x] 비밀번호 해싱 함수 (bcrypt)
- [x] 비밀번호 검증 함수
- [x] 세션 생성/관리 (메모리 기반)
- [x] 현재 사용자 가져오기 함수

### [x] 8. 인증 라우터 구현
- [x] POST /register - 회원가입
- [x] POST /login - 로그인
- [x] POST /logout - 로그아웃
- [x] GET /me - 현재 사용자 정보 (get_current_user 의존성으로 구현)

---

## Phase 4: 메인 애플리케이션

### [x] 9. main.py - FastAPI 앱 설정
- [x] FastAPI 인스턴스 생성
- [x] 미들웨어 설정 (CORS, 세션)
- [x] 정적 파일 마운트
- [x] 템플릿 설정
- [x] 라우터 등록

### [x] 10. 페이지 라우터 구현
- [x] GET / - 메인 페이지
- [x] GET /login - 로그인 페이지
- [x] GET /register - 회원가입 페이지
- [x] GET /chat - 채팅 페이지 (인증 필요)

### [x] 11. 채팅 API 구현
- [x] POST /api/chat - 채팅 메시지 전송
- [x] GET /api/history - 채팅 히스토리 조회

---

## Phase 5: 프론트엔드

### [x] 12. base.html - 기본 레이아웃
- [x] HTML 기본 구조
- [x] 네비게이션 바
- [x] 플래시 메시지 영역
- [x] 콘텐츠 블록

### [x] 13. index.html - 메인 페이지
- [x] 환영 메시지
- [x] 로그인 상태에 따른 분기
- [x] 주요 기능 소개

### [x] 14. login.html - 로그인 페이지
- [x] 로그인 폼 (username, password)
- [x] 회원가입 링크
- [x] 에러 메시지 표시

### [x] 15. register.html - 회원가입 페이지
- [x] 회원가입 폼 (username, email, password, password_confirm)
- [x] 입력 검증
- [x] 로그인 링크

### [x] 16. chat.html - 채팅 페이지
- [x] 채팅 히스토리 표시
- [x] 메시지 입력 폼
- [x] 자동 스크롤
- [x] 로딩 상태 표시

### [x] 17. style.css - 스타일시트
- [x] 기본 스타일 리셋
- [x] 레이아웃 스타일
- [x] 폼 스타일
- [x] 채팅 인터페이스 스타일
- [x] 반응형 디자인

---

## Phase 6: 테스트 및 문서화

### [ ] 18. 기능 테스트
- [ ] 회원가입 테스트
- [ ] 로그인/로그아웃 테스트
- [ ] 채팅 기능 테스트
- [ ] 세션 만료 테스트

### [ ] 19. README.md 작성
- [ ] 프로젝트 소개
- [ ] 설치 방법
- [ ] 실행 방법
- [ ] 주요 기능
- [ ] 기술 스택

### [ ] 20. 코드 최적화
- [ ] 코드 리뷰
- [ ] 주석 추가
- [ ] 불필요한 코드 제거
- [ ] 성능 최적화

---

## 완료된 작업 기록

### 작업 시작: 2024-12-13

#### 완료된 작업:
- Phase 1: 프로젝트 초기 설정 완료
- Phase 2: 데이터베이스 설정 완료
- Phase 3: 인증 시스템 완료
- Phase 4: 메인 애플리케이션 완료 (main.py, 페이지 라우터, 채팅 API)
- Phase 5: 프론트엔드 완료 (모든 템플릿 및 스타일시트)

#### 남은 작업:
- Phase 6: 테스트 및 문서화 필요