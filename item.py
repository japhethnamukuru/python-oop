class Item():
    # class attribute
    pay_rate = 0

    def __init__(self, name: str, price: float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

        # assertions
        assert price >= 0, f"{price} is not greater than or eqaul to 0"
        assert quantity >= 0, f"{quantity} is not greater thanor equal to 0"

    # get the price
    def getPrice(self):
        return self.price * self.pay_rate