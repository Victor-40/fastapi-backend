# procode-task: CH-PATH-PARAMS-TASK3-COURSE-OR-404@1
from fastapi import  HTTPException

def get_course_or_404(courses: dict, course_id):
    # Найдите курс и обработайте отсутствие.
    course =  courses.get(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


#region УСЛОВИЕ ЗАДАЧИ
# Верните курс или поднимите 404
#
# HTTPException уже доступен, импорт не нужен. Реализуйте get_course_or_404(courses, course_id). Верните курс, а для неизвестного ID поднимите HTTPException(status_code=404, detail="Course not found").
#
# Проверка решения:
# procode имя_файла.py
#endregion