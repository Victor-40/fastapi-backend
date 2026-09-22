# procode-task: CH-RESPONSE-MODELS-TASK1-PUBLIC-COURSE@1


PUBLIC_FIELDS = ("id", "title", "slug", "level", "price")


def to_course_read(course):
    result = {}
    for key, value in course.items():
        if key in PUBLIC_FIELDS:
            result[key] = value
    return result

#region УСЛОВИЕ ЗАДАЧИ
# Оставьте публичные поля курса
#
# Реализуйте to_course_read(course). Верните новый словарь только с полями id, title, slug, level и price. Исходный словарь изменять нельзя.
#
# Проверка решения:
# procode имя_файла.py
#endregion