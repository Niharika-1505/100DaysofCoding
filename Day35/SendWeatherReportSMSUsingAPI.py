# import os
import requests
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

""" All the commented code needs to be uncommented while hosting project on 'PythonAnywhere'
Online JSON viewer: http://jsonviewer.stack.hu/
Ventusky website shows live weather of entire world:  https://www.ventusky.com/
Weather condition codes: https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
Sending SMS using Twilio API Docs: https://www.twilio.com/docs/sms/quickstart/python
Trial number generated by Twilio : +19793167486
# The lat and lon are taken for a place 'Aslanapa' considering it is raining at the location on the day of this 
program execution by using ventusky website
"""

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "XXXX"  # Generated at the time of open weather map account creation.
account_sid = "XXXX"  # Generated at the time of Twilio account creation
auth_token = "XXXX"  # Generated at the time of Twilio account creation
weather_parameters = {
    "lat": 39.214510,
    "lon": 29.869400,
    "exclude": "minutely,daily",  # The minutely and daily data will be excluded...so we get current and hourly data
    "appid": api_key
}
response = requests.get(url=OWM_Endpoint, params=weather_parameters)
response.raise_for_status()


"""The other way is to use slicing"""
weather_data = response.json()
weather_slice = response.json()["hourly"][:12]
will_rain_in_next_12_hours = False
for hourly_data in weather_slice:
    weather_status = hourly_data["weather"][0]["id"]
    if 200 <= weather_status < 700:
        will_rain_in_next_12_hours = True

if will_rain_in_next_12_hours:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    client = Client(account_sid, auth_token)  # Comment this line while hosting on Python Anywhere
    message = client.messages.create(
        body="Take an Umbrella it is going to rain in next 12 hours ??????",
        from_='+19793167486',
        to='+44XXXXXXXXXX'  # This should be a number that is verified in Twilio account
    )
    print(message.status)


