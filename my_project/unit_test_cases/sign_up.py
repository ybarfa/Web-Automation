from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
from my_project.utils.xpath import *

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
config_path = os.path.join(parent_directory, "configuration", "config.json")

with open(config_path,"r") as configuration:
    config_data = json.load(configuration)

driver = webdriver.Chrome()
driver.get(config_data["url"])
driver.maximize_window()

search_box = driver.find_element(By.XPATH, sign_up["search_textbox"])
search_box.send_keys("Tshirts for men")

search_button = driver.find_element(By.XPATH, sign_up["search_button"])
search_button.click()

driver_wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='a-size-medium a-text-italic']")))