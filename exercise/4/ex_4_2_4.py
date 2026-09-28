# procode-task: CH-APIROUTER-TASK-SYSTEM-ROUTER@1


# Создайте router и endpoint /health

# from fastapi import APIRouter

router = APIRouter(tags=["system"])

@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "CourseHub API"}

#region УСЛОВИЕ ЗАДАЧИ
# Создайте системный роутер
#
# APIRouter уже доступен, импорт писать не нужно.
#
# Создайте объект router с тегом system. Затем зарегистрируйте GET /health через @router.get(...).
#
# Функция health() должна вернуть:
#
#
# {"status": "ok", "service": "CourseHub API"}
#
# Проверка решения:
# procode имя_файла.py
#endregion