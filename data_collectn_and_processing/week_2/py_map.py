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

states = ['hp','mp','up','tn','ap','asm','pb','mh']

def f (st) :
    return st.upper()

u_states = map(f, states)
# u_states = map (lambda st: st.upper(), states)

print(u_states)