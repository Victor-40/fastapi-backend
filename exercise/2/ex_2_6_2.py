# procode-task: CH-API-BASICS-PRACTICE-TASK2-COURSE-LESSONS-STATE@1


def course_lessons_state(courses, lessons, course_id):
    # Сначала проверьте курс, затем его уроки.
    if not courses.get(course_id):
        return "missing_course"
    result = lessons.get(course_id, [])
    if result:
        return "has_lessons"
    else:
        return "empty"



#region УСЛОВИЕ ЗАДАЧИ
# Различите три состояния
#
# Реализуйте функцию course_lessons_state(courses, lessons, course_id).
#
# courses содержит существующие курсы, а lessons – уроки, сгруппированные по course_id.
#
# Для переданного course_id верните:
#
# - "missing_course", если такого ID нет в courses;
# - "empty", если курс существует, но для этого course_id нет уроков;
# - "has_lessons", если у этого курса есть хотя бы один урок.
#
# Важно: сначала проверьте существование курса. Отсутствующий курс и существующий курс без уроков – это два разных состояния.
#
# Проверка решения:
# procode имя_файла.py
#endregion