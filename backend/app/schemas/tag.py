from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TagCreate(BaseModel):
    name: str
    color: Optional[str] = None

class TagResponse(BaseModel):
    id: int
    name: str
    color: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True