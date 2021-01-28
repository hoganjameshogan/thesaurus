import json

data = {}

with open('data.json') as d:
    data = json.load(d)

print(data['success'])