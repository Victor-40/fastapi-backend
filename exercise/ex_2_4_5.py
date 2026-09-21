# procode-task: CH-QUERY-PARAMS-TASK5-FILTER-COURSES@1


def filter_courses(courses, level=None, q=None):
    result = list(courses)
    # Последовательно примените level и q.
    if level:
        result = [course for course in result if course["level"].lower() == level.lower()]
    if q is None:
        return result
    return [course for course in result if q.lower() in course["title"].lower()]


#region УСЛОВИЕ ЗАДАЧИ
# Примените два фильтра последовательно
#
# Реализуйте filter_courses(courses, level=None, q=None).
#
# Начните с нового списка всех курсов. Если передан level, оставьте только курсы этого уровня без учёта регистра. Затем, если передан q, оставьте среди полученных курсов только те, в названии которых встречается q без учёта регистра.
#
# Оба параметра необязательны. Если они не переданы, функция должна вернуть новый список со всеми курсами.
#
# Пустая строка q="" считается переданным значением. Как и в уроке, она встречается в каждом названии, поэтому такой поиск не должен удалять курсы из текущего результата.
#
# Проверка решения:
# procode имя_файла.py
#endregion