# procode-task: CH-SERVICE-LAYER-TASK-FIND-COURSE@1


class CourseService:
    def get_course(self, course_id: int) -> CourseRead:
        pass


#region УСЛОВИЕ ЗАДАЧИ
# Реализуйте CourseService.get\_course()
#
# Объекты COURSES, CourseRead, HTTPException и status уже подготовлены.
#
# Допишите метод get_course(self, course_id) класса CourseService:
#
# 1. найдите курс через COURSES.get(course_id);
# 2. если курс не найден, выбросьте HTTPException со статусом 404 и текстом "Course not found";
# 3. если курс найден, верните CourseRead(course).
#
# Импорты писать не нужно.
#
# Проверка решения:
# procode имя_файла.py
#endregion