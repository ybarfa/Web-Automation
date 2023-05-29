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

    slider_link = driver.find_element(By.XPATH, herokuapp_feilds["Horizontal Slider"])
    slider_link.click()

    slider = driver.find_element(By.XPATH, '//input[@type="range"]')

    def move_slider_to_position(position):
        action = ActionChains(driver)
        action.click_and_hold(slider).move_by_offset(position, 0).release().perform()

    move_slider_to_position(50)

except NoSuchElementException:
    print("No Such Element Found.")
