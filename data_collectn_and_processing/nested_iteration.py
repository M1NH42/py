# In this program we'll implement the nested iteration concepts using
# * two for loops
# * one loop and a square bracket(indexing)
# * indexing(square bracket) and a for loop

# nested list
nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]

# iterate
for x in nested1:

    # outer loop
    print("level1: ")

    # check if x in nested1 a list or not
    # if yes execute inner for loop
    if type(x) is list :
        for y in x :
            print("     level2: {}".format(y))
    
    # if not the print value of x
    else :
        print(x)
