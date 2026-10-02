from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from sqlalchemy.orm import Session
from ..db.database import get_db
from ..db.models import DiaryImage, DiaryEntry
from ..schemas import ImageCreate, ImageResponse
import os
from datetime import datetime
from pathlib import Path

router = APIRouter()

@router.post("/", response_model=ImageResponse)
async def create_image(
    entry_id: int,
    file: UploadFile = File(...),
    caption: str = None,
    db: Session = Depends(get_db)
):
    # Verify entry exists
    entry = db.query(DiaryEntry).filter(DiaryEntry.id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")

    # Create storage directory if it doesn't exist
    storage_dir = Path("data/images")
    storage_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate unique filename
    file_extension = file.filename.split(".")[-1]
    filename = f"{entry_id}_{datetime.now().timestamp()}.{file_extension}"
    file_path = storage_dir / filename
    
    # Save file
    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    
    # Create image record
    db_image = DiaryImage(
        entry_id=entry_id,
        storage_path=str(file_path),
        caption=caption
    )
    
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    
    return db_image

@router.get("/{image_id}", response_model=ImageResponse)
async def get_image(image_id: int, db: Session = Depends(get_db)):
    image = db.query(DiaryImage).filter(DiaryImage.id == image_id).first()
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    return image

@router.delete("/{image_id}")
async def delete_image(image_id: int, db: Session = Depends(get_db)):
    image = db.query(DiaryImage).filter(DiaryImage.id == image_id).first()
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    
    # Delete file from filesystem
    try:
        os.remove(image.storage_path)
    except OSError:
        pass  # File might already be deleted
    
    db.delete(image)
    db.commit()
    return {"message": "Image deleted successfully"}