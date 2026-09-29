from fastapi import HTTPException, status

from app.data import COURSES, LESSONS
from app.schemas import CourseCreate, CourseRead, CourseUpdate, LessonRead

MIN_SEARCH_QUERY_LENGTH = 2

class CourseService:
    def list_courses(
        self,
        level: str | None = None,
        q: str | None = None,
    ) -> list[CourseRead]:
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

        return [CourseRead(**course) for course in courses]

    def get_course(self, course_id: int) -> CourseRead:
        course = COURSES.get(course_id)
        if course is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found",
            )

        return CourseRead(**course)

    def create_course(self, course_in: CourseCreate) -> CourseRead:
        self._ensure_unique_slug(course_in.slug)

        course_id = self._next_course_id()
        course = {
            "id": course_id,
            **course_in.model_dump(),
        }
        COURSES[course_id] = course
        LESSONS[course_id] = []

        return CourseRead(**course)

    def update_course(self, course_id: int, course_in: CourseUpdate) -> CourseRead:
        course = COURSES.get(course_id)
        if course is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found",
            )

        updates = course_in.model_dump(exclude_unset=True, exclude_none=True)
        new_slug = updates.get("slug")
        if new_slug is not None:
            self._ensure_unique_slug(new_slug, exclude_course_id=course_id)

        course.update(updates)
        return CourseRead(**course)

    def _next_course_id(self) -> int:
        return max(COURSES.keys(), default=0) + 1

    def _find_course_by_slug(
        self,
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
        self,
        slug: str,
        *,
        exclude_course_id: int | None = None,
    ) -> None:
        if self._find_course_by_slug(slug, exclude_course_id=exclude_course_id) is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Course slug already exists",
            )

class LessonService:
    def list_course_lessons(self, course_id: int) -> list[LessonRead]:
        if course_id not in COURSES:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found",
            )

        return [LessonRead(**lesson) for lesson in LESSONS.get(course_id, [])]

def get_course_service() -> CourseService:
    return CourseService()

def get_lesson_service() -> LessonService:
    return LessonService()