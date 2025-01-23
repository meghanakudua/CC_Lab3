#OPTIMIZED CODE
from products import dao
from typing import List, Optional


class Product:
    def _init_(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: dict) -> "Product":
        return Product(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            cost=data['cost'],
            qty=data['qty']
        )


def list_products() -> List[Product]:
    """
    Returns a list of all products.
    """
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Optional[Product]:
    """
    Fetches a product by its ID. Returns None if the product doesn't exist.
    """
    product_data = dao.get_product(product_id)
    return Product.load(product_data) if product_data else None


def add_product(product: dict):
    """
    Adds a new product to the inventory.
    """
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """
    Updates the quantity of a specific product.
    """
    if qty < 0:
        raise ValueError("Quantity cannot be negative")
    dao.update_qty(product_id, qty)


    
'''from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    def load(data):
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    products = dao.list_products()
    result = []
    for product in products:
        result.append(Product.load(product))
    
    return result



def get_product(product_id: int) -> Product:
    return Product.load(dao.get_product(product_id))


def add_product(product: dict):
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)
'''


