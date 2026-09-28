# procode-task: CH-APIROUTER-TASK-COURSES-PREFIX@1

from fastapi import APIRouter

router = APIRouter(prefix="/courses", tags=["courses"])

@router.get("")
def list_courses() -> list:
    return []

# Создайте router и GET /courses


#region УСЛОВИЕ ЗАДАЧИ
# Добавьте prefix к роутеру курсов
#
# APIRouter уже доступен, импорт писать не нужно.
#
# Создайте router с:
#
#
# prefix="/courses"
# tags=["courses"]
#
#
# Зарегистрируйте list_courses() как GET с путём "". Функция должна вернуть пустой список.
#
# Важно: используйте именно пустой путь "", чтобы итоговый адрес был /courses, а не /courses/.
#
# Проверка решения:
# procode имя_файла.py
#endregion