# procode-task: CH-REQUEST-BODY-TASK3-CREATE-RECORD@1


def build_course(course_id, course_in):
    return {
        "id": course_id,
        **course_in.model_dump()
    }


#region УСЛОВИЕ ЗАДАЧИ
# Соберите запись нового курса
#
# Реализуйте build_course(course_id, course_in). course_in – объект CourseCreate.
#
# Верните новый словарь: сначала поле id, затем все данные из course_in. Исходный объект изменять нельзя.
#
# Проверка решения:
# procode имя_файла.py
#endregion