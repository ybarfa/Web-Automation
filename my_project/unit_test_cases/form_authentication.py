from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    fom_auth = driver.find_element(By.XPATH, herokuapp_feilds["Form Authentication"])
    fom_auth.click()

    username = driver.find_element(By.XPATH, form_authentication["username"])
    username.send_keys("tomsmith")

    password = driver.find_element(By.XPATH, form_authentication["password"])
    password.send_keys("SuperSecretPassword!")

    login = driver.find_element(By.XPATH, form_authentication["login button"])
    login.click()

    alert = driver.switch_to.alert
    print("Alert Text:", alert.text)
    alert.accept()

    wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="flash success"]')))

    logout = driver.find_element(By.XPATH, form_authentication["logout button"])
    logout.click()

except NoSuchElementException:
    print("No Such Element Found.")
