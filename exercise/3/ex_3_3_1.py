# procode-task: CH-FIELD-VALIDATION-TASK1-LEVEL@1


def is_valid_level(level):
    valid_values = ["beginner", "intermediate", "advanced"]
    if level in valid_values:
        return True
    else:
        return False


#region УСЛОВИЕ ЗАДАЧИ
# Проверьте допустимое значение уровня
#
# Реализуйте is_valid_level(level). В этой упрощённой проверке допустимы только beginner, intermediate и advanced.
#
# Верните True, если значение входит в этот набор, иначе False.
#
# Проверка решения:
# procode имя_файла.py
#endregion