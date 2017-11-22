import json

data = {}
data["name"] = "Avi"
data["age"] = 30
data["address"] = {
    "city": "Tel Aviv","street": "Hertzel"
}

f = open("jsondata.json","w")
json.dump(data,f)
f.close()