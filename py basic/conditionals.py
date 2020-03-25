# in this program we will implement conditional operations
# available in python 3

first_num = input("Enter a number: ")
first_num = int(first_num)

second_num = input("Enter another number: ")
second_num = int(second_num)

if first_num > second_num :
    print(first_num, "is greater")
    
elif first_num < second_num :
    print(first_num, "is smaller")

else :
    print("Both the numbers are equal")