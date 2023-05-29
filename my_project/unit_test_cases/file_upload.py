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

    file_upload = driver.find_element(By.XPATH, herokuapp_feilds["File Upload"])
    file_upload.click()

    choose_file = driver.find_element(By.XPATH, '//input[@id="file-upload"]')
    choose_file.send_keys(r'C:\Users\barfa\Downloads\6th Sem Marksheet.pdf')

    upload_button = driver.find_element(By.XPATH, '//input[@id="file-submit"]')
    upload_button.click()

    wait = WebDriverWait(driver, 10)
    file_uploaded = wait.until(EC.presence_of_element_located((By.XPATH, '//h3[contains(text(), "File Uploaded!")]')))

except NoSuchElementException:
    print("No Such Element Found.")
