"""
FastAPI 메인 애플리케이션
채팅 애플리케이션의 핵심 로직
"""

from fastapi import FastAPI, Request, Form, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select
from typing import Optional
import httpx
import os
from dotenv import load_dotenv

# 로컬 모듈
from database import create_db_and_tables, get_session
from models import User, ChatMessage
from schemas import UserCreate, UserLogin, ChatRequest, UserResponse, ChatHistoryResponse, ChatMessageResponse
import auth

# 환경 변수 로드
load_dotenv()

# FastAPI 앱 생성
app = FastAPI(
    title="FastAPI 채팅 애플리케이션",
    description="최선의 방식으로 구현한 FastAPI 채팅 앱",
    version="1.0.0"
)

# 정적 파일 마운트
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 템플릿 설정
templates = Jinja2Templates(directory="templates")

# OpenAI API 설정
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"


@app.on_event("startup")
def on_startup():
    """애플리케이션 시작 시 데이터베이스 초기화"""
    create_db_and_tables()


def get_current_user(request: Request, db: Session = Depends(get_session)) -> Optional[User]:
    """
    현재 로그인한 사용자 가져오기
    
    쿠키에서 세션 토큰을 읽어 사용자 정보 반환
    """
    session_token = request.cookies.get("session_token")
    if not session_token:
        return None
    
    session_data = auth.get_session(session_token)
    if not session_data:
        return None
    
    return auth.get_user_by_id(db, session_data["user_id"])


# ===== 페이지 라우트 =====

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, current_user: Optional[User] = Depends(get_current_user)):
    """메인 페이지"""
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "current_user": current_user}
    )


@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    """회원가입 페이지"""
    return templates.TemplateResponse(
        "register.html",
        {"request": request, "error": None}
    )


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    """로그인 페이지"""
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": None}
    )


@app.get("/chat", response_class=HTMLResponse)
async def chat_page(
    request: Request,
    db: Session = Depends(get_session),
    current_user: Optional[User] = Depends(get_current_user)
):
    """채팅 페이지 (로그인 필수)"""
    if not current_user:
        return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
    
    # 사용자의 채팅 히스토리 조회
    statement = select(ChatMessage).where(
        ChatMessage.user_id == current_user.id
    ).order_by(ChatMessage.created_at)
    
    messages = db.exec(statement).all()
    
    return templates.TemplateResponse(
        "chat.html",
        {
            "request": request,
            "current_user": current_user,
            "messages": messages
        }
    )


# ===== 인증 API =====

@app.post("/register")
async def register(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    password_confirm: str = Form(...),
    db: Session = Depends(get_session)
):
    """회원가입 처리"""
    # 비밀번호 확인
    if password != password_confirm:
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "error": "비밀번호가 일치하지 않습니다"}
        )
    
    # 사용자명 중복 확인
    if auth.get_user_by_username(db, username):
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "error": "이미 사용중인 사용자명입니다"}
        )
    
    # 이메일 중복 확인
    statement = select(User).where(User.email == email)
    if db.exec(statement).first():
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "error": "이미 사용중인 이메일입니다"}
        )
    
    try:
        # 사용자 생성
        user = auth.create_user(db, username, email, password)
        
        # 자동 로그인
        session_token = auth.create_session(user.id, user.username)
        
        response = RedirectResponse(url="/chat", status_code=status.HTTP_303_SEE_OTHER)
        response.set_cookie(
            key="session_token",
            value=session_token,
            httponly=True,
            max_age=86400  # 24시간
        )
        
        return response
        
    except Exception as e:
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "error": "회원가입 중 오류가 발생했습니다"}
        )


@app.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_session)
):
    """로그인 처리"""
    user = auth.authenticate_user(db, username, password)
    
    if not user:
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "사용자명 또는 비밀번호가 올바르지 않습니다"}
        )
    
    # 세션 생성
    session_token = auth.create_session(user.id, user.username)
    
    response = RedirectResponse(url="/chat", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(
        key="session_token",
        value=session_token,
        httponly=True,
        max_age=86400  # 24시간
    )
    
    return response


@app.post("/logout")
async def logout(request: Request):
    """로그아웃 처리"""
    session_token = request.cookies.get("session_token")
    
    if session_token:
        auth.delete_session(session_token)
    
    response = RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    response.delete_cookie("session_token")
    
    return response


# ===== 채팅 API =====

@app.post("/api/chat")
async def send_message(
    request: Request,
    message: str = Form(...),
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """채팅 메시지 전송 및 AI 응답"""
    if not current_user:
        raise HTTPException(status_code=401, detail="로그인이 필요합니다")
    
    # 사용자 메시지 저장
    user_message = ChatMessage(
        user_id=current_user.id,
        role="user",
        content=message
    )
    db.add(user_message)
    db.commit()
    
    # OpenAI API 호출
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                OPENAI_API_URL,
                headers={
                    "Authorization": f"Bearer {OPENAI_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-3.5-turbo",
                    "messages": [
                        {"role": "system", "content": "당신은 친절하고 도움이 되는 AI 어시스턴트입니다."},
                        {"role": "user", "content": message}
                    ],
                    "max_tokens": 500,
                    "temperature": 0.7
                },
                timeout=30.0
            )
            
            if response.status_code == 200:
                data = response.json()
                ai_response = data["choices"][0]["message"]["content"]
            else:
                ai_response = "죄송합니다. AI 응답을 생성하는 데 실패했습니다."
                
    except Exception as e:
        print(f"OpenAI API 오류: {e}")
        ai_response = "죄송합니다. 일시적인 오류가 발생했습니다."
    
    # AI 응답 저장
    assistant_message = ChatMessage(
        user_id=current_user.id,
        role="assistant",
        content=ai_response
    )
    db.add(assistant_message)
    db.commit()
    
    # 채팅 페이지로 리다이렉트
    return RedirectResponse(url="/chat", status_code=status.HTTP_303_SEE_OTHER)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)