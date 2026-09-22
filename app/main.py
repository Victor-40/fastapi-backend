from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


app = FastAPI(
    title="CourseHub API",
    version="0.1.0",
    description="Учебный API мини-платформы онлайн-курсов.",
)


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

class CourseRead(BaseModel):
    id: int
    title: str
    slug: str
    level: str
    price: float

class LessonRead(BaseModel):
    id: int
    course_id: int
    title: str
    order: int

class CourseCreate(BaseModel):
    title: str
    slug: str
    level: str
    price: float = 0


def _next_course_id() -> int:
    return max(COURSES.keys(), default=0) + 1



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

@app.get("/courses/{course_id}", response_model=CourseRead, tags=["courses"])
def get_course(course_id: int) -> dict[str, int | float | str]:
    course = COURSES.get(course_id)
    if course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    return course

@app.post("/courses", response_model=CourseRead, status_code=status.HTTP_201_CREATED, tags=["courses"])
def create_course(course_in: CourseCreate) -> dict[str, int | float | str]:
    course_id = _next_course_id()
    course = {
        "id": course_id,
        **course_in.model_dump(),
    }
    COURSES[course_id] = course
    LESSONS[course_id] = []

    return course