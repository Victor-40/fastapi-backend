# procode-task: CH-APIROUTER-TASK-ROUTER-FOR-PATH@1


# Напишите импорты и __all__
from app.routers.courses import router as courses_router
from app.routers.lessons import router as lessons_router
from app.routers.system import router as system_router

__all__ = ["courses_router", "lessons_router", "system_router"]

#region УСЛОВИЕ ЗАДАЧИ
# Экспортируйте роутеры из пакета
#
# Модули app.routers.courses, app.routers.lessons и app.routers.system уже подготовлены. В каждом из них объект называется router.
#
# Напишите код для app/routers/__init__.py:
#
# - импортируйте три объекта router под именами courses_router, lessons_router, system_router;
# - создайте __all__ с этими тремя именами в таком же порядке.
#
# Используйте абсолютные импорты от пакета app.
#
# Проверка решения:
# procode имя_файла.py
#endregion