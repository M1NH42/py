# About : In this program we will se the scope resolution of variable
# * global variable
# * local variable

# Define square funcions
def square(num) :
    sq = num * num
    return sq

# Add sum of square fxn
def sum_of_square(fn, sn, tn) :
    x = square(fn) # called square function
    y = square(sn) # called square function
    z = square(tn) # called square function

    # calculates sum of squares
    sos = x + y + z

    # returns the sum
    return sos

# prints sum of squares
print(sum_of_square(2, 3, 4))

print(sos) # results in error because sos is a local variable to sum_of_square