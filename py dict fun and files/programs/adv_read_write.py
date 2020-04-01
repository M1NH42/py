# ABOUT : This porgramdeals with some advance topic 
# to deal with the python file objects. However it 
# can be easily skipped as we it is used by most of
# the experinced data science or python programmers
# * with statement

# can use "with" keyword to avoid writing
# the easily forgettable close() method
with open("../programs/olympics.txt", "r") as od : # store it as file name here it is od : olympics data
    for line in od :
        print(line)