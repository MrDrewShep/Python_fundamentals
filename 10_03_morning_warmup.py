# Fix the code

from decimal import *

def calculate_savings(prev_price, current_price, amount, tax):
    """
    Function's purpose is to calculate and report savings on a purchase

    prev_price          (float number describing the price before savings)
    current_price       (float number describing the price at purchasing)
    amount              (int number denoting how many were purchased)
    tax                 (float number describing the state's tax percentage)

    This function should return a float number describing how much was saved
    or a string stating "no savings occurred"
    """
    incl_tax_percentage = 1 + tax
    
    previous_total = (prev_price * incl_tax_percentage) * amount
    current_total = (current_price * incl_tax_percentage) * amount
    savings = previous_total - current_total

    # if savings <= 0:                # My answer, not optimal
    #     print("No savings occured. Sucker.")
    # if savings > 0:
    #     print(f"You saved ${savings}!")

    # if savings > 0:                 # Most optimal solution
    #     return savings
    # else:
    #     return "No savings occured."
        
    # return savings if savings > 0 else "No savings occured."     # Slick, one liner way
    return savings


"""
Return statement ends the current block/indentation of code 

Best practice is NOT to print inside of a function
Best practice is NO print statements left in your program, unless it's interactive.
"""

# calculate_savings(12.00, 10.00, 4, 0.10)


# How much was saved on this order?

contracted_items = [
   {
      "id": "A001",
      "name": "Daisy Paper Plates",
      "price": 3.99
   },
   {
      "id": "A002",
      "name": "Solo Red Cups",
      "price": 2.00
   },
   {
      "id": "A199",
      "name": "Dixie Paper Towels",
      "price": 4.50
   }
]

purchased_items = [
   {
      "id": "A088",
      "count": 32,
      "price": 4.88
   },
   {
      "id": "A002",
      "count": 29,
      "price": 3.40
   },
   {
      "id": "A199",
      "count": 2,
      "price": 8.90
   },
   {
      "id": "A332",
      "count": 78,
      "price": 22.78
   },
   {
      "id": "A001",
      "count": 10,
      "price": 3.99
   }
]


total_savings = 0.00


for i in purchased_items:
    previous_price = i["price"]
    for j in contracted_items:
        if i["id"] == j["id"]:
            previous_price = j["price"]
    current_price, amount = i["price"], i["count"]
    tax = 0.08

    savings = calculate_savings(previous_price, current_price, amount, tax)

    total_savings += savings

total_savings = round(total_savings,2)

print(f"You saved ${total_savings}.") if total_savings > 0 else print(f"No savings occured. Sucker. You overpaid ${total_savings}.")

print("%.2f"%total_savings)
print(round(total_savings,2))
print("{0:.2f}".format(total_savings))

#? Overall, how to optimize part(2) of the prompt?
#? Which of the 2 decimal format methods is optimal? Explain the syntax?
#? How to use abs() in the f-string, when they overpaid?
#? autofill for def incorporates "self" as the 1st param. leave it there?