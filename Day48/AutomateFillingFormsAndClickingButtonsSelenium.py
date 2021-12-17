from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://en.wikipedia.org/wiki/Main_Page"
chrome_driver = "D:/Python Related/SeleniumDriver/chromedriver_win32/chromedriver.exe"
s = Service(chrome_driver)
driver = webdriver.Chrome(service=s)
driver.get(url)
articles_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")  # Gets number of articles from wiki page
# articles_count.click()  # This line clicks on the hyperlink of that number of articles

science = driver.find_element(By.LINK_TEXT, "Science")
# science.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Spider-Man: No Way Home")
search.send_keys(Keys.ENTER)