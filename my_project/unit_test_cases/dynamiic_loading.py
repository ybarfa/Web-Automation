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

    dynamic_loading = driver.find_element(By.XPATH, herokuapp_feilds["Dynamic Loading"])
    dynamic_loading.click()

    example1 = driver.find_element(By.XPATH, dynamicLoading["Example1"])
    example1.click()

    Start_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dynamicLoading["Start Button"])))
    Start_Button.click()

    message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, dynamicLoading["Message"])))
    if message.is_displayed():
        print(message.text)

    driver.back()

    example2 = driver.find_element(By.XPATH, dynamicLoading["Example2"])
    example2.click()

    startButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dynamicLoading["Start Button"])))
    startButton.click()

    message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, dynamicLoading["Message"])))
    if message.is_displayed():
        print(message.text)

except NoSuchElementException:
    print("No Such Element Found.")
