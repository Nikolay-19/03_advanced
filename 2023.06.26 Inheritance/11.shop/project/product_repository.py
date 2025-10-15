from typing import Optional

from project.product import Product


class ProductRepository:
    products = []

    def add(self, product):
        ProductRepository.products.append(product)

    def find(self, product_name: str) -> Optional[Product]:
        result = [product for product in self.products if product.name == product_name]
        if result:
            return result[0]

    def remove(self, product_name):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        result = []
        for product in ProductRepository.products:
            result.append(f"{product.name}: {product.quantity}")
        return "\n".join(str(el) for el in result)
