# ABOUT : This program deals with the accumulation pattern 
        # used with the help of dictionary

# Here in this program we will find minimum value associated with the
# key : character in the string

# initialize a string
words = "Welcome back. Take a look in your calendar and mark this date. Today is the day you are crossing over the line, from someone who can just write code that does something to being a real programmer, someone who can abstract from a bit of code that works on one piece of data, to writing a function that will operate on any similar piece of data"

# initialize an empty dictionary
word_d = {}

# calculate how many times a character is appearing in the given string
# and store it in the dictionary created associating key value
for char in words :
    if char not in word_d :
        word_d [char] = 0
    word_d[char] = word_d[char] + 1

# prints the dictionary
print(word_d)

# list of keys
ks = word_d.keys()

# prints keys list
print(ks)

# init the first element as mn value
min_value = list(ks) [0]


# update the min_value
for k in ks :
    if word_d[k] < word_d[min_value]:
        min_value = k

# prints the result as shown
print("The ", min_value, "has :", word_d[min_value])