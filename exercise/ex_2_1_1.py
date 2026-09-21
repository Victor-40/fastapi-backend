# procode-task: CH-PYCHARM-SETUP-TASK1-FIND-PYTHON-312@1


def find_python_312(entries):
    # Найдите первую запись с маркером -V:3.12.
    for item in entries:
        if "-V:3.12" in item:
            return item
    else:
        return None

#region УСЛОВИЕ ЗАДАЧИ
# Найдите Python 3.12
#
# Реализуйте find_python_312(entries).
#
# Функция получает список строк, похожих на вывод py -0p, и должна вернуть первую строку, содержащую маркер версии -V:3.12.
#
# Если такой строки нет, верните None.
#
# Проверка решения:
# procode имя_файла.py
#endregion