# procode-task: CH-QUERY-PARAMS-TASK4-SEARCH-TITLES@1


def search_titles(courses, q=None):
    # Выполните поиск по полю title.
    if q is None:
        return courses.copy()
    return [course for course in courses if q.lower() in course["title"].lower()]

#region УСЛОВИЕ ЗАДАЧИ
# Найдите курсы по части названия
#
# Реализуйте search_titles(courses, q=None). Если q is None, верните новый список всех курсов. Иначе оставьте курсы, в названии которых встречается q без учёта регистра.
#
# Проверка решения:
# procode имя_файла.py
#endregion