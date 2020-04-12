# We are heading towards the week 1 of third course of the python 3
# specialization...
# In this course we'll learn and implement about data collecyion and
# processing of that data

# this prgram is baout nested lists and how indexing can be used to 
# extract information from the nested list

# nested list
animals = [['cat', 'dog', 'mouse'], ['horse', 'cow', 'goat'], ['cheetah', 'giraffe', 'rhino']]

# iteration
for animal in animals :
    print(animal)

# index help
print(animals[1][2])

# incremental approach
# store internal 2nd list in new list
new_list = animals [2]

# print index 2of new list
print(new_list [2])