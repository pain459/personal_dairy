from fastapi import APIRouter
from . import entries, calendar, images, tags, search, backups, settings, health

# Create main API router
router = APIRouter()

# Include all sub-routers
router.include_router(entries.router, prefix="/entries", tags=["entries"])
router.include_router(calendar.router, prefix="/calendar", tags=["calendar"])
router.include_router(images.router, prefix="/images", tags=["images"])
router.include_router(tags.router, prefix="/tags", tags=["tags"])
router.include_router(search.router, prefix="/search", tags=["search"])
router.include_router(backups.router, prefix="/backups", tags=["backups"])
router.include_router(settings.router, prefix="/settings", tags=["settings"])
router.include_router(health.router, prefix="/health", tags=["health"])

__all__ = ["router"]