# Python provides an alternative way to do map and filter operations, called a list comprehension. 
# Many programmers find them easier to understand and write. 
# List comprehensions are concise ways to create lists from other lists. 
# The general syntax is:
# [<transformer_expression> for <loop_var> in <sequence> if <filtration_expression>]


#### question ####

# Code to assign to the variable compri all the values of the key name in 
# any of the sub-dictionaries in the dictionary tester. Do this using a list 
# comprehension.

# nested dictionary
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

import json
print(json.dumps(tester, indent=2))

# extracting info
inner_list = tester['info']

# better representation
print(json.dumps(inner_list,indent=2))


# list comprehension
compri = [name['name'] for name in inner_list]

# print the final result
print(compri)