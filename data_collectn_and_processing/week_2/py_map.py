# In this program we'll be implementing variousthings using map()
# map() function applies some transformer function to every part
# of the list

def double_stuff (things) :
    """ Returns a new list with doubl ethe values than the previous list """

    # accum list
    new_list = []

    # iterate over each item in the prev list
    for thing in things :
        # double each item
        new_elem = thing * 2
        # add to the new list
        new_list.append(new_elem)
    return new_list

# define list
things = [2, 3, 5]

# print
print(things)

# print by calling the defined function
print(double_stuff(things))

####################### map() ##################################

#  map takes two arguments, a function and a sequence. 
# The function is the mapper that transforms items. 
# It is automatically applied to each item in the sequence. 
# You don’t have to initialize an accumulator or iterate with a for loop at all.

states = ['hp','mp','up','tn','ap','asm','pb','mh']

def f (st) :
    return st.upper()

# Technically, in a proper Python 3 interpreter, the map function produces
# an “iterator”, which is like a list but produces the items as they are needed. 
# Most places in Python where you can use a list (e.g., in a for loop) you can use 
# an “iterator” as if it was actually a list. So you probably won’t ever notice the difference. 
# If you ever really need a list, you can explicitly turn the output of map into 
# a list: list(map(...)).
u_states = list(map(f, states))
# u_states = map (lambda st: st.upper(), states)

print(u_states)