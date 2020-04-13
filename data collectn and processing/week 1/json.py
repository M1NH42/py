# In this program we'll see/implement how json module works
# with python 3

# import module
import json

# we'll basically see the working of loads() and dumps() methods

#json.loads() takes a string as input and produces a python object
# (a dictionary or a list) as output

def pretty(obj) :
    return json.dumps(obj, sort_keys=True, indent=2)

d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print(pretty(d))