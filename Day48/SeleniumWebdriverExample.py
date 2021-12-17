from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""Useful links: https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-
deprecated-selenium-python
https://stackoverflow.com/questions/30002313/selenium-finding-elements-by-class-name-in-python
https://stackoverflow.com/questions/61308799/unable-to-locate-elements-in-selenium-python
https://selenium-python.readthedocs.io/getting-started.html"""


url = "https://stackoverflow.com/questions/30002313/selenium-finding-elements-by-class-name-in-python"
# Path where we saved the downloaded chrome driver
chrome_driver = "D:/Python Related/SeleniumDriver/chromedriver_win32/chromedriver.exe"
s = Service(chrome_driver)
driver = webdriver.Chrome(service=s)
driver.get(url)
title = driver.find_element(By.CLASS_NAME, "question-hyperlink")
print(title.text)

# driver.close()  # This closes only that particular tab
# driver.quit()  # This closes entire browser
