class Item():
    # class attribute
    pay_rate = 0
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # validations
        assert price >= 0, f"{price} is not greater than or eqaul to 0"
        assert quantity >= 0, f"{quantity} is not greater thanor equal to 0"  

        #assign parameters to the variables
        self.name = name
        self.price = price
        self.quantity = quantity

        #actions
        Item.all.append(self)


    # get the price
    def getPrice(self):
        return self.price * self.pay_rate

    # represent objects
    def __repr__(self) -> str:
        return f"{self.name}, {self.price}, {self.quantity}"