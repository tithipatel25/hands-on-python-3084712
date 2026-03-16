import requests

response = requests.get( #population statistics
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json",
)

last_twenty_years = response.json()[1][:20] #last 20 items from the json file
#.json method turns the response into python lists and dictionaries

for year in last_twenty_years:
  if not year["value"]: #if there is no year, just continue
    continue
  display_width = year["value"] // 10_000_000 #the _ makes it more readable
  # // floor the valueby 10 million
  print(f"{year['date']}: {year['value']}",display_width * "=") #layout of printing

