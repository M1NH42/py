# ABOUT : This programdeals with the dictionary
#         which special python built-in mapping
#         type that contain a (key, value) pair
#         * unordered
#         * associative collection

# declare an empty dictionary
eng2sp = {}

# store 'uno' to key 'one'
eng2sp['one'] = 'uno'

# link '' to key ''
eng2sp['two'] = 'dos'

# link value 'tres' to key 'three'
eng2sp['three'] = 'tres'

# print the dictionary
print(eng2sp)

# new dictionary definition
new_dictionary = {'gold': 12, 'silver': 21, 'bronze': 23}

# print dictionary
print(new_dictionary)

# assign (key, value) to a variable
medal = new_dictionary['silver']

# print variable value
print(medal)

# delete an element
del new_dictionary['bronze']

# after deletion
print("*****After Deletion*****")

# print after delting a pair
print(new_dictionary)

print("*****After Updation*****")

new_dictionary['silver'] += 10

# prints dictionary after declaration
print(new_dictionary)

# INFO: This will print the dictionary elements in an unorderd format
# which changes every time we run the program

# working of len() of the python 3 module

# prints length of the dictionary
# which means it will print the number of
# key value pair present in the dictionary
print(len(new_dictionary))