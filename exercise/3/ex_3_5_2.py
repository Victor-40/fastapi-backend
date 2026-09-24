# procode-task: CH-SCHEMAS-PRACTICE-TASK2-CREATE@1


def next_course_id(courses):
    if not courses:
        return 1
    return max(courses.keys()) + 1


def create_course(courses, body):
    id = next_course_id(courses)
    new_course =  dict(**body)
    courses[id] = new_course
    return courses



#region УСЛОВИЕ ЗАДАЧИ
# Создайте курс
#
# Функция next_course_id(courses) уже подготовлена.
#
# Реализуйте create_course(courses, body): получите новый серверный ID, создайте новый словарь с полем id и всеми полями из body, сохраните его в courses и верните.
#
# Исходный словарь body изменять нельзя.
#
# Проверка решения:
# procode имя_файла.py
#endregion