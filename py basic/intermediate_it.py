# this programprints the intermediate result in loop
# using print statement we can easily know the values
# of the variables

# store numbers 0 to 9 in 'w'
w = range(10)

# assign 0 to tot
tot = 0

# print a message
print("***** Before the For Loop ******")

for num in w:
    print("***** A New Loop Iteration ******")
    print("Value of num:", num)
    tot += num
    print("Value of tot:", tot)

print("***** End of For Loop *****")

print("Final total:", tot)
