def FUNCTION_NAME_HERE(parameters):
    print(parameters)
    # Code Block
    return "some data"

FUNCTION_NAME_HERE('parameter data')
print(FUNCTION_NAME_HERE("Python is cool"))

# Defaulting the input parms

def FUNCTION_HERE(x=[]):
    pass

def FUNCTION_2(x="default text"):
    pass
    
# Multiple parms
def cash_register_1(total, tendered):         # Bad solution
    if tendered < total:
        return "Hey, I need more monies."
    elif tendered == total:
        return "Have a nice day."
    else:
        return "Here's your change."

def cash_register_2(total, tendered):           # Good solution
    """This takes two numbers and compares them"""      # This is a 'docstring' which can be used throughout the program
    answer = ""

    if tendered < total:
        answer = "Hey, I need more monies."
    elif tendered == total:
        answer = "Have a nice day."
    else:
        answer = "Here's your change."

    return answer

answer = cash_register_2(11.99, 20.00)          # This variable 'answer' is different than the 'answer' variable seen in the function.

print(answer)

help(cash_register_2)

# Default return statment
# Every function will return something
# That return, if nothing, will be 'None'

def combine(x,y,z):
    """
    Takes 3 numbers and prints their sum
    """
    print(x+y+z)

what_is_this = combine(1,2,3)

print(what_is_this)             # Will results in 'None'