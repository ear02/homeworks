"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,

)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from sqlalchemy.orm import declared_attr, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

PG_CONN_URI = "postgresql+asyncpg://postgres:password@localhost/postgres"

engine = create_async_engine(
    PG_CONN_URI,
    echo=True,
)

Session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


class Base:

    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class User(Base):
    username = Column(String(300), nullable=False)
    name = Column(String(100), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    posts = relationship("Post", back_populates="user")


class Post(Base):
    title = Column(String(200), nullable=False)
    body = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="posts")


