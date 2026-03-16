import csv
import json
from pprint import pprint

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

einstein_json = json.dumps(EINSTEIN) #converts the above info (dictionary) into json
back_to_dict = json.loads(einstein_json) #converst json to dictionary
print(einstein_json)
pprint(back_to_dict)

#the following codes turns the .csv file into a .json file
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


with open("laureates.json", "w") as f:
    json.dump(laureates, f, indent=2)
