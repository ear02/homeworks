from sqlalchemy.orm import relationship

from .database import db
from .post import Post
from sqlalchemy import Column, String, Integer


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(300), nullable=False, unique=True)
    name = Column(String(400), nullable=True)
    email = Column(String(50), unique=True, nullable=False)
    post = relationship("Post", back_populates="user")
