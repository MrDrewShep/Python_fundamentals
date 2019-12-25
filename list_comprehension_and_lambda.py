"""
Lambda
    It's an unnamed function
    Used with MAP and FILTER frequently
    e.g. lambda x: x * x
"""
"""
MAP
    It's a function
    Takes 2 args
    eg. map(func, some_iterable)

"""

nums = [3, 4, 5, 6]
sqrs = list(map(lambda x: x * x, nums))
print(sqrs)

"""
FILTER
    Takes in 2 args
    eg. filter(func, some_iterable)
"""

"""
3 Challenges
    x = [i for i in range(100)]

    1. Filter that returns evens
    2. Filter that returns odds
    3. Filter that returns all values not div by 3 or 5
"""

x = [i for i in range(100)]

# 1
one = list(filter(lambda x: x if x % 2 == 0 else "", x))
print("evens\n", one)

# 2
two = list(filter(lambda x: x if x % 2 != 0 else "", x))
print("odds\n", two)

# 3
three = list(filter(lambda x: x if x % 3 != 0 and x % 5 != 0 else "", x))
print("fizzbuzz\n", three)


"""
LIST COMPREHENSION
    Syntax:
            var = [returned logic_that_makes_return]
    List comps rely on MAP and FILTER
    Generates a list
    e.g. my_list = [x for x in range(100)]
"""

something = [1, 2, 3, 4, 5]
print([x*x for x in something])
print([x*x for x in something if x % 2 == 0])

"""
Challenge
"""
four = list(filter(lambda x: x if x % 3 != 0 and x % 5 != 0 else "", x))
print("fizzbuzz\n", four)