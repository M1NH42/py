# in this program we will implement conditional operations
# available in python 3

# ask user to enter first number
first_num = input("Enter a number: ")

# typecast to int data type
first_num = int(first_num)

# ask user to enter second number
second_num = input("Enter another number: ")

# typecast to int data type
second_num = int(second_num)

# check if first number is greater or not
# if greater print the indented statement
if first_num > second_num :
    print(first_num, "is greater")

# elif: else if only
# checks the condition
# if true execute statement
elif first_num < second_num :
    print(first_num, "is smaller")

# if above two conditions are not true then execute this else statement
else :
    print("Both the numbers are equal")