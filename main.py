from product.py import Product

if __name__ == '__main__':
    # Создание экземпляра товара
    product1 = Product("Apple", 100)
    print(product1)

    # Изменение цены товара
    product1.set_price(120)
    print(f"Updated price: {product1.get_price()}")

    # Установка и получение скидки
    Product.set_discount(10)
    print(f"Discount: {Product.get_discount()}%")

    # Цена товара с учетом скидки
    print(f"Current price with discount: {product1.current_price}")

    # Создание товара с фиксированной ценой
    product2 = Product.create_fix_price("Banana")
    print(product2)
