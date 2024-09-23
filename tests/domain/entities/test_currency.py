from src.domain.entities.currency import Currency

data = {"id": 1, "code": "USD", "name": "US Dollar", "symbol": "$"}


def test_currency_creation():
    currency = Currency(**data)

    assert currency.id == data.get("id")
    assert currency.code == data.get("code")
    assert currency.name == data.get("name")
    assert currency.symbol == data.get("symbol")


def test_currency_from_dict():
    currency = Currency.from_dict(data=data)

    assert currency.id == data.get("id")
    assert currency.code == data.get("code")
    assert currency.name == data.get("name")
    assert currency.symbol == data.get("symbol")


def test_currency_to_dict():
    currency = Currency.from_dict(data=data)
    assert currency.to_dict() == data


def test_currency_equality():
    currency1 = Currency.from_dict(data=data)
    currency2 = Currency.from_dict(data=data)
    assert currency1 == currency2
