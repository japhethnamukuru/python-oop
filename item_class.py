import csv

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

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for new_item in items:
            # print(new_item)
            Item(
                name = new_item.get('item'),
                price = float(new_item.get('price')),
                quantity = int(new_item.get('quantity'))
            )

    #  satic method
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # represent objects
    def __repr__(self) -> str:
        return f"{self.name}, {self.price}, {self.quantity}"

# Item.instantiate_from_csv()
print(Item.is_integer(2.0))