from fastapi import Path, Body, APIRouter

category_router = APIRouter(prefix="/categories", tags=["Категория"])

fake_categories = [
    {"id": 1, "name": "Ресторан"},
    {"id": 2, "name": "Магазин"},
    {"id": 3, "name": "Еда"},
    {"id": 4, "name": "Кино"},
    {"id": 5, "name": "Развлечение"},
    {"id": 6, "name": "Отпуск"},
    {"id": 7, "name": "Переводы"},
    {"id": 8, "name": "Личные расходы"},
    {"id": 9, "name": "Транспорт"},
    {"id": 10, "name": "Спорт"},
]


@category_router.get("/",
            status_code=200,
            summary="Список категорий", )
def get_categories():
    return {"status": "ok", "data": fake_categories}


@category_router.get("/category/{category_id}",
            status_code=200,
            summary="Выбор категории")
def get_currency_id(category_id: int = Path(description="id категории")):
    current_category = [category for category in fake_categories if category["id"] == category_id][0]

    return {"status": "ok", "data": current_category}


@category_router.post("/category/",
             status_code=201,
             summary="Добавление новой записи категории")
def add_category(category_id: int = Body(description="id категории"),
                 name: str = Body(str, description="Название категории")):
    new_category = {"id": category_id, "name": name}
    fake_categories.append(new_category)

    return {"status": "ok", "data": new_category}


@category_router.patch("/category/{currency_id}",
              status_code=200,
              summary="Изменение данных категории")
def update_category(currency_id: int = Path( description="id валюты"),
                    name: str = Body(str, description="Название валюты")):
    category = [currency for currency in fake_categories if currency["id"] == currency_id][0]

    if category["name"]:
        category["name"] = name


    return {"status": "ok", "data": category}


@category_router.delete("/category/{category_id}",
                        status_code=204,
                        summary="Удаление записи категории")
def delete_currency(category_id: int = Path(description="id валюты")):
    category = [category for category in fake_categories if category["id"] == category_id][0]

    fake_categories.remove(category)
    # fake_currencies.pop(currency['id'])

    return {"status": "ok", "data": {}}
