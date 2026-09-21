# procode-task: CH-ERRORS-STATUS-CODES-TASK2-NORMALIZE-SEARCH@1


def normalize_search(q):
    # Учтите None, strip и lower.
    if q is None:
        return None
    return q.strip().lower()


#region УСЛОВИЕ ЗАДАЧИ
# Подготовьте поисковую строку
#
# Реализуйте normalize_search(q).
#
# Если q равно None, верните None.
#
# Иначе уберите пробелы по краям строки с помощью strip(), приведите результат к нижнему регистру и верните его.
#
# Проверка решения:
# procode имя_файла.py
#endregion