# About : In this program we will implement/use built-in
# sorting function in python language and methods that are
# used most commonly

# first we'll use the method sort()
# which does not return anything but actually modifies
# the original list

# a list of numbers
l1 = [-2, 2, 1, 0, -9, 73, -32]

# called sort() method
l1.sort()

# print the sorted list
# one thing we noticed here is that the orignal list
# has been modified by thi sort() method
print(l1)

# print what sort() method returns
print(l1.sort())
# it returns NONE

print("********************SORTED() FUNCTION***********************")

# In this code block we'll implement a function called "sorted(pass params)"
# and this can be done with any type of sequance not just lists

# list two
l2 = [-2, 2, 1, 0, -9, 73, -32, 43, 22, -100]

# sort and store in l3
l3 = sorted(l2)

# prints l3: which is actually sorted list
print("The sorted list: ",l3)

# prints return of sorted function
print("The return of sorted() : ",sorted(l2))

# the original list
print("The original list : ",l2)