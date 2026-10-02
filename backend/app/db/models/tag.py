from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Index
from ..database import Base


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True, index=True)

    def __repr__(self):
        return f"<Tag(id={self.id}, name='{self.name}')>"