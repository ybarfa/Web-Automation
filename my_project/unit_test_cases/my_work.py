# import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# import json
# import os
#
# current_directory = os.getcwd()
# parent_directory = os.path.dirname(current_directory)
# config_path = os.path.join(parent_directory, "configuration", "config.json")
#
# with open(config_path, "r") as configuration:
#     config_data = json.load(configuration)
#
# driver = webdriver.Chrome()
# driver.get(config_data["url"])
# driver.maximize_window()
#
# try:
#     option = driver.find_element(By.XPATH, '//a[@href="/broken_images"]')
#     option.click()
#
#     image = driver.find_element(By.XPATH, '//img[@src="img/avatar-blank.jpg"]')
#     url = image.get_attribute('src')
#     response = requests.get(url)
#     if response.status_code != 200:
#         print(f"Broken image detected: {url}")
#     else:
#         print(f"No Broken Image Detected: {url}")
#
# except NoSuchElementException:
#     print("No Such Element Found.")


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from my_project.utils.xpath import *
# import json
# import os
#
# current_directory = os.getcwd()
# parent_directory = os.path.dirname(current_directory)
# config_path = os.path.join(parent_directory, "configuration", "config.json")
#
# with open(config_path, "r") as configuration:
#     config_data = json.load(configuration)
#
#
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/")
# driver.maximize_window()
#
#
# dropdown_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, herokuapp_feilds["Dropdown"])))
# dropdown_link.click()
#
# dropdown_bar = driver.find_element(By.XPATH, '//select[@id="dropdown"]')
# dropdown_bar.click()
#
# option_1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Option 1")))
# option_1.click()
#
# # option_1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dropdown")))
# # option_1.click()
#
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# from my_project.utils.xpath import *
# import json
# import os
# import time
#
# current_directory = os.getcwd()
# parent_directory = os.path.dirname(current_directory)
# config_path = os.path.join(parent_directory, "configuration", "config.json")
#
# with open(config_path, "r") as configuration:
#     config_data = json.load(configuration)
#
# try:
#     driver = webdriver.Chrome()
#     driver.get(config_data["url"])
#     driver.maximize_window()
#
#     dropdown = driver.find_element(By.XPATH, herokuapp_feilds["Dropdown"])
#     dropdown.click()
#
#     option = driver.find_element(By.XPATH, herokuapp_feilds["Option1"])
#     option.click()
#
#     time.sleep(3)
#
# except NoSuchElementException:
#     print("No Such Element Found.")