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

# list
names = ["adam", "eve", "peter", "henry", "william"]

# ask user to enter a string
user_input = input("Enter a string to check: ")

# print boolean value after evaluation
print(user_input in names)


print("********************************")
## we'll perfrom for string 

# take as tring variable
s_t = "quarantine"

# ask user to enter a string
u_i = input("Enter a string : ")

# evaluatin sring with boolean expression
print(u_i in s_t)