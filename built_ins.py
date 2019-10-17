
### GLOBALS

from datetime import datetime

import pprint

class Human:
    earthian = True

    def __init__(self, name, age, birthday):
        self.name = name
        self.age = age
        self.birthday = birthday

    def have_birthday(self):
        self.age += 1

    def greet(self):
        return f"Hello, my name is {self.name}."

mini_me = Human("Carson", 0, datetime(year=2019, month=6, day=27))

pprint.pprint(globals())
print()
pprint.pprint(mini_me.__dict__)
print()
pprint.pprint(dir(mini_me))
print()
pprint.pprint(dir(""))  # Dir for all string methods

### HELP

# help(mini_me)

### MAP()

numbers = [1, 2, 3, 4, 5]
def add_15(val):
    return val + 15
print(list(map(add_15, numbers)))

### LAMBDA - anonymous, unless assigned to a function, users don't know it exists
# Alternative way to process the MAP() example above
# Not preferred way to build a function, limited room to expand and enhance

adding_var = lambda x: x + 15
print(adding_var)
print(adding_var(15))

my_numbers = list(map(lambda x: x + 15, numbers))
print(my_numbers)

# Could be used, for example, to take a giant list of email addreses and identify/remove duplicates, after they are all lowercased
#HW continue reading python docs for built ins, starting at OPEN()