
# FIRST Challenge

num1 = 55
num2 = 9

def addition(starting_num, num_to_add):
    if num_to_add > 0:
        return addition(starting_num + 1, num_to_add - 1)
    else:
        return starting_num

# Alt: One liner
def addition_alt(starting_num, num_to_add):
    return starting_num if num_to_add <= 0 else addition(starting_num + 1, num_to_add - 1)

print(addition(num1, num2))


# SECOND Challenge

def increment_1(num):
    return num + 1

def my_map(iter, func):
    if len(iter) == 1:
        return func(iter[0])
    else:
        return func(iter[0]), my_map(iter[1:], func)

my_list = [5, 6, 7, 8, 9]

print(my_map(my_list, increment_1))

# SECOND Challenge, second attempt

# def increment_1(num):
#     return num + 1

# def my_map(iter, func):
#     if len(iter) == 1:
#         return func(iter[0])
#     else:
#         return func(iter[0]), my_map(iter[1:], func)

# my_list = [5, 6, 7, 8, 9]

# print(my_map(my_list, increment_1))


# Other feature, "separating the head from the tail"

def something(x):
    a, *b, c = x
    return a, b, c

print(something([1, 2, 3, 4, 5]))