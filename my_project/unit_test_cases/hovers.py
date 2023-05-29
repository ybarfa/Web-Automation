from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
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

    hover = driver.find_element(By.XPATH, herokuapp_feilds["Hovers"])
    hover.click()

    user_profiles = driver.find_elements(By.CSS_SELECTOR, ".figure")

    for profile in user_profiles:
        actions = ActionChains(driver)

        actions.move_to_element(profile).perform()

        hidden_text = profile.find_element(By.CSS_SELECTOR, ".figcaption h5")

        print(hidden_text.text)

except NoSuchElementException:
    print("No Such Element Found.")

