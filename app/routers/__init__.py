from app.routers.courses import router as courses_router
from app.routers.lessons import router as lessons_router
from app.routers.system import router as system_router

__all__ = ["courses_router", "lessons_router", "system_router"]