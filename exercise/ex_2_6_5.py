# procode-task: CH-API-BASICS-PRACTICE-TASK5-BUILD-LESSON-PATH@1
# from fastapi import FastAPI

# app = FastAPI

@app.get("/courses/{course_id}/lessons/{lesson_id}")
def get_lesson(course_id: int, lesson_id: int):
    return {"course_id": course_id, "lesson_id": lesson_id}


# Объявите endpoint конкретного урока.


#region УСЛОВИЕ ЗАДАЧИ
# Объявите endpoint конкретного урока
#
# Учебный объект app уже создан. Импортировать FastAPI не нужно.
#
# Объявите маршрут:
#
#
# GET /courses/{course_id}/lessons/{lesson_id}
#
#
# с функцией:
#
#
# get_lesson(course_id: int, lesson_id: int)
#
#
# Функция должна вернуть:
#
#
# {"course_id": course_id, "lesson_id": lesson_id}
#
#
# Оба значения должны быть path-параметрами типа int. Проверять существование курса или урока в этой задаче не нужно.
#
# Проверка решения:
# procode имя_файла.py
#endregion