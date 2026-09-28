# procode-task: CH-APP-FOLDERS-TASK-PACKAGE-FILES@1


import json

files = json.loads(input())

reqs = [
"app/__init__.py",
"app/data.py",
"app/main.py",
"app/schemas.py"]

result = []
for path in reqs:
    if path not in files:
        result.append(path)

print(json.dumps(result,separators=(",", ":")))

# Напишите решение


#region УСЛОВИЕ ЗАДАЧИ
# Найдите отсутствующие файлы после рефакторинга
#
# После этого урока в папке app должны находиться:
#
#
# app/__init__.py
# app/data.py
# app/main.py
# app/schemas.py
#
#
# На вход подаётся одна строка с JSON-массивом существующих путей.
#
# Выведите JSON-массив отсутствующих файлов в указанном выше порядке.
#
# Проверка решения:
# procode имя_файла.py
#endregion