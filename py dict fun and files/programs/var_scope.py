# About : In this program we will se the scope resolution of variable
# * global variable
# * local variable

def square(num) :
    sq = num * num
    return sq

def sum_of_square(fn, sn, tn) :
    x = square(fn)
    y = square(sn)
    z = square(tn)

    sos = x + y + z

    return sos

print(sum_of_square(2, 3, 4))