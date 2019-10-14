# These are two libraries that come with python by default
# os allows you to access your operating system commands
# time allows you to pause for a bit of time during your program
# There is more to these packages, but for ease we only use it for these two operations
import os
import time

import repo as manager

prompt = """
Welcome to the Sleasy Car Saleseman portal!
What would you like to do?

1) View inventory
2) Add vehicle to inventory
3) Change vehicle information
4) Exit

>"""

error_prompt = """
_____________________________

 Error:
 Please select a valid choice

 Press any button to continue
_____________________________
"""

def clear_terminal():
    os.system('cls' if os.name == "nt" else "clear")

while True:
    clear_terminal()
    choice = input(prompt)

    if choice == "1":
        clear_terminal()
        print(manager.retrieve_inventory_list())
        
        input("Press enter to go back to main screen")
    elif choice == "2":
        clear_terminal()
        make = input("Enter vehicle make > ")
        model = input("Enter vehicle model > ")
        year = input("Enter vehicle year > ")
        vin = input("Enter vehicle vin > ")
        price = input("Enter vehicle listing price > ")
        clear_terminal()
        print("Adding vehicle to inventory...")
        time.sleep(1)
        clear_terminal()
        print(manager.add_vehicle(make, model, year, vin, price))
        input("Press Enter to continue...")
    elif choice == "3":
        clear_terminal()
        print(manager.retrieve_inventory_list())
        index = int(input("Choose an ID to edit vehicle"))
        vehicle = manager.retrieve_vehicle(index)
        clear_terminal()
        if vehicle != "":
            print(vehicle)
            print("---- Leave options blank to keep the same ----")
            make = input("Enter vehicle make > ")
            model = input("Enter vehicle model > ")
            year = input("Enter vehicle year > ")
            vin = input("Enter vehicle vin > ")
            price = input("Enter vehicle listing price > ")
            clear_terminal()
            print(manager.modify_vehicle(index, make, model, year, vin, price))
            time.sleep(1)
            input("Press enter to continue")
        else:
            print("Error retrieveing vehicle")
            input("Press enter to return to main screen")
    elif choice == "4":
        clear_terminal()
        print("")
        print("Exiting")
        time.sleep(1)
        clear_terminal()
        exit()
    else:
        clear_terminal()
        input(error_prompt)