# procode-task: CH-REQUEST-BODY-TASK1-BODY-FIELDS@1


def has_required_course_fields(payload):
    reqs = ("title", "slug", "level")
    for item in reqs:
        if item not in payload:
            return False
    return True



#region УСЛОВИЕ ЗАДАЧИ
# Проверьте обязательные поля body
#
# Реализуйте has_required_course_fields(payload). Верните True, если в словаре присутствуют все обязательные поля CourseCreate: title, slug и level. В остальных случаях верните False.
#
# Проверка решения:
# procode имя_файла.py
#endregion