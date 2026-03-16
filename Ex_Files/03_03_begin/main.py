import csv
import json
from pprint import pprint

EINSTEIN = { #python dictionary, looks a lot like json
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

einstein_json = json.dumps(EINSTEIN) #converts the above info (dictionary) into json
back_to_dict = json.loads(einstein_json) #converst json to dictionary
print(einstein_json) #print
pprint(back_to_dict) #pretty-print

#the following codes turns the .csv file into a .json file
with open("laureates.csv", "r") as f: #r is read mode
    reader = csv.DictReader(f) #dictionary reader using the object f
    laureates = list(reader) #creating a list of dictionaries, each one representing Noble prize winner


with open("laureates.json", "w") as f: #w is write mode
    json.dump(laureates, f, indent=2) #
