from item_class import Item

# creating the child class
class Phone(Item):

    # inheritting the parent attributes via init
    def __init__(self, name: str, price: float, quantity=0):
        super().__init__(name, price, quantity)
        self.broken = 0


phone1 = Phone('samsung', 100, 7)
print(Phone.all)
print(Item.all)