# procode-task: CH-API-BASICS-PRACTICE-TASK1-BUILD-LESSONS-PATH@1


def build_lessons_path(course_id):
    # Подставьте ID курса во вложенный путь.
    return f"/courses/{course_id}/lessons"


#region УСЛОВИЕ ЗАДАЧИ
# Постройте путь к урокам курса
#
# Реализуйте build_lessons_path(course_id).
#
# Верните путь к списку уроков курса с переданным course_id в формате:
#
#
# /courses/<course_id>/lessons
#
# Проверка решения:
# procode имя_файла.py
#endregion