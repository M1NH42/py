# About : In this program we see the implementation of a function
# using while loop

# function define
# num as param
def to_sum(num) :
    # init a_num
    a_num = 1
    # init sum so far
    sum_so_far = 0

    # condition while true do this...
    while a_num <= num :
        # Add num to sum
        sum_so_far += a_num
        # increment a number by one (1)
        a_num += 1
    # return the sum of numbers
    return sum_so_far

# prints the sum of numbers
print(to_sum(4))