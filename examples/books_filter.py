import json
import requests


data = {"author": "barbara parisi"}

page = requests.post("http://18.222.189.94/books", data=data)
print(page)
print(json.dumps(page.json(), indent=4))


data = {"id": 363, "author": "barbara parisi"}

page = requests.post("http://18.222.189.94/books", data=data)
print(page)
print(json.dumps(page.json(), indent=4))
