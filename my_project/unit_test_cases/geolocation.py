from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    geological = driver.find_element(By.XPATH, herokuapp_feilds["Geological"])
    geological.click()

    location_button = driver.find_element(By.XPATH, '//button[contains(text(), "Where am I?")]')
    location_button.click()

    wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@href="http://maps.google.com/?q=22.7109277,75.8800256"]')))

    print("Your location is:")
    latitude = driver.find_element(By.XPATH, '//div[contains(text(), "22.7109277")]')
    print("Latitude:")
    print(latitude.text)

    longitude = driver.find_element(By.XPATH, '//div[contains(text(), "75.8800256")]')
    print("Longitude:")
    print(longitude.text)

except NoSuchElementException:
    print("No Such Element Found.")
