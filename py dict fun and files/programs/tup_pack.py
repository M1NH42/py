# About : This is the implementation of the tuple packing functionality
# and its application in function return statement

def circle_info(radius) :
    circum = 2 * 3.14 * radius

    area_cir = 3.14 * radius * radius

    return circum, area_cir

print(circle_info(10))