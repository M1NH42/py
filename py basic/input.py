## This program show how to take input from the user

# addition function
def add(x, y):
    return x + y

# subtraction function
def sub(x, y):
    return x - y

# division function
def div(x, y) :
    return x / y

# multiplication function
def mul (x, y) :
    return x * y

# prints message to enter firts number
x = input("Enter first number: ")

# type casting 'x' because input takes as string
# so we need to type cast the input to perform
# different operations
first_number = int(x)

# prints message to enter second number
y = input("Enter second number: ")

# type casting 'x' because input takes as string
# so we need to type cast the input to perform
# different operations
second_number = int(y)

# calculate average of two numbers
avg = add (first_number, second_number) / 2

# prints average of two numbers
print (avg)

# prints addition of two numbers
print(add (first_number, second_number))

# prints difference between two given numbers
print(sub(first_number, second_number))

# prints multiplication of two numbers
print(mul (first_number, second_number))