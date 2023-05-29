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

    dynamicControl = driver.find_element(By.XPATH, herokuapp_feilds["Dynamic Control"])
    dynamicControl.click()

    checkbox = driver.find_element(By.XPATH, dynamic_control["checkbox"])
    checkbox.click()
    if checkbox.is_selected():
        assert True, "Checkbox is Selected."
    else:
        assert False, "Checkbox is not Selected."

    remove_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dynamic_control["Remove_button"])))
    remove_button.click()

    message1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "message")))

    if message1.is_displayed():
        print("On Clicking Remove Button: ")
        print(message1.text)

    add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dynamic_control["Add_button"])))
    add_button.click()

    message2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "message")))
    if message2.is_displayed():
        print("On Clicking Add Button:")
        print(message2.text)

    enable_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Enable")]')))
    enable_button.click()

    message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, '//p[contains(text(), "It\'s enabled!")]')))
    if message.is_displayed():
        print("On Clicking Enable Button:")
        print(message.text)

    disable_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Disable")]')))
    disable_button.click()

    message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, '//p[contains(text(), "It\'s disabled!")]')))
    if message.is_displayed():
        print("On Clicking Disable Button:")
        print(message.text)

except NoSuchElementException:
    print("No Such element Present.")
