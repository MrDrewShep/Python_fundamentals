# Type  Mutable   Ordered     Denotation
# ---------------------------------------
# List  Yes       Yes         []
# Set   Yes       No          {}
# Tuple No        Yes         (,)

# LIST

names = ["Adam", "Justin", "Xzavier"]
students = [
    "The Rock",
    "Charles",
    "The Undertaker",
    "Big Show",
    "Tony Stark",
    [
        "nested lists",
        "are cool",
        [
            56
        ]
    ]
]

# Lists can be embedded as a list item themselves.
# Lists can be of any type, and can be mixed.
# Lists are mutable, where the item would normally be mutable.

print(names[0])

names[0] = "Potato"     # List items can be changed with this syntax
print(names[0])

names.append("Thanos")  # How to append (goes to the end of the list)
print(names[-1])        # Negative numbers work toward the left of 0, which wraps backwards around to the end of the list

print(students[-1][-1]) # How to pull items from nested lists, example pulls "are cool"

print(students[-1][-1][0])  # Just because '56' is the only item in that list, if you don't specify [0] it will return the list [56]

names.insert(1, "Debbie")   # This inserts her BEFORE the 1st index, this example between Adam and Justin
print(names[1])

students.extend(names)      # To combine multiple lists, use EXTEND
print(students)

print(names)
names.pop(0)                # How to DELETE, if no index it defaults to the last
print(names)

print(len(students))
print(len("Py Class"))

students.remove("Tony Stark")   # Removes that particular value, wherever it lies. Only takes the first "Tony Stark", then stops.
print(students)

# SLICING

new_list = students[0:3:1]      # The 3 S's. Start: Stop: Step. Excludes the final index. This example retuns only 3 items.
                                # ALTERNATIVE: new_list = students[:3:1]  if the START is blank, it infers index 0
print(new_list)

reversed_list = students[::-1]  # Infers start at 0, stop at 0 (which will include the last index), and step backwards
print(reversed_list)

my_string = "testing"
new_string = my_string[1:5]
print(new_string)

reversed_again = reversed(names)    # This creates some sort of weird type stored in memory, but we can recast it as a list again, see just below
print(reversed_again)
reversed_again_list = list(reversed_again)
print(reversed_again_list)
# OR, condense it...
reversed_again = list(reversed(names))  # This is correct way
print(reversed_again)

# Concatenate
# You can concatenate lists with +, and it will merge them together

# TUPLES
# An immutable list

my_tuple = (12, 32)

# Quickly UNPACK a tuple into variables

my_name = ("Drew", "Shepherd")
f_name, l_name = my_name
print(f_name)
print(l_name)

tuple_names = ("Matthew", "Mark", "Luke", "John", "Judas")
something = tuple_names[3:-1]               # If multiple items, they will output as another tuple, instead of a list
print(something)
print(type(something))
something_2 = tuple_names[3]
print(something_2)
print(type(something_2))

single_item_tuple = ("John",)       # Parentheses denote tuple. Must keep a comma, otherwise it will assign it as a string.
print(single_item_tuple)
print(type(single_item_tuple))
                                    # Comma not required for a single item list. Because there is no other interpretation for [].

test_grab = tuple_names[3:-1]
print(test_grab)
# test_grab_2 = tuple_names[5]        # This will result in INDEX OUT OF RANGE error
# print(test_grab_2)

# SET
# Different from a list/tuple because it does not allow duplicate items
# Ignores any instructions that would add a duplicate item, will not error out
# These are unordered, mutable
# Unordered == has no index
# Allows multiple types
# Cannot be sliced, because it's unordered
states = {"Indiana", "Alaska", "Texas"}
# Use case: You have a list of 999 items. Are there duplicates? Cast that list to a set, and check the length. Is it 999?
print(len(states))
states.add(90)
states.remove("Alaska")     # If Alaska is not in the set, it will throw an error
states.discard("Canada")    # If Canada is not in the set, it will silently remove (not throw an error)
print("Indiana" in states)  # Results in boolean
states.clear()              # Empties the set
print(states)

# Do not need a comma to define a single item set

# SPLITTING

sentence = "Mary had a little lamb"
list_of_words = sentence.split()
print(list_of_words)
list_of_1 = sentence.split("l")
print(list_of_1)
list_of_chars = list(sentence)
print(list_of_chars)

# PUZZLE

my_names = ["Wallaby", "Bakersfield", "colGAte", "COcaCOla"]
# remove colgate
# add Crest
# Change cocacola to lowercase
# grab every other item in the list
# print each name individually

my_names.remove("colGAte")
my_names.append("Crest")
my_names[2] = my_names[2].lower()
my_list_2 = my_names[::2]
for x in my_names:
    print(x)

print("\n".join(my_names))                  # Creates one long string, separated by line break

for x in my_names:
    if x.lower() == "Crest".lower():        # Just testing this idea of "string".method()
        print(my_names.index(x))

my_list = [1, 2, 3]
new_list_1 = my_list    # They point to the same data in memory. Changing new_list_1 will affect my_list.
new_list_2 = my_list[:] # We created new memory. Changing new_list_1 will NOT affect my_list.