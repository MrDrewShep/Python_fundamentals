var1 = 1.25
var2 = 3.331
print(var2 // var1)

event_type = input("What type of event are you hosting? ")

if event_type.casefold() != "banquet" and event_type.casefold() != "wedding":
    print("I'm sorry, we are only catering banquets and weddings at this time.")
    quit()

event_attendance = int(input("How many guest do you expect? "))

if event_type.casefold() == "banquet" and event_attendance < 30:
    print("I'm sorry, we require a minimum of 30 guests for banquets.")
    quit()

if event_type.casefold() == "wedding" and event_attendance < 25:
    print("I'm sorry, we require a minimum of 25 guests for weddings.")
    quit()

print("We would be pleased to cater your event!")

# I should have casefolded at the top, then referenced the already lowered variable in the if statements.
# Also can casefold the input statement, without reassigning a new variable
# event_type = input("What kind of event? ").lower()

print(type(event_attendance))
