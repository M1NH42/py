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

print("****************** type of d ************************\n\n")
print(type(d))

print("\n\n****************** prints dictionary ************************\n\n")
print(d)

print("\n\n****************** after dumps function ************************\n\n")
print(pretty(d))

# *************** loads() *****************************
#import json
entertainment = """[{"Library Data": {"count": 3500, "rows": 10, "locations": 3}}, {"Movie Theater Data": {"count": 8, "rows": 25, "locations": 2}}]"""

d = json.loads(entertainment)

print(d)