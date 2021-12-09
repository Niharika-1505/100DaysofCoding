import smtplib

sender_email = "emmathompson1505@gmail.com"
password = "Emma@123"  # This is manually set gmail password. For yahoo we should use generated app password
recipient_email = "emma.clarin@yahoo.com"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # This line makes the connection secure.
    connection.login(user=sender_email, password=password)
    connection.sendmail(
        from_addr=sender_email,
        to_addrs=recipient_email,
        msg="Subject:Hello Welcome\n\nThis is the body"
    )
