import pytest
from src.item import Item

@pytest.fixture
def phone():
    return Item("телефон", 100000, 2)


def test_item_init(phone):
    assert phone.calculate_total_price() == 200000

def test_discount(phone):
    Item.pay_rate = 1.5
    assert phone.apply_discount() == 150000




