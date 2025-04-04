from database.db_connector import DatabaseConnector
from models.orders import Orders
from models.products import Products
from exceptions.customer_exceptions import InsufficientStockException
from datetime import datetime


class OrderManagementService:
    def __init__(self):
        self.db = DatabaseConnector()

    def place_order(self, customer, product, quantity):
        conn = self.db.open_connection()
        cursor = conn.cursor()

        # Check product stock
        cursor.execute("SELECT stock, price FROM products WHERE id = %s", (product.product_id,))
        result = cursor.fetchone()
        if not result:
            raise ValueError("Product not found.")

        stock, price = result
        if stock < quantity:
            raise InsufficientStockException("Not enough stock available.")

        # Calculate total price
        total_price = price * quantity

        # Insert order into the database
        cursor.execute(
            "INSERT INTO orders (customer_id, order_date, total_price) VALUES (%s, %s, %s)",
            (customer.customer_id, datetime.now(), total_price)
        )
        order_id = cursor.lastrowid  # Get the generated order ID

        # Update product stock
        new_stock = stock - quantity
        cursor.execute("UPDATE products SET stock = %s WHERE id = %s", (new_stock, product.product_id))

        conn.commit()
        self.db.close_connection()

        return f"Order placed successfully! Order ID: {order_id}, Total: {total_price}"

