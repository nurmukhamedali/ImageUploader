import json

with open('some.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
with open('some.json', 'w') as file:
    file.write(json.dumps(data, indent=2, sort_keys=False))