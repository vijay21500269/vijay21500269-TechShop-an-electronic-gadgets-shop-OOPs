import mysql.connector

class DatabaseConnector:
    def __init__(self):
        self.host = "localhost"  # Change if different
        self.user = "root"       # Update with your MySQL username
        self.password = "#vijaysql**"       # Update with your MySQL password
        self.database = "TechGadgetShop"  # Ensure the database exists

    def open_connection(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if conn.is_connected():
                print("✅ Database connected successfully!")
                return conn
            else:
                print("❌ Database connection failed!")
                return None
        except mysql.connector.Error as e:
            print(f"❌ Error connecting to database: {e}")
            return None

    def close_connection(self, conn):
        if conn:
            conn.close()
            print("🔒 Database connection closed.")
