# procode-task: CH-RESPONSE-MODELS-TASK5-RESPONSE-MODEL-ROUTE@1

# COURSES = {}

# Добавьте response_model в декоратор.
@app.get("/courses", response_model=list[CourseRead])
def list_courses():
    # Верните список всех курсов из COURSES.
    return list(COURSES.values())


#region УСЛОВИЕ ЗАДАЧИ
# Подключите response_model к endpoint
#
# Класс CourseRead, объект app и словарь COURSES уже существуют.
#
# Создайте функцию list_courses(), зарегистрированную для GET /courses с response_model=list[CourseRead].
#
# Функция должна вернуть список всех курсов из COURSES.
#
# Проверка решения:
# procode имя_файла.py
#endregion