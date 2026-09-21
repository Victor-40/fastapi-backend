# procode-task: CH-ERRORS-STATUS-CODES-TASK4-REQUIRE-COURSE@1


def require_course(courses, course_id):
    # Верните курс или поднимите 404.
    course = courses.get(course_id)
    if not course:
        raise HTTPException(
             status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found",
        )
    else:
        return course


#region УСЛОВИЕ ЗАДАЧИ
# Поднимите 404 для неизвестного курса
#
# HTTPException и status уже доступны. Реализуйте require_course(courses, course_id).
#
# Если курс с переданным course_id найден, верните его. Если такого курса нет, поднимите:
#
#
# HTTPException(
#     status_code=status.HTTP_404_NOT_FOUND,
#     detail="Course not found",
# )
#
# Проверка решения:
# procode имя_файла.py
#endregion