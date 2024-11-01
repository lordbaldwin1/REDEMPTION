import requests

def main():
    API_URL = "https://jsonplaceholder.typicode.com/photos"
    data = fetchData(API_URL)
    # paginate(data)

################################################################################################################################################
# Create a function that paginates the photo results, displaying 10 photos per page. Include functions to go to the next and previous pages.
################################################################################################################################################
def fetchData(API_URL):
    response = requests.get(API_URL)

    if response.status_code == 201 or response.status_code == 200:
        print("Data fetch success! Status code: ", response.status_code)
    else:
        print("Error: Data fetch failed, status code: ", response.status_code)
        exit(1)
    
    return response.json()

def paginate(data):
    start = 0
    end = 10
    option = "g"
    DATA_SIZE = len(data)

    while option != "q":
        if start <= 0 or end > DATA_SIZE:
            print("DATA OUT OF BOUNDS, RESETTING...")
            start = 0
            end = 10

        for row in data[start:end]:
            print(row)

        print("GO TO PREV/NEXT PAGE: 'p' or 'n', 'q' to exit")
        option = input()

        if option == "p":
            start -= 10
            end -= 10
        elif option == "n":
            start += 10
            end += 10
    print("EXITING...")
    return
        
    



main()

