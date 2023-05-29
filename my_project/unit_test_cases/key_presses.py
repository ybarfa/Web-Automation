from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from my_project.utils.xpath import *
import json
import os
import time

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
config_path = os.path.join(parent_directory, "configuration", "config.json")

with open(config_path, "r") as configuration:
    config_data = json.load(configuration)

try:
    driver = webdriver.Chrome()
    driver.get(config_data["url"])
    driver.maximize_window()

    key_presses = driver.find_element(By.XPATH, herokuapp_feilds["Key Presses"])
    key_presses.click()

    input_field = driver.find_element(By.ID, "target")
    input_field.send_keys(Keys.ENTER)

    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.staleness_of(input_field))
    input_field = driver.find_element(By.ID, "target")

    input_field.send_keys(Keys.SPACE)

    result_text = driver.find_element(By.ID, "result").text
    print("Result: " + result_text)


except NoSuchElementException:
    print("No Such Element Found.")
