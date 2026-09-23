# procode-task: CH-FIELD-VALIDATION-TASK3-SLUG@1


import re


def is_valid_slug(slug):
    if not isinstance(slug, str):
        return False
    pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$"
    if re.match(pattern, slug):
        return True
    else:
        return False



#region УСЛОВИЕ ЗАДАЧИ
# Проверьте формат slug
#
# Реализуйте is_valid_slug(slug).
# Функция должна вернуть True, если slug имеет допустимый формат, и False во всех остальных случаях.
# Разрешены только строчные латинские буквы, цифры и одиночные дефисы между непустыми группами.
# Примеры: fastapi-101 -> True, api -> True, FastAPI -> False, -api -> False, api--course -> False, api- -> False, None -> False.
#
# Проверка решения:
# procode имя_файла.py
#endregion