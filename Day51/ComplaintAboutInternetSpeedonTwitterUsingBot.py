import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
# from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
# from time import sleep
from selenium.webdriver.common.by import By
import os

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "D:/Python Related/SeleniumDriver/chromedriver_win32/chromedriver.exe"
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()
        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                           '3]/div/div/div[2]/div[1]/div[ 2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                       'div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/'
                                                       'div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        email = self.driver.find_element(By.XPATH,
                                         '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/'
                                         'div[1]/div/div[5]/label/div/div[2]/div/input')

        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        password = self.driver.find_element(By.XPATH,
                                            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/'
                                            'div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        tweet_compose = self.driver.find_element(By.XPATH,
                                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                                 '2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/'
                                                 'div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for" \
                f" {PROMISED_DOWN}down/{PROMISED_UP}up? "
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                                                          'div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                          'div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
