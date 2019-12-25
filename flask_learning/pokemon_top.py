# Pillow package for images

import requests
import pprint

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
def list_berries():
    html = ""
    for berry in berry_list:
        html += r"<p>" + r'<a href="/' + berry[1] + r'">' + berry[0] + r'</a>'
    return html


if __name__ == "__main__":
    app.run()


