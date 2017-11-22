import json

f = open("jsondata.json")
data = json.load(f)
f.close()
print data
data["student"]["grades"].append(95)
print data
f = open("jsondata.json","w")
json.dump(data,f)
f.close()