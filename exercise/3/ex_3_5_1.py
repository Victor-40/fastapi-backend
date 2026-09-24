# procode-task: CH-SCHEMAS-PRACTICE-TASK1-NEXT-ID@1


def next_course_id(courses):
    if not courses:
        return 1
    return max(courses.keys()) + 1


#region УСЛОВИЕ ЗАДАЧИ
# Найдите ID для нового курса
#
# Реализуйте next_course_id(courses).
#
# courses – словарь, где ключи являются числовыми ID курсов. Функция должна вернуть 1, если каталог пуст, иначе максимальный существующий ID плюс 1.
#
# Количество курсов использовать как новый ID нельзя: в каталоге могут быть пропуски.
#
# Проверка решения:
# procode имя_файла.py
#endregion