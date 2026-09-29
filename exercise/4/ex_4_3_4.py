# procode-task: CH-SERVICE-LAYER-TASK-SERVICE-RULES@1


def get_course_service() -> CourseService:
    return CourseService()


#region УСЛОВИЕ ЗАДАЧИ
# Создайте dependency-провайдер сервиса
#
# Класс CourseService уже подготовлен.
#
# Реализуйте функцию get_course_service(), которая создаёт и возвращает новый экземпляр CourseService.
#
# Функция должна иметь аннотацию возвращаемого типа CourseService.
#
# Импорты писать не нужно.
#
# Проверка решения:
# procode имя_файла.py
#endregion