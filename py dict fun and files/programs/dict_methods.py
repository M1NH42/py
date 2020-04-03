# ABOUT : In this program we will implement some of the important methods
#         we can use with dictionary data structure in python 3


# initiaize a dictionary
inventory = {'apples': 122, 'oranges': 321, 'bananas': 30, 'grapes': 455}

# iterate through the inventory dictionary
for key in inventory:
    print(key, 'got value: ', inventory[key])

# convert the keys and store into a list
boom = list(inventory)

# prints the list
print(boom)

# return values from dictionary
print(inventory.values())

# return tuple of the dictionary items
# which means return the (key, value) pair
print(inventory.items())

# 'in' keyword returns a boolean value
print('bananas' in inventory) # return true
print('cherries' in inventory) # return false

# get('key') return the value linked to that key
print(inventory.get('bananas'))

# if key is not present then it return "None"
# we can also make a default value by passing
# a second variable as a default value
print(inventory.get('cherries', 0))