# About : accumulator used with the string by using an empty string
# and using for loop iterate through and keep on accumulating

s = input ("Enter string : ")

ac = " "

for char in s :
    ac = ac + char + '_' + char + '_'

print(ac)