""" Rick and Morty example """

# CHALLENGE
# Find out how many characters in the API
# Find one that you like

import requests
import pprint
import os

list_of_characters = []

#? How to reprint the "loading" counter without clearing screen?

def get_characters(next_url, total="calculating"):
    os.system("cls")
    print("Loading... ", len(list_of_characters), " of ", total)

    response = requests.get(next_url)
    # print(response.status_code)         # A means of checking if .get() worked
    # print(response.ok, "\n")            # Best method to check if .get() worked

    try:
        data = response.json()
    except Exception:
        pass

    for entry in data["results"]:
        add_me = entry["id"], entry["name"]
        list_of_characters.append(add_me)

    next_url = data["info"]["next"]
    
    if next_url != "":
        get_characters(next_url, data["info"]["count"])


get_characters("https://rickandmortyapi.com/api/character/")

while True:
    for row in list_of_characters:
        print(row[0], row[1])
    selection = input("\nWhich character would you like to see: ")

    os.system("cls")

    get_url = "https://rickandmortyapi.com/api/character/" + selection
    response = requests.get(get_url)
    try:
        data_character_detail = response.json()
    except Exception:
        pass

    for entry in data_character_detail:
        print(entry, ":\t\t", data_character_detail[entry])   #HW figure out how to align 2nd column

    print("\n")
    selection = input("View another character (y/n) ")

    if selection == "y":
        os.system("cls")
        pass
    elif selection == "n":
        os.system("cls")
        quit()  

#HW find a terminal spinner package (github has one)