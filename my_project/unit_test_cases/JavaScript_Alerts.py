from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
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

    javascript_alert = driver.find_element(By.XPATH, herokuapp_feilds["JavaScript Alerts"])
    javascript_alert.click()

    click_for_JS_Alert = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
    click_for_JS_Alert.click()

    alert = Alert(driver)
    alert.accept()

    result_message = driver.find_element(By.ID, "result").text
    print("Result message after accepting alert:", result_message)

    click_for_Js_confirm = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
    click_for_Js_confirm.click()

    alert = Alert(driver)
    alert.accept()

    result_message = driver.find_element(By.ID, "result").text
    print("Result message after dismissing alert:", result_message)

    click_for_Js_prompt = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
    click_for_Js_prompt.click()

    alert = Alert(driver)
    alert.send_keys("Hello, Selenium!")
    alert.accept()

    result_message = driver.find_element(By.ID, "result").text
    print("Result message after accepting prompt:", result_message)

except NoSuchElementException:
    print("No Such Element Found.")
