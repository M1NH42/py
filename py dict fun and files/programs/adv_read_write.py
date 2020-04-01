# ABOUT : This porgramdeals with some advance topic 
# to deal with the python file objects. However it 
# can be easily skipped as we it is used by most of
# the experinced data science or python programmers
# * with statement

with open("olympics.txt", "r") as od :
    for line in od :
        print(line)