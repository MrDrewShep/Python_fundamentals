# Dictionary

my_dictionary = {
    "Key": "Value",
    "Key2": 78
}

product = {
    "id"            : 838200,
    "description"   : "A yellow submarine, etc.",
    "price"         : 9.99,
    "weight"        : 9001,
    "department"    : "grocery",
    "aisle"         : 3,
    "shelf"         : "B"
}

print(product["price"])
location = product["aisle"], product["shelf"]
print(location)

# print(product["quantity"])        This would result in a keyerror
print(product.get("quantity"))      # This results in 'None' so it is a safer method

# Change it to aisle 4
product["aisle"] = 4
print(product["aisle"])

product["aisle"] += 1
print(product["aisle"])

for x in product:
    print(x)            # It will print the keys

for x in product:
    print(product[x])   # This is how to print the values

print(product.values())     # Creates a set-like object, could do a for loop over these
print(product.keys())       # Creates a set-like object

# Create a new key/value pair
product.update({"whatever": "the value"})
print(product)

# CHALLENGE
you = {}

data = [("name", "Drew Shepherd"), ("age", 90), ("class", "python")]
# Put these data points into the empty dictionary as key/value pairs

for x, y in data:           # My solution (not optimal)
    you.update({x:y})

for k, v in data:           # Alternative from Adam
    you[k] = v

you.update(data)            # Optimized solution

print(you)

