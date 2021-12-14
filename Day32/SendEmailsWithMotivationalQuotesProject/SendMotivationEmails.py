import smtplib
import datetime as dt
import random

sender_email = "xxxx"
password = "xxxx"  # This is manually set gmail password. For yahoo we should use generated app password
recipient_email = "emma.clarin@yahoo.com"

now = dt.datetime.now()
weekday = now.weekday()  # Monday = 0 - Sunday = 6
if weekday == 3:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(sender_email, password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=recipient_email,
            msg=f"Subject:Today's Motivation\n\n{quote}"
        )
