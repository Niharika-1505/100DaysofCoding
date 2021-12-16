import smtplib
import os
import requests
# import lxml
from bs4 import BeautifulSoup

"""To get corresponding browser header information : http://myhttpheader.com/"""

url = "https://www.amazon.co.uk/Highams-Weighted-Blanket-Teenagers-Insomnia/dp/B07XXPGFXT/ref=sr_1_9?crid" \
      "=2E9ANCQPH3K96&keywords=weighted%2Bblanket&qid=1639656249&sprefix=weighted%2B%2Caps%2C173&sr=8-9&th=1 "
header = {
    "User-Agent": "Chrome/84.0.4147.125",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price_text = soup.find(name="span", class_="a-offscreen").get_text()
current_price = float(price_text.split("£")[1])
desired_price = 36.99

product_title = soup.find(id="productTitle").getText().strip()

if current_price <= desired_price:
    message = f"{product_title} is now {current_price} which is {desired_price - current_price} " \
              f"less than your desired price"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        result = connection.login(user=os.environ["SENDEREMAIL"], password=os.environ["SENDERPASSWORD"])
        connection.sendmail(
            from_addr=os.environ["SENDEREMAIL"],
            to_addrs=os.environ["RECIPIENTEMAIL"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
