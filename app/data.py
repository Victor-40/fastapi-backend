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