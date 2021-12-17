from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


url = "http://secure-retreat-92358.herokuapp.com/"
chrome_driver = "D:/Python Related/SeleniumDriver/chromedriver_win32/chromedriver.exe"
s = Service(chrome_driver)
driver = webdriver.Chrome(service=s)
driver.get(url)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Niharika")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Gadde")
emailID = driver.find_element(By.NAME, "email")
emailID.send_keys("gaddenih_rika43@gmail.com")
submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
