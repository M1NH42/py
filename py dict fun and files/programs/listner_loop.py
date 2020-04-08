# About : In this we'll implement the listner loop
# also known as while loop as shown

theSum = 0
x = -1
while (x != 0):
    x = int(input("next number to add up (enter 0 if no more numbers): "))
    theSum = theSum + x
print(theSum)