# we will be working with boolean expression in python 3
# we'll different types to evaluate boolean expression
# eg:
# * and
# * or 
# * not
# * in
# * not in

x = 32
# prints boolean result
print(x >= 32 or x <= 50)

print(x != x)

print(not x)


print("********************************")
## we'll perfrom "in" in list to evaluate boolean expression

# list of strings
names = ["adam", "eve", "peter", "henry", "william"]

# list of integer values
numbers = [1, 2, 3, 4, 5, 6, 7, 0, 8]

# ask user to enter a string
user_input = input("Enter a string to check: ")

# print boolean value after evaluation
print(user_input in names)

print("********************************")
# evaluate numbers
number = input("Enter a number")

number = int(number)

print(number in numbers)

print("********************************")
## we'll perfrom for string 

# take as string variable
s_t = "quarantine"

# ask user to enter a string
u_i = input("Enter a string : ")

# evaluatin sring with boolean expression
print(u_i in s_t)