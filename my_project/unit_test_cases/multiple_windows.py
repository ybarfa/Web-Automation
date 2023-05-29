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

try:
    driver = webdriver.Chrome()
    driver.get(config_data["url"])
    driver.maximize_window()

    multiple_windows = driver.find_element(By.XPATH, herokuapp_feilds["Multiple Windows"])
    multiple_windows.click()

    click_here_link = driver.find_element(By.XPATH, '//a[@href="/windows/new"]')
    click_here_link.click()

    driver.switch_to.window(driver.window_handles[1])

    print("New window title:", driver.title)

    driver.close()

    driver.switch_to.window(driver.window_handles[0])

except NoSuchElementException:
    print("No Such Element Found.")
