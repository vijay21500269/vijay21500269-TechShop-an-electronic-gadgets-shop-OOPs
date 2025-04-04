from models.exceptions import InvalidDataException

class Customers:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__address = address

    def get_customer_details(self):
        return f"ID: {self.__customer_id}, Name: {self.__first_name} {self.__last_name}, Email: {self.__email}, Phone: {self.__phone}, Address: {self.__address}"

    def update_customer_info(self, email=None, phone=None, address=None):
        if email and "@" not in email:
            raise InvalidDataException("Invalid email address.")
        if email:
            self.__email = email
        if phone:
            self.__phone = phone
        if address:
            self.__address = address
