# procode-task: CH-FIELD-VALIDATION-TASK2-TITLE@1


def is_valid_title(title):
    if isinstance(title, str) and len(title) in range(3, 81):
        return True
    else:
        return False 


#region УСЛОВИЕ ЗАДАЧИ
# Проверьте длину title
#
# Реализуйте is_valid_title(title).
#
# Верните True, если title – строка длиной от 3 до 80 символов включительно. Во всех остальных случаях верните False.
#
# Проверка решения:
# procode имя_файла.py
#endregion