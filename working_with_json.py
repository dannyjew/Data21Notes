import json

pet_data = {"name": "Bob", "food": "Carrots"}

# converts dict to string
pet_data_json_str = json.dumps(pet_data)
print(pet_data_json_str)

with open("new_json_file.json", "w") as jsonfile:
    json.dump(pet_data, jsonfile)