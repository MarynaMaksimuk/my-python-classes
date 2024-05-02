import requests
import datetime
import os

MY_WEIGHT = 70
MY_HEIGHT = 164
MY_AGE = 80

EXERCISE_ENDPOINT = os.environ["EXERCISE_ENDPOINT"]
DATASHEET_ENDPOINT = os.environ["DATASHEET_ENDPOINT"]
APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]
basic_auth = os.environ["basic_auth"]

sheety_auth_header = {
    "Authorization": basic_auth
}

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

request_param = {
    "query": exercise_text,
    "weight_kg": MY_WEIGHT,
    "height_cm": MY_HEIGHT,
    "age": MY_AGE
}

response = requests.post(EXERCISE_ENDPOINT, json=request_param, headers=headers)
result = response.json()

today_date = datetime.datetime.now().strftime("%x")
time = datetime.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    add_row_params = {
        "sheet1": {
            "date": today_date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(DATASHEET_ENDPOINT, json=add_row_params, headers=sheety_auth_header)
print(sheet_response.text)

