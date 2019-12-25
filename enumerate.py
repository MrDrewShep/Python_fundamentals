# returns a series of tuples

# see example in nefarious network/solution.py

mylist = ["Drew", "Shep", "Danni", "Buster", "Bob"]
for i, name in enumerate(mylist, start=4):
    print(f'Enumerating {i} and name {name}')