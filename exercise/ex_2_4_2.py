# procode-task: CH-QUERY-PARAMS-TASK2-NORMALIZE-QUERY@1


def normalize_query(q):
    # Учтите отдельно None и строку.
    if q is None:
        return None
    if isinstance(q, str):
        return q.lower()


#region УСЛОВИЕ ЗАДАЧИ
# Нормализуйте поисковый запрос
#
# Реализуйте функцию normalize_query(q).
#
# Если q равно None, верните None. Если передана строка, приведите её к нижнему регистру и верните результат.
#
# Пустая строка "" должна остаться пустой.
#
# Проверка решения:
# procode имя_файла.py
#endregion