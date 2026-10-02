from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.database import get_db
from ..db.models import DiaryEntry

router = APIRouter()

@router.get("/")
async def get_settings(db: Session = Depends(get_db)):
    # Get database statistics
    total_entries = db.query(DiaryEntry).count()
    
    # Get storage information
    import os
    
    # Calculate total database size 
    db_size = 0
    if os.path.exists("data/diary.db"):
        db_size = os.path.getsize("data/diary.db")
    
    # Calculate image storage size
    image_size = 0
    if os.path.exists("data/images"):
        for root, dirs, files in os.walk("data/images"):
            for file in files:
                file_path = os.path.join(root, file)
                image_size += os.path.getsize(file_path)
    
    return {
        "database_size": db_size,
        "image_storage_size": image_size,
        "total_storage": db_size + image_size,
        "total_entries": total_entries
    }