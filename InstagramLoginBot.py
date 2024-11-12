from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import random
import getpass

username = input("Enter your Instagram username: ")
password = getpass.getpass("Enter your Instagram password: ")

try:
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()

    url = "https://www.instagram.com/"
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    userinput = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    userinput.send_keys(username)
    time.sleep(random.uniform(1, 2))

    passwordinput = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    passwordinput.send_keys(password)
    time.sleep(random.uniform(1, 2))

    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    login_button.click()
    time.sleep(random.uniform(3, 5))

    try:
        not_now_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))
        )
        not_now_button.click()
        time.sleep(random.uniform(1, 2))
    except:
        pass

    try:
        turn_off_notifications = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))
        )
        turn_off_notifications.click()
        time.sleep(random.uniform(1, 2))
    except:
        pass

    print("Login successful. Keeping browser open for 60 seconds...")
    time.sleep(60)

except Exception as e:
    print(f"An error occurred: {e}")
    time.sleep(10)
finally:
    driver.quit()
