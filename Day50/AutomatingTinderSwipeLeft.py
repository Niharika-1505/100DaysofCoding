from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
from selenium.webdriver.common.by import By
import os

url = "http://www.tinder.com"
chrome_driver = "D:/Python Related/SeleniumDriver/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver))
driver.get(url)

login_button = driver.find_element(By.XPATH, '//*[@id="o-1556761323"]/div/div[1]/div/div/main/div/div[2]/div/'
                                             'div[3]/div/div/button[2]')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, '//*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/div[2]/'
                                         'button/span[2]')
fb_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH, '//*[@id="pass"]')

email.send_keys(os.environ["FB_EMAIL"])
password.send_keys(os.environ["FB_PASSWORD"])
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(5)
allow_location_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    sleep(1)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH,
                                          '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div['
                                          '2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()
