from database.db_connector import DatabaseConnector
from models.exceptions import InsufficientStockException, InvalidDataException


class OrderProcessingService:
    def __init__(self):
        self.db = DatabaseConnector()
        self.db.open_connection()

    def place_order(self, customer_id, product_id, quantity):
        cursor = self.db.connection.cursor()

        # Check product stock
        cursor.execute("SELECT QuantityInStock FROM inventory WHERE ProductID = %s", (product_id,))
        stock = cursor.fetchone()

        if not stock or stock[0] < quantity:
            raise InsufficientStockException("Not enough stock available.")

        # Get product price
        cursor.execute("SELECT Price FROM products WHERE ProductID = %s", (product_id,))
        product_price = cursor.fetchone()[0]
        total_price = product_price * quantity

        # Insert into orders table
        cursor.execute("INSERT INTO orders (CustomerID, OrderDate, TotalAmount) VALUES (%s, NOW(), %s)",
                       (customer_id, total_price))
        self.db.connection.commit()
        order_id = cursor.lastrowid

        # Insert into order details
        cursor.execute("INSERT INTO order_details (OrderID, ProductID, Quantity) VALUES (%s, %s, %s)",
                       (order_id, product_id, quantity))
        self.db.connection.commit()

        # Update inventory
        cursor.execute("UPDATE inventory SET QuantityInStock = QuantityInStock - %s WHERE ProductID = %s",
                       (quantity, product_id))
        self.db.connection.commit()

        print("Order placed successfully!")
        cursor.close()

    def close(self):
        self.db.close_connection()
