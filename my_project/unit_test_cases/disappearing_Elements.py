# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# from my_project.utils.xpath import *
# import json
# import os
# import time
#
# current_directory = os.getcwd()
# parent_directory = os.path.dirname(current_directory)
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
#     disappearing_elements = driver.find_element(By.XPATH, herokuapp_feilds["Disappearing Elements"])
#     disappearing_elements.click()
#     time.sleep(5)
#
#     driver.refresh()
#
#     if driver.find_element(By.XPATH, '//a[@href="/"]').is_displayed():
#         print("Home Button is present.")
#     else:
#         print("Home Button is not present.")
#
#     if driver.find_element(By.XPATH, '//a[@href="/about/"]').is_displayed():
#         print("About Button is present.")
#     else:
#         print("About Button is not present.")
#
#     if driver.find_element(By.XPATH, '//a[@href="/contact-us/"]').is_displayed():
#         print("Contact Us Button is present.")
#     else:
#         print("Contact Us Button is not present.")
#
#     if driver.find_element(By.XPATH , '//a[@href="/portfolio/"]').is_displayed():
#         print("Portfolio Button is present.")
#     else:
#         print("Portfolio Button is not present.")
#
#     if driver.find_element(By.XPATH, '//a[@href="/gallery/"]').is_displayed():
#         print("Gallery Button is present.")
#     else:
#         print("Gallery Button is not present.")
#
#     time.sleep(3)
#
# except NoSuchElementException:
#     print("No Such Element Found.")


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

    disappearing_elements = driver.find_element(By.XPATH, herokuapp_feilds["Disappearing Elements"])
    disappearing_elements.click()

    time.sleep(3)

    element_selectors = ['//a[contains(text(), "Home")]', '//a[@href="/about/"]', '//a[@href="/contact-us/"]', '//a[@href="/portfolio/"]', '//a[@href="/gallery/"]']

    print("Before Reloading the Web page")
    for selector in element_selectors:
        try:
            element = driver.find_element(By.XPATH, selector)
            print(f"Element with selector '{selector}' found")
        except NoSuchElementException:
            print(f"Element with selector '{selector}' not found")

    driver.refresh()

    print("After Reloading the Web page")
    for selector in element_selectors:
        try:
            element = driver.find_element(By.XPATH, selector)
            print(f"Element with selector '{selector}' found after reloading")
        except NoSuchElementException:
            print(f"Element with selector '{selector}' not found after reloading")

    time.sleep(3)

except Exception as e:
    print(f"An error occurred: {str(e)}")
