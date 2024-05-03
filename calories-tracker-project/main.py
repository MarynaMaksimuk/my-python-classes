import requests
from datetime import datetime

with open("token.txt") as token:
    TOKEN = token.read()

USER_NAME = "maksimarina"
GRAPH1 = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(url=pixela_endpoint, json=user_params)
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH1,
    "name": "Calories Tracker",
    "unit": "cal",
    "type": "int",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
requests.post(url=graph_endpoint, json=graph_config, headers=headers)
today = datetime.now()
# today = datetime(year=2024, month=4, day=24)

pixel_post_endpoint = f"{graph_endpoint}/{GRAPH1}"
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many intake cals today? "),
}
requests.post(url=pixel_post_endpoint, json=pixel_params, headers=headers)

update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH1}/{today.strftime('%Y%m%d')}"

pixel_update_params = {
    "quantity": "1250",
}
requests.put(url=update_endpoint, json=pixel_update_params, headers=headers)

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH1}/{today.strftime('%Y%m%d')}"
requests.delete(url=delete_endpoint, headers=headers)
