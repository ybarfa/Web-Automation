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

    Ab_testing = driver.find_element(By.XPATH, herokuapp_feilds["Ab_testing"])
    Ab_testing.click()
    my_data = "Also known as split testing. This is a way in which businesses are able to simultaneously test and " \
              "learn different versions of a page to see which text and/or functionality works best towards a desired " \
              "outcome (e.g. a user action such as a click-through)."

    content = driver.find_element(By.XPATH, "//p[contains(text(),'Also known as split testing.')]")
    print(content.text)
    if my_data == content.text:
        assert True, "Expected Data not found on webpage."
    else:
        assert False, ""
except NoSuchElementException:
    print("Expected Data found on webpage.")
