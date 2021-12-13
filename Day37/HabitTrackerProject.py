from datetime import datetime

import requests

"""Pixela is the website where we are posting our data to keep track of habits : https://pixe.la/v1/users
Use this link to see the changes made to the graph be it put, post, delete
https://pixe.la/v1/users/niharikag/graphs/pixelagraph01.html
"""

USERNAME = "niharikag"
PIXELA_TOKEN = "fdgd23g4fh3fd23df5kl4"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_GRAPH_ID = "pixelagraph01"

user_params = {
    "token": PIXELA_TOKEN,  # Create a token like this with 8 to 128 chars
    "username": USERNAME,  # Create a username
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)  # Once the request is posted comment these two lines of code
# Once the post request is successful profile page is created https://pixe.la/@niharikag

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": PIXELA_GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)  #
# print(response.text)

pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{PIXELA_GRAPH_ID}"
today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# PUT
update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{PIXELA_GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# DELETE
delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{PIXELA_GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
