import requests
import json
import pandas

API_URL = "https://api.thecatapi.com/v1/breeds"

response = requests.get(API_URL)

if response.status_code == 201 or response.status_code == 200:
    print("SUCESS", response.status_code)
    data = response.json()
else:
    print("FAILURE", response.status_code)

print(json.dumps(data, indent=2))

for row in data:
    for key, value in row.items():
        print(f"{key}: {value}")
