from fastapi import FastAPI

from app.routers import courses_router, lessons_router, system_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="CourseHub API",
        version="0.1.0",
        description="Учебный API мини-платформы онлайн-курсов.",
    )

    app.include_router(system_router)
    app.include_router(courses_router)
    app.include_router(lessons_router)
    return app

app = create_app()