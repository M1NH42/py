# In this program we'll implement zip function of python


# The zip function takes multiple lists and turns them 
# into a list of tuples (actually, an iterator, but they 
# work like lists for most practical purposes), pairing 
# up all the first items as one tuple, all the second 
# items as a tuple, and so on. Then we can iterate through 
# those tuples, and perform some operation on all the first items, 
# all the second items, and so on.


a = [1, 2, 4, 5]

b = [5, 4, 3, 7]

for i in range(len(a)):
    print(a[i] + b[i])