# we'll see how this try and exception works in the python 3 programming language

# syntax :

# try:
#    <try clause code block>
# except <ErrorType>:
#    <exception handler code block>

# def square(num):
#     return num * num

# # assertion testingg
# assert square(3) == 9


# try and except block of statement
a_list = ['a', 'b']

try :
    # if something went wrong then in try block next statement will not be executed
    third = a_list[2]
except:
    print("Third element does not exist")

# after except statements are executed
print("heyo")