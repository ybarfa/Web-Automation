# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# create webdriver object
driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element(By.XPATH, '//*[@id="gcse-form"]/button/i')
element.click()

textbox = driver.find_element(By.XPATH, '//input[@class="gcse-search-input__wrapper"]')
textbox.send_keys("Arays")
textbox.click()
time.sleep(5)

# if element:
#
#     element.click()
#
#     textbox = driver.find_element(By.XPATH, "//input[@class='gcse-search-input__wrapper']")
#     # send keys
#     textbox.send_keys("Arrays")
#     time.sleep(5)
#
# else:
#     print("element not found")
