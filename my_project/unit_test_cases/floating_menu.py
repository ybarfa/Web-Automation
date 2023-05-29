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

    floating_menu = driver.find_element(By.XPATH, herokuapp_feilds["Floating Menu"])
    floating_menu.click()



except NoSuchElementException:
    print("No Such Element Found.")


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# driver = webdriver.Chrome()
#
# # Open the webpage
# driver.get("https://the-internet.herokuapp.com/")
#
# # Find and hover over the floating menu
# floating_menu = driver.find_element(By.XPATH, "//div[@id='menu']")
# ActionChains(driver).move_to_element(floating_menu).perform()
#
# # Wait for the menu options to be visible
# wait = WebDriverWait(driver, 10)
# menu_options = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#menu ul li")))
#
# # Print the menu options
# for option in menu_options:
#     print(option.text)
#
# # Close the browser
# driver.quit()
