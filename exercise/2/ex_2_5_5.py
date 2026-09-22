# procode-task: CH-ERRORS-STATUS-CODES-TASK5-PARSE-ID-OR-422@1


@app.get("/orders/{order_id}")
def get_order(order_id: int):
    return {"id": order_id}

     
# Объявите GET /orders/{order_id}


#region УСЛОВИЕ ЗАДАЧИ
# Получите 422 через валидацию FastAPI
#
# Учебный объект app уже создан. Импортировать FastAPI не нужно.
#
# Объявите маршрут:
#
# GET /orders/{order_id}
#
# с функцией:
#
# get_order(order_id: int)
#
# Функция должна вернуть {"id": order_id}.
#
# Не нужно вручную преобразовывать order_id или поднимать HTTPException для неверного типа. 
# Аннотация order_id: int должна позволить FastAPI самому вернуть 422, если в пути придёт значение вроде /orders/python.
#
# Проверка решения:
# procode имя_файла.py
#endregion