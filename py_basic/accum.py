# About: Implementation of accumulator pattern using lists

# list iwth integer
nums = [3, 5, 8]

# An empty list
accum = []

# iterate and append in the empty list
for num in nums :

    # square and store in variable x
    x = num ** 2

    # append in accumulator list
    accum.append( x )

    # prints at every iteration
    print("After iteration: ", accum)

# prints the accum list after squaring and appending
print("Final list: ", accum)