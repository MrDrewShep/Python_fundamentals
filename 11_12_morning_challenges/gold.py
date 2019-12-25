
fruit_list = ['apple', 'apricot', 'bananna', 'bozo', 'cherry', 'Chameleon', 'edgar']

fruit_dict = {}

for fruit in fruit_list:
    if fruit[0].lower() not in fruit_dict.keys():
        fruit_dict[fruit[0].lower()] = [fruit]
    else:
        fruit_dict[fruit[0].lower()].append(fruit)


print(fruit_dict)