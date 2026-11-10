import json


data = {
    "name": "Alan Turing",
    "age": 42 ,
    "city": "London, UK",
    "interests": ["Mathematics", "Logic", "Computer Science"],
    "is_student": False
}

with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("created data.json")