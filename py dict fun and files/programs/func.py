# *About* : We'll define various function to implement our program

def sum(lst):
    tot = 0
    for num in lst :
        tot += num
    return tot

def prod(lst):
    res = 1
    for num in lst :
        res *= num
    return res

sum_list = sum([1, 2, 3, 5])

print(sum_list)

prod_list = prod([1, 2, 3, 5])

print(prod_list)