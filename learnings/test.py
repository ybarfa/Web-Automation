import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
driver.maximize_window()

searchbox = driver.find_element(By.ID, "id-search-field")
searchbox.send_keys("Python For windows")

go_button = driver.find_element(By.ID, "submit")
go_button.click()

time.sleep(3)
