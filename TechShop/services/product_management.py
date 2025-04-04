from database.db_connector import DatabaseConnector
from models.products import Products

class ProductManagementService:
    def __init__(self):
        self.db = DatabaseConnector()
        self.db.open_connection()

    def add_product(self):
        """Get product details from user and add to the database"""
        name = input("Enter Product Name: ")
        description = input("Enter Description: ")
        price = float(input("Enter Price: "))
        Products.add_product(self.db, name, description, price)

    def update_product(self):
        """Update product details"""
        product_id = int(input("Enter Product ID to update: "))
        new_price = input("Enter new price (press enter to skip): ")
        new_description = input("Enter new description (press enter to skip): ")

        new_price = float(new_price) if new_price else None
        new_description = new_description if new_description else None

        Products.update_product(self.db, product_id, new_price, new_description)

    def close_service(self):
        self.db.close_connection()
