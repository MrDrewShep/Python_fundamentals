
from data_layer import Badge, Menu

current_menu = Menu()


def read_menu():
    return current_menu.read()


def create_badge(badge):
    new_badge = Badge(badge)
    current_menu.add_badge(new_badge)
    return f"{new_badge} was successfully added."


def add_doors(add_to_badge, additions=[]):
    # print(add_to_badge, additions)
    # print(type(add_to_badge))
    # print(type(additions))
    # for row in current_menu.contents:
    #     print(row)
    #     print(type(row))
    # print(current_menu.contents)
    # print(type(current_menu.contents))
    print(add_to_badge)
    print(type(add_to_badge))
    add_to = current_menu.contents[add_to_badge]
    add_to.add_permission(additions)










"""
sel = input('')

if sel in ["Y", "y", "g"]:
    print("yes")
else:
    print("no")
"""