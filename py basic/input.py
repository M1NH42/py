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

# prints a boundary line
# print("**************************************")

# calculate average of two numbers
avg = add (first_number, second_number) / 2

# prints a boundary line
print("**************************************")

# prints average of two numbers
print ("Average of two numbers:",avg)

# prints a boundary line
print("**************************************")

# prints addition of two numbers
print("Addition of two numbers:",add (first_number, second_number))

# prints a boundary line
print("**************************************")

# prints difference between two given numbers
print("Subtraction of two numbers:",sub(first_number, second_number))

# prints a boundary line
print("**************************************")

# prints multiplication of two numbers
print("Multiplication o ftwo numbers:",mul (first_number, second_number))

# prints a boundary line
print("**************************************")