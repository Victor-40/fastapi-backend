# procode-task: CH-SERVICE-LAYER-TASK-NORMALIZE-QUERY@1


import json

data = json.loads(input())

courses: list = data["courses"]
level: str|None = data["level"]
q: str|None = data["q"]

result = courses.copy()
if level is not None:
    result = [course for course in result if course["level"].lower() == level.lower()]

if q is not None:
    q = q.strip().lower()
    if len(q) < 2:
        print(json.dumps("too_short"))
    else:
        result = [course for course in result if q in course["title"].lower()] 

        print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
else:
    print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))

# Напишите решение


#region УСЛОВИЕ ЗАДАЧИ
# Отфильтруйте курсы как в сервисе
#
# На вход подаётся одна строка с JSON-объектом:
#
# - courses – список курсов;
# - level – уровень курса или null;
# - q – поисковая строка или null.
#
# Примените правила из CourseService.list_courses():
#
# 1. если level не равен null, оставьте курсы с таким уровнем без учёта регистра;
# 2. если q не равен null, выполните strip().lower();
# 3. если нормализованный q короче 2 символов, выведите JSON-строку "too_short";
# 4. иначе оставьте курсы, в названии которых встречается q без учёта регистра.
#
# Если ошибок нет, выведите итоговый список как JSON. Исходный список менять не нужно.
#
# В настоящем CourseHub слишком короткий q приводит к 400 Bad Request. Здесь проверяется сама логика фильтрации, поэтому вместо HTTP-ошибки используется строка "too_short".
#
# Проверка решения:
# procode имя_файла.py
#endregion