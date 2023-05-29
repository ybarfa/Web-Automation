from selenium import webdriver
from selenium.webdriver.common.by import By
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

driver = webdriver.Chrome()
driver.get(config_data["url"])
driver.maximize_window()

try:
    option = driver.find_element(By.XPATH, herokuapp_feilds["Chechboxes"])
    option.click()

    checkbox_2 = driver.find_element(By.XPATH, '//form[@id="checkboxes"]//input[2]')
    if checkbox_2.is_selected():
        time.sleep(2)
        checkbox_2.click()

    checkbox_1 = driver.find_element(By.XPATH, '//form[@id="checkboxes"]//input[1]')
    if not checkbox_1.is_selected():
        checkbox_1.click()
    time.sleep(2)

    checkbox_1 = driver.find_element(By.XPATH, '//form[@id="checkboxes"]//input[1]')
    if checkbox_1.is_selected():
        checkbox_1.click()
    time.sleep(2)

    checkbox_2 = driver.find_element(By.XPATH, '//form[@id="checkboxes"]//input[2]')
    if not checkbox_2.is_selected():
        checkbox_2.click()
    time.sleep(2)

except NoSuchElementException:
    print("No Such Element Found.")
