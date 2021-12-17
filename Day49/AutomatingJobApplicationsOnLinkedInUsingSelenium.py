from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C" \
      "%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
chrome_driver = "D:/Python Related/SeleniumDriver/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver))
driver.get(url)

# Once the linkedin page is opened click on sign in
time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

# Automate the Entry of username, password and hit login
time.sleep(5)
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(os.environ["ACCOUNT_EMAIL"])
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(os.environ["ACCOUNT_PASSWORD"])
password_field.send_keys(Keys.ENTER)

time.sleep(5)

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(os.environ["PHONE"])

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            print("Application Sent")
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
