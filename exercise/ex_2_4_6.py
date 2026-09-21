# procode-task: CH-QUERY-PARAMS-TASK6-QUERY-ENDPOINT@1


# Объявите endpoint списка с двумя необязательными фильтрами.
# from fastapi import FastAPI

# app =FastAPI()


@app.get("/catalog")
def list_items(category: str | None = None, q: str | None = None,):
    return {"category": category, "q": q}



#region УСЛОВИЕ ЗАДАЧИ
# Объявите endpoint с query-параметрами
#
# Учебный объект app уже создан. Импортировать FastAPI не нужно.
#
# Объявите:
#
# GET /catalog
#
# с функцией:
#
# list_items(
#     category: str | None = None,
#     q: str | None = None,
# )
#
# Функция должна вернуть:
#
# {"category": category, "q": q}
#
# Проверка решения:
# procode имя_файла.py
#endregion