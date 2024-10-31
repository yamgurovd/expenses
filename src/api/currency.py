from fastapi import Path, Body, Query, APIRouter

router = APIRouter(prefix="/currency", tags=["Валюта"])

fake_currencies = [
    {"id": 1, "name": "USD", "unit": 123.00},
    {"id": 2, "name": "EUR", "unit": 456.10},
    {"id": 3, "name": "JPY", "unit": 987.232},
    {"id": 4, "name": "GBP", "unit": 13.23},
    {"id": 5, "name": "CNY", "unit": 234.03},
    {"id": 6, "name": "RUB", "unit": 345.00},
    {"id": 7, "name": "AUD", "unit": 988.23},
    {"id": 8, "name": "NZD", "unit": 345.00},
    {"id": 9, "name": "CHF", "unit": 988.23},
    {"id": 10, "name": "SEK", "unit": 345.00},
]


@router.get("/currencies",
            status_code=200,
            summary="Список валют", )
def get_currencies():
    return {"status": "ok", "data": fake_currencies}


@router.get("/{currency_id}",
            status_code=200,
            summary="Выбор волюты")
def get_currency_id(currency_id: int = Path(description="id валюты")):
    currency = [currency for currency in fake_currencies if currency["id"] == currency_id][0]

    return {"status": "ok", "data": currency}


@router.post("/{currency_id}",
             status_code=201,
             summary="Дабавление новой записи валюты")
def add_currency(currency_id: int = Path(description="id валюты"),
                 name: str = Query(str, description="Название валюты"),
                 unit: float = Query(float, description="Единица")):
    currency = [
        {"id": currency_id, "name": name, "unit": unit}
    ]

    return {"status": "ok", "data": fake_currencies + currency}


@router.patch("/{currency_id}",
              status_code=200,
              summary="Изменение данные валюты")
def update_currency(currency_id: int = Path(description="id валюты"),
                    name: str = Query(str, description="Название валюты"),
                    unit: float = Query(float, description="Единица")):
    currency = [currency for currency in fake_currencies if currency["id"] == currency_id][0]

    if name:
        currency.name = name
    elif unit:
        currency.unit = unit
    else:
        return {"status": "ok", "data": fake_currencies}


@router.delete("/{currency_id}",
               status_code=204,
               summary="Удаление записи валюты")
def delete_currency(currency_id: int = Path(description="id валюты")):
    currency = [currency for currency in fake_currencies if currency["id"] == currency_id][0]

    return {"status": "ok", "data": fake_currencies.pop(currency['id'])}
