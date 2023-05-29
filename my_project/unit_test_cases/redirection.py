from selenium import webdriver
from selenium.webdriver.common.by import By
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

    redirection = driver.find_element(By.XPATH, herokuapp_feilds["Redirect Link"])
    redirection.click()

    button = driver.find_element(By.XPATH, '//a[@id="redirect"]')
    button.click()

    print("Current URL:", driver.current_url)

    page_text = driver.find_element(By.XPATH, '//div[@class="example"]')
    print(page_text.text)

    

except NoSuchElementException:
    print("No Such Element Found.")
