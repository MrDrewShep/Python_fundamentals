
import manager
import os

def clear_screen():
    os.system("cls")

def alter_door_permission(add_or_remove, badge):
    permission = []
    
    def alter_door_permission_2(add_or_remove, badge):
        permission.append(input(f"{add_or_remove} permission to door: "))
        clear_screen()
        print(f"Pending permission changes for {badge}: {permission}")
        repeat = input(f"{add_or_remove} additional permission (y/n)? ").lower()

        if repeat in ["y", "yes"]:
            alter_door_permission_2(add_or_remove, badge)

    alter_door_permission_2(add_or_remove, badge)
        
    if add_or_remove == "Add":
        manager.add_doors(badge, permission)


while True:
    print("""System Admin
    What would you like to do?
    
    1) Add a badge
    2) Update permissions on a badge
    3) List all badges
    4) Exit menu"""
    )
    
    selection = int(input("\t >"))

    if selection == 4:      # Exit
        quit()
    elif selection == 1:    # Add
        new_badge_num = int(input("What is the new badge number: "))
        clear_screen()
        print(manager.create_badge(new_badge_num))
        alter_door_permission("Add", new_badge_num)
    elif selection == 2:    # Update
        existing_badge_num = int(input("Update which badge number: "))
        ###fix Print what that badge has access to
        alter_door_permission("Remove")
    elif selection == 3:    # List
        print(manager.read_menu())


#? In the sleezy auto example, why is changing of individual attributes in the car class, but the modify vehicle method is in the inventory class?