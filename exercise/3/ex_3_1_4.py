# procode-task: CH-RESPONSE-MODELS-TASK4-COURSE-READ-MODEL@1
# from pydantic import BaseModel

class CourseRead(BaseModel):
    id: int 
    title: str 
    slug: str 
    level: str 
    price: float


#region УСЛОВИЕ ЗАДАЧИ
# Опишите модель CourseRead
#
# Объявите класс CourseRead(BaseModel) с полями id: int, title: str, slug: str, level: str, price: float. Импорты уже подготовлены.
#
# Все пять полей должны быть обязательными. Значения по умолчанию задавать не нужно.
#
# Проверка решения:
# procode имя_файла.py
#endregion