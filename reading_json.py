import json

with open("new_json_file.json") as jsonfile:
    pet = json.load(jsonfile)
    print(type(pet))
    print(pet)
    print(pet["name"])