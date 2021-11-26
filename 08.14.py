import json

film = {
    "name":"Wladca Pierscieni",
    "year":1999,
    "actor":"Johny Depp",
    }
jfile=open("myfile.json", "w")
json.dump(film,jfile,indent=3)
jfile.close()