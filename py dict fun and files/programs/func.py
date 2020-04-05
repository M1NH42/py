# *About* : We'll define various function to implement our program

# define sum(param)
def sum(lst):
    # accum variable
    tot = 0
    # iterate through every num and 
    # keep on adding to num tot
    for num in lst :
        tot += num
    # returns total
    return tot

# define product(by passing list as param)
def prod(lst):
    # initialize prod
    res = 1
    # iterate through every num in the list
    # and keep on mult to num res
    for num in lst :
        res *= num
    # returns res
    return res

# define a function : count_num()
# to count the number of elements
# present in the list given by the user
def count_num(lst) :
    num_count = 0
    for num in lst :
        num_count += 1
    return num_count

# called count_num()
print(count_num([1, 2, 4, 5, 7, 9]))

# called
sum_list = sum([1, 2, 3, 5])

# output result of sum
print(sum_list)

# called prod()
prod_list = prod([1, 2, 3, 5])

# output result
print(prod_list)