# In this module we will be working with the new type of paradigm ie
# oop (object oriented programming) with classes and objets

# creating class Point
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # get value of x in the point
    def get_x(self):
        return self.x

    # gets value y of the point
    def get_y(self):
        return self.y

    # distance from origin
    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** .5

    def __str__(self):
        return 'x = {}, y = {}'.format(self.x, self.y)

point1 = Point(12, 43)

# setting instance of point()
point2 = Point(32, 23)


# calling get functions to get values of x and y
print(list([point1.get_x(), point1.get_y()]))

print(point1)

print()

print("Distance from the origin : ", point1.distance_from_origin())