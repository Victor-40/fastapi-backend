# procode-task: CH-APP-FOLDERS-TASK-PATH-TO-MODULE@1


name = input().strip()

if name in ["CourseLevel", "CourseRead", "LessonRead", "CourseCreate", "CourseUpdate"]:
    print("app/schemas.py")

elif name in ["COURSES", "LESSONS"]:
    print("app/data.py")

else:
    print("app/main.py")

# Напишите решение


#region УСЛОВИЕ ЗАДАЧИ
# Определите, куда переносится объект
#
# На вход подаётся имя одного объекта из CourseHub.
#
# В этом уроке:
#
# - CourseLevel, CourseRead, LessonRead, CourseCreate, CourseUpdate переносятся в app/schemas.py;
# - COURSES и LESSONS переносятся в app/data.py;
# - остальные имена пока остаются в app/main.py.
#
# Выведите путь к нужному файлу.
#
# Проверка решения:
# procode имя_файла.py
#endregion