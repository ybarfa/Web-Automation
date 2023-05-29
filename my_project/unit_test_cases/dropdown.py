from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

    element = driver.find_element(By.XPATH, herokuapp_feilds["Dropdown"])
    element.click()

    # dropdown_bar = Select(driver.find_element(By.ID, 'dropdown'))
    #
    # options = dropdown_bar.select_by_value("1")
    dropdown = Select(driver.find_element(By.ID, 'dropdown'))
    dropdown.select_by_visible_text("Option 2")
    time.sleep(2)
    dropdown.select_by_visible_text("Option 1")
    time.sleep(2)
    dropdown.select_by_visible_text("Option 2")
    time.sleep(2)
    dropdown.select_by_visible_text("Option 1")
    time.sleep(3)

except NoSuchElementException:
    print("No Such Element Found.")
