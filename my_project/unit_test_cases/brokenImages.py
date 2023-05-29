import requests
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

driver = webdriver.Chrome()
driver.get(config_data["url"])
driver.maximize_window()

try:
    option = driver.find_element(By.XPATH, herokuapp_feilds["Broken_Images"])
    option.click()

    images = driver.find_elements(By.TAG_NAME, 'img')

    for image in images:
        url = image.get_attribute('src')
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Broken image detected: {url}")

except NoSuchElementException:
    print("No Such Element Found.")


# import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/")
# driver.maximize_window()
#
# option = driver.find_element(By.XPATH, '//a[@href="/broken_images"]')
# option.click()
#
# images = driver.find_elements(By.TAG_NAME, 'img')
# for image in images:
#     url = image.get_attribute('src')
#     response = requests.get(url)
#     if response.status_code != 200:
#         print(f"Broken image detected: {url}")
