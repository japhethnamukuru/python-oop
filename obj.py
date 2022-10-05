from item import Item

item1 = Item("phone", 1000)
item1.pay_rate = 0.7
print("Buy this phone at {}, with a discount of 30%".format(item1.getPrice()))