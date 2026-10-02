from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Index
from sqlalchemy.orm import relationship
from ..database import Base


class EntryTag(Base):
    __tablename__ = "entry_tags"

    entry_id = Column(Integer, ForeignKey("diary_entries.id"), primary_key=True)
    tag_id = Column(Integer, ForeignKey("tags.id"), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    entry = relationship("DiaryEntry", back_populates="tags")
    tag = relationship("Tag")

    def __repr__(self):
        return f"<EntryTag(entry_id={self.entry_id}, tag_id={self.tag_id})>"