# procode-task: CH-PATH-PARAMS-TASK2-FIND-COURSE@1


def find_course(courses, course_id):
    # Верните объект по ключу без исключения KeyError.
    return courses.get(course_id)


#region УСЛОВИЕ ЗАДАЧИ
# Найдите курс по ID
#
# Реализуйте find_course(courses, course_id). courses – словарь с числовыми ключами. Верните найденный курс или None.
#
# Проверка решения:
# procode имя_файла.py
#endregion