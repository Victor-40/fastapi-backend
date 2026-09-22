# procode-task: CH-ERRORS-STATUS-CODES-TASK1-STATUS-FOR-CASE@1


def status_for_case(case):
    # Свяжите причину результата с HTTP-статусом.
    if case == "ok":
        return 200
    if case == "rule":
        return 400
    if case == "missing":
        return 404
    if case == "validation":
        return 422
    return None
    


#region УСЛОВИЕ ЗАДАЧИ
# Выберите статус по причине
#
# Реализуйте status_for_case(case).
#
# Используйте такие обозначения:
#
# - "ok" – запрос выполнен нормально;
# - "rule" – нарушено правило CourseHub;
# - "missing" – конкретный ресурс не найден;
# - "validation" – входные данные не прошли стандартную валидацию FastAPI.
#
# Верните соответственно 200, 400, 404 или 422.
#
# Для неизвестного значения верните None.
#
# Проверка решения:
# procode имя_файла.py
#endregion