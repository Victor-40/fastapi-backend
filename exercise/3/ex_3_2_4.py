# procode-task: CH-REQUEST-BODY-TASK4-COURSE-CREATE-MODEL@1


class CourseCreate(BaseModel):
    title: str
    slug: str
    level: str
    price: float = 0

#region УСЛОВИЕ ЗАДАЧИ
# Опишите входную модель CourseCreate
#
# Объявите CourseCreate(BaseModel) с полями:
#
# - title: str
# - slug: str
# - level: str
# - price: float = 0
#
# Поля id в модели быть не должно.
#
# Проверка решения:
# procode имя_файла.py
#endregion