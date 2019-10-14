# Challenge 
# Create a python file in python, that itself modifies the testing.txt file to say:
# "I'm sorry, I cannot do that."

injection = """

new_text = open("./file_io_hub/testing.txt", "w")
new_text.write("I'm sorry, I cannot do that DAVE")
new_text.close()

"""

new_file = open("./file_io_hub/file_two.py", "w")
new_file.write(injection)
new_file.close()

import os
# import file_io_hub.file_two
# exec(file_io_hub/file_two.py)

if os.path.isfile("./file_io_hub/file_two.py"):
    os.system("py ./file_io_hub/file_two.py")
    print("yes")
else:
    print("no")

"""    PREFERRED AND ALTERNATE MEANS OF THE ABOVE """
# It not only requires less syntax, but it closes the file on our behalf once the with statement is departed

with open("./file_io_hub/file_two.py", "w") as f:
    f.write("#I'm a comment\nprint(\"Hello World.\")")

#HW download a skin mod