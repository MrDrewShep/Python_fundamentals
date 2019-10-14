# For loop

animals = ["Jaguar", "Raccoon", "Fox", "Cat", "Toucan"]

for x in animals:       # Variable here only exists in the For loop
    print(x)

# C# version of this for(i=0; i<len(animals); i++), you declare the exit condition to be checked each run

# Nested For loop, example runs 30 x 30 times
for i in range(30):
    for j in range(30):
        if i == j:
            print("They match", i)

expenses = [
    ("McDonalds", 12.00),
    ("Steam", 49.99),
    ("Rent", 900.00)
]
# To total this, must declare the total variable before the for loop. Because any vars in the for loop will be garbage collected at the end of each for loop.

total = 0.0

for expense in expenses:
    total += expense[1]

print(total)

# While loop

x = 0

while x < 100:
    print(x)
    x += 4
else:                       # Called a "finally" statement
    print("All done.")
    print(x + 100)

# Challenge

products = ["nvidia", "amd", "arm", "intel", "risc"]
search_term = "intel"

x = 0
while x < len(products) and search_term != products[x]:
    print(f"{x} {products[x]} is not the product you're looking for.")
    x += 1                      # Incrementation must be at BOTTOM of while loop, otherwise it presents incorrect details.
else:
    print("Search complete.")

# In reality, we wouldn't use a While loop for this, we'd instead use:

print()

if search_term in products:
    print(products.index(search_term))
else:
    print("Not found.")

# Break statement
while x < 100:
    print(x)
    x += 4
    if x == 92
        break
