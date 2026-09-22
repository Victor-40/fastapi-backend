# procode-task: CH-COURSEHUB-START-TASK4-REGISTER-HEALTH@1

@app.get("/health", tags=["system"])
def health() -> dict:
    return {"status": "ok", "service": "CourseHub API"}



# Объявите endpoint GET /health.


#region УСЛОВИЕ ЗАДАЧИ
# Зарегистрируйте GET /health
#
# Учебный объект app уже создан. Импортировать FastAPI не нужно.
#
# Объявите функцию health(), зарегистрированную для GET /health с тегом system. Функция должна вернуть {"status": "ok", "service": "CourseHub API"}.
#
# Проверка решения:
# procode имя_файла.py
#endregion