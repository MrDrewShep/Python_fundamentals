# In order to test:
# 1. Bring in pytest in a virtual environment
# 2. Define test functions with "test_" ...
# 3. In powershell: pytest .\testing_functions.py


def find_largest(x, y):
    # or return max(x, y)
    if x > y:
        return x
    else:
        return y

def test_find_largest():
    assert find_largest(1, 2) == 1      # Syntax

def test_other_test():
    assert "test" == "test"


# New example

def find_user(user_id):
    if not isinstance(user_id, int):
        try:
            user_id = int(user_id)
        except Exception as e:
            print(e)
            raise TypeError("User_id must be a number.")
    return "A user"
    # Rest of code block here

def test_find_user_returns_string():
    assert find_user(2) == "A user"

# How to assert that a certain exception is raised
import pytest
def test_find_user_exception():
    with pytest.raises(TypeError):
        find_user("hello")

def test_find_user_takes_string_returns_string():
    assert find_user("2") == "A user"



#HW Agile prework for Friday's lecture