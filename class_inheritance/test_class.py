# Create a class called Animal that accepts two numbers as inputs and assigns 
# them respectively to two instance variables: arms and legs. Create an instance 
# method called limbs that, when called, returns the total number of limbs the animal has. 
# To the variable name spider, assign an instance of Animal that has 4 arms and 4 legs. 
# Call the limbs method on the spider instance and save the result to the variable name spidlimbs.


# def class 
class Animals():
    # parametrized constructor with legs, arms
    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs
    
    # def method that returns sum of limbs
    def limbs(self):
        return self.arms + self.legs

# creating instance of animals class
spider = Animals(4, 4)

# store result of limbs func
spidlimbs = spider.limbs()

# prints result
print(spidlimbs)