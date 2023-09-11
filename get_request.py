# importing the requests library
import requests

# API-endpoint
API_endpoint = "https://dog.ceo/api/breeds/list/all"

# sending get request and saving the response as response object
r = requests.get(url = API_endpoint)

# extracting data in json format
data = r.json()

# getting dictionary Key:Value pairs from message data
dict = data["message"]

# extracting dict keys
dog_breeds = list(dict.keys())

# printing the list using * operator separated by comma
# print in new line
print(*dog_breeds, sep="\n")