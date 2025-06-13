"""
데이터베이스 설정 모듈
SQLModel을 사용한 SQLite 데이터베이스 연결 및 세션 관리
"""

from sqlmodel import create_engine, Session, SQLModel
from typing import Generator
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# 데이터베이스 URL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./chat_app.db")

# SQLite 엔진 생성
# connect_args={"check_same_thread": False}는 SQLite를 멀티스레드 환경에서 사용하기 위함
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False  # SQL 쿼리 로깅 비활성화 (개발 시 True로 변경 가능)
)


def create_db_and_tables():
    """데이터베이스와 테이블 생성"""
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """
    데이터베이스 세션 생성기
    FastAPI의 Depends를 통해 의존성 주입에 사용
    """
    with Session(engine) as session:
        yield session