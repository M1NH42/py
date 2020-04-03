# ABOUT : In this program we will implement some of the important methods
#         we can use with dictionary data structure in python 3

inventory = {'apples': 122, 'oranges': 321, 'bananas': 30, 'grapes': 455}

for key in inventory:
    print(key, 'got value: ', inventory[key])

boom = list(inventory)
print(boom)

print(inventory.values())

print(inventory.items())