# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# from my_project.utils.xpath import *
# import json
# import os
#
# current_directory = os.getcwd()
# parent_directory = os.path.dirname(current_directory)
#
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
#     frames = driver.find_element(By.XPATH, '')
#
# except NoSuchElementException:
#     print("No Such Element Found.")
#

from selenium import webdriver
from selenium.webdriver.common.by import By
# Set up the Selenium webdriver
driver = webdriver.Chrome()
# Navigate to the Nested Frames page
driver.get("https://the-internet.herokuapp.com/nested_frames")
# Find the top frame
driver.switch_to.frame("frame-top")
# Find the left frame within the top frame
driver.switch_to.frame("frame-left")
# Print the content of the left frame
print(driver.find_element(By.TAG_NAME, "body").text)
# Switch back to the top frame
driver.switch_to.default_content()
# Find the middle frame within the top frame
driver.switch_to.frame("frame-middle")
# Print the content of the middle frame
print(driver.find_element(By.TAG_NAME, "body").text)
# Switch back to the top frame
driver.switch_to.default_content()
# Find the right frame within the top frame
driver.switch_to.frame("frame-right")
# Print the content of the right frame
print(driver.find_element(By.TAG_NAME, "body").text)
# Switch back to the top frame
driver.switch_to.default_content()
# Find the bottom frame
driver.switch_to.frame("frame-bottom")
# Print the content of the bottom frame
print(driver.find_element(By.TAG_NAME, "body").text)
# Close the browser
driver.quit()