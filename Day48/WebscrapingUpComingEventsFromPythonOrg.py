from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://www.python.org/"
# Path where we saved the downloaded chrome driver
chrome_driver = "D:/Python Related/SeleniumDriver/chromedriver_win32/chromedriver.exe"
s = Service(chrome_driver)
driver = webdriver.Chrome(service=s)
driver.get(url)

# Get times
times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_times = [event_time.text for event_time in times]

# Get Event names
event_titles = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
event_names = [event_title.text for event_title in event_titles]

events_info = {}

for i in range(len(event_times)):
    events_info[i] = {
        "time": event_times[i],
        "name": event_names[i]
    }
print(events_info)



