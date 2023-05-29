from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    element = driver.find_element(By.XPATH, herokuapp_feilds["Dynamic_Content"])
    element.click()

    dynamic_content = driver.find_element(By.CSS_SELECTOR, ".large-10.columns")

    initial_text = dynamic_content.text

    time.sleep(3)

    driver.refresh()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//div[contains(text(),'" + initial_text + "')]")))

    updated_text = driver.find_element(By.CSS_SELECTOR, ".large-10.columns").text

    if initial_text != updated_text:
        print("Dynamic content has been changed!")
    else:
        print("Dynamic content has not been changed!")

    time.sleep(3)

except NoSuchElementException:
    print("No Such element Found.")
