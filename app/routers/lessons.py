from fastapi import APIRouter, HTTPException, status

from app.data import COURSES, LESSONS
from app.schemas import LessonRead

router = APIRouter(prefix="/courses", tags=["lessons"])

@router.get("/{course_id}/lessons", response_model=list[LessonRead])
def list_course_lessons(course_id: int) -> list[dict[str, int | str]]:
    if course_id not in COURSES:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found",
        )

    return LESSONS.get(course_id, [])