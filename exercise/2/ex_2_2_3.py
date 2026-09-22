# procode-task: CH-COURSEHUB-START-TASK3-ROUTE-LABEL@1


def route_label(method: str, path: str):
    # Нормализуйте метод и путь.
    method = method.upper()
    if not path.startswith("/"):
        path = "/" + path
    return f"{method} {path}"


#region УСЛОВИЕ ЗАДАЧИ
# Соберите обозначение маршрута
#
# Реализуйте route_label(method, path). Метод приведите к верхнему регистру. Если путь не начинается с /, добавьте его в начало. Пустой путь должен превратиться в /.
#
# Верните строку вида GET /health.
#
# Проверка решения:
# procode имя_файла.py
#endregion