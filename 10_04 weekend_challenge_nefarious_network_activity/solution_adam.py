
employees = open("employees.csv", "r").readlines()          # open.readlines() splits creates a list of each row's contents
access_list = open("access_list.csv", "r").readlines()

#HW Challenge to finish this function below

to_return = []

def convert_to_list_of_dictionaries(the_list):
    keys = the_list.pop(0).split(",")                       # pop() removes that item from the actual list data AND IT RETURNS THAT VALUE
    to_return = []
    for row in the_list:                                    # the .pop() did affect the_list already, so we don't need to start on index 1
        entry = {}
        values = row.split(",")
        print(type(values))
        for i, key in enumerate(keys):      # these 2 lines are loading up the dictionary
            entry[key] = values[i]
        to_return.append(entry)
    return to_return


print(convert_to_list_of_dictionaries(employees))

print(to_return)
