# procode-task: CH-SERVICE-LAYER-TASK-SERVICE-CALL@1


@router.get("/{course_id}", response_model=CourseRead)
def get_course(
    course_id: int,
    service: CourseService = Depends(get_course_service),
) -> CourseRead:
    return service.get_course(course_id)


#region УСЛОВИЕ ЗАДАЧИ
# Получите сервис через Depends
#
# router, Depends, CourseService, CourseRead и get_course_service уже подготовлены.
#
# Допишите endpoint GET /{course_id}.
#
# Функция должна иметь сигнатуру:
#
#
# def get_course(
#     course_id: int,
#     service: CourseService = Depends(get_course_service),
# ) -> CourseRead:
#
#
# Внутри функции не ищите курс самостоятельно. Передайте course_id в service.get_course(course_id) и верните результат.
#
# Важно: в Depends передаётся get_course_service без скобок.
#
# Проверка решения:
# procode имя_файла.py
#endregion