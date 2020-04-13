### Since strings are not mutable we can still modify the 
### string by using below method

# string
greeting = "Hero Alom"

# new string using previous one
newGreeting = greeting [ : 7] + 'a' + greeting [8 : ]

# print new string
print(newGreeting)

# print original string
print(greeting)          # same as it was