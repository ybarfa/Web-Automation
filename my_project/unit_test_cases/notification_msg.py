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

    notification_message = driver.find_element(By.XPATH, herokuapp_feilds["Notification Messages"])
    notification_message.click()

    message = driver.find_element(By.XPATH, '//div[@class="flash notice"]')
    print(message.text)

    click_here = driver.find_element(By.XPATH, '//a[@href="/notification_message"]')
    click_here.click()

    message1 = driver.find_element(By.XPATH, '//div[@class="flash notice"]')
    print(message1.text)

except NoSuchElementException:
    print("No Such Element Found.")
