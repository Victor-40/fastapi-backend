# procode-task: CH-ERRORS-STATUS-CODES-TASK3-VALIDATE-SEARCH@1

# from fastapi import HTTPException, status


def validate_search(q):
    # Нормализуйте q и проверьте минимальную длину.
    if q is None:
        return None
    q = q.strip().lower()
    if len(q) < 2:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Search query must contain at least 2 characters")
    return q



#region УСЛОВИЕ ЗАДАЧИ
# Поднимите 400 для короткого поиска
#
# HTTPException и status уже доступны. Реализуйте validate_search(q). Для None верните None. Нормализуйте строку через strip().lower(). 
# Если длина нормализованной строки меньше двух символов, поднимите HTTPException со статусом 400 и detail Search query must contain at least 2 characters. Иначе верните нормализованную строку.
#
# Проверка решения:
# procode имя_файла.py
#endregion