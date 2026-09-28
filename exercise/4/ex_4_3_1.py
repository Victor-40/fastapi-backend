# procode-task: CH-SERVICE-LAYER-TASK1@1


import json

q = json.loads(input())

if q is None:
    print(json.dumps(q))
else:
    q_norm = q.strip().lower()
    if len(q_norm) < 2:
        print(json.dumps("too_short"))
    else:
        print(json.dumps(q_norm))

# Напишите решение


#region УСЛОВИЕ ЗАДАЧИ
# Нормализуйте поисковый запрос
#
# На вход подаётся одно JSON-значение: строка или null.
#
# Если пришёл null, выведите null.
#
# Для строки:
#
# - уберите пробелы по краям через strip();
# - приведите строку к нижнему регистру;
# - если после этого длина меньше 2 символов, выведите строку "too_short";
# - иначе выведите нормализованную строку.
#
# Результат выведите как JSON.
#
# Это упрощённая отдельная тренировка логики, которая затем используется в CourseService.list_courses().
#
# Проверка решения:
# procode имя_файла.py
#endregion