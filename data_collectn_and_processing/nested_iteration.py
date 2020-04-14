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

    if type(x) is list :
        for y in x :
            print("     level2: {}".format(y))
    else :
        print(x)
