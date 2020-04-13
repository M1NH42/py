# About : accumulator used with the string by using an empty string
# and using for loop iterate through and keep on accumulating

# take input form the user
s = input ("Enter string : ")

# empty string
ac = " "

# iterate through each character of the string given
for char in s :
    ac = ac + char + '_' + char + '_'

# print the final result
print(ac)