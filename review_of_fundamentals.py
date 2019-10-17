
# Want to edit items? LIST
# Strict set of sequence? TUPLE
# Want everything to be unique? SET


# List
# CRUD
my_list = [2, 4, 3]       # create
first_item = my_list[0]   # read
#nested_item = my_list[0][2] # read within a nested list
my_slice = my_list[-2::]  # returns last 2
print(my_slice)
my_slice = my_list[::-1]  # Start at beginning, work backwards
my_list.append(6)         # update
my_list.append([10, 11, 12])         # update
my_list.insert(2, 8)
my_list.extend([10, 11, 12])
my_list.pop()             # update, pop last off the list, and return it

my_list[1] = 777          # insert, as indexed
print(my_list)


print(my_list)
my_list.remove(777)       # remove a specific item
del my_list               # delete


# Loops
# Ability to iterate over an interable, or until a condition becomes False
x=0
for i in range(10):
    x += 1
    if i >= 7:
        break           # this will technically end the loop
    if i > 8:
        continue        # continue will goto the next iteration of the loop
    a = i + i           # this line never fires


n = 8
while n >= 0:
    print("not yet")
    n -= 1
print("finally done")

# Dictionary
# key value collection, unordered and mutable {}

my_dictionary = {
    "name":"drew shep",
    "age": 31
}

#my_dictionary.get()
my_dictionary["name"] = "mr squiggles"

my_dictionary["hobby"] = "python"
print(my_dictionary)
my_dictionary.update({ "hobby": "golf", "age" : 33 })   # hobby was added, age was updated

print(my_dictionary)

my_dictionary.keys()
my_dictionary.values()
my_dictionary.items()       # grabs key/value pairs in a list of tuples


# Functions

def func_name(param1, param2):

func_name(arg1, arg2)


# Classes
# A custom, datatype object that holds attributes and methods

class Animal:

    def __init__(self, kingdom):
        self.kingdom = kingdom
    
    def get_kingdom(self):
        return self.kingdom


class Human(Animal):

    def __init__(self, kingdom, name, age):
        super().__init__                        # Takes the Human we just created and also initializes them as an animal
        self.name = name
        self.age = age

    def speak(self):
        return f'Hello, I am {self.name}'


me = Human("camelot", "drewbie", 31)
print(me.get_kingdom())


# Virtual environments
# isolated environment in python used to test and share projects in order to keep dependencies local
