### Since strings are not mutable we can still modify the 
### string by using below method

greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting)          # same as it was