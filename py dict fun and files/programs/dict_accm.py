# ABOUT : This program deals with the accumulation pattern 
        # used with the help of dictionary

words = "Welcome back. Take a look in your calendar and mark this date. Today is the day you are crossing over the line, from someone who can just write code that does something to being a real programmer, someone who can abstract from a bit of code that works on one piece of data, to writing a function that will operate on any similar piece of data"

word_d = {}

for char in words :
    if char not in word_d :
        word_d [char] = 0
    word_d[char] = word_d[char] + 1

print(word_d)

ks = word_d.keys()

min_value = list(ks) [0]

for k in ks :
    if word_d[k] < word_d[min_value]:
        min_value = k

print("The ", min_value, "has :", word_d[min_value])