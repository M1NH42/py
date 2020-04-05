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