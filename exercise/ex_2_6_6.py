# procode-task: CH-API-BASICS-PRACTICE-TASK6-NESTED-ENDPOINT@1
# from fastapi import FastAPI, HTTPException

# app = FastAPI
# COURSES = {}
# LESSONS = {}

@app.get("/courses/{course_id}/lessons", tags=["lessons"])
def list_course_lessons(course_id: int):
    if not COURSES.get(course_id):
        raise HTTPException(status_code=404, detail="Course not found")
    return LESSONS.get(course_id, [])



# Создайте вложенный endpoint CourseHub.


#region УСЛОВИЕ ЗАДАЧИ
# Объявите вложенный endpoint
#
# app, HTTPException, COURSES и LESSONS уже доступны.
#
# Объявите GET /courses/{course_id}/lessons с тегом lessons.
#
# Функция list_course_lessons(course_id: int) должна:
#
# - поднять HTTPException со статусом 404 и detail="Course not found", если курса нет в COURSES;
# - для существующего курса вернуть LESSONS.get(course_id, []).
#
# Проверка решения:
# procode имя_файла.py
#endregion