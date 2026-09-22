# procode-task: CH-REQUEST-BODY-TASK2-NEXT-ID@1


def next_course_id(courses):
    if len(courses) == 0:
        return 1
    return max(courses.keys()) + 1


#region УСЛОВИЕ ЗАДАЧИ
# Назначьте следующий ID
#
# Реализуйте next_course_id(courses). courses - словарь, где ключи являются ID. Для пустого каталога верните 1, иначе максимальный ID плюс 1.
#
# Проверка решения:
# procode имя_файла.py
#endregion