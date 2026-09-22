# procode-task: CH-RESPONSE-MODELS-TASK2-MISSING-FIELDS@1


REQUIRED_FIELDS = ("id", "title", "slug", "level", "price")


def missing_course_fields(course) -> list:
    result = []
    for key in REQUIRED_FIELDS:
        if key not in course:
            result.append(key)
    return result


#region УСЛОВИЕ ЗАДАЧИ
# Найдите нарушение контракта ответа
#
# Реализуйте missing_course_fields(course). Верните список отсутствующих обязательных полей CourseRead в порядке id, title, slug, level, price.
#
# Проверка решения:
# procode имя_файла.py
#endregion