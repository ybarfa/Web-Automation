from selenium import webdriver
from selenium.webdriver.common.by import By
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
    driver.maximize_window()

    JqueryUiMenu = driver.find_element(By.XPATH, herokuapp_feilds["JQuery UI Menus"])
    JqueryUiMenu.click()

    enable_button = driver.find_element(By.XPATH, '//a[contains(text(), "Enabled")]')
    enable_button.click()

    time.sleep(2)

    download_button = driver.find_element(By.XPATH, '//a[contains(text(), "Downloads")]')
    download_button.click()

    csv_file = driver.find_element(By.XPATH, '//    a[@href="/download/jqueryui/menu/menu.csv"]')
    csv_file.click()

except NoSuchElementException:
    print("No Such Element Found.")


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
#
# # Set up Selenium
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# # Open the website
# driver.get("https://the-internet.herokuapp.com/jqueryui/menu")
#
# # Find the menu item to hover over
# menu_item = driver.find_element(By.ID, "ui-id-2")
#
# # Perform the hover action
# hover = ActionChains(driver).move_to_element(menu_item)
# hover.perform()
#
# # Find the submenu item to click
# submenu_item = driver.find_element(By.ID, "ui-id-4")
#
# # Click on the submenu item
# submenu_item.click()
#
# # Wait for a while to see the result
# driver.implicitly_wait(5)
#
# # Close the browser
# driver.quit()
