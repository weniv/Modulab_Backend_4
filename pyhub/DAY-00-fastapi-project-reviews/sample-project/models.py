"""
데이터베이스 모델 정의
SQLModel을 사용한 User와 ChatMessage 모델
"""

from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime


class User(SQLModel, table=True):
    """사용자 모델"""
    __tablename__ = "users"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True, min_length=3, max_length=50)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.now)
    
    # 관계 설정: 한 사용자는 여러 채팅 메시지를 가질 수 있음
    chat_messages: List["ChatMessage"] = Relationship(back_populates="user")


class ChatMessage(SQLModel, table=True):
    """채팅 메시지 모델"""
    __tablename__ = "chat_messages"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    role: str = Field(min_length=1, max_length=20)  # 'user' 또는 'assistant'
    content: str = Field(min_length=1)
    created_at: datetime = Field(default_factory=datetime.now)
    
    # 관계 설정: 각 메시지는 한 사용자에게 속함
    user: Optional[User] = Relationship(back_populates="chat_messages")