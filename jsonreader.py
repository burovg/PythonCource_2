import json

f = open("jsondata.json","r")

data = json.load(f)

print data["address"]["city"]