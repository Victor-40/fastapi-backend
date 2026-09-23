# procode-task: CH-FIELD-VALIDATION-TASK6-FIELD-SCHEMA@1
# from pydantic import BaseModel, Field
# from typing import Literal

class CourseCreate(BaseModel):
    title: str = Field(min_length=3, max_length=80)
    slug: str = Field(min_length=3, max_length=60, pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    level: Literal["beginner", "intermediate", "advanced"]
    price: float = Field(default=0, ge=0)



#region УСЛОВИЕ ЗАДАЧИ
# Опишите ограничения CourseCreate
#
# Объявите класс CourseCreate(BaseModel) с четырьмя полями:
#
# - title: str – строка длиной от 3 до 80 символов;
# - slug: str – строка длиной от 3 до 60 символов, соответствующая шаблону
#   r"^[a-z0-9]+(?:-[a-z0-9]+)*$";
# - level – одно из трёх значений: beginner, intermediate или advanced.
#   Тип поля задайте с помощью Literal;
# - price: float – цена со значением по умолчанию 0.
#   Цена не может быть меньше нуля.
#
# Для ограничений title, slug и price используйте Field.
# Необходимые импорты уже подготовлены.
#
# Проверка решения:
# procode имя_файла.py
#endregion