import requests
from datetime import datetime
import smtplib
import time

"""https://www.latlong.net/"""
# My Current Location BH13JS Latitude : 50.727960 Longitude: -1.834420
sender_email = "XXXX"
password = "XXXX"  # This is manually set gmail password. For yahoo we should use generated app password
recipient_email = "emma.clarin@yahoo.com"
MY_LAT = 50.727960  # Your latitude
MY_LONG = -1.834420  # Your longitude


def is_iss_AboveMyLocation():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_AboveMyLocation() and is_night():
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=recipient_email,
            msg="Subject:Hello Welcome\n\nThis is the body"
        )
