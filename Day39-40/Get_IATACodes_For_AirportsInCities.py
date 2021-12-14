import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "XXXX"
CITY = "Bangalore"

location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
headers = {"apikey": TEQUILA_API_KEY}
query = {"term": CITY, "location_types": "city"}
response = requests.get(url=location_endpoint, headers=headers, params=query)
results = response.json()["locations"]
code = results[0]["code"]
print(code)
