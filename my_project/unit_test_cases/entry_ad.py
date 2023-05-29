from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    entry_ad = driver.find_element(By.XPATH, herokuapp_feilds["Entry Ad"])
    entry_ad.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="modal"]')))

    close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//p[contains(text(), "Close")]')))
    close_button.click()

except NoSuchElementException:
    print("No Such Element Found.")

#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import ElementNotInteractableException
# from my_project.utils.xpath import *
# import json
# import os
#
# current_directory = os.getcwd()
# parent_directory = os.path.dirname(current_directory)
#
# config_path = os.path.join(parent_directory, "configuration", "config.json")
#
# with open(config_path, "r") as configuration:
#     config_data = json.load(configuration)
#
# try:
#     driver = webdriver.Chrome()
#     driver.get(config_data["url"])
#     driver.maximize_window()
#
#     entry_ad = driver.find_element(By.XPATH, herokuapp_feilds["Entry Ad"])
#     entry_ad.click()
#
#     wait = WebDriverWait(driver, 10)
#     modal = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="modal"]')))
#
#     # Scroll to the close button
#     close_button = driver.find_element(By.XPATH, '//p[contains(text(), "Close")]')
#     driver.execute_script("arguments[0].scrollIntoView();", close_button)
#
#     # Wait for the close button to be clickable
#     wait.until(EC.element_to_be_clickable((By.XPATH, '//p[contains(text(), "Close")]')))
#
#     close_button.click()
#
# except NoSuchElementException:
#     print("No Such Element Found.")
# except ElementNotInteractableException:
#     print("Element Not Interactable.")
