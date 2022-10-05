#!/usr/bin/python3

# test file for looping a dict item and fetch keys via the dict.get.method

dict_list = []

new_dict = {'name':'phone', 'price': 100, 'quantity': 10}

def create_list(new_dict):
    for i in range(6):
        dict_list.append(new_dict)
    return dict_list

create_list(new_dict)
#print(dict_list)

for item in dict_list:
    key = item.get('name')
    # print(key)

def getInt(num):
    if isinstance(num, int):
        return True
    elif isinstance(num, float):
        return False
    else:
        return False

active = True
while active:
    num = input("Enter a value: ")
    if num:
        if num =='q':
            active = False
        else:
            num = int(num)
            print(getInt(num))


# print(getInt(2))