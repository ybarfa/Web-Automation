from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from my_project.utils.xpath import *
import os
import json

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

config_path = os.path.join(parent_directory, "configuration", "config.json")

with open(config_path, "r") as configuration:
    config_data = json.load(configuration)

try:
    driver = webdriver.Chrome()
    driver.get(config_data["url"])
    driver.maximize_window()

    input_link = driver.find_element(By.XPATH, herokuapp_feilds["Input"])
    input_link.click()

    input_element = driver.find_element(By.XPATH, '//input[@type="number"]')

    input_element.clear()

    input_element.send_keys("12345")

    entered_value = input_element.get_attribute("value")

    print("Your Entered value:", entered_value)

except NoSuchElementException:
    print("No Such Element Found.")
