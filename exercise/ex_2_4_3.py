# procode-task: CH-QUERY-PARAMS-TASK3-FILTER-LEVEL@1


def filter_by_level(courses, level=None):
    # Верните новый отфильтрованный список.
    if level is None:
        return courses.copy()
    return [course for course in courses if course["level"].lower() == level.lower()]


#region УСЛОВИЕ ЗАДАЧИ
# Отфильтруйте курсы по уровню
#
# Реализуйте filter_by_level(courses, level=None).
#
# Если level равен None, верните новый список, содержащий все курсы.
#
# Если уровень передан, верните новый список только с теми курсами, у которых значение course["level"] совпадает с level без учёта регистра.
#
# Проверка решения:
# procode имя_файла.py
#endregion