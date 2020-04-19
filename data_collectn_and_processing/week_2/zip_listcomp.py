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

# Basic approach
# for i in range(len(a)):
#     print(a[i] + b[i])


# above program can be done using zip()
# make a list zips together
# c = list(zip(a, b))

# # print the list after zipping the two lists
# print(c)

# temp = []

# # addition can be done by using zip
# for (x, y) in c:
#     temp.append(x+y)

# print(temp)


# addition and zipping can be combined together using list
# comprehension and zip()
# unpacking is also done using varibales x and y
temp_list = [x+y for (x, y) in list(zip(a, b))]

print(temp_list)