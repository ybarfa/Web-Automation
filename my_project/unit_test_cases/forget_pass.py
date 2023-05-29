from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from my_project.utils.xpath import *
import json
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

config_path = os.path.join(parent_directory, "configuration", "config.json")

with open(config_path, "r") as configuration:
    config_data = json.load(configuration)

try:
    driver = webdriver.Chrome()
    driver.get(config_data["url"])
    driver.maximize_window()

    forget_pass = driver.find_element(By.XPATH, herokuapp_feilds["Forget Password"])
    forget_pass.click()

    textbox = driver.find_element(By.XPATH, sign_up["username_textbox"])
    textbox.send_keys("barfayash2@gmail.com")

    retrieve_pass = driver.find_element(By.XPATH, '//i[contains(text(), "Retrieve password")]')
    retrieve_pass.click()

    wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Internal Server Error")]')))

except NoSuchElementException:
    print("No Such Element Found.")
