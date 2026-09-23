from typing import Literal

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


CourseLevel = Literal["beginner", "intermediate", "advanced"]
MIN_SEARCH_QUERY_LENGTH = 2


app = FastAPI(
    title="CourseHub API",
    version="0.1.0",
    description="Учебный API мини-платформы онлайн-курсов.",
)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "CourseHub API",
    }


COURSES = {
    1: {
        "id": 1,
        "title": "FastAPI для начинающих",
        "slug": "fastapi-for-beginners",
        "level": "beginner",
        "price": 0.0,
    },
    2: {
        "id": 2,
        "title": "Python Backend Practice",
        "slug": "python-backend-practice",
        "level": "intermediate",
        "price": 49.0,
    },
}

LESSONS = {
    1: [
        {
            "id": 1,
            "course_id": 1,
            "title": "Первый запуск FastAPI",
            "order": 1,
        },
        {
            "id": 2,
            "course_id": 1,
            "title": "Path-параметры",
            "order": 2,
        },
    ],
    2: [
        {
            "id": 3,
            "course_id": 2,
            "title": "HTTP-ответы backend API",
            "order": 1,
        },
    ],
}


class CourseRead(BaseModel):
    id: int
    title: str
    slug: str
    level: CourseLevel
    price: float


class LessonRead(BaseModel):
    id: int
    course_id: int
    title: str
    order: int


class CourseCreate(BaseModel):
    title: str = Field(min_length=3, max_length=80)
    slug: str = Field(min_length=3, max_length=60, pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    level: CourseLevel
    price: float = Field(default=0, ge=0)


class CourseUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=80)
    slug: str | None = Field(default=None, min_length=3, max_length=60, pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    level: CourseLevel | None = None
    price: float | None = Field(default=None, ge=0)


@app.get("/courses/{course_id}", response_model=CourseRead, tags=["courses"])
def get_course(course_id: int) -> dict[str, int | float | str]:
    course = COURSES.get(course_id)
    if course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    return course


@app.get("/courses", response_model=list[CourseRead], tags=["courses"])
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


@app.get("/courses/{course_id}/lessons", response_model=list[LessonRead], tags=["lessons"])
def list_course_lessons(course_id: int) -> list[dict[str, int | str]]:
    if course_id not in COURSES:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    return LESSONS.get(course_id, [])


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


def _ensure_unique_slug(slug: str, *, exclude_course_id: int | None = None) -> None:
    if _find_course_by_slug(slug, exclude_course_id=exclude_course_id) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Course slug already exists",
        )


@app.post("/courses", response_model=CourseRead, status_code=status.HTTP_201_CREATED, tags=["courses"])
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


@app.patch("/courses/{course_id}", response_model=CourseRead, tags=["courses"])
def update_course(course_id: int, course_in: CourseUpdate) -> dict[str, int | float | str]:
    course = COURSES.get(course_id)
    if course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    updates = course_in.model_dump(exclude_unset=True, exclude_none=True)
    new_slug = updates.get("slug")
    if new_slug is not None:
        _ensure_unique_slug(new_slug, exclude_course_id=course_id)

    course.update(updates)
    return course