import json
from random import randint

import requests

from flask import Flask

app = Flask(__name__)


poke_url = "https://pokeapi.co/api/v2/berry/?limit=100"
response = requests.get(poke_url).json()

berry_list = []
for berry in response["results"]:
    add_item = []
    berry_name = berry["name"]
    parse_url = berry["url"].split("/")
    berry_id = parse_url[-2]
    add_item.append(berry_name)
    add_item.append(berry_id)
    berry_list.append(add_item)


@app.route('/')
def home_page():
    html = ""
    for berry in berry_list:
        html += r"<p>" + r'<a href="/' + berry[1] + r'">' + berry[0] + r'</a>'
    return html

@app.route('/<pokeid>')
def hello_world(pokeid):
    random_choce = pokeid
    selection = 'https://pokeapi.co/api/v2/berry/' + f'{random_choce}'
    request = requests.get(selection)
    mydict = request.json()
    berry_name = str(mydict['item']['name'])
    flavor = str(mydict['flavors'][0]['flavor']['name'])
    item_link = mydict['item']['url']
    item_request = requests.get(item_link)
    itemdict = item_request.json()
    sprite_link = itemdict['sprites']['default']
    my_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
<img src="{sprite_link}">
    <title>{berry_name}</title>
</head>
<h1>Berry Name:{berry_name}</h1>
<h2>Berry Flavor:{flavor}</h2>
<body>
<a href ="http://127.0.0.1:5000/">HOME</a>
</body>
</html>"""
    return my_page
