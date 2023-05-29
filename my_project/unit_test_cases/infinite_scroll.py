# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# from selenium.common.exceptions import NoSuchElementException
# from my_project.utils.xpath import *
# import os
# import json
# import time
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
#     infinite_scroll = driver.find_element(By.XPATH, herokuapp_feilds["Infinite Scroll"])
#     infinite_scroll.click()
#
#     scroll_area = driver.find_element(By.XPATH, '//div[@class="scroll large-8 columns large-centered"]')
#
#     scrolls = 5
#     scroll_pause = 2
#
#     for i in range(scrolls):
#         actions = ActionChains(driver)
#         actions.move_to_element(scroll_area).perform()
#         time.sleep(scroll_pause)
#
#     scroll_area = driver.find_element(By.XPATH, "//div[@class='jscroll-inner']")
#     scroll_text = scroll_area.text
#
#     print(scroll_text)
#
# except NoSuchElementException:
#     print("No Such Element Found.")
import time

from selenium import webdriver
# Create a new instance of the Chrome driver
driver = webdriver.Chrome()
# Navigate to the page
driver.get("https://the-internet.herokuapp.com/infinite_scroll")
# Execute JavaScript to scroll down the page
for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait for a brief moment to allow the content to load
    driver.implicitly_wait(1)
    time.sleep(2)
# Close the browser
driver.quit()
