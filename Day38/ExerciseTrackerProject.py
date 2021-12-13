import requests
from datetime import datetime

GENDER = "XXXX"
WEIGHT_KG = "XX"
HEIGHT_CM = "XXX"
AGE = "XX"

NUTRITIONIX_API_ID = "XXXX"  # Generated at the time of Nutritionix account creation
NUTRITIONIX_API_KEY = "XXXX"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# Sheety is a website where we connect google sheets
sheet_endpoint = "SHEETY_ENDPOINT"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": NUTRITIONIX_API_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # No Auth
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    # Basic Auth
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=("SHEETY_USERNAME", "SHEETY_PASSWORD")
    )

    print(sheet_response.text)
