from fastapi import APIRouter, Depends, status

from app.schemas import CourseCreate, CourseRead, CourseUpdate
from app.services import CourseService, get_course_service

router = APIRouter(prefix="/courses", tags=["courses"])

@router.get("", response_model=list[CourseRead])
def list_courses(
    level: str | None = None,
    q: str | None = None,
    service: CourseService = Depends(get_course_service),
) -> list[CourseRead]:
    return service.list_courses(level=level, q=q)

@router.get("/{course_id}", response_model=CourseRead)
def get_course(
    course_id: int,
    service: CourseService = Depends(get_course_service),
) -> CourseRead:
    return service.get_course(course_id)

@router.post("", response_model=CourseRead, status_code=status.HTTP_201_CREATED)
def create_course(
    course_in: CourseCreate,
    service: CourseService = Depends(get_course_service),
) -> CourseRead:
    return service.create_course(course_in)

@router.patch("/{course_id}", response_model=CourseRead)
def update_course(
    course_id: int,
    course_in: CourseUpdate,
    service: CourseService = Depends(get_course_service),
) -> CourseRead:
    return service.update_course(course_id, course_in)