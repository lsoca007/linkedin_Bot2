from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "XXXX"
ACCOUNT_PASSWORD = "XXXX"

chrome_driver_path = "/Users/luisdavid/Development/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3266641134&f_LF=f_AL&geoId=102394087&keywords=junior%20software%20engineer&location=Miami%2C%20Florida%2C%20United%20States&refresh=true")

sign_in_button = driver.find_element(By.LINK_TEXT,"Sign in")
sign_in_button.click()

#Wait for the next page to load.
time.sleep(5)

email_field = driver.find_element(By.ID,"username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID,"password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# applications

time.sleep(3)

#all_listings = driver.find_elements(By.CLASS_NAME,"scaffold-layout__list-container")
all_listings = driver.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")
for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR,".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element(By.CLASS_NAME,"fb-single-line-text__input")

        if phone.text == "":
            phone.send_keys("XXXXX")


        next_button = driver.find_element(By.ID, "ember666")
        next_button.click()

        time.sleep(1)
        next_button.click()

        submit_button = driver.find_element(By.CSS_SELECTOR,"footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
            close_button.click()

            time.sleep(2)
            discard_button = driver.find_element(By.CLASS_NAME,"artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()

#-------------------------------------
driver.close()  # closes current tab
