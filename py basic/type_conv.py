# this program shows the working of type conversion in python 3

print(90, int(90))
print(165.90, int(165.90))
print('123', int('123'))
print(60, float(60))
print(9, float(9))

print(type(str(435))) # type convrsion to string
print(type(int('334'))) # type conversion to int

# used in concatenation such as
print("Age " + str(22))