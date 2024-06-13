class Product:
    _discount = 0  # защищенный атрибут класса для хранения процента скидки при акциях

    def __init__(self, name, price):
        self.name = name
        self._price = price  # защищенный атрибут объекта для хранения цены товара

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price > 0:
            self._price = price

    @classmethod
    def get_discount(cls):
        return cls._discount

    @classmethod
    def set_discount(cls, discount):
        if discount > 0:
            cls._discount = discount

    @property
    def current_price(self):
        return self._price * (1 - self._discount / 100)

    @staticmethod
    def create_fix_price(name):
        return Product(name, 99)

    def __str__(self):
        return f"Product(name={self.name}, price={self._price})"
