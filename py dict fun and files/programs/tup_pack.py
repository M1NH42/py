# About : This is the implementation of the tuple packing functionality
# and its application in function return statement


# define func and pass radius as param
def circle_info(radius) :
    # calculate circumference
    circum = 2 * 3.14 * radius
    # calculate area of the circle
    area_cir = 3.14 * radius * radius
    # return both as tuple
    return circum, area_cir

# prints in the form of tuple   
print(circle_info(10))