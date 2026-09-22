# procode-task: CH-PATH-PARAMS-TASK4-DYNAMIC-ROUTE@1
# from fastapi import  FastApi


# app =  FastApi()

@app.get("/courses/{course_id}", tags=["courses"])
def get_course(course_id: int):
    return {"id": course_id}


# Объявите динамический endpoint.


#region УСЛОВИЕ ЗАДАЧИ
# Объявите типизированный маршрут
#
# Учебный объект app уже создан. Импортировать FastAPI не нужно.
#
# Объявите маршрут:
#
#
# GET /courses/{course_id}
#
#
# с тегом courses.
#
# Функция get_course(course_id: int) должна вернуть:
#
#
# {"id": course_id}
#
# Проверка решения:
# procode имя_файла.py
#endregionfrom fastapi import  HTTPException