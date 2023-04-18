""" Object Oriented Programming In Python"""

"""
 'self' refers to the instance of the object we are currently using.
"""

"""
 Class attributes - are specific to the class, not specific to an instance object of that class so they dont use 'self'. 
 It's good to use when you want to use a constant to keep your code robust so that your code isnt relying oon variables outside of it's class container.
 They can be accessed directly outside (and inside) of the class by '[class name].[static method name]'.
"""

"""
 Class methods - contain 'cls' and need the '@classmethod' decorator to denote that it's a class method.
 They are also specific to the class, not specific to an instance object of that class so they dont use 'self'.
 They can be accessed directly outside (and inside) of the class by '[class name].[static method name]'.
"""

"""
 Static methods - are specific to the class, not specific to an instance object of that class.
 They don't access anything in the class (e.g. attributed or other methods) so don't contain anything like self or cls.
 They can be accessed directly outside (and inside) of the class by '[class name].[static method name]'.
"""

"""
 Class attributes, class methods and static methods all do something but don't change anything specific to an instance
"""


class Animal:

    number_of_animals = 0 # A class attribute
    my_learning_ranking = 1

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Animal.number_of_animals +=1  #To access a class attribute (when we arent inside a class method) we must mention the class name first.


    # A class method
    @classmethod
    def increase_to_my_learning_ranking(cls):
        cls.my_learning_ranking *=5 #To access a class attribute (when we are inside a class method) we can use either 'cls' or the class name first - Best practise to use 'cls'.
        return f"Your learning has been increased to {cls.my_learning_ranking}"

    # A static method
    @staticmethod
    def animals_can_multiple(num1,num2):
        return f"{num1} * {num2} = {num1*num2}"


    def get_name(self):
        return f"My name is {self.name}!"

    def get_age(self):
        return f"I am {self.age}."

    def sound(self):
        return "I don't know what sound I make"




# the child class 'Cat' inherits from parent/super class 'Animal'
class Cat(Animal):

    def __init__(self,name,age,number_of_kittens):
        super().__init__(name,age)  # initialise attributes/instance variables from the super class
        self.number_of_kittens = number_of_kittens
        Cat.number_of_animals +=3  #To access class attributes we must mention the class name first


    # override 'sound' method from the super class
    def sound(self):
        return "meow"

    def update_number_of_kittens(self,noOfKittens):
        self.number_of_kittens=noOfKittens
        return "Number of Kittens Updated"

    def get_number_of_kittens(self):
        return f"I have {self.number_of_kittens} kittens."




class Dog(Animal):

    def sound(self):
        return "woof"

    def go_sleep(self):
        return "Doggy sleeping..."




# Test cases

animal1=Animal("ani",6)
dog1=Dog("Brandy", 12)
cat1=Cat("Kitkat", 3,5)

print(animal1.get_name())
print(animal1.sound())
print(animal1.number_of_animals)


print("\n")
print(dog1.get_name())
print(dog1.get_age())
print(dog1.go_sleep())
print(dog1.sound())
print(dog1.number_of_animals)



print("\n")
print(cat1.get_name())
print(cat1.get_age())
print(cat1.get_number_of_kittens())
print(cat1.update_number_of_kittens(7))
print(cat1.get_number_of_kittens())
print(cat1.sound())
print(cat1.increase_to_my_learning_ranking())
print(cat1.increase_to_my_learning_ranking())
print(cat1.number_of_animals)


print("\n")


print(Animal.animals_can_multiple(5,10))
