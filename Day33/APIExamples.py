import requests

"""https://www.latlong.net/"""
# My Current Location BH13JS Latitude : 50.727960 Longitude: -1.834420
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()  # This is the other way to raise exceptions without manually writing them

if response.status_code == 200:
    iss_object = response.json()
    print(iss_object)
    print(iss_object["iss_position"])  # prints current longitude and latitude of ISS
    print(f"Longitude:{iss_object['iss_position']['longitude']}")
    print(f"Latitude:{iss_object['iss_position']['latitude']}")
elif response.status_code == 404:
    raise Exception("The page does not exist or the link you entered is incorrect")
elif response.status_code == 401:
    raise Exception("You are not authorized to access this data.")

