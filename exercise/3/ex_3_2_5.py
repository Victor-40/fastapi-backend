# procode-task: CH-REQUEST-BODY-TASK5-POST-COURSE@1


@app.post("/courses", response_model=CourseRead, status_code=201)
def create_course(course_in: CourseCreate):
    return {
        "id": 1,
        **course_in.model_dump()
    }


#region УСЛОВИЕ ЗАДАЧИ
# Зарегистрируйте POST /courses
#
# Объекты app, CourseCreate и CourseRead подготовлены. 
# Создайте create_course(course_in: CourseCreate), зарегистрированную для POST /courses с response_model=CourseRead и status_code=201.
#
# Верните новый словарь с id=1 и данными из course_in.
#
# Проверка решения:
# procode имя_файла.py
#endregion