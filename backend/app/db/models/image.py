from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from ..database import Base


class DiaryImage(Base):
    __tablename__ = "diary_images"

    id = Column(Integer, primary_key=True, index=True)
    entry_id = Column(Integer, ForeignKey("diary_entries.id"), nullable=False, index=True)
    storage_path = Column(String(500), nullable=False)
    thumbnail_path = Column(String(500))
    caption = Column(Text)
    sort_order = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    entry = relationship("DiaryEntry", back_populates="images")

    def __repr__(self):
        return f"<DiaryImage(id={self.id}, entry_id={self.entry_id}, path='{self.storage_path}')>"