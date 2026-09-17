from fastapi import FastAPI, HTTPException


app = FastAPI(
    title="CourseHub API",
    version="0.1.0",
    description="Учебный API мини-платформы онлайн-курсов.",
)


COURSES = {
    1: {
        "id": 1,
        "title": "FastAPI для начинающих",
        "level": "beginner",
    },
    2: {
        "id": 2,
        "title": "Python Backend Practice",
        "level": "intermediate",
    },
}


@app.get("/courses/{course_id}", tags=["courses"])
def get_course(course_id: int) -> dict[str, int | str]:
    course = COURSES.get(course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    return course