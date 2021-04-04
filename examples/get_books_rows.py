import json
import requests

number_of_rows = 5

page = requests.get(f"http://18.222.189.94/books?rows={number_of_rows}")
print(page)
print(json.dumps(page.json(), indent=4))
