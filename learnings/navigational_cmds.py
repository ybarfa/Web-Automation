from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://openai.com/blog/chatgpt")
print(driver.title)
time.sleep(3)

driver.get("https://www.geeksforgeeks.org/selenium-python-tutorial/")
print(driver.title)
time.sleep(3)


driver.back()
print(driver.title)
time.sleep(3)


driver.forward()
print(driver.title)
time.sleep(3)

driver.close()