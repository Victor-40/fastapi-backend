# procode-task: CH-API-BASICS-PRACTICE-TASK4-VALIDATE-LESSON-LINKS@1


def validate_lesson_links(course_id, lesson_items):
    # Проверьте course_id каждого урока.
    if len(lesson_items) == 0:
        return True
    result = []
    for lesson in lesson_items:
        if lesson.get("course_id") == course_id:
            result.append(True)
        else:
            result.append(False)
    return all(result)


#region УСЛОВИЕ ЗАДАЧИ
# Проверьте связь данных с URL
#
# Реализуйте validate_lesson_links(course_id, lesson_items).
#
# Верните True, если каждый словарь урока содержит ключ course_id и его значение совпадает с переданным course_id.
#
# Если хотя бы у одного урока ключа course_id нет или значение отличается, верните False.
#
# Для пустого списка верните True.
#
# Проверка решения:
# procode имя_файла.py
#endregion