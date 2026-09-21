# procode-task: CH-QUERY-PARAMS-TASK1-QUERY-VALUES@1
# from fastapi import FastAPI, HTTPException

# app = FastAPI()

# @app.get("/courses")
def query_values(level: str|None = None, q: str|None  = None):
    # Верните оба значения, включая None и пустые строки.
    return {"level": level, "q": q,}


#region УСЛОВИЕ ЗАДАЧИ
# Соберите значения query-параметров
#
# Реализуйте query_values(level=None, q=None).
#
# Верните словарь:
#
#
# {
#     "level": level,
#     "q": q,
# }
#
#
# Переданные значения менять нельзя. Если аргумент не передан, в словаре должно остаться None. Пустая строка "" также должна сохраняться без изменений.
#
# Проверка решения:
# procode имя_файла.py
#endregion