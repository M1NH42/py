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
    return res

sum_list = sum([1, 2, 3, 5])

print(sum_list)

prod_list = prod([1, 2, 3, 5])

print(prod_list)