# procode-task: CH-API-BASICS-PRACTICE-TASK3-LIST-LESSONS-OR-404@1
from fastapi import HTTPException, status


def list_lessons_or_404(courses, lessons, course_id):
    # Проверьте родительский курс и верните его уроки.
    if not courses.get(course_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return  lessons.get(course_id, [])


#region УСЛОВИЕ ЗАДАЧИ
# Верните уроки или поднимите 404
#
# HTTPException уже доступен. Реализуйте list_lessons_or_404(courses, lessons, course_id).
#
# Если курса с переданным course_id нет в courses, поднимите HTTPException со статусом 404 и detail="Course not found".
#
# Если курс существует, верните:
#
# lessons.get(course_id, [])
#
# Проверка решения:
# procode имя_файла.py
#endregion