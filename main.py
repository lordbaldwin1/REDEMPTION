import requests

API_URL = "https://jsonplaceholder.typicode.com/albums"
TARGET_API_URL = "https://example.com/api/endpoint"

response = requests.get(API_URL)

data = response.json()

for arr in data:
    arr["id"] = arr["id"] * 2
    title = arr["title"]
    arr["title"] = title[0].upper() + title[1:]

#print(data[:5])

post = requests.post(TARGET_API_URL, json=data)

