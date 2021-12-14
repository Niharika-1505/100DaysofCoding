from datetime import datetime
import pandas
import random
from twilio.rest import Client

TWILIO_SID = "XXXX"
TWILIO_AUTH_TOKEN = "XXXX"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        receiver_mobile_number = f"+{birthday_person['phone_number']}"
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=contents,
        from_='+19793167486',
        to=receiver_mobile_number,  # This should be a number that is verified in Twilio account
    )
    print(message.status)
