import json

with open("convertjson.json") as file:
    data = json.load(file)
    
print(data)
          