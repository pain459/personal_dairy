from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional, List

class DiaryEntryBase(BaseModel):
    entry_date: date
    title: Optional[str] = None
    body: Optional[str] = None
    mood: Optional[str] = None
    favorite: bool = False

class DiaryEntryCreate(DiaryEntryBase):
    pass

class DiaryEntryUpdate(DiaryEntryBase):
    pass

class DiaryEntryResponse(DiaryEntryBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class CalendarDayResponse(BaseModel):
    day: int
    has_entry: bool
    title: Optional[str] = None
    mood: Optional[str] = None
    favorite: bool
    date: date
    
    class Config:
        from_attributes = True