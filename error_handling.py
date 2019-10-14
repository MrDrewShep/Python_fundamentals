# TRY EXCEPT


def proclaim_user_birthday(name, age):
    try:
        new_age = age + 1
        message = f"{name} is now {new_age} years old!"
        print(message)
    except Exception as e:
        print(e)
    print("ONLY WHEN MY PROGRAM CONTINUES")

proclaim_user_birthday("Drew", "45")
print("I'm after proclaim.")    

# Anytime you're deailing with user-input data, use error handling.
# When dealing with data that only we control, might be safe enough to disregard error handling.

def find_user(user_id):
    if not isinstance(user_id, int):
        try:
            user_id = int(user_id)
        except Exception as e:
            print(e)
            raise TypeError("User_id must be a number.")
    return "A user"
    # Rest of code block here

find_user("test")


"""
def example_fn(PARAMETER):
    code block here
    code block here

example_fun(ARGUMENT)
"""