import json
filename = '10\\json_files\\numbers.json'
with open(filename,'r') as f:
    numbers = json.load(f)
print(numbers)