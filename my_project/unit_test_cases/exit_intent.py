from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
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

    exit_intent = driver.find_element(By.XPATH, herokuapp_feilds["Exit Intent"])
    exit_intent.click()

    pyautogui.moveTo(100, 100, duration=1)

    driver.implicitly_wait(5)

    close_button = driver.find_element(By.XPATH, "//div[@id='ouibounce-modal']//div[@class='modal-footer']/p")
    close_button.click()

except NoSuchElementException:
    print("No Such Element Found.")
