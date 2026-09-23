# procode-task: CH-FIELD-VALIDATION-TASK4-PRICE@1


def is_valid_price(price):
    if isinstance(price, bool):
        return False
    if (isinstance(price, int) or isinstance(price, float)) and price >= 0:
        return True
    else:
        return False


# print(is_valid_price(1))

#region УСЛОВИЕ ЗАДАЧИ
# Проверьте цену
#
# Реализуйте is_valid_price(price).
#
# В этой упрощённой ручной проверке цена должна иметь тип int или float и быть не меньше нуля. Значения bool ценой не считаются.
#
# Это обычная Python-проверка. Pydantic при работе с моделью может дополнительно преобразовывать совместимые входные значения.
#
# Проверка решения:
# procode имя_файла.py
#endregion