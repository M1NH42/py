# About : In this we'll implement the listner loop
# also known as while loop as shown

# init sum
theSum = 0

# init x
x = -1

# while loop to iterate
# checks if x equals 0 or not
while (x != 0):
    # Message to enter a number
    x = int(input("next number to add up (enter 0 if no more numbers): "))
    # update sum
    theSum = theSum + x
# prints sum
print(theSum)