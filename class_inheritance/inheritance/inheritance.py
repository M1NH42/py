# Intro : Inheritance in python 3

# current year
CURRENT_YEAR = 2020

# base class
class Person:

    # constructor
    def __init__(self, name, year_born):
        self.name= name
        self.year_born = year_born
    
    # def methods
    def get_age(self):
        return CURRENT_YEAR - self.year_born

    # def __str__(self):
    #     return self.name

# inheritance syntax
# class derived_class(base_class)
# use inheritance to derive properties of the base class
class Student (Person):

    # constructor
    def __init__(self):
        # derive from the person class
        Person.__init__(self, name, year_born)
        self.knowledge = 0

    # def method
    def study(self):
        return self.knowledge + 1

# create instance
minhaz = Person("Minhaz Alam", 1997)
# print(minhaz.study())
print(minhaz.get_age())

