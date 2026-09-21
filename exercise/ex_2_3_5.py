# procode-task: CH-PATH-PARAMS-TASK5-ROUTE-ORDER@1
# from fastapi import FastAPI

# app = FastAPI()

@app.get("/courses/latest")
def latest_course():
    return {"kind": "latest"}

@app.get("/courses/{course_id}")
def get_course(course_id: int):
    return {"id": course_id}



# Сначала фиксированный маршрут, затем динамический.


#region УСЛОВИЕ ЗАДАЧИ
# Объявите маршруты в правильном порядке
#
# Учебный объект app уже создан.
#
# Сначала объявите GET /courses/latest с функцией latest_course(), которая возвращает:
#
#
# {"kind": "latest"}
#
#
# Затем объявите GET /courses/{course_id} с функцией get_course(course_id: int), которая возвращает:
#
#
# {"id": course_id}
#
# Проверка решения:
# procode имя_файла.py
#endregion