from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

GOOGLE_FORMS_URL = "https://docs.google.com/forms/d/e/1FAIpQLSc5JqPVUBpn1EAK6TjG_hTNWvrwYHTQeyuDhQqNraNn10TMUg" \
                   "/viewform?usp=sf_link "
ZILLOW_URL = "https://www.zillow.com/homes/San-Francisco," \
             "-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C" \
             "%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C" \
             "%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B" \
             "%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A" \
             "%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B" \
             "%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D" \
             "%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B" \
             "%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C" \
             "%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22" \
             "%3Atrue%2C%22mapZoom%22%3A12%7D "


# Create Spreadsheet using Google Form
def create_spreadsheet():
    chrome_driver_path = "D:/Python Related/SeleniumDriver/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(service=Service(chrome_driver_path))

    for n in range(len(all_links)):
        driver.get(GOOGLE_FORMS_URL)

        time.sleep(2)
        address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                                '1]/div/div[1]/input')
        address.send_keys(all_addresses[n])
        cost = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                             '1]/div/div[1]/input')
        cost.send_keys(all_prices[n])
        link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                             '1]/div/div[1]/input')
        link.send_keys(all_links[n])
        submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit_button.click()


header = {
    "User-Agent": "Chrome/84.0.4147.125",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(ZILLOW_URL, headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".list-card-top a")

all_links = []
for links in all_link_elements:
    href = links["href"]
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)
all_address_elements = soup.select(".list-card-info address")
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

all_price_elements = soup.select(".list-card-heading")
all_prices = []
for element in all_price_elements:
    # Get the prices. Single and multiple listings have different tag & class structures
    # print(element)
    try:
        # Price with only one listing
        price = element.select(".list-card-price")[0].contents[0]
    except IndexError:
        print('Multiple/No listings for the card')
        create_spreadsheet() # In my case I am stopping to look for new properties and adding existing ones to form
        # # Price with multiple listings
        # price = element.select(".list-card-details li")[0].contents[0]
    finally:
        all_prices.append(price)
