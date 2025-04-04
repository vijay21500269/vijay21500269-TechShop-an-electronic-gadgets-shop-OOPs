from database.db_connector import DatabaseConnector
from models.exceptions import InvalidDataException

class CustomerService:
    def __init__(self):
        self.db = DatabaseConnector()
        self.db.open_connection()

    def register_customer(self, first_name, last_name, email, phone, address):
        cursor = self.db.connection.cursor()

        # Check if email already exists
        cursor.execute("SELECT * FROM customers WHERE Email = %s", (email,))
        if cursor.fetchone():
            raise InvalidDataException("Email already registered.")

        # Insert new customer record
        query = "INSERT INTO customers (FirstName, LastName, Email, Phone, Address) VALUES (%s, %s, %s, %s, %s)"
        values = (first_name, last_name, email, phone, address)

        try:
            cursor.execute(query, values)
            self.db.connection.commit()
            print("Customer registered successfully!")
        except Exception as e:
            print(f"Error registering customer: {e}")
        finally:
            cursor.close()

    def close(self):
        self.db.close_connection()
