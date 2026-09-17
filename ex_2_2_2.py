# procode-task: CH-COURSEHUB-START-TASK2-STRING-RESPONSE@1


def is_string_response(payload):
    # Проверьте словарь, его ключи и значения.
    if not isinstance(payload, dict):
        return False
    for key, value in payload.items():
        if not isinstance(key, str) or not isinstance(value, str):
            return False
    return True


#region УСЛОВИЕ ЗАДАЧИ
# Проверьте типы данных ответа
#
# Реализуйте is_string_response(payload).
#
# Функция должна вернуть True, если payload – словарь, в котором все ключи и значения являются строками.
#
# Пустой словарь также считается подходящим.
#
# Для остальных данных верните False.
#
# Проверка решения:
# procode имя_файла.py
#endregion