# procode-task: CH-PATH-PARAMS-TASK6-PRODUCT-ENDPOINT@1
# from fastapi import FastAPI, HTTPException

# app = FastAPI()
# PRODUCTS = {}

@app.get("/products/{product_id}", tags=["products"])
def get_product(product_id: int):
    product = PRODUCTS.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# Создайте endpoint каталога товаров.


#region УСЛОВИЕ ЗАДАЧИ
# Получите товар по ID
#
# app, HTTPException и словарь PRODUCTS уже доступны.
#
# Создайте маршрут:
#
#
# GET /products/{product_id}
#
#
# с тегом products.
#
# Функция:
#
#
# get_product(product_id: int)
#
#
# должна вернуть найденный товар. Если товара с таким ID нет, поднимите:
#
#
# HTTPException(status_code=404, detail="Product not found")
#
# Проверка решения:
# procode имя_файла.py
#endregion