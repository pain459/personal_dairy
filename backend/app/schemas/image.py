from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ImageCreate(BaseModel):
    entry_id: int
    storage_path: str
    thumbnail_path: Optional[str] = None
    caption: Optional[str] = None
    sort_order: int = 0

class ImageResponse(BaseModel):
    id: int
    entry_id: int
    storage_path: str
    thumbnail_path: Optional[str] = None
    caption: Optional[str] = None
    sort_order: int = 0
    created_at: datetime
    
    class Config:
        from_attributes = True