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

option = driver.find_element(By.XPATH, herokuapp_feilds["Add/Remove Elements"])
option.click()

for i in range(3):
    add_element = driver.find_element(By.XPATH, '//button[@onclick="addElement()"]')
    add_element.click()
    time.sleep(1)

try:
    delete_buttons = driver.find_elements(By.XPATH, '//button[@class="added-manually"]')
    num_delete_buttons = len(delete_buttons)

    assert num_delete_buttons in [1, 2, 3], f"{num_delete_buttons} Delete Buttons are Present."
    assert num_delete_buttons == 3, "Three Delete Buttons must be Present."
except NoSuchElementException:
    print("Delete Buttons not found")
