from fastapi import APIRouter, HTTPException, status

from app.data import COURSES, LESSONS
from app.schemas import CourseCreate, CourseRead, CourseUpdate

MIN_SEARCH_QUERY_LENGTH = 2

router = APIRouter(prefix="/courses", tags=["courses"])

@router.get("", response_model=list[CourseRead])
def list_courses(
    level: str | None = None,
    q: str | None = None,
) -> list[dict[str, int | float | str]]:
    courses = list(COURSES.values())

    if level is not None:
        courses = [
            course
            for course in courses
            if str(course["level"]).lower() == level.lower()
        ]

    if q is not None:
        query = q.strip().lower()
        if len(query) < MIN_SEARCH_QUERY_LENGTH:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Search query must contain at least {MIN_SEARCH_QUERY_LENGTH} characters",
            )

        courses = [
            course
            for course in courses
            if query in str(course["title"]).lower()
        ]

    return courses

@router.get("/{course_id}", response_model=CourseRead)
def get_course(course_id: int) -> dict[str, int | float | str]:
    course = COURSES.get(course_id)
    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found",
        )

    return course

def _next_course_id() -> int:
    return max(COURSES.keys(), default=0) + 1

def _find_course_by_slug(
    slug: str,
    *,
    exclude_course_id: int | None = None,
) -> dict[str, int | float | str] | None:
    for course_id, course in COURSES.items():
        if exclude_course_id is not None and course_id == exclude_course_id:
            continue

        if course["slug"] == slug:
            return course

    return None

def _ensure_unique_slug(
    slug: str,
    *,
    exclude_course_id: int | None = None,
) -> None:
    if _find_course_by_slug(slug, exclude_course_id=exclude_course_id) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Course slug already exists",
        )

@router.post("", response_model=CourseRead, status_code=status.HTTP_201_CREATED)
def create_course(course_in: CourseCreate) -> dict[str, int | float | str]:
    _ensure_unique_slug(course_in.slug)

    course_id = _next_course_id()
    course = {
        "id": course_id,
        **course_in.model_dump(),
    }
    COURSES[course_id] = course
    LESSONS[course_id] = []

    return course

@router.patch("/{course_id}", response_model=CourseRead)
def update_course(course_id: int, course_in: CourseUpdate) -> dict[str, int | float | str]:
    course = COURSES.get(course_id)
    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found",
        )

    updates = course_in.model_dump(exclude_unset=True, exclude_none=True)
    new_slug = updates.get("slug")
    if new_slug is not None:
        _ensure_unique_slug(new_slug, exclude_course_id=course_id)

    course.update(updates)
    return course