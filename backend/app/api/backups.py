from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from ..db.database import get_db
import os
import shutil
import tarfile
import datetime
from pathlib import Path

router = APIRouter()

@router.post("/create")
async def create_backup(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    # Create backup filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    backup_filename = f"backup/personal-diary-{timestamp}.tar.gz"
    
    # Ensure backup directory exists
    Path("backup").mkdir(exist_ok=True)
    
    try:
        # For SQLite database, we need to copy the database file
        db_path = "data/diary.db"
        if not os.path.exists(db_path):
            raise HTTPException(status_code=404, detail="Database not found")
        
        # Create a temporary directory for backup files
        temp_dir = f"temp_backup_{timestamp}"
        os.makedirs(temp_dir, exist_ok=True)
        
        # Copy database file to temp directory
        shutil.copy2(db_path, f"{temp_dir}/diary.db")
        
        # Create tar.gz archive
        with tarfile.open(backup_filename, "w:gz") as tar:
            tar.add(temp_dir, arcname="backup")
        
        # Clean up temporary directory
        shutil.rmtree(temp_dir)
        
        return {"message": "Backup created successfully", "filename": backup_filename}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Backup creation failed: {str(e)}")

@router.get("/list")
async def list_backups():
    try:
        backups = []
        if os.path.exists("backup"):
            for filename in os.listdir("backup"):
                if filename.endswith(".tar.gz"):
                    filepath = os.path.join("backup", filename)
                    file_stats = os.stat(filepath)
                    backups.append({
                        "filename": filename,
                        "size": file_stats.st_size,
                        "created_at": datetime.datetime.fromtimestamp(file_stats.st_mtime)
                    })
        return {"backups": backups}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to list backups: {str(e)}")