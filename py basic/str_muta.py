### Since strings are not mutable we can still modify the 
### string by using below method

# string
greeting = "Hello, world!"

# new string using previous one
newGreeting = 'J' + greeting[1:]

# print new string
print(newGreeting)

# print original string
print(greeting)          # same as it was