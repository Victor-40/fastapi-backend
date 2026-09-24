# procode-task: CH-SCHEMA-SEPARATION-TASK2-CREATE-FIELDS@1


import json

payload = json.loads(input())
fields = ["title", "slug", "level", "price"]
result = {}
for field in fields:
    if field in payload:
        value = payload[field]
        result[field] = value

print(json.dumps(result), sep=None)

# print("a", sep=None)
# Напишите решение


#region УСЛОВИЕ ЗАДАЧИ
# Отделите поля создания
#
# На вход подаётся одна строка с JSON-объектом – данные, которые клиент прислал для создания курса.
#
# Сформируйте новый словарь только из разрешённых полей:
#
#
# title
# slug
# level
# price
#
#
# Если какого-то из этих полей нет во входных данных, добавлять его в результат не нужно. Поле id и любые другие лишние поля игнорируйте.
#
# Поля в результате должны идти в порядке: title, slug, level, price.
#
# Выведите получившийся словарь как JSON в одну строку без лишних пробелов. Для работы с JSON можно использовать json.loads() и json.dumps().
#
# Проверка решения:
# procode имя_файла.py
#endregion