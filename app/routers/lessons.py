from fastapi import APIRouter, Depends

from app.schemas import LessonRead
from app.services import LessonService, get_lesson_service

router = APIRouter(prefix="/courses", tags=["lessons"])

@router.get("/{course_id}/lessons", response_model=list[LessonRead])
def list_course_lessons(
    course_id: int,
    service: LessonService = Depends(get_lesson_service),
) -> list[LessonRead]:
    return service.list_course_lessons(course_id)