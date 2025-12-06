import json
import yaml

def normalize(d):
    
    if isinstance(d, dict):
        return {k.lower().replace(" ", "_"): normalize(v) for k, v in d.items()}
    
    elif isinstance(d, list):
        return [normalize(i) for i in d]
    
    return d
    
filename = "sample1.json"

if filename.endswith(".json"):
    data = json.load(open(filename))
else:
    data = yaml.safe_load(open(filename))

result = normalize(data)
print(result)