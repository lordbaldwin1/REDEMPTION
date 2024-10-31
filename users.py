import requests
import json

# Fetch the data
# Extract name and email from each user into list of dictionaries
# Post this list to endpoint

API_URL = "https://jsonplaceholder.typicode.com/users"
TARGET_API_URL = "https://httpbin.org/"
response = requests.get(API_URL)

data = response.json()

users = []

for row in data:
    user = {"name": row["name"], "email": row["email"]}
    users.append(user)

for i in users:
    print(i)

# DONT NEED TO CONVERT TO POST
# json_users = json.dumps(users, indent=4)
# print(json_users)
# 
# PASS IN LIST OF DICT, json='' CONVERTS IT AUTOMATICALLY
# Otherwise you would need to specify Content Type: application/json
# headers = { "Content Type": "application/json" }
# post = requests.post(TARGET_API_URL, data=json_users, headers=headers)

post = requests.post(TARGET_API_URL, json=users)

if post.status_code == 200 or post.status_code == 201:
    print("POST SUCESSFUL")
else:
    print(f"Failed to post data: ${post.status_code}")
    print("Response: ", post.text)



