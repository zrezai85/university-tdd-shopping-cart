from abc import ABC, abstractmethod


class ProductInterface(ABC):
    @abstractmethod
    def get_price(self):
        pass


class Book(ProductInterface):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total):
        pass


class NoDiscount(DiscountStrategy):
    def apply(self, total):
        return total


class ShoppingCart:
    def __init__(self, discount_strategy=None):
        self.products = []
        self.discount_strategy = (
            discount_strategy or NoDiscount()
        )

    def add_product(self, product):
        self.products.append(product)

    def total(self):
        subtotal = sum(
            product.get_price()
            for product in self.products
        )
        return self.discount_strategy.apply(subtotal)
