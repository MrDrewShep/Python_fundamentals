# CLASSES
# Capitalize the first letter
# A class is just a template, of in this case, what will exist for and operate on a Student. What they will look, behave like.
# method - a function inside of a Class. always requires min 1 argument, 'self'
# dunder - built in methods, on classes. in other languages, known as the constructor. 
# __init__ - the 1 required method you must give to each class. if we don't overwrite this it has a default method, and this default method accepts no arguments.
# instance - 
# invoke - 
# object - something that resides, at a memory address. aka, everything is an object in python.
# attributes - characteristics that can exist on an instance of a class. two types of attributes: (1) Class attribute: Defined above the initilizer. These do apply to each instance as well. Instance attribute: Defined within the initilizer, apply specifically to that instance.
# overwriting - 

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):                          # This allows student to inherit Person attributes

    school = "1150 Academy"                     # Class attribute
    counter = 0

    def __init__(self, name, grade, age):
        super().__init__(name, age)             # Grabs all attributes and methods from above, and makes them available for class Student
        self.grade = grade                      # Instance attributes
        Student.counter += 1                    # This alters the class-level counter. As opposed to a self.counter which would only mess with the instance.

    def have_birthday(self):
        self.age += 1

    def greeting(self):
        return f"Hello, my name is {self.name}. I am in grade {self.grade}."

xzavier = Student("Justin", 8, 32)             # Python know to call the initilizer __init__
xzavier = Student("Justin", 8, 32)             # Python know to call the initilizer __init__
xzavier = Student("Justin", 8, 32)             # Python know to call the initilizer __init__

print(xzavier.greeting())
print(Student.counter)

# OOP Object Oriented Programming
# APIE - 4 pillars of OOP: abstraction, polymorphism, inheritance, encapsulation
# abstraction - dealing with things at our level, not sweating always how it works underneath. stay at the highest level, solve the problem, move on. be lazy. hiding lower level operations for user friendliness. dealing with the idea rather than the process.
# polymorphism - functions that operate differently depending on the data given
# inheritance - bringing data and functionality in from a parent class/object
#             - To go up the chain, in our example...
#               Object
#               Person
#               Student
# single inheritance - class inherits from a single other class
# multi level inheritance - class inherits from multiple other classes
# 


"""
"""

# __repr__ and __str__
# Only necessary for us when debugging

class Cat:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"< CAT: {self.name} >"

    def __str__(self):
        return f"{self.name} is a cat."

fido = Cat("Fido")

print(fido)         # Print wants to print a string. It will look for that in __str__. If we didn't define that, it'll use the __repr__.
print(str(fido))