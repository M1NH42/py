# About: Implementation of the accumulator program
# in python 3 specialization

# ask to enter string
phrase = input("Enter a string: ")

# initialize total variable with zero
tot = 0

# iterate through the string
for char in phrase :
    if char != " " :
        tot += 1

# print the result
print(tot)