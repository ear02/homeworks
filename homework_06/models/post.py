from sqlalchemy.orm import relationship

from .database import db
from sqlalchemy import Column, String, Integer, ForeignKey, Text


class Post(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    body = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User", back_populates="post")
