import requests

API_URL = "https://jsonplaceholder.typicode.com/photos"

response = requests.get(API_URL)

#print(response.text)

data = response.json()

# for row in data[:10]:
#     print(row)

# for row in data[:5]:
#     print(row["title"])

################################################################################################################################################
# filter photos by albumId
# display titles of all photos in that album

# for row in data:
#     if row["albumId"] == 1:
#         print(row["title"], row["albumId"])

################################################################################################################################################
### search by title, if includes keyboard, print title with first letter capitalized and with a period at the end

# print("ENTER TITLE")
# tinput = input()
# for row in data:
#     if tinput.lower() in row["title"].lower():
#         title = row["title"]
#         row["title"] = title[:1].upper() + title[1:] + "."
#         print(row["title"])
################################################################################################################################################
# Retreive photos with even id
# Fetch all photos and display only those with an even id. Show the title and id of each matching photo.

for row in data:
    if row["id"] % 2 == 0:
        print("id: ", row["id"], "title", row["title"])
# assuming id starts at 1 lets print every other id and title for the same result for fun
for row in data[1::2]:
    print("id: ", row["id"], "title: ", row["title"])