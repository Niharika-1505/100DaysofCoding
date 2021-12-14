import requests

SHEETY_PRICES_ENDPOINT = "XXXX"
SHEETY_USERS_ENDPOINT = "XXXX"


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = []

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=("USERNAME", "PASSWORD"))
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data, auth=("USERNAME", "PASSWORD")
            )
            print(f"Data_manager.py file: {response.text}")

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint, auth=("USERNAME", "PASSWORD"))
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
