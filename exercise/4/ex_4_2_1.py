# procode-task: CH-APIROUTER-TASK1-BUILD-ROUTE-PATH@1


prefix = input().strip()
route_path = input().strip()


if not prefix and not route_path:
    print("/")
else:
    print(f"{prefix}{route_path}")

# Напишите решение


#region УСЛОВИЕ ЗАДАЧИ
# Соберите полный путь endpoint
#
# На вход подаются две строки:
#
# - prefix роутера;
# - route_path – путь операции из декоратора.
#
# В этой задаче prefix либо пустой, либо начинается с / и не заканчивается им. route_path либо пустой, либо начинается с /.
#
# Соберите полный URL так же, как в примерах урока: /courses + /{course_id} даёт /courses/{course_id}.
#
# Важно: путь "/" не равен пустой строке. Например, /courses + / даёт /courses/.
#
# Если обе строки пустые, выведите /.
#
# Проверка решения:
# procode имя_файла.py
#endregion