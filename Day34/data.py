import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}
# The actual Trivia api link https://opentdb.com/api.php?amount=10&type=boolean but params pass the values.
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
print(f"data.py file : {question_data}")
