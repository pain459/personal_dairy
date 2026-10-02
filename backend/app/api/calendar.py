from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, date
from typing import List
from ..db.database import get_db
from ..db.models import DiaryEntry
from ..schemas import CalendarDayResponse

router = APIRouter()

@router.get("/month/{year}/{month}", response_model=List[CalendarDayResponse])
async def get_month_entries(
    year: int, 
    month: int, 
    db: Session = Depends(get_db)
):
    # Get first and last day of the month
    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)
    
    first_day = date(year, month, 1)
    
    # Query entries for this month
    entries = db.query(DiaryEntry).filter(
        DiaryEntry.entry_date >= first_day,
        DiaryEntry.entry_date < next_month
    ).all()
    
    # Create response structure with all days in the month
    import calendar
    
    # Get number of days in month
    num_days = calendar.monthrange(year, month)[1]
    
    # Create list of days (1-31) with entry info
    response = []
    
    # Initialize all days as having no entries
    for day in range(1, num_days + 1):
        response.append(CalendarDayResponse(
            day=day,
            has_entry=False,
            title=None,
            mood=None,
            favorite=False,
            date=date(year, month, day)
        ))
    
    # Add actual entries to relevant days
    for entry in entries:
        day_index = entry.entry_date.day - 1
        if 0 <= day_index < len(response):
            response[day_index] = CalendarDayResponse(
                day=entry.entry_date.day,
                has_entry=True,
                title=entry.title,
                mood=entry.mood,
                favorite=entry.favorite,
                date=entry.entry_date
            )
    
    return response