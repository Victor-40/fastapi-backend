# procode-task: CH-APP-FOLDERS-TASK-REQUIRED-FILES@1


def add_course(course):
    for key in course.keys():
        COURSES[course["id"]] = course
    return COURSES


#region УСЛОВИЕ ЗАДАЧИ
# Измените общий словарь COURSES
#
# Словарь COURSES уже подготовлен и считается импортированным из app.data.
#
# Реализуйте add_course(course). Добавьте переданный курс в существующий словарь COURSES по его id и верните сам словарь COURSES.
#
# Важно: не создавайте новый словарь и не переназначайте COURSES. Нужно изменить уже существующий объект.
#
# Проверка решения:
# procode имя_файла.py
#endregion