from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoAlertPresentException
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

    context_menu = driver.find_element(By. XPATH, herokuapp_feilds["context_menu"])
    context_menu.click()

    right_click_element = driver.find_element(By.XPATH, "//div[@id='hot-spot']")

    ActionChains(driver).context_click(right_click_element).perform()

    time.sleep(3)

    alert = driver.switch_to.alert
    print("Alert Text:", alert.text)
    alert.accept()

except NoAlertPresentException:
    print("No alert found.")
