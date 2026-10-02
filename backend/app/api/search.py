from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import text
from ..db.database import get_db
from ..db.models import DiaryEntry

router = APIRouter()

@router.get("/")
async def search_entries(
    query: str = Query(...),
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 50
):
    # Perform full-text search in diary entries
    sql_query = text("""
        SELECT id, entry_date, title, body, mood, favorite, created_at, updated_at
        FROM diary_entries 
        WHERE body LIKE :search OR title LIKE :search
        ORDER BY entry_date DESC
        LIMIT :limit OFFSET :skip
    """)
    
    result = db.execute(sql_query, {
        "search": f"%{query}%",
        "limit": limit,
        "skip": skip
    })
    
    entries = []
    for row in result:
        entries.append({
            "id": row[0],
            "entry_date": row[1],
            "title": row[2],
            "body": row[3],
            "mood": row[4],
            "favorite": row[5],
            "created_at": row[6],
            "updated_at": row[7]
        })
    
    return {"results": entries, "count": len(entries)}