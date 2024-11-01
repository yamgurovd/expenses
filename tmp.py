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


def st_add(currency_id: int,
           name: str,
           unit: float):
    currency = {"id": currency_id, "name": name, "unit": unit}

    fake_currencies.append(currency)

    print(fake_currencies)

    return currency


def st(currency_id):
    currency = [currency for currency in fake_currencies if currency["id"] == currency_id][0]
    return currency


tmp1 = st_add(77, "test 123", 11.1)

print(tmp1)

tmp = st(77)
print(tmp)
