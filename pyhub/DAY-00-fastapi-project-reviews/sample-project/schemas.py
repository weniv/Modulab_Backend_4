"""
Pydantic 스키마 정의
요청/응답 데이터 검증을 위한 스키마
"""

from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional, List
from datetime import datetime


class UserCreate(BaseModel):
    """회원가입 요청 스키마"""
    username: str = Field(..., min_length=3, max_length=50, description="사용자명")
    email: EmailStr = Field(..., description="이메일 주소")
    password: str = Field(..., min_length=8, max_length=100, description="비밀번호")
    password_confirm: str = Field(..., description="비밀번호 확인")
    
    @field_validator('username')
    def validate_username(cls, v):
        """사용자명 검증: 영문, 숫자, 언더스코어만 허용"""
        import re
        if not re.match("^[a-zA-Z0-9_]+$", v):
            raise ValueError('사용자명은 영문, 숫자, 언더스코어만 사용 가능합니다')
        return v
    
    @field_validator('password_confirm')
    def passwords_match(cls, v, values):
        """비밀번호 일치 검증"""
        if 'password' in values.data and v != values.data['password']:
            raise ValueError('비밀번호가 일치하지 않습니다')
        return v


class UserLogin(BaseModel):
    """로그인 요청 스키마"""
    username: str = Field(..., description="사용자명")
    password: str = Field(..., description="비밀번호")


class UserResponse(BaseModel):
    """사용자 응답 스키마"""
    id: int
    username: str
    email: str
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


class ChatRequest(BaseModel):
    """채팅 요청 스키마"""
    message: str = Field(..., min_length=1, max_length=1000, description="사용자 메시지")


class ChatMessageResponse(BaseModel):
    """채팅 메시지 응답 스키마"""
    id: int
    role: str
    content: str
    created_at: datetime
    
    class Config:
        from_attributes = True


class ChatHistoryResponse(BaseModel):
    """채팅 히스토리 응답 스키마"""
    messages: List[ChatMessageResponse]
    total: int