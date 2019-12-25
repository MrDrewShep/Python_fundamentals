# Fill out the truth table
"""
a       b       not (a and b or b)
            aka not ((a and b) or b)    in an 'or true' situation, it resolves to true
----------------------------------
False   False   True
True    False   True
False   True    False
True    True    False
========================================
# Each student that has an A in their name, print their age.
# Make your program able to handle any list of students (this format below)
students = [("AJ", 25), ("XD", 19), ("JA", 27), ("IS", 27)]
"""

students = [("AJ", 25), ("XD", 19), ("JA", 27), ("IS", 27)]

for kid in students:                    # Wrong. If "a" is anywhere in the name
    if kid[0][0].casefold() == "a":
        print(kid[1])

for a, b in students:                   # Correct solution
    if "a" in a.casefold():
        print(a, b)

for a, b in students: if "a" in a.casefold(): print(a, "is", b) 
