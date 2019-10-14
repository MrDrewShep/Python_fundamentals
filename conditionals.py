left = True
right = False

left == True    # == can be read as, "True or false, left is equal to True." In this case it resolves to TRUE
right != "train"    # ! is pronounced 'bang.' != is 'is not equal to.' In this case it resolves to TRUE
left is right   # Example resolves to FALSE
left is not right   # Example resolves to TRUE

# Equality Operators
# != True or False, items are NOT equivalent?
# == True or False, items ARE equivalent?
# is True or False, items have same IDENTITY?
# is not True or False, items DO NOT have same identity?

# Comparison Operators, also return TRUE or FALSE
# age_1 = 23
# age_2 = 45
# >
# <
# >=
# <=

# Compound Logical Operators
# and
# e.g. age_1 == 4 and age_2 < 22
# or
# e.g. age_1 == 4 or age_2 < 22
# not, flips the question
# e.g. not age_1 == 23      example returns FALSE

# 'AND' TRUTH TABLE

# a         b           a and b
# ------------------------------
# True      True        True
# True      False       False
# False     True        False
# False     False       False

# a         b           a or b
# ------------------------------
# True      True        True
# True      False       True
# False     True        True
# False     False       False

x = 4

if x > 3:
    print('X is pretty big')

name = "Ryan"

if x > 3 and name == 'Ryan':
    print('both apply')
elif x > 0 and name == 'Ryan':
    print('at least he\'s older than 0 yrs.')
else:
    print('not the case')

# Nested if's or Multiple if's (start with the occurance that will be LEAST frequent)

if x > 3 and name == "Ryan":
    if x > 0:
        print("example of nexted if")

# CHALLENGE
# Take a name and age, and if the person is under 18, say "NAME, you are not an adult."
# If the person is 18 but not 21, say "NAME, you are an adult, but not quite yet."
# If the person is 21 or older, say "NAME, you are fully an adult."

# Extra spicy challenge
# If their name starts with an A, say "Cool name."

name = input('What is your name? ')
age = int(input('What is your age? '))

if age < 18:
    print(f"{name}, you are not an adult.")
elif age < 21:
    print(f"{name}, you are an adult, but not quite yet.")
else:
    print(f"{name}, you are fully an adult.")

if name[0].casefold() == 'a':
    print("P.S. Cool name.")

# Alternative      elif age in range(18, 20):

# Fizz Buzz - A clasic interview question
# Declare a number
# If a number is divisible by 3, return Fizz
# If a number is divisible by 5, return Buzz
# If a number is divisible by both, return FizzBuzz
# Otherwise, just print the number
# Test: 1, 3, 5, 10, 15 98

var1 = int(input("Give me a number: "))

if var1 % 3 == 0 and var1 % 5 != 0:
    print("Fizz")
elif var1 % 3 != 0 and var1 % 5 == 0:
    print("Buzz")
elif var1 % 3 == 0 and var1 % 5 == 0:
    print("FizzBuzz")
else:
    print(var1)

for num in range(1, 99):
    if num % 3 == 0 and num % 5 != 0:       # Could also use 1 conditional asking for % 15, which is LCM least common multiple
        print(f"{num} Fizz")
    elif num % 3 != 0 and num % 5 == 0:     # Too much code, if you start with both ==, then the elif statements don't need to check both results, can just check for one at a time.
        print(f"{num} Buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print(f"{num} FizzBuzz")
    else:
        print(num)
