from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..db.database import get_db
from ..db.models import DiaryEntry
from ..schemas import DiaryEntryCreate, DiaryEntryUpdate, DiaryEntryResponse

router = APIRouter()

@router.get("/", response_model=List[DiaryEntryResponse])
async def list_entries(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
):
    entries = db.query(DiaryEntry).offset(skip).limit(limit).all()
    return entries

@router.get("/{entry_id}", response_model=DiaryEntryResponse)
async def get_entry(entry_id: int, db: Session = Depends(get_db)):
    entry = db.query(DiaryEntry).filter(DiaryEntry.id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry

@router.post("/", response_model=DiaryEntryResponse)
async def create_entry(entry: DiaryEntryCreate, db: Session = Depends(get_db)):
    db_entry = DiaryEntry(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

@router.put("/{entry_id}", response_model=DiaryEntryResponse)
async def update_entry(
    entry_id: int, 
    entry_update: DiaryEntryUpdate, 
    db: Session = Depends(get_db)
):
    db_entry = db.query(DiaryEntry).filter(DiaryEntry.id == entry_id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    
    update_data = entry_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_entry, key, value)
    
    db.commit()
    db.refresh(db_entry)
    return db_entry

@router.delete("/{entry_id}")
async def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    db_entry = db.query(DiaryEntry).filter(DiaryEntry.id == entry_id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    
    db.delete(db_entry)
    db.commit()
    return {"message": "Entry deleted successfully"}