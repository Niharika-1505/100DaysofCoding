import requests
from twilio.rest import Client

"""Alphavantage stock price API's : https://www.alphavantage.co/documentation/#daily
Get News related to companies API's : https://newsapi.org/
"""

STOCK_NAME = "AAPL"
COMPANY_NAME = "Apple Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "XXXX"  # Generated at the time of alphavantage account creation
NEWS_API_KEY = "XXXX"  # Generated at the time of News api account creation

TWILIO_SID = "XXXX" # Both Twilio SID and Auth token are generated at the time of twilio account creation
TWILIO_AUTH_TOKEN = "XXXX"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [values for (key, values) in stock_data.items()]

yesterday_stock_closing_price = stock_data_list[0]["4. close"]
day_before_yesterday_stock_closing_price = stock_data_list[1]["4. close"]

difference = float(yesterday_stock_closing_price) - float(day_before_yesterday_stock_closing_price)
up_or_down = None

if difference > 0:
    up_or_down = "🔺"
else:
    up_or_down = "🔻"

difference_percentage = round((difference / float(yesterday_stock_closing_price)) * 100)

if abs(difference_percentage) > 1:

    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    latest_3_articles = news_response.json()["articles"][:3]
    formatted_articles = [f"{STOCK_NAME}: {up_or_down}{difference_percentage}%\n"
                          f"Headline:{articles['title']}.\n"
                          f"Brief: {articles['description']}"
                          for articles in latest_3_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+19793167486',
            to='+44XXXXXXXXXX'  # This should be a number that is verified in Twilio account
        )
        print(message.status)
