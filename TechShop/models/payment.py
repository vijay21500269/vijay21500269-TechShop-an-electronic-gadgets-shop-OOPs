from models.exceptions import PaymentFailedException

class Payment:
    def __init__(self, payment_id, order, amount, status="Pending"):
        self.__payment_id = payment_id
        self.__order = order
        self.__amount = amount
        self.__status = status

    def process_payment(self, success=True):
        if success:
            self.__status = "Completed"
        else:
            raise PaymentFailedException("Payment was declined.")
