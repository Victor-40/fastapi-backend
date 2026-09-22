# procode-task: CH-API-BASICS-PRACTICE-TASK7-SEARCH-COURSE-LESSONS@1
# from fastapi import FastAPI, HTTPException

# app = FastAPI
# COURSES = {}
# LESSONS = {}

@app.get("/courses/{course_id}/lessons", tags=["lessons"])
def search_course_lessons(course_id: int, q: str | None = None,):
    if not COURSES.get(course_id):
        raise HTTPException(status_code=404, detail="Course not found")
    lessons = LESSONS.get(course_id, [])
    if q == "" or q is None:
        return lessons 
    return [lesson for lesson in lessons if q.lower() in lesson["title"].lower()]



# Создайте вложенный endpoint с необязательным q.

#region УСЛОВИЕ ЗАДАЧИ
# Добавьте поиск к вложенному endpoint
#
# app, HTTPException, COURSES и LESSONS уже доступны.
#
# Объявите GET /courses/{course_id}/lessons с тегом lessons и функцией:
#
#
# search_course_lessons(
#     course_id: int,
#     q: str | None = None,
# )
#
#
# Функция должна:
#
# - поднять HTTPException со статусом 404 и detail="Course not found", если курса нет;
# - получить уроки через LESSONS.get(course_id, []);
# - если q is not None, оставить уроки, в названии которых встречается q без учёта регистра;
# - пустая строка q="" должна сохранить весь текущий список;
# - если курс существует, но уроков нет, вернуть [].
#
# Проверка решения:
# procode имя_файла.py
#endregion