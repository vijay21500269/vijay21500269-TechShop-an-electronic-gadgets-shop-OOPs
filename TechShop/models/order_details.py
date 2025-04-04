from exceptions.customer_exceptions import InvalidDataException

class OrderDetails:
    def __init__(self, order_detail_id, order, product, quantity):
        if quantity <= 0:
            raise InvalidDataException("Quantity must be positive.")
        self.__order_detail_id = order_detail_id
        self.__order = order
        self.__product = product
        self.__quantity = quantity

    def calculate_subtotal(self):
        return self.__quantity * self.__product.get_price()  # Assuming get_price() exists in Products

    def update_quantity(self, new_quantity):
        if new_quantity <= 0:
            raise InvalidDataException("Quantity must be positive.")
        self.__quantity = new_quantity
