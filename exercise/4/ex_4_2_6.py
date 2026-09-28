# procode-task: CH-APIROUTER-TASK-INCLUDE-ROUTERS@1


app.include_router(system_router)
app.include_router(courses_router)
app.include_router(lessons_router)


# Подключите три роутера


#region УСЛОВИЕ ЗАДАЧИ
# Подключите роутеры к приложению
#
# Объекты app, system_router, courses_router и lessons_router уже созданы.
#
# Подключите все три роутера через app.include_router(...) в таком порядке:
#
# 1. system_router;
# 2. courses_router;
# 3. lessons_router.
#
# Проверка решения:
# procode имя_файла.py
#endregion