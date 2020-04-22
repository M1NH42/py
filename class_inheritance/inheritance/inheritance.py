# Intro : Inheritance in python 3

CURRENT_YEAR = 2020
class Person:
    def __init__(self, name, year_born):
        self.name= name
        self.year_born = year_born
    
    def get_age(self):
        return CURRENT_YEAR - self.year_born

class Student (Person):

    def __init__(self):
        Person.__init__(self, name, year_born)
        self.knowledge = 0

    def study(self):
        return self.knowledge += 1


minhaz = Student("Minhaz Alam", 1997)

print(minhaz.get_age)