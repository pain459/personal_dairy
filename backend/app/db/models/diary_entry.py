from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Date, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


class DiaryEntry(Base):
    __tablename__ = "diary_entries"

    id = Column(Integer, primary_key=True, index=True)
    entry_date = Column(Date, index=True, nullable=False)
    title = Column(String(255))
    body = Column(Text)
    mood = Column(String(50))
    favorite = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    images = relationship("DiaryImage", back_populates="entry", cascade="all, delete-orphan")
    tags = relationship("EntryTag", back_populates="entry", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<DiaryEntry(id={self.id}, date={self.entry_date}, title='{self.title}')>"