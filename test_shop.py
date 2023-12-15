"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    cart = Cart()
    return cart


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(10000) == False
        assert product.check_quantity(100) == True
        assert product.check_quantity(10000) == False
        assert product.check_quantity(0) == True

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(10)
        assert product.quantity == 990

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        product.buy(10)
        assert not product.quantity == 1001


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_pruducts(self, product, cart):
        cart.add_product(product, 5)
        assert cart.products[product] == 5

    def test_add_pruducts_negative_nubmer(self, product, cart):
        cart.add_product(product, -5)
        assert not cart.products[product] == 5

    def test_remove_pruducts(self, product, cart):
        cart.remove_product(product, 5)
        assert cart.products == {}

    def test_clear(self, product, cart):
        cart.add_product(product, 55)
        cart.clear()
        assert cart.products == {}

    def test_get_total_price(self, product, cart):
        cart.add_product(product, 5)
        cart.add_product(product, 10)
        exp_total_price = product.price * (5 + 10)

        actual_total_price = cart.get_total_price(product.price)

        assert actual_total_price == exp_total_price

    def test_buy(self, product, cart):
        cart.add_product(product, 5)
        cart.add_product(product, 10)
        cart.buy()
        assert product.quantity == 985

