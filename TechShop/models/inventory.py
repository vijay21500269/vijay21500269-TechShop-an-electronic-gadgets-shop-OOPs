class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock):
        self.__inventory_id = inventory_id
        self.__product = product
        self.__quantity_in_stock = quantity_in_stock

    def remove_from_inventory(self, quantity):
        if quantity > self.__quantity_in_stock:
            raise InsufficientStockException("Not enough stock available.")
        self.__quantity_in_stock -= quantity

    def is_product_available(self, quantity_to_check):
        return self.__quantity_in_stock >= quantity_to_check
