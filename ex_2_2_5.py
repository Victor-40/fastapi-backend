# procode-task: CH-COURSEHUB-START-TASK5-CREATE-PING-APP@1
# from fastapi import FastAPI


app = FastAPI(
    title="Inventory API",
)

@app.get("/ping", tags=["system"])
def ping() -> dict:
    return {"message": "pong"}



# Создайте приложение и endpoint GET /ping.


#region УСЛОВИЕ ЗАДАЧИ
# Перенесите приём на другой API
#
# Класс FastAPI уже доступен, импорт не нужен. Создайте объект app с названием Inventory API. 
# Добавьте GET /ping с тегом system. Функция ping() должна вернуть {"message": "pong"}.
#
# Проверка решения:
# procode имя_файла.py
#endregion