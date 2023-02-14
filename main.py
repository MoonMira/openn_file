import pprint
import json
import requests


url = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url)
list_hero = ["Hulk", "Captain America", "Thanos"]
dict_herous = {}
for dict_hero in response.json():
    if dict_hero['name'] in list_hero:
        dict_herous[dict_hero["name"]] = dict_hero['powerstats']['intelligence']
        max_values = max(dict_herous)

print(f'Самый умный из супергероев {max_values}')



