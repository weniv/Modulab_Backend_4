"""
인증 관련 기능 모듈
비밀번호 해싱, 세션 관리, 사용자 인증
"""

from passlib.context import CryptContext
from sqlmodel import Session, select
from typing import Optional, Dict
from datetime import datetime, timedelta
import secrets
from models import User

# 비밀번호 해싱 설정 (bcrypt 사용)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 메모리 기반 세션 저장소
# 실제 운영 환경에서는 Redis 등의 영구 저장소 사용 권장
sessions: Dict[str, Dict] = {}


def hash_password(password: str) -> str:
    """비밀번호를 bcrypt로 해싱"""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """평문 비밀번호와 해시된 비밀번호 비교"""
    return pwd_context.verify(plain_password, hashed_password)


def create_session(user_id: int, username: str) -> str:
    """
    새로운 세션 생성
    
    Args:
        user_id: 사용자 ID
        username: 사용자명
        
    Returns:
        세션 토큰
    """
    # 안전한 랜덤 토큰 생성
    session_token = secrets.token_urlsafe(32)
    
    # 세션 정보 저장
    sessions[session_token] = {
        "user_id": user_id,
        "username": username,
        "created_at": datetime.now(),
        "expires_at": datetime.now() + timedelta(hours=24)  # 24시간 후 만료
    }
    
    return session_token


def get_session(session_token: str) -> Optional[Dict]:
    """
    세션 토큰으로 세션 정보 조회
    
    Args:
        session_token: 세션 토큰
        
    Returns:
        세션 정보 또는 None
    """
    if session_token not in sessions:
        return None
    
    session = sessions[session_token]
    
    # 만료된 세션 확인
    if datetime.now() > session["expires_at"]:
        del sessions[session_token]
        return None
    
    return session


def delete_session(session_token: str) -> bool:
    """
    세션 삭제 (로그아웃)
    
    Args:
        session_token: 세션 토큰
        
    Returns:
        삭제 성공 여부
    """
    if session_token in sessions:
        del sessions[session_token]
        return True
    return False


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    """사용자명으로 사용자 조회"""
    statement = select(User).where(User.username == username)
    return db.exec(statement).first()


def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    """사용자 ID로 사용자 조회"""
    return db.get(User, user_id)


def create_user(db: Session, username: str, email: str, password: str) -> User:
    """
    새로운 사용자 생성
    
    Args:
        db: 데이터베이스 세션
        username: 사용자명
        email: 이메일
        password: 평문 비밀번호
        
    Returns:
        생성된 사용자 객체
    """
    hashed_password = hash_password(password)
    
    user = User(
        username=username,
        email=email,
        hashed_password=hashed_password
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user


def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
    """
    사용자 인증
    
    Args:
        db: 데이터베이스 세션
        username: 사용자명
        password: 평문 비밀번호
        
    Returns:
        인증된 사용자 객체 또는 None
    """
    user = get_user_by_username(db, username)
    
    if not user:
        return None
    
    if not verify_password(password, user.hashed_password):
        return None
    
    return user