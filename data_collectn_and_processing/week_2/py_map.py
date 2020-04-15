# In this program we'll be implementing variousthings using map()
# map() function applies some transformer function to every part
# of the list

def double_stuff (things) :
    new_list = []
    for thing in things :
        new_elem = thing * 2
        new_list.append(new_elem)
    return new_list

things = [2, 3, 5]

print(things)

print(double_stuff(things))